import os
import sys
import ctypes
import pysvn
import threading
import datetime
from xml.dom import minidom


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
                print("SVN Binary Directory : "+str[1])        
                self.SvnBinaryDir = str[1];
                
            if(str[0]=="REPO"):                
                print("Repository Directory : "+str[1])
                self.RepositoryDir = str[1];
                
            if(str[0]=="PORT"):
                print("Server Port : "+str[1])   
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
        os.system(CommandString)
        os.system('sc start svn_server');

        
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
            print(rev)
            
            ath = RevisionList[index].getElementsByTagName('author')            
            print(ath[0].firstChild.data)
            
            date = RevisionList[index].getElementsByTagName('date')            
            print(date[0].firstChild.data)
            
            path = RevisionList[index].getElementsByTagName('path')                        
            NumberOfpath = len(path)
            for pidx in range(NumberOfpath):
                print(path[pidx].firstChild.data)
                df = path[pidx].getAttribute('kind')
                act = path[pidx].getAttribute('action')
                print(df)
                print(act)
                
            msg = RevisionList[index].getElementsByTagName('msg')     
            if(msg[0].firstChild != None):
                print(msg[0].firstChild.data)
                
            #print(msg[0].firstChild.data)
            
            print('-------------------------------------------------------------')    
            
        """
                   
            if(len(msg) != 0):
                print(msg[0].firstChild.data)
            """
            

        
    
class SvnRevisionHistory:
        
        
    def __init__(self, rev, author, date, df, action, file):
        self.Revision = rev
        self.Author = author
        self.Date = date
        self.FileOrDir = df
        self.Action = action
        self.Filename = file
        
    
        
    
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
svn.LoadRootRevision()


#svn.ShowAllUsers()
#svn.AddNewUser('newbie','passwd');
#svn.ShowAllUsers()
#svn.SetUserPasswd('leehana','hana2');

"""
res = svn.DeleteUser('newbie');
if(res == True ):
    print('delete success')
else :
    print('no match user')    
    
"""



#Permission User - Read only, Write Allow