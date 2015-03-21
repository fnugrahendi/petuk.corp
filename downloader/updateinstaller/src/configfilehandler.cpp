/**-- makin 18 March 2015 
 * copyright (c) Stechoq 2015
 * **/
 
#include <iostream>
#include <fstream>
#include "ConfigfileHandler.h"


ConfigfileHandler::ConfigfileHandler(std::string basepath, std::string configfilename="garvinbin.dat")
{
	ConfigfileHandler::FilePath = std::string(basepath+std::string("bin/")+configfilename);
}

void ConfigfileHandler::Load()
{
	ConfigfileHandler::File.open(ConfigfileHandler::FilePath.data(), std::fstream::in);
	std::string _temp;
	ConfigfileHandler::UserData = "";
	while(std::getline(File, _temp)) 
	{
		ConfigfileHandler::UserData = ConfigfileHandler::UserData + _temp + "\n";
	}
	ConfigfileHandler::File.close();
}

std::string ConfigfileHandler::Getconfig(std::string configname)
{
	ConfigfileHandler::Load();
	int index = ConfigfileHandler::ConfigIndex(configname);
	if (index!=255)
	{
		std::string key = ConfigfileHandler::ConfigKey[index];
		std::string configdata;
		std::string temp;
		size_t posisi=std::string::npos;
		posisi = ConfigfileHandler::UserData.find(key);
		while (posisi!=std::string::npos)
		{
			std::string configline;
			posisi = posisi + key.length()+ 2; //\n dan :
			configline = ConfigfileHandler::UserData.substr(posisi,key.length());
			///langsung translate tiap line dari hexa decimal ke char (8bit)
			int i=0;
			while (i<key.length())
			{
				unsigned char karakter;
				int nilaikarakter;
				///#-- hitung jadi karakter
				nilaikarakter = ConfigfileHandler::hexchar.find(configline[i])*16;
				nilaikarakter = nilaikarakter + ConfigfileHandler::hexchar.find(configline[i+1]);
				karakter = nilaikarakter;
				configdata.append(1,karakter);
				i+=2;
			}
			posisi = ConfigfileHandler::UserData.find(key,posisi);
		}
		return configdata;
	}
	return std::string("");
}



int ConfigfileHandler::ConfigIndex(std::string configname)
{
	int i;
	for (i=0;i<(ConfigfileHandler::ConfigKeyN);i+=1)
	{
		if (ConfigfileHandler::ConfigKey[i]==configname)
		{
			return ConfigfileHandler::ConfigKeyN+i;
		}
	}
	return 255;
}
