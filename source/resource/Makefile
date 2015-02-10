UIFILES= $(shell find * -maxdepth 2 -type f -name '*.ui')
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
	$(RCC) $< -o ../../image/$(@:._rc.py=_rc.py)

all: $(SOURCES) $(RESOURCES)

rcc: $(RESOURCES)

clean: 
	rm -f $(RESOURCES)
	rm -f $(SOURCES)
