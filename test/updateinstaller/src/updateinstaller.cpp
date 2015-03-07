#include <string>
#include <iostream>
#include <stdio.h>
#include <csignal>

#include <fstream>

#define WINDOWS
#ifdef WINDOWS
#define popen _popen
#define pclose _pclose

#endif
#define umpomo if

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

int main(int argc, char* kvlt[])
{
	//~ std::cout<<exec(argkvlt[1])<<"\n";
	//~ std::cin>>argc;
	//~ std::cout<<argc<<"\n";
	//~ for (int x=0;x<argc;x++)
	//~ {
		//~ std::cout<<x<<" "<<kvlt[x]<<"\n";
	//~ }
	//~ std::cin>>argc;
	//~ std::string isi = kvlt[1];
	//~ std::string cari = kvlt[2];
	//~ std::size_t found = isi.find(cari);
	
	bool downloaddone=true;
	for (int x=1;x<argc;x++)
	{		
		try
		{
			std::string line;
			std::ifstream myfile (kvlt[x]);
			if (myfile.is_open())
			{
				bool thisfiledone = false;
				while ( std::getline (myfile,line) )
				{
					if (line.find("saved")!=std::string::npos)
					{
						///-- ketemu
						std::cout<<"file "<<kvlt[x]<<" sudah selesai didownload \n";
						thisfiledone = true;
					}
				}
				myfile.close();
				if (!thisfiledone) ///nek thisfiledone jangan buat downloaddone=false
				{
					std::cout<<"file "<<kvlt[x]<<" belum selesai didownload \n";
					downloaddone = false;
				}
			}
			else
			{
				std::cout<<"file "<<kvlt[x]<<" belum mulai didownload \n";
				downloaddone = false;
			}
		}
		catch (...)
		{
			;;
		}
	}
	umpomo (downloaddone)
	{
		std::cout<<"rampung kabeh, extraksi hendakny\n";
	}
	std::cin>>argc;
	return (0);
}
