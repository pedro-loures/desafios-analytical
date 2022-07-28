#include "utils.h"


void opcao_usuario(int argc,char* argv[]){
  // loop over all of the options
  while ((ch = getopt_long(argc, argv, "t:a:", long_options, NULL)) != -1)
  {
      // check to see if a single character or long option came through
      switch (ch)
      {
          // short option 't'
          case 't':
              field.title = optarg; // or copy it if you want to
              break;
          // short option 'a'
          case 'a':
              field.artist = optarg; // or copy it if you want to
              break;
      }
  }
}


