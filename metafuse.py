#!/usr/bin/env python


#this program uses fusepy(http://github.com/terencehonles/fusepy)
#needed library:FUSE 2.6 (or later) 
#needed python modules: requests
#this file is mostly copy of http://github.com/terencehonles/fusepy/blob/master/examples/memory.py


import logging
import requests
import pickle
import sys
import logging
import io
import struct

from collections import defaultdict
from errno import ENOENT
from stat import S_IFDIR, S_IFLNK, S_IFREG
from sys import argv, exit
from time import time

from fuse import FUSE, FuseOSError, Operations, LoggingMixIn

NODE_URL="http://node1.metadisk.org"

if not hasattr(__builtins__, 'bytes'):
    bytes = str

class MetaDiskFS(LoggingMixIn, Operations):
    'Example MetaDisk filesystem. Supports only one level of files, and not support symlink.'

    def __init__(self):
#        logging.basicConfig(filename='metafuse.log',level=logging.DEBUG)
        self.files = {}
        self.token=""
        self.data = defaultdict(bytes)
        self.fd = 0
        now = time()
        self.files['/'] = dict(st_mode=(S_IFDIR | 0o755), st_ctime=now,
                               st_mtime=now, st_atime=now, st_nlink=2)
        self.loadInfo()
        self.getToken()

    def saveInfo(self):
        byteio=io.BytesIO(pickle.dumps(self.files))
        r = requests.post(NODE_URL+"/api/upload", 
                files={'file':("fileInfo.dat",byteio)},data={"token":self.token})
        j=r.json()
        hk=j["filehash"]+"?key="+j["key"]
        logging.debug("filehash+key of fileInfo"+hk)
        f=open("metafuse.dat","w")
        f.write(hk)
        f.close()

    def loadInfo(self):
        try:
            f=open("metafuse.dat")
            r = requests.get(NODE_URL+"/api/download/"+f.readline())
            self.files=pickle.load(io.BytesIO(r.content))
            logging.debug(self.files)
            f.close()
        except IOError as e:
            logging.warning("metafuse.dat not found,continuing...")


    def getToken(self):
        r = requests.post(NODE_URL+"/accounts/token/new")
        self.token=r.json()["token"]
        logging.debug("token="+self.token)

    def upload(self,path):
        byteio=io.BytesIO(self.data[path])
        r = requests.post(NODE_URL+"/api/upload", files={'file':(path,byteio)},
                data={"token":self.token})
        j=r.json()
        self.files[path]["url"]=j["filehash"]+"?key="+j["key"]
        self.saveInfo()
        logging.debug("path="+path+",token="+self.files[path]["url"])

    def download(self,path):
        r = requests.get(NODE_URL+"/api/download/"+self.files[path]["url"])
        self.data[path]=r.content

    def chmod(self, path, mode):
        self.files[path]['st_mode'] &= 0o770000
        self.files[path]['st_mode'] |= mode
        self.saveInfo()
        return 0

    def chown(self, path, uid, gid):
        self.files[path]['st_uid'] = uid
        self.files[path]['st_gid'] = gid
        self.saveInfo()

    def create(self, path, mode):
        self.files[path] = dict(st_mode=(S_IFREG | mode), st_nlink=1,
                                st_size=0, st_ctime=time(), st_mtime=time(),
                                st_atime=time())
        self.fd += 1
        self.saveInfo()
        return self.fd

    def getattr(self, path, fh=None):
        if path not in self.files:
            raise FuseOSError(ENOENT)
        return self.files[path]

    def getxattr(self, path, name, position=0):
        attrs = self.files[path].get('attrs', {})
        try:
            return attrs[name]
        except KeyError:
            return ''       # Should return ENOATTR

    def listxattr(self, path):
        attrs = self.files[path].get('attrs', {})
        return attrs.keys()

    def mkdir(self, path, mode):
        self.files[path] = dict(st_mode=(S_IFDIR | mode), st_nlink=2,
                                st_size=0, st_ctime=time(), st_mtime=time(),
                                st_atime=time())
        self.files['/']['st_nlink'] += 1
        self.saveInfo()

    def open(self, path, flags):
        self.fd += 1
        return self.fd

    def read(self, path, size, offset, fh):
        if path not in self.data and path in self.files:
            self.download(path)
        return self.data[path][offset:offset + size]

    def readdir(self, path, fh):
        return ['.', '..'] + [x[1:] for x in self.files if x != '/']

    def readlink(self, path):
        if path not in self.data and path in self.files:
            self.download(path)
        return self.data[path]

    def removexattr(self, path, name):
        attrs = self.files[path].get('attrs', {})
        try:
            del attrs[name]
        except KeyError:
            pass        # Should return ENOATTR

    def rename(self, old, new):
        self.files[new] = self.files.pop(old)
        self.saveInfo()

    def rmdir(self, path):
        self.files.pop(path)
        self.files['/']['st_nlink'] -= 1
        self.saveInfo()

    def setxattr(self, path, name, value, options, position=0):
        # Ignore options
        attrs = self.files[path].setdefault('attrs', {})
        attrs[name] = value

    def statfs(self, path):
        return dict(f_bsize=512, f_blocks=4096, f_bavail=2048)

#   i know i must do something to MetaDisk, but Patrasche, I'm exhausted...
#   MetaDiskに何かしないといけなのはわかってるんだ、でもね、パトラッシュ、もう、僕疲れちゃったよ。
    def symlink(self, target, source):
        self.files[target] = dict(st_mode=(S_IFLNK | 0o777), st_nlink=1,
                                  st_size=len(source))
        self.data[target] = source

    def truncate(self, path, length, fh=None):
        self.data[path] = self.data[path][:length]
        self.files[path]['st_size'] = length
        self.upload(path)

#   must i do anything to MetaDisk?　i dont know how to remove files from storj...
    def unlink(self, path):
        self.files.pop(path)


    def utimens(self, path, times=None):
        now = time()
        atime, mtime = times if times else (now, now)
        self.files[path]['st_atime'] = atime
        self.files[path]['st_mtime'] = mtime

    def write(self, path, data, offset, fh):
        self.data[path] = self.data[path][:offset] + data
        self.files[path]['st_size'] = len(self.data[path])
        self.upload(path)
        return len(data)


if __name__ == '__main__':
    if len(argv) != 2:
        print('usage: %s <mountpoint>' % argv[0])
        exit(1)

    logging.getLogger().setLevel(logging.DEBUG)
    fuse = FUSE(MetaDiskFS(), argv[1], foreground=True)
