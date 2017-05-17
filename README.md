# Description
**GStation-Edit** is a linux replacement for the Windows based J-Edit software
from Johnson Amplification. J-Edit is an interface for the J-Station guitar /
bass amp modeling and effect processing system.
The original J-Edit doesn't work properly with Wine. Communication is ok,
but the UI isn't. See http://appdb.winehq.org/objectManager.php?sClass=version&iId=12067

GStation-Edit is already usable, though it lakes functionalities (see TODOs i
sources and Not supported yet section below). Current architecture is sufficient
to support every missing functionalities easily.

# Screenshots
## With default GNOME theme
![Default theme](assets/gstation-edit_default-theme.png)
<br/>
## With dark GNOME theme
![Dark theme](assets/gstation-edit_dark-theme.png)


# Features
- (auto-)connect to a valid J-Station unit.
- Load user's bank from the J-Station.
- Modify parameters from the UI and get feedback from the J-Station.
- Modify parameters from the J-Station and update the UI accordingly.
- Change program from the UI.
- Change program from the J-Station.
- Rename a program from the contextual menu. Note that the new name will not be
changed in the J-Station by now since store is not implemented yet.
- Track changes with a * in the bank list. GStation-Edit clears the flag when
initial values are restored (just like the Store button's LED on the J-Station).


# Not supported yet
- Apply changes to a program when changing program from the UI. Need to check
the actual behavior in J-Edit. FTM, just use the Store button on the J-Station.
- The following items in the program list's contextual menu : store and reload
a program, export and import a program, copy / paste.
- Global parameters (digital output level, MIDI merge, ...) These parameters are
loaded during initialization, I only need to build a UI component for them.
- Scale widgets display raw values. Actual units should be displayed instead
(such as dB, ms, etc.)
- Scale widgets will not get to their full range.
- Factory banks are selectable from the J-Station, but will not be reflected
in the UI. I don't remember how this works in J-Edit.
- Only firmware 2.0 is supported (I updated mine a long time ago). However,
very few messages gstation-edit uses are specific to this version.
For the moment, I think ReceiveProgramUpdateRequest is the only one.
The architecture could easily be adapted to previous version.
I don't have a unit to test this (and I don't want to downgrade mine :).


# How to run gstation-edit
## Dependencies
Make sure your system includes the following dependencies:
- python-2.7 or higher
- GTK 3.16 or higher
- gobject-introspection
- pyalsa or python-alsa

## Runing from source
You can launch GStation-Edit from the download root directory:
``` bash
$ ./gstation-edit
```

## Install
You can install gstation-edit in order to integrate with your DE.
After the installation, there should be a "GStation-Edit" entry in
the Audio and Video menu.
### User install
From the dowload root directory:
``` bash
$ ./setup.py install --user
```
### System wide install
From the dowload root directory:
``` bash
# sudo ./setup.py install
```
