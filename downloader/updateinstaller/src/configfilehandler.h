/**-- makin 18 March 2015 
 * copyright (c) Stechoq 2015
 * **/
#include <iostream>
#include <fstream>
#include <vector> 

#ifndef CONFIGFILEHANDLER_HAH
#define CONFIGFILEHANDLER_HAH

class ConfigfileHandler{
public:
	std::fstream File;
	std::string FilePath;
	//~ static std::string ConfigKey[4];
	
	const std::string ConfigKey[4] = {	"FILE VERSION", 
										"LAST LOGIN", 
										"1011D2004C4C204B4542414200434F43412D434F2B", 
										"101262004472696E6B202020202020202020202024"
										};
	static const int ConfigKeyN = 2;
	std::string UserData; /** The Data Saved Here **/
	
	ConfigfileHandler(std::string, std::string);
	void Load();
	std::string Getconfig(std::string); /** Read Config **/
	void Setconfig(std::string, std::string);
private:
	int ConfigIndex(std::string);
	const std::string hexchar = "0123456789ABCDEF";
};

template<typename T, size_t N>
T * end(T (&ra)[N]) {
    return ra + N;
}



#endif
