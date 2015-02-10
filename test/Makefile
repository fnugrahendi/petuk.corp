UIFILES = $(shell find * -maxdepth 2 -type f -name '*.ui')
QRCFILES= $(shell find * -maxdepth 2 -type f -name '*.qrc')
EXE = Garvin

PYC = pyinstaller
UIC = pyuic4
RCC = pyrcc4
SOURCES = $(UIFILES:.ui=.py)
RESOURCES=$(QRCFILES:.qrc=._rc.py)

%.py: %.ui
	$(UIC)  $< -o $@

%._rc.py: %.qrc
	$(RCC) $< -o $(@:._rc.py=_rc.py)

all: $(SOURCES)
	# Mbuh piye dadine kui mau wkwk

rcc: $(RESOURCES)

clean: 
	rm -f $(SOURCES)

binary:
	rm -fr ../bin/*
	$(PYC) $(EXE).py -i garvin.ico --distpath=../bin/ -w
	mv ../bin/Garvin/* ../bin/

commit:
	git commit -a
	
#########~ all: rcconvert guiconvert 
