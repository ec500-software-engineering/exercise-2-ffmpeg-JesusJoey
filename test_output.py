import main
from math import isclose
def test_duration():
    fnin = 'video.mp4'
    fnout1 = 'video_480p.mp4'
    fnout2 = 'video_720p.mp4'

    orig_meta = main.ffprobe(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])
    test = main.MyProcess()
    test.convert()
    meta_480 = main.ffprobe(fnout1)
    meta_720 = main.ffprobe(fnout2)
    duration_480 = float(meta_480['streams'][0]['duration'])
    duration_720 = float(meta_720['streams'][0]['duration'])
    assert isclose(orig_duration, duration_480, abs_tol=1)
    assert isclose(orig_duration, duration_720, abs_tol=1)
    print('all successful!')

test_duration()
