import os
import sys
import pysvn

class MushroomScmSvn:
    
    url=""
    client=""
    
    def __init__(self, _url):
        self.url = _url;
        self.client = pysvn.Client();
        
    def CreateRepository(self, dir):
        e = os.system('C:\\svn_bin\\bin\\svnadmin.exe create '+dir);
    
    def Checkout(self, dir):
        self.client.checkout(self.url, dir);

    def Addfile(file):
        self.client.add(file);


svn = MushroomScmSvn('svn://210.118.56.213/SVN_TEST');
#svn.Checkout('./test2');
svn.CreateRepository('./repo');
#'C:\Program Files (x86)\Subversion\bin\svnadmin'
