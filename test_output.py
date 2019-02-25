from pytest import approx
import subprocess


def test_duration():
    inp='.output-video/IMG_0753.480.mp4'
    out='.output-video/IMG_0753.720.mp4'
    outLen = subprocess.call(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1',out])
    inLen  = subprocess.call(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1',inp])
    assert inLen == approx(outLen)
