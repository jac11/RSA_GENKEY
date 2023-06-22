#!/usr/bin/env python

#d = (e^-1) mod phi(n)
#C = (M^e) mod n = 31^7 mod 33 = 4
#: M = (C^d) mod n = 4^3 mod 33 = 31
# 1<e<phi(n) and gcd(phi(n), e) = 1 

import random
import math
import base64
import argparse
import sys
import os
import time
import string
import shutil
from threading import Thread
print("""                                                      
   ╦═╗╔═╗╔═╗   ╔═╗╔═╗╔╗╔╦╔═╔═╗╦ ╦ 🔐
   ╠╦╝╚═╗╠═╣───║ ╦║╣ ║║║╠╩╗║╣ ╚╦╝
   ╩╚═╚═╝╩ ╩   ╚═╝╚═╝╝╚╝╩ ╩╚═╝ ╩ 🎲️
               @jacstory🗝️
"""
)
list_Str = []
VKEY = []
if os.path.exists("./Decrypt_Data/") :
    pass
else:
    os.mkdir("./Decrypt_Data/")  
path = str(os.getcwd()+"/Decrypt_Data/")
with open(".path",'w',) as pathf:
     pathf.write(path)
with open('.path','r') as pathf:
     path = pathf.read()

list =[
        1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051,
        1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109,
        1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187,
        1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249,
        1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303,
        1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399,
        1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453,
        1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511,
        1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579,
        1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627,
        1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709,
        1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783,
        1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867,
        1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931,
        1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999
     ]
    
class RSA_algorithm:
    def __init__(self):
        self.Usage()
        self.Sys_argv()
        self.algorithm()
    def ReadMessage(self): 
        try:
            with open (self.args.message,'r') as readM:
                Mes_txt = readM.read()
                self.Len = len(Mes_txt)
            if os.path.exists(path+self.args.message.split("/")[-1]) :
               pass
            else:  
                 os.mkdir(path+self.args.message.split("/")[-1])  
           
            for L in Mes_txt :
               Num_str =list_Str.append(ord(L))
            self.Len = len(list_Str)
            time.sleep(.15)   
            print("✉️   Message        ::------------:: ", str("".join(self.args.message.split("/")[-1])))   
            print("🧶️  length         ::------------:: ", str(self.Len)) 
        except Exception as E :
            print("🚨️🚧️ Error  ::------------:: ".strip() , E)  
            exit() 
    def Gen_PP(self): 
        try : 
            for V in range(0,10):
                add = str(random.random())
                SValue = str(random.random())+"-"
                Value = str(SValue[12:].join(str(add[1:6])))\
                .replace("0.",'').replace('\n','')
                VKEY.append(Value)
            p_Num = random.choice(list)
            q_Num = random.choice(list)
            Public_key_list = []
            if p_Num == q_Num:
                p_Num = random.choice(list)
            N_Num = p_Num * q_Num
            QT_Num = (p_Num - 1) * (q_Num - 1)
            for Public_key in range(int(QT_Num)):
                if 1 < Public_key < QT_Num:
                    if math.gcd( QT_Num , Public_key ) == 1:
                        if Public_key == p_Num :
                            continue
                        else:
                            Public_key_list.append(Public_key)
            Public_key = random.choice(Public_key_list)
            for private_key in range (QT_Num) :
                if (private_key * Public_key) % QT_Num == 1 :
                    if private_key  == Public_key :
                        private_key +=1
                    else:    
                        break
            Value1 = str(Public_key)+"-"+str(VKEY).replace("[",'').replace("]",'')\
            .replace("'",'').replace(",",'').replace(".",'')+str(N_Num)
            Value1 = str(base64.b64encode(bytes(Value1, 'utf-8')))
            Value1 = "".join('\n%s'%Value1[i:i+56] for i in range(0, len(Value1),56))\
            .replace("\n",'',1).replace("b'",'').replace("'",'')
            Value2 = str(private_key)+"-"+str(VKEY).replace("[",'').replace("]",'')\
            .replace("'",'').replace(",",'').replace(".",'')+str(N_Num)
            Value2 = str(base64.b64encode(bytes(Value2, 'utf-8')))     
            Value2 = "".join('\n%s'%Value2[i:i+56] for i in range(0, len(Value2),56))\
            .replace("\n",'',1).replace("b'",'').replace("'",'')
            Style = "#"+"-"*20+"#"

            if self.args.message:

                pbkey = path+self.args.message.split("/")[-1]+"/"+self.args.message.split("/")[-1]    #str(self.args.key)
                with open(pbkey+"-Public-key.pem" ,'w') as Publickey:
                    Publickey.write(Style+"BEGIN RSA PUBLIC KEY"+Style+"\n"+Value1+\
                    '\n'+Style+"END RSA PUBLIC KEY"+Style)  
                with open(pbkey+"-Private-Key.pem" ,'w') as PrivateKey:
                    PrivateKey.write(Style+"BEGIN RSA PRIVATE KEY"+Style+"\n"+Value2+\
                    '\n'+Style+"END RSA PRIVATE KEY"+Style) 

            if self.args.key  and not self.args.message :
                if os.path.exists(path+self.args.key+"-KEY"+"/") :
                       pass
                else:   
                    os.mkdir(path+self.args.key+"-KEY"+"/")   
                pbkey = path+self.args.key+"-KEY"+"/"+self.args.key
                with open(pbkey+"-Public-key.pem" ,'w') as Publickey:
                    Publickey.write(Style+"BEGIN RSA PUBLIC KEY"+Style+"\n"+Value1+\
                    '\n'+Style+"END RSA PUBLIC KEY"+Style)  
                with open(pbkey+"-Private-Key.pem" ,'w') as PrivateKey:
                    PrivateKey.write(Style+"BEGIN RSA PRIVATE KEY"+Style+"\n"+Value2+\
                    '\n'+Style+"END RSA PRIVATE KEY"+Style)    

            self.N_Num       = N_Num 
            self.private_key = private_key
            self.Public_key  = Public_key   

            time.sleep(.15) 
            print("🛟️  P-Value        ::------------::  **********     ✔️")
            time.sleep(.15) 
            print("💡️  Q-Value        ::------------::  **********     ✔️")
            time.sleep(.15) 
            print("📌️  P*Q-Value      ::------------::  **********     ✔️")
            time.sleep(.15) 
            print("🎯  Euler-Totient  ::------------::  **********     ✔️")
            time.sleep(.15) 
            print("🔑  Public_key     ::------------::  Genreagted 🗝️   ✔️")
            time.sleep(.15) 
            print("🔑  Private_key    ::------------::  Genreagted 🗝️   ✔️")
            time.sleep(.15) 
            print("="*40)

            if  self.args.key   and not (self.args.message\
            and self.args.decrypt and not self.args.enctypt) :
                print("🔑  Keys-Info 🔑  : "+'\n'+"="*20)
                print("🗝️   Public_key     ::------------:: ",self.args.key+"-Public-key.pem")
                time.sleep(.15) 
                print("🔑  Private_key    ::------------:: ",self.args.key+"-Private-key.pem")
                time.sleep(.15) 
                print("💾  location       ::------------::  file://"+str("/".join(pbkey.split("/")[0:-1])))
                exit()
            else:
                 pass   
            with open(".path",'w')as newpath:
                newpath.write(str("/".join(pbkey.split("/")[:-1])))      
            with open(".path2",'w') as path2:
                path2.write(pbkey)
        except Exception as E:
            print("🚨️🚧️  Error  : ::------------::".strip(),E)  
        except KeyboardInterrupt :
            print("🚨️🚧️  Error ::------------: KeyboardInterrupt".strip())    
            exit()                          
    def En_crypt_Message(self): 
        with open(".path",'r') as readnewpath:
            path = readnewpath.read()       
        try: 
            if self.args.public:
                with open(".path",'r') as readnewpath:
                    path = readnewpath.read()       
                with open(self.args.public,'r') as Symmetric_public :
                    secret_F = Symmetric_public.read().replace("\n","",2).split("#")  
                    secret = str("".join(secret_F[4:-4]))
                    secret_F = str(base64.b64decode(bytes(secret,'utf-8')))\
                    .replace(" ",'').replace("b'",'').replace("'",'').split("-")
                    Key = secret_F
                    self.key = int(Key[0])
                    self.NKey= int(Key[-1][1:]) 
            elif self.args.private:
                with open(".path",'r') as readnewpath:
                    path = readnewpath.read()  
                with open(self.args.private,'r') as Symmetric_Private :
                    secret_F = Symmetric_Private.read().replace("\n","",2).split("#")
                    secret = str("".join(secret_F[4:-4]))
                    secret_F = str(base64.b64decode(bytes(secret,'utf-8')))\
                    .replace(" ",'').replace("b'",'').replace("'",'').split("-")
                    Key = secret_F
                    self.key = int(Key[0])
                    self.NKey= int(Key[-1][1:])        
            print("🔐 Encrypt-Info 🔐 : "+'\n'+"="*20)                
            list_Encrypt = []
            self.i = 0
            self.s=len(list_Str)
            for Mas in list_Str :   
                if self.args.public or self.args.private:
                    Ciphertext = ( Mas ** self.key ) % self.NKey
                else:   
                    Ciphertext = ( Mas ** self.Public_key ) % self.N_Num
                list_Encrypt.append(Ciphertext)
                self.Progress_bar()                  
            if self.args.base64 and self.args.enctypt :   
                Encrypt = str("".join(str(list_Encrypt))).replace("[",'')\
                .replace(',','').replace("]",'')   
                E_base64 = str(base64.b64encode(bytes(Encrypt, 'utf-8')))\
                .replace("b'",'').replace("'",'')
                if self.args.private or self.args.public:
                    with open(path+self.args.message.split("/")[-1]+\
                        "/EncryptB64-"+self.args.message.split("/")[-1] ,'w') as DecryptW:
                        DecryptW.write(E_base64)
                else:     
                    with open(path+"/EncryptB64-"+str(path.split("/")[-1]) ,'w') as DecryptW:
                         DecryptW.write(E_base64)
            if  self.args.hex and self.args.enctypt  :
                if self.args.private or self.args.public:
                    with open (path+self.args.message.split("/")[-1]+\
                            "/EncryptHEX-"+self.args.message.split("/")[-1] ,'a') as HEXData :
                        for Hex in list_Encrypt :
                            Hex  = hex(Hex)
                            with open (path+self.args.message.split("/")[-1]+\
                                "/EncryptHEX-"+self.args.message.split("/")[-1] ,'a') as HEXData :
                                HEX_ST = HEXData.write(str(Hex).replace("0x",' '))

                else:        
                    with open (path+"/EncryptHEX-"+str(path.split("/")[-1]),'w') as HEXData :
                        for Hex in list_Encrypt :
                            Hex  = hex(Hex)
                            with open (path+"/EncryptHEX-"+str(path.split("/")[-1]) ,'a') as HEXData :
                                 HEX_ST = HEXData.write(str(Hex).replace("0x",' '))
           
            time.sleep(.15) 
            print("✍️   Plain-text           ::------------:: ", str("".join(self.args.message.split("/")[-1])))
            time.sleep(.15)
            if  self.args.base64 and not (self.args.private or not self.args.public) : 
                print("🛡️   Ciphertext           ::------------::  Format Base64 ")
                time.sleep(.15)
                print("🔐  Encrypted message    ::------------:: " ,"EncryptB64-"+str(path.split("/")[-1]) )
            if (self.args.private or self.args.public) :
                if self.args.base64:
                    print("🛡️   Ciphertext           ::------------::  Format Base64 ")
                    time.sleep(.15)
                    print("🔐  Encrypted message    ::------------:: " ,"EncryptB64-"+str(self.args.message.split("/")[-1]) ) 
                else :
                    if self.args.hex :
                        print("🛡️   Ciphertext           ::------------::  Format Hex String ")
                        time.sleep(.15) 
                        print("🔐  Encrypted message    ::------------:: " ,"EncryptHEX-"+str(self.args.message.split("/")[-1]) )    
            else:
                print("🛡️   Ciphertext           ::------------::  Format Hex String ")
                time.sleep(.15) 
                print("🔐  Encrypted message    ::------------:: " ,"EncryptHEX-"+str(path.split("/")[-1]) )
            time.sleep(.15) 
            print("💯  Encrypted Process    ::------------::  Done ")   
            time.sleep(.15)
            if self.args.image:
                print("📸️  Matted               ::------------::  Hiden Data In Image" )
                print("🦊️  Type                 ::------------::  MeteData" )
                print("🏜️   Image name           ::------------:: ",self.args.image.split("/")[-1] )
            if self.args.private or self.args.public :
                print("💾  location             ::------------::  file://"+path+self.args.message.split("/")[-1])
            else:    
                print("💾  location             ::------------::  file://"+path)            
        except Exception as E:
            print("🚨️🚧️  Error  ::------------:: ".strip(),E)
        except KeyboardInterrupt :
            print("🚨️🚧️  Error ::------------:: KeyboardInterrupt".strip())    
            exit()                               
    def De_crypt_Message(self):
        print("🎲️ Decryption-Info 🎲️ : "+'\n'+"="*20)
        with open(".path",'r') as readnewpath:
            path = readnewpath.read()    
        if self.args.secret :
            if '/' not in self.args.secret or '/' not in self.args.file:
                path = path+'/'+str(self.args.secret.split('-')[0])+'/'
                NewPath = path
            else:    
                 path = path+'/'+"".join(str(self.args.secret.split('/')[-1]).split('-')[0])

        elif self.args.private or self.args.public:
                if '/' not in self.args.private or "/" not in self.args.public :
                    try:  
                        path = path+'/'+str(self.args.public.split('-')[0])+'/'
                    except Exception:
                        path = path+'/'+str(self.args.private.split('-')[0])+'/'
                else:      
                     pass     
        if os.path.exists(path):
            for dir in  os.listdir(path) : 
                if ".pem" in dir :
                    pass
                else:
                    if self.args.secret:
                        try:
                            shutil.copy(self.args.secret , path)
                        except shutil.SameFileError:
                            pass 
                    else:
                        if self.args.public :
                            try:
                                shutil.copy(self.args.public , path)
                            except shutil.SameFileError:
                                pass   
                        else:
                            if self.args.private :
                                try:
                                   shutil.copy(self.args.private , path)
                                except shutil.SameFileError:
                                    pass              
        else:
            os.mkdir(path)
            if self.args.secret:
                try:
                   shutil.copy(self.args.secret , path) 
                except shutil.SameFileError:
                    pass   
            elif self.args.public :
                try:
                     shutil.copy(self.args.public , path)
                except shutil.SameFileError:
                    pass   
            elif self.args.private :
                try:
                    shutil.copy(self.args.private , path)
                except shutil.SameFileError:
                    pass 
        list_Decrypt = []  
        try : 
            if self.args.public:
               with open(self.args.public,'r') as Symmetric_public :
                secret_F = Symmetric_public.read().replace("\n","",2).split("#")  
            elif self.args.private:
                with open(self.args.private,'r') as Symmetric_Private :
                    secret_F = Symmetric_Private.read().replace("\n","",2).split("#")    
            elif self.args.image and self.args.exif:
                if '/' not in self.args.image :
                    try:
                        path = path = path+self.args.image.split(".")[0]+'/'+self.args.image.split(".")[0]
                    except Exception :
                        path = path+'/'+str("".join(self.args.image.split('/')[-1])).split(".")[0]+'/'+self.args.image.split('.')[0]  
                else:           
                    path = path +'/'+str("".join(self.args.image.split('/')[-1]).split('.')[0])+'/'+str("".join(self.args.image.split('/')[-1]).split('.')[0])            
                with open (path+"-Public-key.pem",'r') as write_Image_Key:
                    secret_F = write_Image_Key.read().replace("\n","",2).split("#")
            else:
                try:
                    with open (path+path.split('/')[-2]+"-Private-Key.pem",'r') as R_secret :            
                       secret_F = R_secret.read().replace("\n","",2).split("#")    
                except Exception:
                    NewPath = path+'/'+"".join(str(self.args.secret.split('/')[-1]).split('-')[0])
                    with open (NewPath+"-Private-Key.pem",'r') as R_secret :    
                        secret_F = R_secret.read().replace("\n","",2).split("#")         
            secret = str("".join(secret_F[4:-4]))
            secret_F = str(base64.b64decode(bytes(secret,'utf-8')))\
            .replace(" ",'').replace("b'",'').replace("'",'').split("-")
            Key = secret_F
            privateK = int(Key[0])
            NKey= int(Key[-1][1:])   
            if self.args.base64 :
                if self.args.image and self.args.exif :
                   with open(str("/".join(path.split('/')[0:-1]))+'/'+"Message.txt",'r') as Ciphertext_R :
                        DeCipher = Ciphertext_R.read()
                else:     
                    with open(self.args.file,'r') as Ciphertext_R :
                        DeCipher = Ciphertext_R.read()     
                D_baes64 = base64.b64decode(DeCipher).decode("utf-8").split(" ")
                self.s = len(D_baes64 )
                self.i = 0
                for Char in D_baes64 :     
                    Char = int(Char)   
                    Decrypt =chr((Char ** int(privateK) )%int(NKey))
                    list_Decrypt.append(Decrypt) 
                    Plaintext = "".join(list_Decrypt) 
                    self.Progress_bar()     
                if self.args.secret  and '/' in self.args.secret:    
                    with open(str("/".join(NewPath.split('/')[0:-1]))+"/DecryptB64_"+\
                           str(NewPath.split('/')[-1]),'w') as Text :
                           Text.write(Plaintext)  
                elif self.args.image:
                    NewPath = path
                    with open(str("/".join(NewPath.split('/')[0:-1]))+"/DecryptB64_"+\
                           str(NewPath.split('/')[-1]),'w') as Text :
                           Text.write(Plaintext)                            
                else:
                    NewPath = path
                    with open(str("/".join(NewPath.split('/')[0:-1]))+"/DecryptB64_"+\
                        str(NewPath.split('/')[-2]),'w') as Text :
                        Text.write(Plaintext)  
                   
            if self.args.hex:
                if self.args.file: 
                    with open(self.args.file,'r') as Ciphertext_R :
                        DeCipher = Ciphertext_R.read().split(" ")
                        DeCipher  = DeCipher[1:]
                        self.s=len(DeCipher) 
                        self.i = 0
                        for HEX in DeCipher :                          
                            HEXTONUM = int(HEX,16)
                            Decrypt =chr((HEXTONUM  ** int(privateK) )%int(NKey))
                            list_Decrypt.append(Decrypt) 
                            self.Progress_bar() 
                       
                elif self.args.image and self.args.exif :
                    with open(str("/".join(path.split('/')[0:-1]))+'/'+"Message.txt",'r') as Ciphertext_R : 
                        DeCipher = Ciphertext_R.read().replace(' ','',1).split(" ")
                        DeCipher  = DeCipher[1:]
                        self.s=len(DeCipher) 
                        self.i = 0
                        for HEX in DeCipher :                          
                            HEXTONUM = int(HEX,16)
                            Decrypt =chr((HEXTONUM  ** int(privateK) )%int(NKey))
                            list_Decrypt.append(Decrypt) 
                            self.Progress_bar() 
                Plaintext = "".join(list_Decrypt)
                if self.args.secret : 
                   if '/' in self.args.secret:   
                        with open(str("/".join(NewPath.split('/')[0:-1]))+"/DecryptHEX_"+\
                           str(NewPath.split('/')[-1]),'w') as Text :
                           Text.write(Plaintext)
                elif self.args.image and self.args.exif:
                    NewPath = path
                    with open(str("/".join(NewPath.split('/')[0:-1]))+"/DecryptHEX_"+\
                           str(NewPath.split('/')[-1]),'w') as Text :
                           Text.write(Plaintext)            
                else:
                    with open(str("/".join(NewPath.split('/')[0:-1]))+"/DecryptHEX_"+\
                        str(NewPath.split('/')[-2]),'w') as Text :
                        Text.write(Plaintext)   
            time.sleep(.15) 
            if self.args.image and self.args.exif:
                print("📸️  Matted                ::------------::  Hiden Data In Image" )
                print("🦊️  Type                  ::------------::  MeteData" )
                print("🏜️   Image name            ::------------:: ",self.args.image.split("/")[-1] )
            else:     
                print("🔐  Eecryption-message    ::------------::  " +str(self.args.file.split("/")[-1]) )
            if self.args.base64 :
                time.sleep(.15) 
                print("🖨️   Decrypted-message     ::------------::  DecryptB64-"+str(path.split("/")[-2]))
            if self.args.hex:
                time.sleep(.15) 
                print("🖨️   Decrypted-message     ::------------::  DecryptHEX-"+str(path.split("/")[-2]))  
            time.sleep(.15)    
            print("💯  Decryption Process    ::------------::  Done ")   
            time.sleep(.15)            
            print("💾  location              ::------------::  file://"+"/".join(NewPath.split('/')[:-1])+'/') 
        except Exception as E:
            print("🚨️🚧️  Error  ::------------:: ".strip(),E) 
        except KeyboardInterrupt :
            print("🚨️🚧️ Error ::------------:: KeyboardInterrupt".strip())    
            exit()   
    def algorithm (self):
        if self.args.message\
        and not self.args.private\
        and not self.args.public:
           self.ReadMessage()
           self.Gen_PP()
           self.En_crypt_Message()
           if self.args.image and self.args.hiden:
              self.Image_Hiden_Data() 
        elif self.args.key and self.args.key and not self.args.message:
           self.Gen_PP()   
        elif self.args.secret and self.args.file\
        and self.args.decrypt\
        and (self.args.base64 or self.args.hex):
           self.De_crypt_Message()
        elif (self.args.public  or self.args.private) and self.args.message\
        and self.args.enctypt and not self.args.key :
            self.ReadMessage()
            self.En_crypt_Message()
            if self.args.image and self.args.hiden:
               self.Image_Hiden_Data()
        elif (self.args.public  or self.args.private) and\
        self.args.decrypt and not self.args.message :
             self.De_crypt_Message()    
        elif self.args.image and self.args.exif  :
              self.Decrypt_MataData_Image()                                 
        else:
            print(
                   """usage: rsa.py [-h] [-M] [-D] [-E] [-H] [-S] [-B] [-K] [-F] [-O]\n"""
                   """Usage: [OPtion] [arguments] [ -w ] [arguments]"""
                )
    def  Progress_bar (self):
        D = '-'*100
        s = self.s
        if s <=20 :
            p =int(100*(int(self.i)/int(s)))+5
        elif  s <= 30:
            p =int(100*(int(self.i)/int(s)))+4
        elif s >= 40 and  s <=50:
            p =int(100*(int(self.i)/int(s)))+3
        elif s <= 50 and s >=90:
            p =int(100*(int(self.i)/int(s)))+2
        elif s >= 100:   
            p =int(100*(int(self.i)/int(s)))+1  
        else:
            p =int(100*(int(self.i)/int(s)))+1  
        self.p = p             
        self.c = D.replace("-",'#',p)
        print("⏳ Ciphertext   ::------------:: "+str(random.random())[2:])
        print("⚙️  Progress:    ::------------:: [%"+f"{self.p}"+']['+self.c+']')
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        self.i +=1
    def Image_Hiden_Data(self):
        try:
           from PIL import Image
           from PIL.PngImagePlugin import PngInfo  
        except Exception :
           os.system("pip install Pillow 2>/dev/null 2>&1")  
           from PIL import Image
           from PIL.PngImagePlugin import PngInfo 
        targetImage = Image.open(self.args.image)
        metadata = PngInfo()
        if self.args.message and self.args.enctypt:
            if self.args.base64:
                with open(path+self.args.message.split("/")[-1]+"/EncryptB64-"+\
                    self.args.message.split("/")[-1] ,'r') as Imagedata:
                    Data_read = Imagedata.read()
            elif self.args.hex:
                with open(path+self.args.message.split("/")[-1]+"/EncryptHEX-"+\
                    self.args.message.split("/")[-1] ,'r') as Imagedata:
                    Data_read = Imagedata.read()     
            if self.args.private :
                with open(self.args.private.replace("-Private-Key.pem",'')+"-Public-key.pem",'r' ) as Key_Image :
                    Key_Image = str(base64.b64encode(bytes(Key_Image.read(), 'utf-8')))

            elif self.args.public : 
                with open(self.args.public.replace("-Public-key.pem",'')+"-Private-Key.pem",'r' ) as Key_Image :
                    Key_Image = str(base64.b64encode(bytes(Key_Image.read(), 'utf-8')))
            else:
                with open(path+self.args.message.split("/")[-1]+'/'+\
                self.args.message.split("/")[-1]+"-Private-Key.pem" ,'r') as Key_Image:     
                    Key_Image = str(base64.b64encode(bytes(Key_Image.read(), 'utf-8'))) 
        metadata.add_text("AddressM",Data_read )
        metadata.add_text("KeyM",Key_Image  )
        targetImage.save(path+self.args.message.split("/")[-1]+\
        '/'+str(self.args.image.split("/")[-1]).split(".")[0]+".png", pnginfo=metadata)
    def Decrypt_MataData_Image(self):
        path = str(os.getcwd()+"/Decrypt_Data/")
        try:
           from PIL import Image
           from PIL.PngImagePlugin import PngInfo  
        except Exception :
           os.system("pip install Pillow 2>/dev/null 2>&1")  
           from PIL import Image
           from PIL.PngImagePlugin import PngInfo 
        if '/' not in self.args.image:
            try:
                path = path+self.args.image.split(".")[0]+'/'
            except Exception :
                path = path+str("".join(self.args.image.split('/')[-1])).split(".")[0]+'/'    
        else:
            path = path+str("".join(self.args.image.split('/')[-1])).split(".")[0]+'/'               
        if os.path.exists(path+self.args.image.split('.')[0]):
           pass
        else:
            try:
                os.mkdir(path)   
            except FileExistsError :
                 pass     
        targetImage = Image.open(str(self.args.image))
        Dumps = str(targetImage.text).split(':')
        Message  = Dumps[1].replace(", 'KeyM'",'').replace("'",'')
        Key = Dumps[2].replace('"','').replace('}','')
        with open(path+"Message.txt",'w') as Messages :
            Messages.write(str(Message))
        with open(path+"Key.txt",'w') as Key_write :
            Key_write.write(Key)
        with open(path+"Key.txt",'r') as Key_R : 
            Key = Key_R .read().replace('b','').replace("'",'')
            D_Key =  base64.b64decode(Key).decode("utf-8")
        for line in D_Key.split():
            if "PUBLIC" in line :
                with open (path+path.split('/')[-2]+"-Public-key.pem",'w') as write_Image_Key:
                    write_Image_Key.write(D_Key)
                    break
            else:
                if "PRIVATE" in line :
                    with open (path+path.split('/')[-2]+"-Public-key.pem",'w') as write_Image_Key:
                        write_Image_Key.write(D_Key)
                        break
        self.De_crypt_Message()     
    def Sys_argv(self) :   
        if self.args.message and not (self.args.image  and not self.args.private and not self.args.public\
        and not self.args.decrypt):
            if self.args.message and self.args.enctypt and (self.args.base64 or self.args.hex) and not self.args.image \
                 and not  self.args.hiden and not self.args.exif:
                 self.algorithm()
                 exit()
            else:
                print(
                """⛔️ usage: rsa.py [-h] [-M] [-D] [-E] [-H] [-S] [-B] [-K] [-F] [-p] [-P] [-I] [-N] [-e]\n"""
                """💡️ rsa.py -M Message.txt --hex or --beas64 """)    
                exit() 
        elif self.args.secret and self.args.file :         
            if  self.args.decrypt and self.args.secret and self.args.file\
            and(self.args.hex or self.args.base64) and not (self.args.image or self.args.hiden ) and not self.args.enctypt:
                self.algorithm()
                exit()   
            else:
                print(
                """⛔️ usage: rsa.py [-h] [-M] [-D] [-E] [-H] [-S] [-B] [-K] [-F] [-p] [-P] [-I] [-N] [-e]\n"""
                """💡️ rsa.py --secret key-Private-Key.pem -F EncryptB64-Cryto --base64 --decrypt \n"""
                """💡️ rsa.py --secret key-Private-Key.pem -F EncryptHEX-Cryto --hex --decrypt """)
                exit()    
        elif  self.args.private or self.args.public  and not self.args.image and not self.args.decrypt :
                if (self.args.private or self.args.public) and self.args.enctypt and \
                self.args.message and (self.args.base64 or self.args.hex) : 
                    self.algorithm()
                    exit()
                else:
                    print(
                    """⛔️ usage: rsa.py [-h] [-M] [-D] [-E] [-H] [-S] [-B] [-K] [-F] [-p] [-P] [-I] [-N] [-e]\n"""
                    """💡️ rsa.py --private name-Private-Key.pem  or --public name-Public-Key.pem  --message  Cryto.txt  --hex or --base64 --encrypt""")   
                    exit()
        elif self.args.decrypt and not self.args.image :          
            if  (self.args.private or self.args.public) and self.args.decrypt \
            and (self.args.base64 or self.args.hex) and self.args.file:
                self.algorithm()
                exit()
            else:
                print(
                """⛔️ usage: rsa.py [-h] [-M] [-D] [-E] [-H] [-S] [-B] [-K] [-F] [-p] [-P] [-I] [-N] [-e]\n"""
                """💡️rsa.py --decrypt --public name-Public-key.pem  or --private name-Key-kry.pem -F EncryptB64-Cryto -base64 or --hex """) 
                exit() 
        elif self.args.image  and not self.args.exif:         
            if (self.args.image and self.args.hiden) and self.args.message and\
            (self.args.base64  or self.args.hex) and self.args.enctypt\
            and not (self.args.public or self.args.private )and not self.args.decrypt :
                self.algorithm()
                exit()
            else:
                print(
                """⛔️ usage: rsa.py [-h] [-M] [-D] [-E] [-H] [-S] [-B] [-K] [-F] [-p] [-P] [-I] [-N] [-e]\n"""
                """💡️ rsa.py --Message Cryto.txt --enctypt --image image.jpeg --hiden --base64 or --hex """)
                exit() 
        elif self.args.hiden:           
            if self.args.image and self.args.hiden and self.args.message and\
            (self.args.base64  or self.args.hex) and self.args.enctypt \
            and  (self.args.public or self.args.private ) and not(self.args.secret):
                print('6[*] argv error')
                self.algorithm()
                exit()
            else:
                print('6[*] argv error')
                print(
                """⛔️ usage: rsa.py [-h] [-M] [-D] [-E] [-H] [-S] [-B] [-K] [-F] [-p] [-P] [-I] [-N] [-e]\n"""
                """💡️ rsa.py -I Image.png -e  --hex or --base64 """)
                exit() 
        elif self.args.exif:        
            if self.args.image and self.args.exif and (self.args.base64 or self.args.hex) :
               print('7[*] argv error')
               self.algorithm()
               exit()
            else:
                print('7[*] argv error')
                print(
                """⛔️ usage: rsa.py [-h] [-M] [-D] [-E] [-H] [-S] [-B] [-K] [-F] [-p] [-P] [-I] [-N] [-e]\n"""
                """💡️ rsa.py -I Image.png -e  --hex or --base64 """)
                exit()
        elif self.args.key:
            self.algorithm()
            exit()
        else:
            print(
            """⛔️ usage: rsa.py [-h] [-M] [-D] [-E] [-H] [-S] [-B] [-K] [-F] [-p] [-P] [-I] [-N] [-e]\n"""
            """💡️ rsa.py --key test """)
            exit()
    def Usage (self):
        parser = argparse.ArgumentParser(description="Usage: [OPtion] [arguments] [ -w ] [arguments]")      
        parser.add_argument("-M",'--message'   , metavar=''          ,help   = " Path of  Plaintext message to Decrypt ")
        parser.add_argument("-D",'--decrypt'   , action="store_true" ,help   = " Decrypt Mode")
        parser.add_argument("-E",'--enctypt'   , action="store_true" ,help   = " Enctypt Mode")
        parser.add_argument("-H",'--hex'       , action="store_true" ,help   = " Output Message Encrypt Hex Format")
        parser.add_argument("-S",'--secret'    , metavar=''          ,help   = " Private key To Decrypt Cihper Text")
        parser.add_argument("-B",'--base64'    , action="store_true" ,help   = " Output Message Encrypt Base64 Format")
        parser.add_argument("-K",'--key'       , metavar=''          ,help   = " Genreagte Key public-key , Private-Key")
        parser.add_argument("-F",'--file'      ,metavar=''           ,help   = " Encrypt Cihper Text file To Decrypt ")
        parser.add_argument("-p",'--public'    ,metavar=''           ,help   = " Encrypt or Decrypt use Symmetric Key public key")
        parser.add_argument("-P",'--private'   ,metavar=''           ,help   = " Encrypt or Decrypt use Symmetric Key private key ")
        parser.add_argument("-I",'--image'    ,metavar=''            ,help   = " Image to write matadata into ")
        parser.add_argument("-N",'--hiden'    ,action='store_true'   ,help   = " write hiden data into the image the Encrypt message and key for Decrypt the message ")
        parser.add_argument("-e",'--exif'    ,action='store_true'   ,help   = " exif the data from image ")
        self.args = parser.parse_args()  
        if len(sys.argv)!=1 :
            pass
        else:
            self.parser = parser.print_help()
            exit()       
if  __name__ == '__main__':
    RSA_algorithm()

