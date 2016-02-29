#!/usr/bin/python
import urllib
import argparse
'''
	A script to download WSDC profile picture of any student @NITW
	example
	python wsdc_profilepic.py <start_regno>
'''
_dir=''
url = 'http://wsdc.nitw.ac.in/student/assets/upload/thumbs/'
def download(id):
	d_url = url+id+'.jpg'
	path = _dir+id+'.jpg'
	# print 'downloaded '+path
	urllib.urlretrieve(d_url, path)

parser = argparse.ArgumentParser()
parser.add_argument('regno', help='Enter Starting Regno of Your First Year Section')
parser.add_argument('-p', '--path', dest='path', help='path from script directory')
args = parser.parse_args()
start = args.regno[:-2]
if args.path:
	_dir = args.path
if args.regno:
	for i in range(1, 10):
		download(start+'0'+str(i))
	for i in range(10, 81):
		download(start+str(i))
