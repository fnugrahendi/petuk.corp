EXE = updateinstaller

CFLAGS   = 
CXXFLAGS = -Wall -Wextra 
LDFLAGS  = 

INCLUDE = 

CXXFILES   = $(shell find src -maxdepth 1 -type f -name '*.cpp')
CXXOBJECTS = $(CXXFILES:.cpp=.o)

SOURCES = $(CXXFILES)
OBJECTS = $(CXXOBJECTS)


all: $(EXE)
	# Mbuh pie dadine kui mau wkwkwk

$(EXE): $(OBJECTS)
	# Linking...
	$(MUTE)$(CXX) $(OBJECTS) -o $(EXE) $(LDFLAGS)

src/%.o: src/%.cpp
	# Compiling $<...
	$(MUTE)$(CXX) $(CXXFLAGS) $(INCLUDE) $< -c -o $@
	$(BUILD)

src/%.o: src/%.c
	# Compiling $<...
	$(MUTE)$(CC) $(CFLAGS) $(INCLUDE) $< -c -o $@

run: all
	$(MUTE)./$(EXE)

clean:
	# Cleaning...
	-$(MUTE)rm -f $(EXE) $(OBJECTS)

