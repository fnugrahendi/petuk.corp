#include <string>
#include <iostream>
#include <stdio.h>
#include <csignal>
#include <fstream>
#define uint32_t unsigned int

//~ #define WINDOWS
#ifdef WINDOWS
	#define popen _popen
	#define pclose _pclose
	#include <windows.h>
	#define delay(x) Sleep(x)
	#define CEKPROSES (char*)"wmic process get commandline "
#else
	#include <unistd.h> //posix
	#define delay(x) usleep(x*1000)
	#define CEKPROSES (char*)"ps -ef | grep Garvin"
#endif
	
#define umpomo if
#define nekra else
#define njerone(panggongolek,singdigoleti) panggongolek.find(singdigoleti)!=std::string::npos
#define print(x) std::cout<<x<<"\n"

namespace Garvin{
	#ifndef umpomo
		#define umpomo if
		#define nekra else
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

	std::string replace(std::string apa, std::string denganapa, std::string padaapa)
	{
		size_t posisi;
		posisi = padaapa.find(apa);
		umpomo (posisi==std::string::npos)
		{
			return (padaapa);
		}
		nekra
		{
			return (padaapa.replace(posisi,apa.length(),denganapa));
		}
	}
};

int main(int argc, char* kvlt[])
{
	std::string Path;
	std::string BasePath;
	std::string DataPath;
	std::string SevenZip;
	Path = kvlt[0];
	BasePath = Garvin::replace("updateinstaller.exe","",Path)+"..\\..\\";
	DataPath = BasePath+"data\\";
	SevenZip = BasePath+"downloader\\7z_win\\7z.exe ";
	print(DataPath);
	
	
	bool downloaddone=true;
	do
	{
		downloaddone=true;
		for (int x=1;x<argc;x++)
		{
			try
			{
				std::string line;
				std::ifstream myfile ((DataPath+std::string(kvlt[x])+std::string(".o")).data());///tambah .o manual di program ini... btw digest std::string ke char* dengan method ::data()
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
				}/**if (myfile.is_open())**/
				else
				{
					std::cout<<"file "<<kvlt[x]<<" belum mulai didownload \n";
					downloaddone = false;
				}/**if (myfile.is_open())**/
			}/**try**/
			catch (...)
			{
				;;
			}/**try**/
		}/**for (int x=1;x<argc;x++) // perulangan tiap argumen/file yang dicek**/
		delay(3000);
	}
	while (!downloaddone);
	
	while (njerone(Garvin::exec(CEKPROSES),"Garvin"))
	{
		std::cout<<"download selesai, pemasangan update akan dilakukan bila pengguna sudah siap (sudah menutup Garvin)\n";
		delay(3000);
	}
	std::cout<<"Memasang update\n";
	std::string perintah;
	
	for (int x=1;x<argc;x++)
	{
		std::cout<<"Memasang "<<kvlt[x]<<"... ";
		perintah = SevenZip + " -y x "+(DataPath+std::string(kvlt[x])).data()+" -o\""+BasePath+"\" -pnyungsep";
		std::cout<<Garvin::exec((char *)perintah.data());
		std::cout<<"[OK]\n";
	}
	std::cout<<"Updater selesai\n";
	//~ std::cin>>argc;
	delay(10000);
	return (0);
}
