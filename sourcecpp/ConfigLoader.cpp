#ifdef NGANGGOLINUX
	#define DLLEXPORT extern "C" 
#else
	#define DLLEXPORT extern "C" __declspec(dllexport) 		
#endif

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

DLLEXPORT int tambah(int a, int b)
{
    return a + b;
}

//~ DLLEXPORT string 
