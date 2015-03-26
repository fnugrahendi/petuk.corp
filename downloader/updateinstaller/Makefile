EXE = updateinstaller

CFLAGS   =
CPPFLAGS = -Wall -Wextra
CXXFLAGS = -Wall -Wextra -std=c++11

#~ ifdef SYSTEMROOT
#~ 	LDFLAGS  = -DWINDOWS
#~ else
#~ 	LDFLAGS = -DLINUX
#~ endif
LDFLAGS  = -DWINDOWS

INCLUDE = 

CPPFILES   = $(shell find src -maxdepth 1 -type f -name '*.cpp')
CPPOBJECTS = $(CPPFILES:.cpp=.opp)
CXXFILES   = $(shell find src -maxdepth 1 -type f -name '*.cxx')
CXXOBJECTS = $(CXXFILES:.cxx=.oxx)

SOURCES = $(CXXFILES) $(CPPFILES)
OBJECTS = $(CXXOBJECTS) $(CPPOBJECTS)


all: $(EXE)
	# Mbuh pie dadine kui mau wkwkwk

$(EXE): $(OBJECTS)
	# Linking...
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $(EXE) $(LDFLAGS)

src/%.opp: src/%.cpp
	# Compiling $<...
	$(CXX) $(CPPFLAGS) $(INCLUDE) $(LDFLAGS) $< -c -o $@
	
src/%.oxx: src/%.cxx
	# Compiling $<...
	$(CXX) $(CXXFLAGS) $(INCLUDE) $(LDFLAGS) $< -c -o $@
	
src/%.o: src/%.c
	# Compiling $<...
	$(MUTE)$(CC) $(CFLAGS) $(INCLUDE) $< -c -o $@

run: all
	$(MUTE)./$(EXE)

clean:
	# Cleaning...
	rm -f $(EXE) $(OBJECTS)

