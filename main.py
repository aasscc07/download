from Crypto.Cipher import AES 
import glob
import os
import math
import hashlib
import base64

MPath = "folder"

class encryption:
    FileStr = ""
    for Path in os.listdir(MPath):
        pass
    
    
        

class Decryption:
    pass

Kinput = input("암호화 : E / 복호화 : D\n : ")
if Kinput == "E":
    FileStr = ""
    for Path in os.listdir(MPath):
        try:
            with open(os.path.join(MPath,Path),'rb') as f:
                FileStr = f.read().decode('utf-8')
                f.close()
        except:
            with open(os.path.join(MPath,Path),'rb') as f:
                FileStr = f.read()#.decode('ascii')
                f.close()
            

        try:               
            with open(str(os.path.join(MPath,Path) + ".jun"),'wb') as f:
                FileStr_base64 = FileStr.encode('ascii')
                FileStr_base64 = base64.b64encode(FileStr_base64)
                FileStr = FileStr_base64.decode('ascii')
                f.write(FileStr.encode('utf-8'))
                f.close()
        except:
            with open(str(os.path.join(MPath,Path) + ".jun"),'wb') as f:
                FileStr_base64 = FileStr
                FileStr_base64 = base64.b64encode(FileStr_base64)
                FileStr = FileStr_base64
                f.write(FileStr)
                f.close()
        
        os.remove(os.path.join(MPath,Path))


elif Kinput == "D":
    FileStr = ""
    for Path in os.listdir(MPath):
        try:
            with open(os.path.join(MPath,Path),'rb') as f:
                FileStr = f.read().decode('utf-8')
                f.close()
        except:
            with open(os.path.join(MPath,Path),'rb') as f:
                FileStr = f.read()
                f.close()
            
        try:
            with open(os.path.join(MPath,Path).split(".jun")[0],'wb') as f:
                FileStr_base64 = base64.b64decode(FileStr)
                FileStr = FileStr_base64.decode('ascii')
                f.write(FileStr.encode('utf-8'))
                f.close()
                
        except:
            with open(os.path.join(MPath,Path).split(".jun")[0],'wb') as f:
                FileStr_base64 = base64.b64decode(FileStr)
                FileStr = FileStr_base64
                f.write(FileStr)
                f.close()
        
        os.remove(os.path.join(MPath,Path))

else:
    print("키보드 입력이 잘못되었습니다")