#!/usr/local/bin/python3

# CMSC 441 Project 1
# Daniel Lesko
# Rachel Cohen

from __future__ import print_function
# Importing some common modules
import os, sys
import numpy as np

#main function for our dynamic programming problem
def linePairing(data):
	S = set()
	dataLength = len(data)
	OPT_array = createArray(dataLength)

	for k in range(min_distance, dataLength):
		for i in range(dataLength - k):
			j = i + k
			OPT_array[i][j] = opt(i, j, data)


def opt(i,j, data):
	
	if (i >= j - min_distance):
		return 0

	else:
		notPaired = opt(i, j-1, data)

		best = -1;

		for t in range(i, j-4):
			if (matchFn(data[t], data[j])):
				temp = (1 + opt(i, t-1, data) + opt(t+1, j-1, data))
				if temp > best:
					best = temp
		paired = best

		return max(notPaired, paired)

def createArray(dataLength):
	OPT_array = np.empty((dataLength,dataLength))
	OPT_array[:] = np.NAN

	for k in range(1, min_distance):
		for i in range(dataLength-k):
			j = i+k
			OPT_array[i][j] = 0
	return OPT_array

def matchFn(i, j):
	isMatch = i + j

	matches = set(["TW", "WT", "GH", "HG"])

	if isMatch in matches:
		print ("Yes")
		return True
	else:
		print ("No")
		return False


def readString(stringFile):
	with open(stringFile, "r") as f:
		data = f.read().replace('\n', '')

	return data

min_distance = 4 

# This is the main function that acts as an entry point to your program
if __name__=="__main__":

	stringFile = sys.argv[1]

	data = readString(stringFile)

	linePairing(data)

	#matchFn("T", "W")

	print (data)
	print (len(data))
