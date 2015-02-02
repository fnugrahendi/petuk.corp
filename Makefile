UIFILES = $(shell find * -maxdepth 2 -type f -name '*.ui')
EXE = Garvin

PYC = pyinstaller
UIC = pyuic4
RCC = pyrcc4
SOURCES = $(UIFILES:.ui=.py)

%.py: %.ui
	$(UIC)  $< -o $@

guiconvert:
	pyuic4 GUI.ui -o GUI.py

kasbank:
	pyuic4 kasbank/ui_kasbank.ui -o kasbank/ui_kasbank.py
all: $(SOURCES)
	# kompile library yg diprogram pakai cpp di folder garvinlibrary
	make -C garvinlibrary/src all
	# Mbuh piye dadine kui mau wkwk
	
rcconvert:
	pyrcc4 DataMaster.qrc -o DataMaster_rc.py

binary:
	$(PYC) $(EXE).py 
	cp data --recursive dist/Garvin/

commit:
	git commit -a
	
#########~ all: rcconvert guiconvert 
