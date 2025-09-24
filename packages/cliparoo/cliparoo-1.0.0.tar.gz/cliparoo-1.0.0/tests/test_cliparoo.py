from cliparoo.main import Video, ClipRange
import os


def test_video():
    v = Video("tos_720p.mp4")
    assert v.shape == (720, 1280)
    assert len(v) == 17616
    assert v.is_well_formed()


def test_video_not_exists():
    try:
        v = Video("non_existent_file.MP4")
    except FileNotFoundError:
        assert True
    else:
        assert False, "Expected FileNotFoundError but did not raise it."


def test_repr():
    v = Video("tos_720p.mp4")
    assert repr(v) == f"Video(path='tos_720p.mp4')"


def test_clip_range():
    v = Video("tos_720p.mp4")  # Exactly 24 FPS

    cr = ClipRange(v, "0-10")
    assert list(cr) == [(0, 10)]

    cr = ClipRange(v, "10-20")
    assert list(cr) == [(10, 20)]

    cr = ClipRange(v, "0-10,30-40")
    assert list(cr) == [(0, 10), (30, 40)]

    cr = ClipRange(v, "0/1-1/24")
    assert list(cr) == [(0, 1)]

    cr = ClipRange(v, "0/1-3/1")
    assert list(cr) == [(0, 24 * 3)]


def test_clip_range_start_end():
    v = Video("tos_720p.mp4")

    cr = ClipRange(v, "0-end")
    assert list(cr) == [(0, 17615)]

    cr = ClipRange(v, "start-end")
    assert list(cr) == [(0, 17615)]

    cr = ClipRange(v, "start-10")
    assert list(cr) == [(0, 10)]

    cr = ClipRange(v, "10-end")
    assert list(cr) == [(10, 17615)]

    cr = ClipRange(v, "0-end,start-end,start-10,10-end")
    assert list(cr) == [(0, 17615), (0, 17615), (0, 10), (10, 17615)]


def test_clip_range_list():
    v = Video("tos_720p.mp4")  # Exactly 24 FPS

    cr = ClipRange(v, [0, 1, 2, 3, 4, 5])
    assert list(cr) == [(0, 5)]
    assert len(cr) == 6

    cr = ClipRange(v, [0, 1, 2, 3, 4, 5, 3, 4, 5, 6])
    assert list(cr) == [(0, 5), (3, 6)]
    assert len(cr) == 10

    cr = ClipRange(v, [3, 4, 5, 6, 0, 1, 2, 3, 4, 5])
    assert list(cr) == [(3, 6), (0, 5)]
    assert len(cr) == 10


def test_basic_plan():
    v = Video("tos_720p.mp4")
    cr = ClipRange(v, "0-10")
    plan = cr.plan("/tmp/test_basic_clip.mp4")
    assert plan["outputs"][-1] == "/tmp/test_basic_clip.mp4"


def test_basic_clip():
    v = Video("tos_720p.mp4")
    cr = ClipRange(v, "0-10")
    cr.run("/tmp/test_basic_clip.mp4")

    assert os.path.exists("/tmp/test_basic_clip.mp4")
    tmp_video = Video("/tmp/test_basic_clip.mp4")
    assert tmp_video.shape == (720, 1280)
    assert len(tmp_video) == 11
    os.remove("/tmp/test_basic_clip.mp4")


def test_every_other_second():
    v = Video("tos_720p.mp4")
    frames_wanted = [i for i in range(len(v)) if i // 24 % 2 == 0 and i // 24 < 12]
    cr = ClipRange(v, frames_wanted)
    assert len(cr) == len(frames_wanted)
    cr.run("/tmp/test_every_other_second.mp4")

    assert os.path.exists("/tmp/test_every_other_second.mp4")
    tmp_video = Video("/tmp/test_every_other_second.mp4")
    assert tmp_video.shape == (720, 1280)
    assert len(tmp_video) == len(frames_wanted)
    os.remove("/tmp/test_every_other_second.mp4")


def test_tos_720p_structure():
    v = Video("tos_720p.mp4")
    assert v.shape == (720, 1280)
    assert len(v) == 17616
    assert v.is_well_formed()

    assert 0 in v._keyframes
    assert 126 in v._keyframes
    assert 214 in v._keyframes
    assert 323 in v._keyframes


def test_plan_approx_inner():
    v = Video("tos_720p.mp4")
    cr = ClipRange(v, "0-10")
    plan = cr.plan("/tmp/test_approx_inner.mp4", mode="approx_inner")
    assert plan is None

    cr = ClipRange(v, "0-125")
    plan = cr.plan("/tmp/test_approx_inner.mp4", mode="approx_inner")
    assert plan is not None
    assert plan["commands"][-1][1] == 126

    cr = ClipRange(v, "0-126")
    plan = cr.plan("/tmp/test_approx_inner.mp4", mode="approx_inner")
    assert plan is not None
    assert plan["commands"][-1][1] == 126

    cr = ClipRange(v, "0-212")
    plan = cr.plan("/tmp/test_approx_inner.mp4", mode="approx_inner")
    assert plan is not None
    assert plan["commands"][-1][1] == 126

    cr = ClipRange(v, "0-213")
    plan = cr.plan("/tmp/test_approx_inner.mp4", mode="approx_inner")
    assert plan is not None
    assert plan["commands"][-1][1] == 214

    cr = ClipRange(v, "0-214")
    plan = cr.plan("/tmp/test_approx_inner.mp4", mode="approx_inner")
    assert plan is not None
    assert plan["commands"][-1][1] == 214

    cr = ClipRange(v, "126-213")
    plan = cr.plan("/tmp/test_approx_inner.mp4", mode="approx_inner")
    assert plan is not None
    assert plan["commands"][-1][1] == 213 - 126 + 1

    cr = ClipRange(v, "0-17615")
    plan = cr.plan("/tmp/test_approx_inner.mp4", mode="approx_inner")
    assert plan is not None
    assert plan["commands"][-1][1] == 17616


def test_plan_approx_outer():
    v = Video("tos_720p.mp4")
    cr = ClipRange(v, "0-10")
    plan = cr.plan("/tmp/test_approx_outer.mp4", mode="approx_outer")
    assert plan is not None
    assert plan["commands"][-1][1] == 126

    cr = ClipRange(v, "0-17615")
    plan = cr.plan("/tmp/test_approx_outer.mp4", mode="approx_outer")
    assert plan is not None
    assert plan["commands"][-1][1] == 17616


def test_run_approx_inner():
    v = Video("tos_720p.mp4")

    cr = ClipRange(v, "126-213")
    cr.run("/tmp/test_run_approx_inner.mp4", mode="approx_inner")
    assert os.path.exists("/tmp/test_run_approx_inner.mp4")
    tmp_video = Video("/tmp/test_run_approx_inner.mp4")
    assert tmp_video.shape == (720, 1280)
    assert len(tmp_video) == 213 - 126 + 1
    os.remove("/tmp/test_run_approx_inner.mp4")

    cr = ClipRange(v, "0-250")
    cr.run("/tmp/test_run_approx_inner.mp4", mode="approx_inner")
    assert os.path.exists("/tmp/test_run_approx_inner.mp4")
    tmp_video = Video("/tmp/test_run_approx_inner.mp4")
    assert tmp_video.shape == (720, 1280)
    assert len(tmp_video) == 214
    os.remove("/tmp/test_run_approx_inner.mp4")
