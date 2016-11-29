#include <iostream>
#include <fstream>
#include <omp.h>
#include <stdio.h>
#include <string>

using namespace std; 

//define the minimum distance between pairs
const int minDistance = 4;

//initialize a counter for the number of iterations
long iterCnt = 0;

bool matchFn(char i, char j);

void opt(const char* A, int ** optArray, int seqLength);

int main(int argc, char *argv[]) {

	//initialize sequence length based on command line argument
	int seqLength = atoi(argv[2]);

	//take in file and parse command line arguments	
	string dataFile = argv[1];
	string data;
	fstream infile(dataFile.c_str(), ios::in);
	getline(infile, data);
	infile.close();
	const char *dataSeq = data.c_str();

	//define optArray as a matrix used to store the number of pairs between given endpoints
	int ** optArray;

	//define optArray in terms of given data length and iterate through
	optArray = new int*[seqLength];
	for (int i = 0; i < seqLength; i++) {
		optArray[i] = new int[seqLength];
	}
	for (int i = 0; i < seqLength; i++)
		for (int j = 0; j < seqLength; j++)
			optArray[i][j] = 0;

	//call to the opt function
	opt(dataSeq, optArray, seqLength);
	
	//delete the dynamically created array to free up memory
	for (int g = 0; g < seqLength; g++){
		delete[] optArray[g];
	}

	delete [] optArray;
}


//main algorithm
void opt(const char* dataSeq, int ** optArray, int seqLength) {
	
	//timer
	double t0 = omp_get_wtime();

	/* initialize variables
         * 
         * j = ending value in data sequence
         * paired = max number of values between a sequence returned by OPT(i, j-1)
         * notPaired = max number of pairs given an initial pair
         * best = stores best pair up until a given point */

	int notPaired, paired, best, j;

	//iterate from minDistance to given data length
	for (int k = minDistance; k < seqLength; k++) {
		//parallel for loop call to help multithread the algorithm
		#pragma omp parallel for
		for (int i = 0; i < seqLength - k; i++) {
			
			//keeps track of which thread the algorithm is running on
			int threadNum = omp_get_thread_num();
			j = i + k;
			notPaired = optArray[i][j - 1];
			//set the best pair up until this point 
			best = notPaired;
			
			//increase the number of iterations 
			for (int t = i; t < j - minDistance; t++) {

				//statement to count the number of iterations performed with P processors
				if (threadNum == 0){
					iterCnt++;
					}
				
				//if the data is a match, update paired variable
				if (matchFn(dataSeq[t], dataSeq[j])) {
					
					paired = 1 + optArray[i][t - 1] + optArray[t + 1][j - 1];
					
					//if the new paired value is greater than the best up until this point, set it equal to best
					if (paired > best) {
						best = paired;
					}
				}
			}

			optArray[i][j] = best;
		}
	}

	double t = omp_get_wtime() - t0;

	//output results
	cout << "Max pairings: " << optArray[0][seqLength - 1] << endl;
	cout << "Time: " << t << endl;
	cout << "IterCount: " << iterCnt << endl;
}

//define allowable pairs H & G, W & T
bool matchFn(char i, char j) {
	if (i == 'H' && j == 'G')
		return true;
	else if (i == 'G' && j == 'H')
		return true;
	else if (i == 'W' && j == 'T')
		return true;
	else if (i == 'T' && j == 'W')
		return true;
	else
		return false;
}
