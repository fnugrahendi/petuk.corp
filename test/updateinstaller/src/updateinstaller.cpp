#include <string>
#include <iostream>
#include <stdio.h>
#define WINDOWS
#ifdef WINDOWS
#define popen _popen
#define pclose _pclose

#endif


std::string exec(char* cmd) {
    FILE* pipe = popen(cmd, "r");
    if (!pipe) return "ERROR";
    char buffer[128];
    std::string result = "";
    while(!feof(pipe)) {
    	if(fgets(buffer, 128, pipe) != NULL)
    		result += buffer;
    }
    pclose(pipe);
    return result;
}

int main(int argc, char* argkvlt[])
{
	std::cout<<argkvlt[0]<<"\n";
	return (0);
}
