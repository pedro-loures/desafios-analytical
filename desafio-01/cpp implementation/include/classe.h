#ifndef UTILS 
#define UTILS

#include <iostream>
#include <string>

using namespace std;


struct fields field =
{
    char *[] title;
    char *[] artist;
    char *[] album;
    int year;
    char *[] comment;
    int track;
}


static struct option long_options[] =
{
    {"title", required_argument, NULL, 't'},
    {"artist", required_argument, NULL, 'a'},
    {NULL, 0, NULL, 0}
};



#endif
