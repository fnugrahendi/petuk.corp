UIFILES = $(shell find * -maxdepth 2 -type f -name '*.ui')
EXE = Garvin

PYC = pyinstaller
UIC = pyuic4
RCC = pyrcc4
SOURCES = $(UIFILES:.ui=.py)

%.py: %.ui
	$(UIC)  $< -o $@

all: $(SOURCES)
	# Mbuh piye dadine kui mau wkwk
	
clean: 
	rm -f $(SOURCES)

binary:
	$(PYC) $(EXE).py  --distpath=../bin/ -w
	mv ../bin/Garvin/* ../bin/

commit:
	git commit -a
	
#########~ all: rcconvert guiconvert 
