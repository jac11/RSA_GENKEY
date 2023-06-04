#!/usr/bin/en#!/usr/bin/env python
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
        self.algorithm()
    def ReadMessage(self): 
        try:
            with open (self.args.message,'r') as readM:
                Mes_txt = readM.read()
            if os.path.exists(path+self.args.message.split("/")[-1]) :
               pass
            else:  
                 os.mkdir(path+self.args.message.split("/")[-1])  
           
            for L in Mes_txt :
               Num_str =list_Str.append(ord(L))
            time.sleep(.15)   
            print("✉️   Message        ::------------:: ", str("".join(self.args.message.split("/")[-1])))   
        except Exception as E :
            print(" 🚨️🚧️ Error  ::------------:: " , E)  
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

                pbkey = path+self.args.message.split("/")[-1]+"/"+str(self.args.output)
                with open(pbkey+"-Public-key.pem" ,'w') as Publickey:
                    Publickey.write(Style+"BEGIN RSA PUBLIC KEY"+Style+"\n"+Value1+\
                    '\n'+Style+"END RSA PUBLIC KEY"+Style)  
                with open(pbkey+"-Private-Key.pem" ,'w') as PrivateKey:
                    PrivateKey.write(Style+"BEGIN RSA PRIVATE KEY"+Style+"\n"+Value2+\
                    '\n'+Style+"END RSA PRIVATE KEY"+Style) 

            if self.args.key  and not self.args.message :
                if os.path.exists(path+self.args.output+"-KEY"+"/") :
                       pass
                else:   
                    os.mkdir(path+self.args.output+"-KEY"+"/")   
                    print(1)
                pbkey = path+self.args.output+"-KEY"+"/"+self.args.output
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
            print("📌️  P*Q-Value      ::------------::  **********     ✔️ ")
            time.sleep(.15) 
            print("🎯  Euler-Totient  ::------------::  **********     ✔️")
            time.sleep(.15) 
            print("🔑  Public_key     ::------------::  Genreagted 🗝️   ✔️")
            time.sleep(.15) 
            print("🔑  Private_key    ::------------::  Genreagted 🗝️   ✔️")
            time.sleep(.15) 
            print("="*40)

            if (self.args.key  and self.args.output ) and not (self.args.message\
            and self.args.decrypt and not self.args.enctypt) :
                print("🔑  Keys-Info 🔑  : "+'\n'+"="*20)
                print("🗝️   Public_key     ::------------:: ",self.args.output+"-Public-key.pem")
                time.sleep(.15) 
                print("🔑  Private_key    ::------------:: ",self.args.output+"-Private-key.pem")
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
            print("🚨️🚧️  Error  : ::------------::",E)  
        except KeyboardInterrupt :
            print("🚨️🚧️  Error ::------------: KeyboardInterrupt")    
            exit()                          
    def En_crypt_Message(self): 
        try:  
            print("🔐 Encrypt-Info 🔐 : "+'\n'+"="*20)
            with open(".path",'r') as readnewpath:
                path = readnewpath.read()                      
            list_Encrypt = []
            for Mas in list_Str :
                Ciphertext = ( Mas ** self.Public_key ) % self.N_Num
                list_Encrypt.append(Ciphertext)
                print("⏳ Ciphertext   ::------------:: ",str(random.random())[2:])
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
            if self.args.base64 and self.args.enctypt :   
                Encrypt = str("".join(str(list_Encrypt))).replace("[",'')\
                .replace(',','').replace("]",'')   
                E_base64 = str(base64.b64encode(bytes(Encrypt, 'utf-8')))\
                .replace("b'",'').replace("'",'')
                with open(path+"/EncryptB64-"+str(path.split("/")[-1]) ,'w') as DecryptW:
                    DecryptW.write(E_base64)
            if  self.args.hex and self.args.enctypt :
                with open (path+"/EncryptHEX-"+str(path.split("/")[-1]),'w') as HEXData :
                    for Hex in list_Encrypt :
                        Hex  = hex(Hex)
                        with open (path+"/EncryptHEX-"+str(path.split("/")[-1]) ,'a') as HEXData :
                            HEX_ST = HEXData.write(str(Hex).replace("0x",' '))
           
            time.sleep(.15) 
            print("✍️   Plain-text           ::------------:: ", str("".join(self.args.message.split("/")[-1])))
            time.sleep(.15)
            if  self.args.base64 : 
                print("🛡️   Ciphertext           ::------------::  Format Base64 ")
                time.sleep(.15)
                print("🔐  Encrypted message    ::------------:: " ,"EncryptB64-"+str(path.split("/")[-1]) )
            else:
                print("🛡️   Ciphertext           ::------------::  Format Hex String ")
                time.sleep(.15) 
                print("🔐  Encrypted message    ::------------:: " ,"EncryptHEX-"+str(path.split("/")[-1]) )
            time.sleep(.15) 
            print("💯  Encrypted Process    ::------------::  Done ")   
            time.sleep(.15)
            print("💾  location             ::------------::  file://"+path)            
        except Exception as E:
            print("🚨️🚧️  Error  ::------------:: ",E)  
        except KeyboardInterrupt :
            print("🚨️🚧️  Error ::------------:: KeyboardInterrupt")    
            exit()                               
    def De_crypt_Message(self):
        print("🎲️ Decryption-Info 🎲️ : "+'\n'+"="*20)
        with open('.path','r') as path :
            path = path.read()
        with open('.path2','r') as path2:
             path2 = path2.read()    
        list_Decrypt = []
       
        try : 
            with open (path2+"-Private-Key.pem",'r') as R_secret :            
                secret_F = R_secret.read().replace("\n","",2).split("#")
            secret = str("".join(secret_F[4:-4]))
            secret_F = str(base64.b64decode(bytes(secret,'utf-8')))\
            .replace(" ",'').replace("b'",'').replace("'",'').split("-")
            Key = secret_F
            privateK = int(Key[0])
            NKey= int(Key[-1][1:])   
            if self.args.base64 :
                with open(self.args.file,'r') as Ciphertext_R :
                     DeCipher = Ciphertext_R.read()     
                D_baes64 = base64.b64decode(DeCipher).decode("utf-8").split(" ")
                for Char in D_baes64 :  
                    print("⏳ Decryption   ::------------:: ",str(random.random())[2:]) 
                    sys.stdout.write('\x1b[1A')
                    sys.stdout.write('\x1b[2K') 
                    Char = int(Char)   
                    Decrypt =chr((Char ** int(privateK) )%int(NKey))
                    list_Decrypt.append(Decrypt) 
                Plaintext = "".join(list_Decrypt)            
                with open(str("/".join(path2.split("/")[0:-1]))+"/DecryptB64_"+\
                    str("".join(path2.split("/")[-2])),'w') as Text :
                      Text.write(Plaintext)
            if self.args.hex:
                with open(self.args.file,'r') as Ciphertext_R :
                    DeCipher = Ciphertext_R.read().split(" ")
                    DeCipher  = DeCipher[1:]
                    for HEX in DeCipher :
                        print("⏳ Decryption   ::------------:: ",str(random.random())[2:]) 
                        sys.stdout.write('\x1b[1A')
                        sys.stdout.write('\x1b[2K') 
                        HEXTONUM = int(HEX,16)
                        Decrypt =chr((HEXTONUM  ** int(privateK) )%int(NKey))
                        list_Decrypt.append(Decrypt)
                Plaintext = "".join(list_Decrypt)
                with open(str("/".join(path2.split("/")[0:-1]))+"/DecryptHEX_"+\
                    str("".join(path2.split("/")[-2])),'w')as Text :
                      Text.write(Plaintext)
            time.sleep(.15) 
            print("🔐  Eecryption-message    ::------------::  " +str(self.args.file.split("/")[-1]) )
            if self.args.base64 :
                time.sleep(.15) 
                print("🖨️   Decrypted-message     ::------------::  DecryptB64-"+str(path2.split("/")[-2]))
            if self.args.hex:
                time.sleep(.15) 
                print("🖨️   Decrypted-message     ::------------::  DecryptHEX-"+str(path2.split("/")[-2]))  
            time     
            print("💯  Decryption Process    ::------------::  Done ")   
            time.sleep(.15)
            print("💾  location              ::------------::  file://"+path+str(path2.split("/")[-2]))  
        except Exception as E:
            print("🚨️🚧️  Error  ::------------:: ",E)  
        except KeyboardInterrupt :
            print("🚨️🚧️  Error ::------------:: KeyboardInterrupt")    
            exit()                   
    def algorithm (self):
        if self.args.message and self.args.output:
           self.ReadMessage()
           self.Gen_PP()
           self.En_crypt_Message()
        elif self.args.key and self.args.output and not self.args.message:
           self.Gen_PP()   
        elif self.args.secret and self.args.file\
        and self.args.decrypt\
        and (self.args.base64 or self.args.hex):
           self.De_crypt_Message()
        else:
            print(
                   """usage: rsa.py [-h] [-M] [-D] [-E] [-H] [-S] [-B] [-K] [-F] [-O]\n"""
                   """Usage: [OPtion] [arguments] [ -w ] [arguments]"""
                )
    def Usage (self):
        parser = argparse.ArgumentParser(description="Usage: [OPtion] [arguments] [ -w ] [arguments]")      
        parser.add_argument("-M",'--message'   , metavar=''          ,help   = " path of Message to Encrypit")
        parser.add_argument("-D",'--decrypt'   , action="store_true" ,help   = " Decrypt Message")
        parser.add_argument("-E",'--enctypt'   , action="store_true" ,help   = " Enctypt Message")
        parser.add_argument("-H",'--hex'       , action="store_true" ,help   = "output Message Encrypt Hex Format")
        parser.add_argument("-S",'--secret'    , metavar=''          ,help   = "add private key To Decrypt Cihper Text")
        parser.add_argument("-B",'--base64'    , action="store_true" ,help   = "output Message Encrypt Base64 Format")
        parser.add_argument("-K",'--key'       , action="store_true" ,help   = "Genreagte Key public-key , Private-Key")
        parser.add_argument("-F",'--file'      ,metavar=''           ,help   = " EnCrypited Cihper Text file To Decrypt ")
        parser.add_argument("-O",'--output'    ,metavar=''           ,help   = " output key Name")
        self.args = parser.parse_args() 
        if len(sys.argv)!=1 :
            pass
        else:
            parser.print_help()         
            exit()       
if  __name__ == '__main__':
    RSA_algorithm()
