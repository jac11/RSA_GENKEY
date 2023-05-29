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

list_Str = []
VKEY = []
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
        self.Useage()
        self.algorithm()
    def ReadMessage(self):   
        try:
            with open (self.args.message,'r') as readM:
                Mas_txt = readM.read()
            for L in Mas_txt :
               Num_str =list_Str.append(ord(L))
        except Exception :
            print("[+] Error Read Meassage")  
            exit() 
    def Gen_PP(self):  
        for V in range(0,10):
            add = str(random.random())
            SValue = str(random.random())+"-"
            Value = str(SValue[12:].join(str(add[1:6]))).replace("0.",'').replace('\n','')
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
        Value1 = str(Public_key)+"-"+str(VKEY).replace("[",'').replace("]",'').replace("'",'').replace(",",'').replace(".",'')+str(N_Num)
        Value1 = str(base64.b64encode(bytes(Value1, 'utf-8')))
        Value1 = "".join('\n%s'%Value1[i:i+56] for i in range(0, len(Value1),56)).replace("\n",'',1).replace("b'",'').replace("'",'')
        Value2 = str(private_key)+"-"+str(VKEY).replace("[",'').replace("]",'').replace("'",'').replace(",",'').replace(".",'')+str(N_Num)
        Value2 = str(base64.b64encode(bytes(Value2, 'utf-8')))     
        Value2 = "".join('\n%s'%Value2[i:i+56] for i in range(0, len(Value2),56)).replace("\n",'',1).replace("b'",'').replace("'",'')
        Style = "-"*20
        if self.args.key or self.args.message:
            with open("./Public-key.pem" ,'w') as Publickey:
                Publickey.write(Style+"BEGIN RSA PUBLIC KEY"+Style+"\n"+Value1+\
                '\n'+Style+"END RSA PUBLIC KEY"+Style)  
            with open("./Praivate-Key.pem" ,'w') as PraivateKey:
                PraivateKey.write(Style+"BEGIN RSA PRIVATE KEY"+Style+"\n"+Value2+\
                '\n'+Style+"END RSA PRIVATE KEY"+Style)                           
        self.N_Num       = N_Num 
        self.private_key = private_key
        self.Public_key = Public_key                      
    def En_crypt_Message(self):                    
        list_Encrypt = []
        for Mas in list_Str :
            Ciphertext = ( Mas ** self.Public_key ) % self.N_Num
            list_Encrypt.append(Ciphertext)
        if self.args.base64 and self.args.enctypt :   
            Encrypt = str("".join(str(list_Encrypt))).replace("[",'').replace(',','').replace("]",'')   
            E_base64 = str(base64.b64encode(bytes(Encrypt, 'utf-8'))).replace("b'",'').replace("'",'')
            with open("Encrypt64.txt",'w') as DecryptW:
                DecryptW.write(E_base64)
        if  self.args.hex and self.args.enctypt :
            with open ("EncryptHEX.txt",'w') as HEXData :
                pass
            for Hex in list_Encrypt :
                Hex  = hex(Hex)
                with open ("EncryptHEX.txt",'a') as HEXData :
                    HEX_ST = HEXData.write(str(Hex).replace("0x",' '))
    def De_crypt_Meassage(self):
        list_Decrypt = []
        try : 
            with open ("Praivate-Key.pem",'r') as R_secret :            
                secret_F = R_secret.read().split()
            secret = str("".join(secret_F[5:-4]))
            secret_F = base64.b64decode(secret).decode('utf8', errors='ignore').replace(" ",'').split("-")
            Key = secret_F
            privateK = Key[0]
            NKey= Key[-1][1:]
            if self.args.base64 :
                with open(self.args.file,'r') as Ciphertext_R :
                     DeCipher = Ciphertext_R.read()
                D_baes64 = base64.b64decode(DeCipher).decode("utf-8").split(" ")
                for Char in D_baes64 :
                    Char = int(Char)
                    Decrypt =chr((Char ** int(privateK) )%int(NKey))
                    list_Decrypt.append(Decrypt)
                Plaintext = "".join(list_Decrypt)
                print(Plaintext)
        except Exception as E:
            print("[+] Error read File : ",E)                 
    def algorithm (self):
        if self.args.message :
           self.ReadMessage()
           self.Gen_PP()
           self.En_crypt_Message()
        if self.args.key:
           self.Gen_PP()   
        if self.args.secret and self.args.file:
           self.De_crypt_Meassage()
    def Useage (self):
        parser = argparse.ArgumentParser(description="Usage: [OPtion] [arguments] [ -w ] [arguments]")      
        parser.add_argument("-M",'--message'   , metavar=''          ,help   = " path of Massage to Encrypit")
        parser.add_argument("-D",'--decrypt'   , action="store_true" ,help   = " Decrypt Massage")
        parser.add_argument("-E",'--enctypt'   , action="store_true" ,help   = " Enctypt Massage")
        parser.add_argument("-H",'--hex'       , action="store_true" ,help   = "output Massage Encrypt Hex Format")
        parser.add_argument("-S",'--secret'    , metavar=''          ,help   = "output Massage Encrypt Hex Format")
        parser.add_argument("-B",'--base64'    , action="store_true" ,help   = "output Massage Encrypt Base64 Format")
        parser.add_argument("-K",'--key'       , action="store_true" ,help   = "Genreagte Key public-key , Praivate-Key")
        parser.add_argument("-F",'--file'      ,metavar=''           ,help   = "Genreagte Key public-key , Praivate-Key")
        parser.add_argument("-L",'--len'       , action="store_true" ,help   = "length of the Key Genreagte")
        self.args = parser.parse_args() 
        if len(sys.argv)!=1 :
            pass
        else:
            parser.print_help()         
            exit()   	 
if  __name__ == '__main__':
    RSA_algorithm()
