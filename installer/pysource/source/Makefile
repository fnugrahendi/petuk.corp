UIFILES = $(shell find * -maxdepth 2 -type f -name '*.ui')
PYFILES = $(shell find * -maxdepth 2 -type f -name '*.py')
EXE = installer

PYC = pyinstaller
UIC = pyuic4
RCC = pyrcc4
SED = sed
PYUIC = pyuic4
SOURCES = $(UIFILES:.ui=.py)
PYQTCONVERT = $(PYFILES:.py=.pyqtc)
PYQTREVERT = $(PYFILES:.py=.pyqtr)

%.py: %.ui
	$(UIC)  $< -o $@
all: $(SOURCES)
	# Mbuh piye dadine kui mau wkwk

%pyqtc: %py
	#~ $(SED) s/PySide/PyQt4/ <$< >$<
%pyqtr: %py
	#~ $(SED) s/PyQt4/PySide/ <$< >$<

clean: 
	rm -f $(SOURCES)

pyqtc: $(PYQTCONVERT)
pyqtr: $(PYQTREVERT)

binary:
	rm -fr ../bin/*
	$(PYC) $(EXE).py -F -i ../archive/garvin.ico  --distpath=../bin/
	mv ../bin/$(EXE)/* ../bin/
	rm -rf ../bin/$(EXE)

commit:
	git commit -a
	
#########~ all: rcconvert guiconvert 
