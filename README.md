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
* FUSE 2.6 (or later) ,[FUSE for OS X](http://osxfuse.github.io/)

metafuse.py came mostly from http://github.com/terencehonles/fusepy/blob/master/examples/memory.py

fuse.py came from [fusepy](http://github.com/terencehonles/fusepy)

## Usage
1. install requests
1. git clone https://github.com/utamaro/MetaFuse.git
or just copy [fuse.py](https://raw.githubusercontent.com/utamaro/MetaFuse/master/fuse.py) and [metafuse.py](https://raw.githubusercontent.com/utamaro/MetaFuse/master/metafuse.py)
1. mkdir test
1. /metafuse.py test

## Install
just run, no need to install.

## Contribution
Feel free to make any improvements, and to pull requests. Any comments are welcomed.

## !!!Warnings!!!
1. THIS TOOL IS ONLY FOR REFERENCE.
1. Never trust this tool. Never use this tool for practical uses.
1. Every time you write files, these are uploaded to MetaDisk. So this tool is very inefficient. Don't handle large files, or it costs too much.
1. I checked only write/create/read files, and didn't check symlink, directory-related operations, and others.
1. Even if you delete files, these are NOT deleted from MetaDisk NOW.  Don't create and delete files too frequently, or MetaDisk will be MetaGarbage. I understood that when  MetaDisk will start to work officially and no heartbeats occurs, garbage files will be deleted.

## To improve more
* Implementing Partial write/read. to do this, MetaDisk API must support partial uploading/downloading.
* peridical uploading/downloading at sync timing of disk.

## Background
Most cloud strage services don't provide mounting for free plan because when evil people mount cloud strage, they write and read many many garbage data. But on MetaDisk, they don't want to do this becase it costs a lot. When free causes 'tragedy of commons', nothing will be more expensive than free.

I think many people want to use files on the net as if these are on their local file as cheaper as possible. Nobody want to download full 2 hours movie data to view a part of it for 1 minute, but they may want to use their favourite and native movie viewer, not in browser. One may want to get huge logs temporarily on one board computer, like raspberry pie, which is difficult to have additional HDD.

I hope this tool will be a proof of concept of my thought above, and
when Storj/MetaDisk will be wildly used, I hope the concept will help more talent developers than me ^^).
(But maybe anybody can come up with this  kind of tool, so this tool has no meaning...)


## Licence
BSD license

