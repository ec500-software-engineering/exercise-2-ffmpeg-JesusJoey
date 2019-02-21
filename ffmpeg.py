#!/usr/bin/env python
import os
import subprocess
#import threading
import time
import queue

outpath="/Users/joe/Desktop/BU_19_Spring/EC500/output-video"

def ffmpeg_convert(filepath):
	files = os.listdir(filepath)
	q=queue.Queue()
	for file in files:
		q.put(file)

	while not q.empty():
		video = q.get()
		video_720p = "ffmpeg -i "+filepath+"/"+video+" -s hd720 -b:v 2M -r 30 "+outpath+"/"+video[:-4]+"720.mp4"
		video_480p = "ffmpeg -i "+filepath+"/"+video+" -s hd480 -b:v 1M -r 30 "+outpath+"/"+video[:-4]+"480.mp4"
		subprocess.call(video_720p,shell=True)
		print('Converting to 720p video')
		subprocess.call(video_480p,shell=True)
		print('Converting to 480p video')
	print('All videos converted!')


def main():
	start=time.clock()
	ffmpeg_convert('/Users/joe/Desktop/videos')
	consume=time.clock()-start
	print("Time used:",consume)


if __name__=="__main__":
	main()



