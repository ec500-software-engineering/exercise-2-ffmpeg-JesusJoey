import subprocess
import pytest
import json
import os

def test_one(self):
    while not (os.path.exists('./output-video/IMG_0753.480.mp4')):
        pass
    info_in = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format', 'json', '-show_streams',
                                           '-show_format', './output-video/IMG_0753.480.mp']) 
    info_in = json.loads(info_in)
    info_out = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format', 'json', '-show_streams',
                                            '-show_format', './output-video/IMG_0753.480.mp'])
    info_out = json.loads(info_out)
    orig_duration = float(info_in['streams'][0]['duration'])  
    new_duration = float(info_out['streams'][0]['duration'])
    assert orig_duration == new_duration
