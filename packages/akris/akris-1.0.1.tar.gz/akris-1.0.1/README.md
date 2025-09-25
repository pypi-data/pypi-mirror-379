# Akris 

## Description

Akris implements the Pest protocol.  It provides a [station](http://www.loper-os.org/?p=4003#2-the-pest-station) library that can be used 
to connect to a pest network.  It also provides a client library that can be used to issue commands to a station.

This document is a work in progress.

## Getting Akris

### Using [V](https://archive.ph/pRfAz)

This guide assumes a working [pentacle](http://problematic.site/src/pentacle/) chroot environment

#### Press Akris
Download Akris patches and seals from [v.alethepedia.com/akris](https://v.alethepedia.com/akris).

    mkdir -p patches
    mkdir -p seals
    curl -o patches/akris-genesis-VERSION.vpatch http://v.alethepedia.com/akris/akris-genesis-VERSION.vpatch
    curl -o seals/akris-genesis-VERSION.vpatch.thimbronion.sig http://v.alethepedia.com/akris/akris-genesis-VERSION.vpatch.thimbronion.sig

Pentacle v expects gpg public keys to be found in ~/wot.

Using the bash implementation of v provided in [pentacle](http://problematic.site/src/pentacle/),
press Akris with the leaf you wish to target (usually the patch with the lowest version number):

    v press akris patches/akris-genesis-99999.vpatch

### From signed tarball [WIP]

```bash
wget https://v.alethepedia.com/akris/akris-genesis-99999.tar.gz
tar zxvf akris-genesis-99999.tar.gz
cd akris
python -m venv venv
source venv/bin/activate
pip install -e .
```

## Install using a package manager
### From PyPI [WIP]

```bash
pip install akris
```

## Installation from Source

### Setup a virtual environment

In the akris project root directory, run:
```bash
cd akris
python -m venv venv
source venv/bin/activate
```

### Install Akris from source

```bash
pip install -e .
```

### Running Akris

There are several command line options you'll need to set.  You can get a list of them by running akris with the --help option:
```bash
bin/main.py
```

## Development

### Editable install
This will allow tests to find the akris package, while still allowing you to edit the source code
and have the changes be reflected immediately without reinstalling.

```bash
pip install -e .
```

### Install development dependencies

```bash
pip install .[dev] 
```

### Run tests

```bash
make test
```

### Code formatting
    
    black .

### Database Management
#### Create a new migration
    caribou create -d akris/migrations <migration name>

### Create a static binary build
#### Pre-requisites
##### Debian/Ubuntu
    sudo apt-get install patchelf
#### Linux
    make dist
### Creating distribution build
#### Build a PyPI package [WIP]
    python3 -m build
The output will be in the dist/ directory.  Upload to PyPI with twine:
```bash
python3 -m twine upload  dist/*
```