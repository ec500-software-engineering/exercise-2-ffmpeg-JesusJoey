#!/usr/bin/env python
import os
import subprocess
import threading
import time
import queue

filepath='/Users/joe/Desktop/videos'
outpath='/Users/joe/Desktop/BU_19_Spring/EC500/output-video'


def file_input(filepath):
	files = os.listdir(filepath)
	q=queue.Queue()
	for file in files:
		q.put(file)
	return q

def ffmpeg_convert_720p(queue,filepath):
	index=0
	while not q.empty():
		video = q.get()
		video_720p = "ffmpeg -i "+filepath+"/"+video+" -s hd720 -b:v 2M -r 30 "+outpath+"/"+video[:-4]+"720.mp4"
		subprocess.call(video_720p,shell=True)
		print('vedio',index,'has been converted to 720p')
		index=index+1
		time.sleep(1)
	print('All videos converted to 720p!')

def ffmpeg_convert_480p(queue,filepath):
	idx=0
	while not q.empty():
		video = q.get()
		video_480p = "ffmpeg -i "+filepath+"/"+video+" -s hd480 -b:v 1M -r 30 "+outpath+"/"+video[:-4]+"480.mp4"
		subprocess.call(video_480p,shell=True)
		print('vedio',idx,'has been converted to 480p')
		idx=idx+1
		time.sleep(1)
	print('All videos converted to 480p!')

def main():
	start=time.clock()
	q=file_input(filepath)
	t1=threading.Thread(target=ffmpeg_convert_720p,args=(q,filepath))
	t1.start
	t2=threading.Thread(target=ffmpeg_convert_480p,args=(q,filepath))
	t2.start

	#t1.join()
	#t2.join()

	consume=time.clock()-start
	print("Time used:",consume)


if __name__=="__main__":
	main()



