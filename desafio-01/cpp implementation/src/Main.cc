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
#include <opencv2/opencv.hpp>

#include "utils.h"

using namespace std;

int reduce_factor = DEF_REDUCE_FACTOR;
int filter_size = DEF_FILTER_SIZE;
int filter_sensibility = DEF_FILTER_SENSIBILITY;
int convolution_factor = DEF_CONVOLUTION_FACTOR;
int padding = DEF_PADDING;
float scan_threshold = DEF_SCAN_TRESHOLD;
std::string image_file = "";


int main(int argc, char* argv[]) {
  // process the arguments
  ProcessArgs(argc, argv);
  string path = "/mnt/c/Users/PLour/OneDrive - Universidade Federal de Minas Gerais/01_Trabalho/MostQI/desafio01/img"

  printf("teste\n");
  return 0;
}
