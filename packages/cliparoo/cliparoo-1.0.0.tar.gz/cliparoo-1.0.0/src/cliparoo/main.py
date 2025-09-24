import subprocess
import sys
import json
from fractions import Fraction
import argparse
import shutil
import os


def check_ffmpeg():
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        subprocess.run(
            ["ffprobe", "-version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError:
        print("ffmpeg or ffprobe is not installed. Please install them to proceed.")
        sys.exit(1)
    except FileNotFoundError:
        print(
            "ffmpeg or ffprobe command not found. Please ensure they are installed and in your PATH."
        )
        sys.exit(1)


class Video:
    def __init__(self, path):
        self._path = path

        # Check the file exists, raise an error if it does not
        if not os.path.exists(path):
            raise FileNotFoundError(f"Video file {path} does not exist.")

        try:
            cmd = [
                "ffprobe",
                "-v",
                "error",
                "-select_streams",
                "v:0",
                "-show_entries",
                "stream=index,codec_name,codec_type,width,height,bit_rate,duration,time_base,r_frame_rate,pix_fmt",
                "-show_entries",
                "packet=pts,flags",
                "-of",
                "json",
                path,
            ]
            result = subprocess.run(
                cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            output = result.stdout.decode("utf-8").strip()

            if not output:
                print("No packets found in the video.")
                return

        except subprocess.CalledProcessError as e:
            print(
                f"An error occurred while running ffprobe: {e.stderr.decode('utf-8')}"
            )
            sys.exit(1)

        frames = []

        # Parse the JSON output
        try:
            data = json.loads(output)
            stream_info = data.get("streams", [])[0] if data.get("streams") else {}
            packets = data.get("packets", [])

            if not packets:
                print("No packets found in the video.")
                return

            for packet in packets:
                pts = packet.get("pts")
                flags = packet.get("flags", "")
                is_keyframe = "K" in flags
                frames.append({"pts": pts, "is_keyframe": is_keyframe})
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON output: {e}")
            sys.exit(1)

        stream_info["bit_rate"] = int(stream_info.get("bit_rate", -1))
        stream_info["r_frame_rate"] = Fraction(stream_info["r_frame_rate"])
        stream_info["time_base"] = Fraction(stream_info["time_base"])
        stream_info["calculated_duration"] = (
            Fraction(len(frames), 1) / stream_info["r_frame_rate"]
        )

        keyframes = [i for i, frame in enumerate(frames) if frame["is_keyframe"]]

        self._stream_info = stream_info
        self._frames = frames
        self._keyframes = keyframes

    def __repr__(self):
        return f"Video(path='{self._path}')"

    @property
    def shape(self):
        stream_info = self._stream_info
        return (stream_info["height"], stream_info["width"])

    def __len__(self):
        return len(self._frames)

    def is_well_formed(self):
        time_base = self._stream_info["time_base"]
        r_frame_rate = self._stream_info["r_frame_rate"]
        frames = self._frames

        f_multiplier = 1 / (time_base * r_frame_rate)
        if f_multiplier.denominator != 1:
            print(f"Warning: f_multiplier is not an integer: {f_multiplier}")
        f_multiplier = f_multiplier.numerator
        last_keyframe_pts = None
        for frame in frames:
            frame_pts = frame["pts"]

            if frame["is_keyframe"]:
                if last_keyframe_pts is not None:
                    if frame["pts"] <= last_keyframe_pts:
                        print(
                            f"Keyframe with pts {frame['pts']} is not well-formed (not greater than last keyframe pts {last_keyframe_pts})"
                        )
                        return False
                last_keyframe_pts = frame["pts"]
            else:
                if last_keyframe_pts is None:
                    print(
                        f"Non-keyframe with pts {frame['pts']} is not well-formed (no previous keyframe)"
                    )
                    return False
                elif frame["pts"] < last_keyframe_pts:
                    print(
                        f"Non-keyframe with pts {frame['pts']} is not well-formed (less than last keyframe pts {last_keyframe_pts})"
                    )
                    return False
            assert type(frame_pts) is int, f"Frame pts {frame_pts} is not an integer"
            if frame_pts % f_multiplier != 0:
                print(
                    f"Frame with pts {frame_pts} is not well-formed (not a multiple of f_multiplier {f_multiplier})"
                )
                return False
        return True

    def __iter__(self):
        return iter(self._frames)


class ClipRange:
    def __init__(self, video: Video, clip: str | list[int]):
        if not clip:
            return []

        self._video = video

        if type(clip) is list:
            ranges = []
            clip_copy = clip.copy()
            range_start = None
            range_len = 0
            while clip_copy:
                if type(clip_copy[0]) is not int:
                    raise ValueError("Clip list must contain only integers.")

                if clip_copy[0] > len(video) or clip_copy[0] < 0:
                    raise ValueError(f"Clip point {clip_copy[0]} is out of bounds.")

                if range_start is None:
                    range_start = clip_copy[0]
                    range_len = 1
                elif clip_copy[0] == range_start + range_len:
                    range_len += 1
                else:
                    if range_len == 1:
                        raise ValueError("All clip ranges must be of length > 1.")

                    ranges.append((range_start, range_len + range_start - 1))
                    range_start = clip_copy[0]
                    range_len = 1

                clip_copy.pop(0)

            if range_start is not None:
                ranges.append((range_start, range_len + range_start - 1))

            self._ranges = ranges
            return

        assert type(clip) is str, "Clip must be a string or a list of integers."

        def parse_numeric(value):
            try:
                if "/" in value:  # Fraction
                    return Fraction(value)
                elif "." in value:  # Float
                    return float(value)
                elif value == "end":
                    return len(video) - 1
                elif value == "start":
                    return 0
                else:  # Integer
                    return int(value)
            except ValueError:
                print(
                    f"Invalid numeric value: {value}. Expected 'start', 'end', or a float, integer, or fraction."
                )
                sys.exit(1)

        ranges = []
        for part in clip.split(","):
            try:
                start, end = part.split("-")
                # Handle float, integer, and fraction
                start = parse_numeric(start.strip())
                end = parse_numeric(end.strip())
                # Ensure start and end have the same type
                if type(start) != type(end):
                    print(
                        f"Start and end values must be of the same type: {start} and {end}."
                    )
                    sys.exit(1)

                if start > end:
                    print(
                        f"Invalid clip range: {part}. Start ({start}) cannot be greater than end ({end})."
                    )
                    sys.exit(1)

                ranges.append((start, end))
            except ValueError:
                print(f"Invalid clip range format: {part}. Expected format X-Y.")
                sys.exit(1)

        sorted_frames_pts_fractions = sorted(
            [
                Fraction(frame["pts"]) * video._stream_info["time_base"]
                for frame in video
            ]
        )

        index_only_clip_ranges = []

        for start, end in ranges:
            if type(start) is Fraction:
                try:
                    start_index = sorted_frames_pts_fractions.index(start)
                except ValueError:
                    print(f"Start point rational {start} not found in video frames.")
                    sys.exit(1)
                try:
                    end_index = sorted_frames_pts_fractions.index(end)
                except ValueError:
                    print(f"End point rational {end} not found in video frames.")
                    sys.exit(1)

                index_only_clip_ranges.append((start_index, end_index))
            elif type(start) is float:
                try:
                    start_index = next(
                        i
                        for i, v in enumerate(sorted_frames_pts_fractions)
                        if v >= start
                    )
                except StopIteration:
                    print(f"Start point float {start} not found in video frames.")
                    sys.exit(1)
                try:
                    end_index = (
                        next(
                            i
                            for i, v in enumerate(sorted_frames_pts_fractions)
                            if v > end
                        )
                        - 1
                    )
                except StopIteration:
                    print(f"End point float {end} not found in video frames.")
                    sys.exit(1)

                index_only_clip_ranges.append((start_index, end_index))
            elif type(start) is int:
                # Just ensure the start and end are within bounds
                if start < 0 or start >= len(sorted_frames_pts_fractions):
                    raise ValueError(
                        f"Start index {start} is out of bounds for video frames."
                    )
                if end < 0 or end >= len(sorted_frames_pts_fractions):
                    raise ValueError(
                        f"End index {end} is out of bounds for video frames."
                    )

                index_only_clip_ranges.append((start, end))

        self._ranges = index_only_clip_ranges

    def __iter__(self):
        return iter(self._ranges)

    def __len__(self):
        return sum(end - start + 1 for start, end in self._ranges)

    def plan(self, output_path: str, mode: str = "exact"):
        """
        Plan the video clipping operation.

        Returns None if the clip would result in an empty video.
        Mode can be one of the following:
        - "exact": Clips the video exactly at the specified frames.
        - "approx_inner": Clips the video approximately, but ensuring it stays within the specified range.
        - "approx_outer": Clips the video approximately, but ensuring it includes the specified range.

        Result is a dict with the following keys:
        - "commands": A list of ffmpeg command strings to execute.
        - "outputs": A list of output file paths.
        - "delete_artifacts": A set of temporary files to delete after processing.
        """

        assert mode in ["exact", "approx_inner", "approx_outer"]

        ts_epsilon = 1 / self._video._stream_info["r_frame_rate"] / 2
        delete_artifacts = set()

        sorted_frames_pts_fractions = sorted(
            [
                Fraction(frame["pts"]) * self._video._stream_info["time_base"]
                for frame in self._video
            ]
        )

        ffmpeg_commands = []
        outputs = []
        if mode == "exact":
            for start, end in self:
                start_fraction = sorted_frames_pts_fractions[start]
                end_fraction = sorted_frames_pts_fractions[end]
                duration = end_fraction - start_fraction
                ffmpeg_commands.append(
                    (
                        f"ffmpeg -hide_banner -loglevel error -i {self._video._path} -ss {float(start_fraction - ts_epsilon):0.6f} -t {float(duration + ts_epsilon)} {output_path}_{start}_{end}.mp4 -y",
                        end - start + 1,
                    )
                )
                outputs.append(f"{output_path}_{start}_{end}.mp4")
                delete_artifacts.add(f"{output_path}_{start}_{end}.mp4")
        elif (
            mode == "approx_inner" or mode == "approx_outer"
        ):  # Use stream copying, and only include GOPs entirely within the range
            video_keyframe_indexes = self._video._keyframes
            gops = []  # (start, end) tuples
            for i in range(len(video_keyframe_indexes)):
                start = video_keyframe_indexes[i]
                if i == len(video_keyframe_indexes) - 1:
                    end = len(sorted_frames_pts_fractions) - 1
                else:
                    end = video_keyframe_indexes[i + 1] - 1
                gops.append((start, end))

            for start, end in self:
                if mode == "approx_inner":
                    gops_in_range = [
                        i
                        for i in range(len(gops))
                        if gops[i][0] >= start and gops[i][1] <= end
                    ]
                elif mode == "approx_outer":
                    gops_in_range = [
                        i
                        for i in range(len(gops))
                        if gops[i][0] < end and gops[i][1] > start
                    ]

                if gops_in_range:
                    start_i = gops[gops_in_range[0]][0]
                    end_i = gops[gops_in_range[-1]][1]
                    start_t_fraction = sorted_frames_pts_fractions[start_i]
                    end_t_fraction = sorted_frames_pts_fractions[end_i]

                    ffmpeg_commands.append(
                        (
                            f"ffmpeg -hide_banner -loglevel error -ss {float(start_t_fraction - ts_epsilon):0.6f} -i {self._video._path} -t {float(end_t_fraction - start_t_fraction - ts_epsilon)} -c:v copy {output_path}_{start}_{end}.mp4 -y",
                            end_i - start_i + 1,
                        )
                    )
                    outputs.append(f"{output_path}_{start}_{end}.mp4")
                    delete_artifacts.add(f"{output_path}_{start}_{end}.mp4")

        if outputs:
            total_frames = sum(
                expected_frames for _, expected_frames in ffmpeg_commands
            )

            # Create a temporary file in the current directory to hold the list of files
            with open(f"{output_path}_chunks.txt", "w") as f:
                for output in outputs:
                    f.write(f"file '{output}'\n")

            ffmpeg_commands.append(
                (
                    f"ffmpeg -hide_banner -loglevel error -f concat -safe 0 -i {output_path}_chunks.txt -c copy {output_path} -y",
                    total_frames,
                )
            )
            outputs.append(output_path)
            delete_artifacts.add(f"{output_path}_chunks.txt")
            return {
                "commands": ffmpeg_commands,
                "outputs": outputs,
                "delete_artifacts": delete_artifacts,
            }

    def run(self, output_path: str, mode="exact"):
        plan = self.plan(output_path, mode=mode)

        for command in plan["commands"]:
            subprocess.run(command[0], shell=True, check=True)

        for delete_artifact in plan["delete_artifacts"]:
            os.remove(delete_artifact)


def main():
    check_ffmpeg()
    parser = argparse.ArgumentParser(
        prog="cliparoo", description="A video scrubbing utility."
    )
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")
    parser.add_argument(
        "-i", "--input", type=str, required=True, help="Input video file path"
    )
    parser.add_argument(
        "--input-info",
        action="store_true",
        help="Print stats about the input video file",
    )
    parser.add_argument(
        "--clip",
        type=str,
        help="Specify a clip range in the format X-Y,X2-Y2,... where X and Y are (float,fraction,integer)",
    )
    parser.add_argument(
        "--clip-mode",
        type=str,
        choices=["exact", "approx_inner", "approx_outer"],
        default="exact",
        help="Specify the clipping mode",
    )
    parser.add_argument("-o", "--output", type=str, help="Output video file path")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )
    parser.add_argument(
        "--verify", action="store_true", help="Verify the output video file"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run the script without making any changes (dry run mode)",
    )
    parser
    args = parser.parse_args()

    # ANSI escape codes for colored output
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    MAGENTA = "\033[35m"
    RED = "\033[31m"
    BLUE = "\033[34m"
    term_width = shutil.get_terminal_size((80, 20)).columns

    if not args.input:
        print("Input file is required. Use -i or --input to specify the video file.")
        sys.exit(1)

    video = Video(args.input)

    stream_props = video._stream_info.copy()

    def print_profile_info(video):
        def colorize_dict(d, indent=2):
            for k, v in d.items():
                key_str = f"{BOLD}{CYAN}{k}{RESET}"
                val_str = (
                    f"{GREEN}{v}{RESET}"
                    if isinstance(v, (int, float, str))
                    else f"{YELLOW}{v}{RESET}"
                )
                print(" " * indent + f"{key_str}: {val_str}")

        print(f"{BOLD}{MAGENTA}{'─' * term_width}{RESET}")
        print(f"{BOLD}{BLUE}📹 File:{RESET} {BOLD}{args.input}{RESET}")
        print(f"{BOLD}{MAGENTA}{'─' * term_width}{RESET}")

        print(f"{BOLD}{CYAN}Stream info:{RESET}")
        colorize_dict(stream_props, indent=4)

        num_frames = len(video)
        num_keyframes = sum(1 for frame in video._frames if frame["is_keyframe"])
        well_formed = video.is_well_formed()
        print(
            f"\n{BOLD}{CYAN}Frames:{RESET} {BOLD}{num_frames}{RESET} ({GREEN}{num_keyframes} keyframes{RESET})"
        )
        wf_color = GREEN if well_formed else RED
        print(
            f"{BOLD}{CYAN}Well formed timestamps:{RESET} {wf_color}{well_formed}{RESET}"
        )
        print(f"{BOLD}{MAGENTA}{'─' * term_width}{RESET}")

    if args.input_info:
        print_profile_info(video)

    sorted_frames_pts_fractions = sorted(
        [Fraction(frame["pts"]) * stream_props["time_base"] for frame in video]
    )

    if args.clip:
        clip_ranges = ClipRange(video, args.clip)

        if args.verbose:

            def fmt_ts(t: Fraction):
                total_seconds = t.numerator / t.denominator
                hours = int(total_seconds // 3600)
                minutes = int((total_seconds % 3600) // 60)
                seconds = total_seconds % 60
                return f"{hours:02}:{minutes:02}:{seconds:06.3f}"

            print(f"{BOLD}{MAGENTA}{'─' * term_width}{RESET}")
            print(f"{BOLD}{CYAN}Clip ranges:{RESET}")
            for start, end in clip_ranges:
                start_fraction = sorted_frames_pts_fractions[start]
                end_fraction = sorted_frames_pts_fractions[end]
                print(
                    f"{BOLD}{CYAN}Range:{RESET} {BOLD}{start}-{end}{RESET} "
                    f"({BOLD}{start_fraction}{RESET} - {BOLD}{end_fraction}{RESET}) "
                    f"({fmt_ts(start_fraction)} - {fmt_ts(end_fraction)})"
                )
            print(f"{BOLD}{MAGENTA}{'─' * term_width}{RESET}")

        if args.output:
            plan = clip_ranges.plan(args.output, mode=args.clip_mode)
            if plan is None:
                print(
                    f"{BOLD}{YELLOW}Clip would include no frames! Refusing to create empty clip.{RESET}"
                )
            else:
                ffmpeg_commands = plan["commands"]
                outputs = plan["outputs"]
                delete_artifacts = plan["delete_artifacts"]

                if args.dry_run:
                    print(
                        f"{BOLD}{YELLOW}Dry run mode enabled. The following commands would be executed:{RESET}"
                    )
                    for cmd, expected_frames in ffmpeg_commands:
                        print(
                            f"{BOLD}{CYAN}{cmd}{RESET} #({BOLD}{YELLOW}{expected_frames}{RESET} frames)"
                        )
                else:
                    print(f"{BOLD}{GREEN}Executing the following commands:{RESET}")
                    for i, (cmd, expected_frames) in enumerate(ffmpeg_commands):
                        print(
                            f"{BOLD}{CYAN}{cmd}{RESET} #({BOLD}{YELLOW}{expected_frames}{RESET} frames)",
                            end="",
                            flush=True,
                        )
                        result = subprocess.run(cmd, shell=True)
                        if result.returncode != 0:
                            print(f"{BOLD}{RED}Error executing command: {cmd}{RESET}")
                            sys.exit(1)

                        if args.verify:
                            # Validate the output file has the expected number of frames
                            tmp_output_file = outputs[i]
                            tmp_profile = Video(tmp_output_file)
                            if len(tmp_profile) != expected_frames:
                                print(
                                    f"{BOLD}{RED}Error: Output file {tmp_output_file} has {len(tmp_profile)} frames, expected {expected_frames}.{RESET}"
                                )
                                sys.exit(1)
                            print(f"{BOLD}{GREEN} - Verified{RESET} ✅")
                        else:
                            print()

                if not args.dry_run:
                    print(f"{BOLD}{GREEN}Cleaning up temporary files...{RESET}")
                    for artifact in delete_artifacts:
                        if os.path.exists(artifact):
                            os.remove(artifact)
                        else:
                            print(f"{BOLD}{YELLOW}File not found: {artifact}{RESET}")
                print(f"{BOLD}{GREEN}Done!{RESET}")


if __name__ == "__main__":
    main()
