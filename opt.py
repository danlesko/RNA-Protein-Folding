#!/usr/local/bin/python3

# CMSC 441 Project 1
# Daniel Lesko
# Rachel Cohen

from __future__ import print_function
# Importing some common modules
import os, sys
import numpy as py

#main function for our dynamic programming problem
def linePairing(data):
	dataLength

	min_distance = 4

	if (j - i <= min_distance):
		return 0

def opt(i,j):
	pass

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


# This is the main function that acts as an entry point to your program
if __name__=="__main__":

	stringFile = sys.argv[1]

	data = readString(stringFile)

	matchFn("T", "W")

	print (data)
	print (len(data))
