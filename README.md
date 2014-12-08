MetaFuse
====

[MetaDisk](http://metadisk.org/) on [FUSE(Filesystem in Userspace)](http://fuse.sourceforge.net/)

## Description
You can mount MetaDisk on your local disk. You can use MetaDisk as if it is on your local storage.
After you run metefuse.py and write files to mounted directory, the files and file informations are uploaded automatically to MetaDisk.
And even once metafuse.py is stopped and restart, files are restored from MetaDisk automatically.

## Requirement
* linux kernel supporting FUSE, maybe MacOS(I didn't check )
* python3
* ["requests" module](http://docs.python-requests.org/en/latest/)
* FUSE 2.6 (or later) , or [FUSE for OS X](http://osxfuse.github.io/)

metafuse.py came mostly from http://github.com/terencehonles/fusepy/blob/master/examples/memory.py

fuse.py came from [fusepy](http://github.com/terencehonles/fusepy), and is not modified.

## Usage
1. install requests
1. git clone https://github.com/utamaro/MetaFuse.git
or just copy [fuse.py](https://raw.githubusercontent.com/utamaro/MetaFuse/master/fuse.py) and [metafuse.py](https://raw.githubusercontent.com/utamaro/MetaFuse/master/metafuse.py)
1. mkdir test
1. /metafuse.py test
1. any files you write in ./test directory will be uploaded to MetaDisk.
1. stop metafuse.py by ctrl-c and restart. you can access files you created in previous step.

## Install
just run, no need to install.

## Contribution
Feel free to make any improvements, and to pull requests. 

## !!!Warnings!!!
1. THIS TOOL IS ONLY FOR REFERENCE.
1. Never trust this tool. Never use this tool for practical uses.
1. Every time you write files, these are uploaded to MetaDisk. So this tool is very inefficient. Don't handle large files, or it costs too much.
1. I checked only write/create/read files, and didn't check symlink, directory-related operations, and others.
1. Even if you delete files, these are NOT deleted from MetaDisk NOW.  Don't create and delete files too frequently, or MetaDisk will be MetaGarbage. I think some actions to MetaDisk are needed not to heartbeat to needless files, but I don't know how.
 
## For improvement
* Implementing Partial write/read. to do this, MetaDisk API must support partial uploading/downloading.
* peridical uploading/downloading at a "certain" timing. (But it's very difficult to balance upload/download cost, memory usage and risk of lost file.)

## Licence
BSD license

