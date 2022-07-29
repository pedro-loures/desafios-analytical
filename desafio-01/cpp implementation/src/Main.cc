// Author: Pedro Loures Alzamora
// Description: Removes white background from digitalizations

// General
// TODO list


// remove white
// TODO list
// -0 OK get parameters from argv
// -1 TODO Read Image 
// -2 TODO Apply exponential filter
// -3 TODO Scan image using the image mean as a threshold
// -4 TODO Apply local filter
// -5 TODO Convolute image
// -6 TODO Get min rectangle
// -7 TODO expand/reduce min rectangle (with/whithout padding)
// -EXTRA minimum quadrange to correct perspective
// -EXTRA separete documents 

#include <iostream>
#include <fstream>
#include <string>
#include <string.h>


#include "utils.h"

using namespace std;

int reduce_factor = 7;
int filter_size = 10;
int filter_sensibility = 15;
int convolution_factor = 20;
int padding = 15;
float scan_threshold = 0.5;
std::string image_file = "";


int main(int argc, char* argv[]) {
  // process the arguments
  ProcessArgs(argc, argv);

  printf("teste\n");
  return 0;
}
