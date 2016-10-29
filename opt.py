#!/usr/local/bin/python3

# CMSC 441 Project 1
# Daniel Lesko
# Rachel Cohen

from __future__ import print_function
# Importing some common modules
import os, sys
import pprint
import time
import functools

memoOPT={}

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

	#main functionality for our program
	#create OPT_array to store line folding lengths
	start_time = time.time()
	#nested loops for i,j where i must have 4 chars between j
	for i in range(0, dataLength - min_distance):
		for j in range(i+min_distance, dataLength):
			OPT_array[i][j] = opt(i, j, data)
	elapsed_time = time.time() - start_time

	#flip the array so we have opt(1,n) and opt(n,1)
	for i in range(dataLength):
		for j in range(0, i):
			OPT_array[i][j] = OPT_array[j][i]

	path(OPT_array, data, 0, dataLength-1, S)



	#print(sorted(S))
	print(len(S))
	print(elapsed_time)
	#print(memoOPT)
	#pp = pprint.PrettyPrinter(indent=4)
	#pp.pprint(OPT_array)

def opt(i,j, data):

	#return if already exists
	if (i,j) in memoOPT:
		return memoOPT[(i,j)]
	
	if (i >= j - min_distance):
		return 0

	else:
		if (i,j-1) not in memoOPT:
			notPaired = opt(i, j-1, data)
		else:
			notPaired = memoOPT[(i,j-1)]

		best = -1;

		for t in range(i, j-min_distance):
			if (matchFn(data[t], data[j])):

				if (i, t-1) not in memoOPT:
					call1 = opt(i, t-1, data)
				else:
					call1 = memoOPT[(i, t-1)]

				if (t+1, j-1) not in memoOPT:
					call2 = opt(t+1, j-1, data)
				else:
					call2 = memoOPT[(t+1, j-1)]

				temp = (1 + call1 + call2)
				if temp > best:
					#memoOPT[(i,j)] = temp
					best = temp
		paired = best

		memoOPT[(i,j)] = max(notPaired, paired)
		return max(notPaired, paired)

def path(OPT_array, data, i, j, S):

	if i <= j-min_distance:

		#check path under to see if the same
		if OPT_array[i][j] == OPT_array[i+1][j]:
			path(OPT_array, data, i+1, j, S)

		#check path to the left to see if the same
		elif OPT_array[i][j] == OPT_array[i][j-1]:
			path(OPT_array, data, i, j-1, S)

		#check path to the diagonal to check for match
		elif OPT_array[i][j] == OPT_array[i+1][j-1] + matchFn(data[i], data[j]):
			#print ("Found match!")
			S.add((i, j))
			#call opt from new position in matrix
			path(OPT_array, data, i+1, j-1, S)

		#trace path for smaller sub problems
		else:
			for k in range(i, j):
				if OPT_array[i][j] == OPT_array[i][k] + OPT_array[k+1][j]:
					path(OPT_array, data, i, k, S)
					path(OPT_array, data, k+1, j, S)
					break

	return

#function to check and see if there is a pair
def matchFn(i, j):
	isMatch = i + j

	matches = set(["TW", "WT", "GH", "HG"])

	if isMatch in matches:
		#print ("Yes")
		return True
	else:
		#print ("No")
		return False

#function to read in the line of fans
def readString(stringFile, stringLength):
	with open(stringFile, "r") as f:
		data = f.read().replace('\n', '')

		if stringLength != -1:
			data = data[:int(stringLength)]


	return data

#define the max number of pairings that we need between each pair
min_distance = 4 

# This is the main function that acts as an entry point for the program
if __name__=="__main__":

	stringFile = sys.argv[1]

	if (len(sys.argv) > 2):
		stringLength = sys.argv[2]
	else:
		stringLength = -1

	data = readString(stringFile, stringLength)

	linePairing(data)

	# if (0,11) in memoOPT:
	# 	print ("It exists!")

	#matchFn("T", "W")

	print (data)
	print (len(data))


'''
Times

2000 : 1183.7687077522278
1500 : 482.6276047229767
1000 : 139.41797423362732
500  : 17.00997304916382
100  : 0.11900687217712402
90   : 0.08600497245788574
80   : 0.06000351905822754
70   : 0.04200243949890137
60   : 0.026001453399658203
50   : 0.014000654220581055
40   : 0.008000373840332031
30   : 0.0030002593994140625
20   : 0.0010001659393310547
10   : 0.0009999275207519531

http://arachnoid.com/polysolve/




'''

	
