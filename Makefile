guiconvert:
	pyuic4 GUI.ui -o GUI.py

all: rcconvert guiconvert 

rcconvert:
	pyrcc4 DataMaster.qrc -o DataMaster_rc.py

guib:
	pyuic4 GUI_b.ui -o GUI.py

build:
	pyinstaller UGM_Akunting.py --icon p.ico

commit:
	git commit -a
	
all: rcconvert guiconvert 
