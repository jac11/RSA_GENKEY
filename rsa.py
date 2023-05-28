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
        list_Encrypt = []
        list_Decrypt = []
        for Mas in list_Str :
           Ciphertext = ( Mas ** Public_key ) % N_Num
           list_Encrypt.append(Ciphertext)
        Encrypt =str("".join(str(list_Encrypt))).replace("[",'').replace(',','').replace("]",'') 
        E_base64 = str(base64.b64encode(bytes(Encrypt, 'utf-8'))).replace("b'",'').replace("'",'') 
        D_baes64 =base64.b64decode(E_base64).decode("utf-8").split(" ")
        for Char in D_baes64 :
            Char = int(Char)
            Decrypt =chr((Char ** private_key ) % N_Num)
            list_Decrypt.append(Decrypt)
        Plaintext = "".join(list_Decrypt)
        print("Decrypt : ", E_base64)
        print("="*40)
        print("Massage : ",Plaintext)
    def algorithm (self):
    	if self.args.message:
    	   self.ReadMessage()
    	   self.Gen_PP()
            
    def Useage (self):
        parser = argparse.ArgumentParser(description="Usage: [OPtion] [arguments] [ -w ] [arguments]")      
        parser.add_argument("-M",'--message'   , metavar=''          ,help   = " path of Massage to Encrypit")
        parser.add_argument("-D",'--decrypt'   , action="store_true" ,help   = " Decrypt Massage")
        parser.add_argument("-E",'--enctypt'   , action="store_true" ,help   = " Enctypt Massage")
        parser.add_argument("-H",'--hex'       , action="store_true" ,help   = "output Massage Encrypt Hex Format")
        parser.add_argument("-B",'--base64'    , action="store_true" ,help   = "output Massage Encrypt Base64 Format")
        parser.add_argument("-K",'--key'       , action="store_true" ,help   = "Genreagte Key public-key , Praivate-Key")
        parser.add_argument("-L",'--len'       , action="store_true" ,help   = "length of the Key Genreagte")
        self.args = parser.parse_args() 
        if len(sys.argv)!=1 :
            pass
        else:
            parser.print_help()         
            exit()   	 
if  __name__ == '__main__':
    RSA_algorithm()
