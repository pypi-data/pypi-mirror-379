# cliparoo

<img src="roo.svg" alt="drawing" width="200"/>

A video clipper, cutter, and splicer.

## install

```bash
pip install cliparoo
```

You need `ffmpeg` and `ffprobe` installed. That's it.

## cli

Here is an example on how to extract the first 5000 frames of `myout.mp4`:

```bash
cliparoo -i tos_720p.mp4 --input-info --clip 0-4999 -o myout.mp4 --verbose --clip-mode approx_inner --verify
```

The `-i` flag sets the input and the `-o` flag sets the output.

The `--clip` flag takes the clip range. These can be multiple values joined by commas, which are spliced together. Integers represent frame indexes, floating point values represent times in seconds, and HH:MM:SS.MMMM format videos are similar. Keywords "`start`" and "`end`" also work. All clip ranges are *inclusive*.

The `--clip-mode` defines how to perform the clip. Values are `exact` (default), `approx_inner`, and `approx_outer`. Approx refers to the handling of time; counterintuitively this means to use a lossless stream copy.

The `--verify` flag will add additional checks to ensure the output and any temporary files have the correct frames.

The `--input-info` flag displays information about the video, and the `--verbose` adds additional fields.

There are other flags, like `--dry-run`, which you can find with `--help`.

## python

The python library allows for programmatic use.
It's pretty simple to use, the `ClipRange` takes either a string (matching the command line syntax) or a list of integers.

```python
import cliparoo
vid = cliparoo.Video("tos_720p.mp4")
cr = cliparoo.ClipRange(vid, [0, 1, 2, 3, 4, 5]) # same as "0-5"
cr.run("output.mp4", mode="exact")
```
