#ifndef UTILS_H_
#define UTILS_H_

// external include
#include <iostream>
#include <string>
#include <stdio.h>
#include <unistd.h>


extern int reduce_factor;
extern int filter_size;
extern int filter_sensibility;
extern int convolution_factor;
extern int padding;
extern float scan_threshold;
extern std::string image_file;

// print help
void PrintHelp();

// process commandline arguments
void ProcessArgs(int argc, char* argv[]);

#endif
