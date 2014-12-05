MetaFuse
====

[MetaDisk](http://metadisk.org/) on [FUSE(Filesystem in Userspace)](http://fuse.sourceforge.net/)

## Description
You can mount MetaDisk on your local disk. You can use MetaDisk as if it is on your local storage.
After you run metefuse.py and write files to mounted directory, the files and file informations are uploaded automatically to MetaDisk.
And even once metafuse.py is stopped and restart, files are restored from MetaDisk automatically.

## Requirement
* linux kernel supporting FUSE
* requests python module
* FUSE 2.6 (or later) 

## Usage
1. install requests
1. git clone https://github.com/utamaro/MetaFuse.git
1. mkdir test
1. /metafuse.py test

## Install
just run, no need to install.

## Restriction
1. THIS TOOL IS ONLY FOR REFERENCE.
1. Never trust this tool. Never use this tool for actual use.
1. Every time you write files, these are uploaded to MetaDisk. So this tool is very inefficient. Don't edit large files, or it costs too much.
1. I checked only write/create/read files, and didn't check symlink, directory-related operations.

## Licence
BSD license


## Author
[utamaro](https://github.com/utamaro)
