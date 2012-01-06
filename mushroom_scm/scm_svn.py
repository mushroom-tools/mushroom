import os
import sys
import ctypes
import threading
import datetime
from xml.dom import minidom


svnLogList = []


configFile="config.txt"
XMLconfigFile="config.xml"

"""
Service Register : sc create svn_local binpath= "\"c:\svn_bin\bin\svnserve.exe\" --service -r c:\svn_test" start= auto
Service start    : sc start svn_local
Service Stop     : sc stop svn_local
Service Delete   : sc delete svn_local

"""
"""
class DbgOut:
    def write(self, msg):
    #    conout.write(msg)
        msg = "[MUSHROOM]"+msg
        trace(msg);

trace       = ctypes.windll.kernel32.OutputDebugStringA
dbgout      = DbgOut()
conout      = sys.stdout
conerr      = sys.stderr
sys.stdout  = dbgout
sys.stderr  = dbgout
"""




class MushroomScmSvn:
    url=""    
    RepositoryDir=""
    ServerPort=""
    RunningState=""
    SvnBinaryDir=""
    
    """def __init__(self):
        dbg = DbgOut()
        dbg.write("Debuging Start")"""
    
    def LoadConfigFile(self):
        confFile=open(configFile)        
        for s in confFile:
            str = s.split('=')            
            
            if(str[0]=="BIN"):                
            #    print("SVN Binary Directory : "+str[1])        
                self.SvnBinaryDir = str[1];
                
            if(str[0]=="REPO"):                
            #    print("Repository Directory : "+str[1])
                self.RepositoryDir = str[1];
                
            if(str[0]=="PORT"):
            #    print("Server Port : "+str[1])   
                self.ServerPort = str[1]
            
                
                             
        confFile.close();
        
    #def LoadXMLConfigFile(self):
        
    def SetPortNumber(self,port):
        ServerPort = port

    
    def SetRepositoryDirectory(self,dir):
        RepositoryDir = dir

        
    def SaveConfigFile():
        print(configFile)

        
    def StartServerDeamon(self):        
        binPath=self.SvnBinaryDir.strip() + '\\svnserve.exe"'
        binPath='""'+binPath    
        CommandString = 'sc create svn_server binpath= ' + binPath + ' --service -r "' + self.RepositoryDir.strip() + ' start= auto'
        print CommandString
        #os.system(CommandString)
        #os.system('sc start svn_server');

        
    def StopServerDeamon(self): 
        os.system('sc stop svn_server')
        os.system('sc delete svn_server')

        
    def RestartServerDeamon(self): 
        os.system('sc stop svn_server')
        os.system('sc start svn_server');
        
        
    def ShowCurrentServerStatus(self):
        os.system('sc query svn_server > out')
        file = open('out', 'r');
        lines = file.readlines()
        res = False
        for line in lines:
            if(line.find('SERVICE_NAME') == 0):
                res = True
        
        file.close()
        os.system('del out')
        if res == True :
            return True
        else:  
            return False
        
                
    
    
    def ShowAllUsers(self):
        authzFilePath = self.RepositoryDir.strip() + '\\conf\\passwd'
        file = open(authzFilePath, 'r')
        while 1:
            line = file.readline()
            if not line:
                break         
               
            if(line[0] != '#' and line[0] != '\n'):
                str = line.split('=')
                if(len(str) == 2):
                    name = str[0]
                    passwd = str[1]
                    print(name)
        file.close()
                    
                    
    def AddNewUser(self, nName, nPasswd):
        authzFilePath = self.RepositoryDir.strip() + '\\conf\\passwd'
        file = open(authzFilePath, 'a') 
       
       
        file.write(nName + ' = ' + nPasswd)        
        file.close()
             
        
    def DeleteUser(self, nName):
        authzFilePath = self.RepositoryDir.strip() + '\\conf\\passwd'
        file = open(authzFilePath, 'r')
        
        names = []
        passwds = []
        
        while 1:
            line = file.readline()
            if not line:
                break         
               
            if(line[0] != '#' and line[0] != '\n'):
                str = line.split('=')
                if(len(str) == 2):
                    name = str[0].strip()
                    passwd = str[1].strip()
                    names.append(name)
                    passwds.append(passwd)
        file.close()
        for n in names:
            if( n == nName):                
                idx = names.index(nName)
                names.pop(idx)
                passwds.pop(idx)                
                file = open(authzFilePath, 'w')
                file.write('[users]\n')
                for i in names:
                    
                    file.write(i + ' = ' + passwds[names.index(i)] + '\n')                
                              
                return True 
        return False
        
    def SetUserPasswd(self, nName, nPasswd):
        authzFilePath = self.RepositoryDir.strip() + '\\conf\\passwd'
        file = open(authzFilePath, 'r')
        
        names = []
        passwds = []
        
        while 1:
            line = file.readline()
            if not line:
                break         
               
            if(line[0] != '#' and line[0] != '\n'):
                str = line.split('=')
                if(len(str) == 2):
                    name = str[0].strip()
                    passwd = str[1].strip()                    
                    names.append(name)
                    passwds.append(passwd)
        file.close()
                
        for n in names:
            if( n == nName):
                
                idx = names.index(nName)
                names.pop(idx)
                passwds.pop(idx)                
                
                names.append(nName)
                passwds.append(nPasswd)
                
                file = open(authzFilePath, 'w')
                file.write('[users]\n')
                
                for i in names:                    
                    file.write(i + ' = ' + passwds[names.index(i)] + '\n') 
                return True 
        return False

    SvnAddress = 'svn://127.0.0.1'
    
    def LoadRootRevision(self):
        os.system('svn log -v '+ self.SvnAddress + ' --xml > __log.xml')
        file = open('__log.xml','r')
        text = file.read()
        xmlraw = minidom.parseString(text)
        
        RevisionList = xmlraw.getElementsByTagName('logentry')
        
        logSize = len(RevisionList)
        
        for index in range(logSize):
            rev = RevisionList[index].getAttribute('revision')                        
             
            ath = RevisionList[index].getElementsByTagName('author')
            s_ath = ath[0].firstChild.data      
            
            date = RevisionList[index].getElementsByTagName('date')            
            s_date = date[0].firstChild.data
            
            PathLists = []
            path = RevisionList[index].getElementsByTagName('path')                        
            NumberOfpath = len(path)
            for pidx in range(NumberOfpath):
                df = path[pidx].getAttribute('kind')
                act = path[pidx].getAttribute('action')

                PathLists.append(Paths(df, act, path[pidx].firstChild.data))

            msg_data =""
            msg = RevisionList[index].getElementsByTagName('msg')     
            if(msg[0].firstChild != None):
                msg_data = msg[0].firstChild.data
            
            
            svnLogList.append(SvnRevisionHistory(rev,s_ath,s_date, PathLists, msg_data))
 
        file.close();
        os.system('del __log.xml')
    
    
    def SVNGetFileListRoot(self, list):
                
        os.system('svn list ' + self.SvnAddress+ ' --xml > __file_list.xml' )
        
        file=open('__file_list.xml', 'r')
        
        text = file.read()
        xmlraw = minidom.parseString(text)
        
        FileList = xmlraw.getElementsByTagName('entry')
        
        listSize = len(FileList)
        
        for entry in range(listSize):
                        
            
            s_kind = FileList[entry].getAttribute('kind')
            
            
            name = FileList[entry].getElementsByTagName('name')
            s_name = name[0].firstChild.data
             
            commit = FileList[entry].getElementsByTagName('commit')
            
            s_rev = commit[0].getAttribute('revision')
                        
            ath = commit[0].getElementsByTagName('author')
            s_ath = ath[0].firstChild.data      
            
            date = commit[0].getElementsByTagName('date')            
            s_date = date[0].firstChild.data
            
            list.append(FileAndFolerList(s_kind, s_name, s_date, s_rev, s_ath))
        file.close()
        os.system('del __file_list.xml')


    def SVNGetFileListFolder(self, list, path):
        os.system('svn list ' + self.SvnAddress+ '/'+path +' --xml > __file_list.xml')
    
        file=open('__file_list.xml', 'r')
        
        text = file.read()
        xmlraw = minidom.parseString(text)
        
        FileList = xmlraw.getElementsByTagName('entry')
        
        listSize = len(FileList)
        
        for entry in range(listSize):
                        
            
            s_kind = FileList[entry].getAttribute('kind')
            
            
            name = FileList[entry].getElementsByTagName('name')
            s_name = name[0].firstChild.data
             
            commit = FileList[entry].getElementsByTagName('commit')
            
            s_rev = commit[0].getAttribute('revision')
                        
            ath = commit[0].getElementsByTagName('author')
            s_ath = ath[0].firstChild.data      
            
            date = commit[0].getElementsByTagName('date')            
            s_date = date[0].firstChild.data
            
            list.append(FileAndFolerList(s_kind, path+'/'+s_name, s_date, s_rev, s_ath))
        file.close()
        os.system('del __file_list.xml')
        
    
    def GetCommitMsgByRev(self, rev):        
        for log in svnLogList:
            if log.Revision == rev :
                return log.Message
        return ""
    
    def GetFileContext(self, path):
        os.system('svn export ' + self.SvnAddress+ '/'+path +'  __tmp.txt > __log')
            
        file = open('__tmp.txt', 'r')
        text = file.read()
        file.close()
        os.system('del __tmp.txt')
        os.system('del __log')
        
        return text
        
    def GetFileContextByRev(self, path, rev):
        os.system('svn export ' +  self.SvnAddress+ '/'+path  +' -r '+ str(rev) +'  __tmp.txt > __log')
        
        file = open('__tmp.txt', 'r')        
        text = file.read()
        file.close()
        os.system('del __tmp.txt')
        os.system('del __log')
        
        return text

    def SVNGetFileListFolderAndRev(self, list, path, rev):
        
        os.system('svn list ' + self.SvnAddress+ '/'+path +' -r '+ str(rev) +' --xml > __file_list.xml')
        
    
        file=open('__file_list.xml', 'r')
        
        text = file.read()
        xmlraw = minidom.parseString(text)
        
        FileList = xmlraw.getElementsByTagName('entry')
        
        listSize = len(FileList)
        
        for entry in range(listSize):
                        
            
            s_kind = FileList[entry].getAttribute('kind')
            
            
            name = FileList[entry].getElementsByTagName('name')
            s_name = name[0].firstChild.data
             
            commit = FileList[entry].getElementsByTagName('commit')
            
            s_rev = commit[0].getAttribute('revision')
                        
            ath = commit[0].getElementsByTagName('author')
            s_ath = ath[0].firstChild.data      
            
            date = commit[0].getElementsByTagName('date')            
            s_date = date[0].firstChild.data
            
            list.append(FileAndFolerList(s_kind, s_name, s_date, s_rev, s_ath))
        file.close()
        os.system('del __file_list.xml')
    

class FileAndFolerList:
    def __init__(self, fd, path, date, rev, ath):
        self.fd = fd
        self.path = path
        self.date = date
        self.rev  = rev
        self.author = ath
        

class Paths:
    def __init__(self, kind, action, path):
        self.kind = kind
        self.action = action
        self.path = path    

    
class SvnRevisionHistory:
        
    Paths = []

    def __init__(self, rev, author, date, pPaths, msg):
        self.Revision = rev
        self.Author = author
        self.Date = date
        self.Paths = pPaths
        self.Message = msg     
           
    
svn = MushroomScmSvn()
svn.LoadConfigFile()

#svn.LoadXMLConfigFile()
#svn.StartServerDeamon();
#svn.StopServerDeamon();
#svn.RestartServerDeamon();
"""
res = svn.ShowCurrentServerStatus();
if(res == True ):
    print('Svn Service Running')
else :
    print('Svn Service Stop')
"""

"""
res = svn.DeleteUser('newbie');
if(res == True ):
    print('delete success')
else :
    print('no match user')    
    
"""

#svn.ShowAllUsers()
#svn.AddNewUser('newbie','passwd');
#svn.ShowAllUsers()
#svn.SetUserPasswd('leehana','hana2');

"""
def PrintSVNLog():
    for log in svnLogList:
        print 'Revision :'+log.Revision
        print 'Author   :'+log.Author
        print 'Date     :'+log.Date
        print 'Message  :'+log.Message
        
                
        for path in log.Paths:
            print 'Action   :'+ path.action
            print 'kind     :'+ path.kind
            print 'path     :'+ path.path
        print '------------------------------------------'
        

PrintSVNLog()
"""
svn.LoadRootRevision()

filelist = []
#svn.SVNGetFileListRoot(filelist)
#svn.SVNGetFileListFolder(filelist, 'Folder1/')
#svn.SVNGetFileListFolderAndRev(filelist, "", 7)



def PrintSVNFileList(list):
    for name in list:
        if name.fd == 'file':
            print 'FILE   :' + name.path
            print 'author :' + name.author
            print 'revision :' + name.rev
            print 'date :' + name.date
            msg = svn.GetCommitMsgByRev(name.rev)
            print 'message : ' + svn.GetCommitMsgByRev(name.rev)
        else :
            print 'FOLDER :' + name.path
            print 'author :' + name.author
            print 'revision :' + name.rev
            print 'date :' + name.date
            msg = svn.GetCommitMsgByRev(name.rev)
            print 'message : ' + svn.GetCommitMsgByRev(name.rev)
            


#svn.SVNGetFileList(filelist)

#svn.SVNGetFileListFolderAndRev(filelist, "", 7)



#flist = []
#svn.SVNGetFileListRoot(flist)

svn.SVNGetFileListRoot(filelist)
#PrintSVNFileList(filelist)


def PrintSVNAllFileList(list):
    
    for name in list:
        if name.fd == 'file':
            print 'FILE   :' + name.path
        else :
            print 'FOLDER :' + name.path
            sublist=[]
            svn.SVNGetFileListFolder(sublist, name.path)
            PrintSVNAllFileList(sublist)

        
#PrintSVNAllFileList(filelist)

#test1 = svn.GetFileContext('test.txt')
#test1 = svn.GetFileContextByRev('test.txt', 10)
#test1 = svn.GetFileContextByRev('Folder1/inFolder1_test1.txt', 10)









