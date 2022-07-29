#ifndef UTILS_H_
#define UTILS_H_

// external include
#include <iostream>
#include <string>
#include <stdio.h>
#include <unistd.h>

/*********** /include ***********/
/************ define ***********/

#define DEF_REDUCE_FACTOR 7
#define DEF_FILTER_SIZE 10
#define DEF_FILTER_SENSIBILITY 15
#define DEF_CONVOLUTION_FACTOR 20
#define DEF_PADDING 15
#define DEF_SCAN_TRESHOLD 0.5
/*********** /define ***********/
/******** global variables ***********/


extern int reduce_factor;
extern int filter_size;
extern int filter_sensibility;
extern int convolution_factor;
extern int padding;
extern float scan_threshold;
extern std::string image_file;

/******** /global variables ***********/
/******* function calls ********/
// print help
void PrintHelp();

// process commandline arguments
void ProcessArgs(int argc, char* argv[]);

#endif
