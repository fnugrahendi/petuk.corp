![petuk100](https://cloud.githubusercontent.com/assets/6647566/5687789/0079917a-9883-11e4-9316-f692b5e60a5c.png)


Njemput
============
Contact goodel.akunting@gmail.com

Bug:
* issue issues

`Important Folder hierarchy`
```

- petuk.corp (root folder)

  - bin (binary file)

  - data (user-data folder)

  - image (resource folder)

  - source (source file)
  
  - mysql (3rd party database engine root folder, containing bin & other folders)
    
    - bin (mysql binary)
    
  - downloader (other component & 3rd party software)
  
    - updateinstaller (Garvin's updater program, binary stored here)
      
      - src (updateinstaller source)
      
    - wget_win (wget downloader)
    
    - 7z_win (7zip archive extractor)

```

building
`make all`
`make binary`
`make -C installer/pysource/source all`
`make -C installer/pysource/source binary`
`make -C downloader/updateinstaller all`
