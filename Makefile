UIFILES = $(shell find * -maxdepth 2 -type f -name '*.ui')
EXE = Garvin

PYC = pyinstaller
UIC = pyuic4
RCC = pyrcc4
SOURCES = $(UIFILES:.ui=.py)

%.py: %.ui
	$(UIC)  $< -o $@
	# siki nek nyeluk all, nganti sing kene2 di compile juga, tapi hanya nek ono perubahan

guiconvert:
	pyuic4 GUI.ui -o GUI.py

kasbank:
	pyuic4 kasbank/ui_kasbank.ui -o kasbank/ui_kasbank.py
all: $(SOURCES)
	# Mbuh piye dadine kui mau wkwk                                                                                                  Nek kosong berarti ora ono perubahan
	
rcconvert:
	pyrcc4 DataMaster.qrc -o DataMaster_rc.py

binary:
	$(PYC) $(EXE).py 
	cp data --recursive dist/Garvin/ #test sampai sini

commit:
	git commit -a
	
#########~ all: rcconvert guiconvert 
