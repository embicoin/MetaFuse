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

metafuse.py came mostly from http://github.com/terencehonles/fusepy/blob/master/examples/memory.py

fuse.py came from [fusepy](http://github.com/terencehonles/fusepy)

## Usage
1. install requests
1. git clone https://github.com/utamaro/MetaFuse.git
1. mkdir test
1. /metafuse.py test

## Install
just run, no need to install.

## !!!Warnings!!!
1. THIS TOOL IS ONLY FOR REFERENCE.
1. Never trust this tool. Never use this tool for practical uses.
1. Every time you write files, these are uploaded to MetaDisk. So this tool is very inefficient. Don't handle large files, or it costs too much.
1. I checked only write/create/read files, and didn't check symlink, directory-related operations, and others.
1. Even if you delete files, these are NOT deleted from MetaDisk. Don't create and delete files too frequently, or MetaDisk will be a MetaGarbage. I don't know how to delete files from MetaDisk. Please inform me if you know.


## Licence
BSD license


## Author
[utamaro](https://github.com/utamaro)
