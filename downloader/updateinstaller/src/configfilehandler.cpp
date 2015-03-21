/**-- makin 18 March 2015 
 * copyright (c) Stechoq 2015
 * **/
 
#include <iostream>
#include <fstream>
#include "ConfigfileHandler.h"


ConfigfileHandler::ConfigfileHandler(std::string binpath, std::string configfilename="garvinbin.dat")
{
	ConfigfileHandler::FilePath = std::string(binpath+configfilename);
	
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
			unsigned int i=0;
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


void ConfigfileHandler::Setconfig(std::string configname, std::string configvalue)
{
	ConfigfileHandler::Load();
	int index = ConfigfileHandler::ConfigIndex(configname);
	if (index!=255)
	{
		std::string key;
		size_t posisi = std::string::npos;
		std::string bagianatas;
		std::string bagianbawah;
		std::string encodeddata("");
		std::string lbaris("");
		
		key = ConfigfileHandler::ConfigKey[index]; 
		posisi = ConfigfileHandler::UserData.find(key);
		if (posisi!=std::string::npos)
		{
			/// Sudah ada, sehingga mengedit
			///--- Ambil bagian atas dan bawah dari konfig ini,
			bagianatas = ConfigfileHandler::UserData.substr(0,posisi-1);///-- Dikurangi satu untuk karakter titikdua
			bagianbawah = ConfigfileHandler::UserData.substr(posisi+1);
			bagianbawah = bagianbawah.substr(bagianbawah.find("\n")+1);
			posisi = bagianbawah.find(key);
			while (posisi!=std::string::npos)
			{
				bagianbawah = bagianbawah.substr(bagianbawah.find("\n")+1);
				posisi = bagianbawah.find(key);
			}
			///-- satu kali lagi
			bagianbawah = bagianbawah.substr(bagianbawah.find("\n")+1);
		}
		else
		{
			///belum ada, sehingga bagian atas kasih orinya saja
			bagianatas = ConfigfileHandler::UserData;
		}
		///--- sekarang silahkan menulis
		encodeddata = "";
		int i;
		for (i=0;i<configvalue.length();i++)
		{
			int charvalue;
			charvalue = (int)configvalue[i];
			encodeddata.append(1,ConfigfileHandler::hexchar[charvalue/16]);
			encodeddata.append(1,ConfigfileHandler::hexchar[charvalue%16]);
		}
		///-- bila encoded data lebih besar dari 42 karakter (intel ihex) maka dibagi dalam n baris
		lbaris = encodeddata;///-- kopi encoded data ke lbaris, 
		encodeddata = ":";
		while (lbaris.length()>42) ///-- selama baris terakhir masih lebih besar dari 42 karakter (intel ihex) maka dibagi dalam n baris
		{
			encodeddata = encodeddata + key +std::string("\n:")+lbaris.substr(0,42)+std::string("\n:");
			lbaris = lbaris.substr(42);
		}
		
		while (lbaris.length()<42) ///--selanjutnya fill up baris terakhir genap 42 karakter
		{
			lbaris = lbaris + std::string("0");
		}
		encodeddata = encodeddata + key +std::string("\n:")+lbaris.substr(0,42)+std::string("\n");///-- tambah newline juga di akhir
		
		ConfigfileHandler::UserData = bagianatas + encodeddata + bagianbawah;
		std::cout<<ConfigfileHandler::UserData;
	}
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
