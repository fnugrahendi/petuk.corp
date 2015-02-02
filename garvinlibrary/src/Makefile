## makin 2 Feb 2015: 16.30WIB
CPPFILES = $(shell find * -maxdepth 1 -type f -name '*.cpp')
DLLFILES = $(shell find ../* -maxdepth 1 -type f -name '*.dll')

CXX = g++
SUMBEROBYEK = $(CPPFILES:.cpp=.o)
SUMBERDLL = $(DLLFILES)

# beda compile di linux dan window: 
# 	variabel RM untuk
#		rm di linux, del di windows
#	variable DLLEXPORT untuk
#		.cpp file definisi di windows dan linux beda:
#			linux:		#define DLLEXPORT extern "C" 
#			windows:	#define DLLEXPORT extern "C" __declspec(dllexport) 		
#	FixPath untuk / di linux, \ di windows
ifdef SystemRoot
	RM = del /Q
	FixPath = $(subst /,\,$1)
else
	ifeq ($(shell uname), Linux)
		RM = rm -f
		FixPath = $1
		DLLEXPORT = -DNGANGGOLINUX
	endif
endif

# Kompile ke object file kemudian ke .o.dll
%.o: %.cpp
	$(CXX) $(DLLEXPORT) -c $< -o $@
	$(CXX) -shared -o ../$@.dll $@

clean:
	$(RM) $(SUMBEROBYEK)
	$(RM) $(SUMBERDLL)

kompel: $(SUMBEROBYEK)
all: kompel
	#mbuh piye dadine kui mau wkwk
