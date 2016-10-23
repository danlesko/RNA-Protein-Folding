#!/usr/local/bin/python3

# CMSC 441 Project 1
# Daniel Lesko
# Rachel Cohen

from __future__ import print_function
# Importing some common modules
import os, sys
import pprint

#main function for our dynamic programming problem
def linePairing(data):

	S = set()
	dataLength = len(data)

	#create array to store a list of max pairs in a line
	OPT_array = [[-1 for x in range(dataLength)] for y in range(dataLength)]

	#initilize array to 0s where there can be a possible max # of pairs
	for k in range(1, min_distance):
			for i in range(dataLength-k):
				j = i+k
				OPT_array[i][j] = 0

	#main function for our program
	for k in range(min_distance, dataLength):
		for i in range(dataLength - k):
			j = i + k
			OPT_array[i][j] = opt(i, j, data)

	#flip the array so we have opt(1,n) and opt(n,1)
	for i in range(dataLength):
		for j in range(0, i):
			OPT_array[i][j] = OPT_array[j][i]

	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(OPT_array)

def opt(i,j, data):
	
	if (i >= j - min_distance):
		return 0

	else:
		notPaired = opt(i, j-1, data)

		best = -1;

		for t in range(i, j-min_distance):
			if (matchFn(data[t], data[j])):
				temp = (1 + opt(i, t-1, data) + opt(t+1, j-1, data))
				if temp > best:
					best = temp
		paired = best

		return max(notPaired, paired)

def matchFn(i, j):
	isMatch = i + j

	matches = set(["TW", "WT", "GH", "HG"])

	if isMatch in matches:
		#print ("Yes")
		return True
	else:
		#print ("No")
		return False


def readString(stringFile):
	with open(stringFile, "r") as f:
		data = f.read().replace('\n', '')

	return data

#define the max number of pairings that we need between each pair
min_distance = 4 

# This is the main function that acts as an entry point to your program
if __name__=="__main__":

	stringFile = sys.argv[1]

	data = readString(stringFile)

	linePairing(data)

	#matchFn("T", "W")

	print (data)
	print (len(data))
