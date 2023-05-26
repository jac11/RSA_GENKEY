#d = (e^-1) mod phi(n)
#C = (M^e) mod n = 31^7 mod 33 = 4
#: M = (C^d) mod n = 4^3 mod 33 = 31
# 1<e<phi(n) and gcd(phi(n), e) = 1 

import random
import math
import base64
list_Str = []
string  = "Welcome Back Jacstory to Home 23"
for L in string :
    Num_str = ord(L)
    list_Str.append(Num_str)
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
        self.algorithm()
    def algorithm (self):
        p = random.choice(list)
        q = random.choice(list)
        liste = []
        if p == q:
           p = random.choice(list)
        n = p*q
        QN = (p-1)*(q-1)
        for e in range(int(QN)):
            if 1< e < QN:
               if math.gcd(QN,e) == 1:
                    if e == p :
           	           continue
                    else:
            	        liste.append(e)
        e = random.choice(liste)
        for d in range(QN):
            if (d*e)% QN ==1 :
                if d == e :
                  d +=1
                else:    
                   break        
        list_ency = []
        list_chr = []
        for m in list_Str :
            C = (m**e)%n 
            list_ency.append(C)
        encrypit =str("".join(str(list_ency))).replace("[",'').replace(',','').replace("]",'') 
        enbase64 = str(base64.b64encode(bytes(encrypit, 'utf-8'))).replace("b'",'').replace("'",'') 
        Debaes64 =base64.b64decode(enbase64).decode("utf-8").split(" ")
        for S in Debaes64 :
            S = int(S)
            D = (S**d)%n
            chr_c = chr(D)
            list_chr.append(chr_c)
        text = "".join(list_chr)
        print("C  : ", enbase64)
        print("Massage : ",text)	 
if  __name__ == '__main__':
    RSA_algorithm()
