#!/usr/local/bin/python3

# CMSC 441 Project 1
# Daniel Lesko
# Rachel Cohen

from __future__ import print_function
# Importing some common modules
import os, sys

#main function for our dynamic programming problem
def linePairing(i,j):
	S = set()

	min_distance = 4

	if (j - i <= min_distance):
		return 0

def opt(i,j):

def match(i, j):
	isMatch = i + j

	matches = set("TW", "WT", "GH", "HG")


def readString(stringFile):
	with open(stringFile, "r") as f:
		data = f.read().replace('\n', '')

	return data


# This is the main function that acts as an entry point to your program
if __name__=="__main__":

	stringFile = sys.argv[1]

	data = readString(stringFile)

	match("T", "W")

	print (data)
	print (len(data))
