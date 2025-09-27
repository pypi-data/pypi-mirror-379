# Akris Desktop 
## Description
Akris Desktop is a pest station graphical client implemented using the Akris Pest station library.

## Getting Akris Desktop

This guide assumes a working [pentacle](http://problematic.site/src/pentacle/) chroot environment

### Using [V](https://archive.ph/pRfAz)
Download all patches and seals from [v.alethepedia.com/akris_desktop](http://v.alethepedia.com/akris_desktop):

    mkdir -p patches
    mkdir -p seals
    curl -o patches/akris-desktop-genesis-VERSION.vpatch http://v.alethepedia.com/akris/akris-desktop-genesis-VERSION.vpatch
    curl -o seals/akris-desktop-genesis-VERSION.vpatch.thimbronion.sig http://v.alethepedia.com/akris/akris-desktop-genesis-VERSION.vpatch.thimbronion.sig

Pentacle v expects gpg public keys to be found in ~/wot.

Using the bash implementation of v provided in [pentacle](http://problematic.site/src/pentacle/),
press Akris Desktop with the leaf you wish to target (usually the patch with the lowest version number):

    v press akris-desktop patches/akris-desktop-genesis-99999.vpatch

### Download and run the signed binary

    curl -o akris-desktop-VERSION.linux.x86_64.bin https://v.alethepedia.com/akris_desktop/akris-desktop-VERSION.linux.x86_64.bin
    curl -o akris-desktop-VERSION.linux.x86_64.bin.thimbronion.sig https://v.alethepedia.com/akris_desktop/akris-desktop-VERSION.linux.x86_64.bin.thimbronion.sig

#### Run Akris Desktop
    
    ./akris-desktop-VERSION.linux.x86_64.bin

### From PyPI [WIP]

    pip install akris-desktop

### From a signed tarball [WIP]
#### Download and unzip Akris Desktop 
#### Download and unzip Akris

## Build and Install Akris Desktop from source

### Pre-requisites
- Python >= 3.11
- tk
- python3.11-dev

### Dependency installation
#### Debian/Ubuntu
    # These steps may or may not be necessary depending on the state of your system
    sudo apt-get install python3.11-dev
    sudo apt-get install python3-tk
    sudo apt-get install python3-pil python3-pil.imagetk

##### Gentoo [WIP]

### Create a python virtual environment.
This is optional but is recommended to avoid cluttering up your system python site-packages.

#### Create the virtual environment
    cd akris-desktop
    python -m venv venv
    source venv/bin/activate

### Install tk in the virtual environment

    pip install tk

### Install Akris into the virtual environment from a local copy of the source code

    pip install -e file:../akris

### Install Akris Desktop into the virtual environment

    pip install -e .

### Run Akris Desktop

    python3 bin/main.py

### Configure Akris Desktop
Akris desktop is inert on initial startup.  To connect to a configure your station via the console tab:
1. Set your handle (this is the name others must use for you when peering with your station):

    `> handle cortes`
   
2. Enable presence reporting (this will update akris desktop when peers come online or go offline):

    `> knob presence.report_interval 1`
   
3. Set the address cast interval (this is how often your station will broadcast its address to peers):

    `> knob address.cast_interval 1`
     
4. Add a peer:

    `> peer pizarro`
   
5. Generate a symmetric key to share with the peer:

    `> genkey`
   
6. Set the peer's key:

    `> key pizarro <key>`
   
7. Set the peer's address:

    `> at pizarro W.X.Y.Z:12345`

If this pestnet has been around a while, you should start to see messages syncing in the 
'broadcast messages' tab momentarily. If this is a new pestnet, feel free to send the 
first message.

## Development
### Install development dependencies
    pip install .[dev]

### Build a binary distribution
#### Linux
    make dist
#### OSX
    make dist-osx

### Database Management
#### Run new migrations if any have been added
    caribou upgrade akris.db migrations

### Client API Documentation [WIP]
