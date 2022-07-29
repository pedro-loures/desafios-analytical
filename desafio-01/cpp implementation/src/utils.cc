/*********** include ***********/
// local include
#include "utils.h"

// external include
#include <iostream>
#include <string>
#include <stdio.h>
#include <unistd.h>
#include <getopt.h>


void PrintHelp()
{
	std::cout <<
			/*0*/ 	"--image_file <i>:              Set path/to/image.jpg"
			/*1*/		"--reduce_factor <r>:         	Set number of times image will be divided\n"
			/*2*/		"--filter_size <f>:            	Set size of the filter as a percentage of the size of the image"
			/*3*/		"--filter_sensibility <s>:      Set sensibility of the filter as a percentage"
			/*4*/		"--convolution_factor <c>:      Set the factor by which the image will be convolutet"
			/*5*/		"--padding <p>:									Set the size of the padding border on the image"
			/*6*/		"--scan_threshold <f>:          Set scan_threshold of program\n"
			/*7*/	"--help:                            Show help\n";
	exit(1);
}

void ProcessArgs(int argc, char *argv[])
{
	const char *const short_opts = "r:f:s:c:p:t:i:h";
	const option long_opts[] = {
			{"image_file", required_argument, nullptr, 'i'},
			{"reduce_factor", optional_argument, nullptr, 'r'},
			{"filter_size", optional_argument, nullptr, 'f'},
			{"filter_sensibility", optional_argument, nullptr, 's'},
			{"convolution_factor", optional_argument, nullptr, 'c'},
			{"padding", optional_argument, nullptr, 'p'},
			{"scan_threshold", optional_argument, nullptr, 't'},
			{"help", no_argument, nullptr, 'h'},
			{nullptr, no_argument, nullptr, 0}};

	while (true)
	{
		const auto opt = getopt_long(argc, argv, short_opts, long_opts, nullptr);

		if (-1 == opt)
			break;

		switch (opt)
		{
		case 'r':
			reduce_factor = std::stoi(optarg);
			std::cout << "reduce_factor set to: " << reduce_factor << std::endl;
			break;

		case 'f':
			filter_size = std::stof(optarg);
			std::cout << "filter_size set to: " << filter_size << std::endl;
			break;

		case 's':
			filter_sensibility = std::stof(optarg);
			std::cout << "filter_sensibility set to: " << filter_sensibility << std::endl;
			break;

		case 'c':
			convolution_factor = std::stof(optarg);
			std::cout << "convolution_factor set to: " << convolution_factor << std::endl;
			break;

		case 'p':
			padding = std::stof(optarg);
			std::cout << "padding set to: " << padding << std::endl;
			break;

		case 't':
			scan_threshold = std::stof(optarg);
			std::cout << "scan_threshold set to: " << scan_threshold << std::endl;
			break;

		case 'i':
			image_file = std::string(optarg);
			std::cout << "Image file set to: " << image_file << std::endl;
			break;

		case 'h': // -h or --help
		case '?': // Unrecognized option
		default:
			PrintHelp();
			break;
		}
	}
}
/******* /function calls ********/
/****** /argument handling ******/