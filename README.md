# RSA_GENKEY
## RSA algorithm {Decrypt-Encrypt}
## what is "RSA"
* RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem, one of the oldest, that is widely used for secure data transmission. The acronym "RSA" comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, who publicly described the algorithm in 1977. An equivalent system was developed secretly in 1973 at Government Communications Headquarters (GCHQ) (the British signals intelligence agency) by the English mathematician Clifford Cocks. That system was declassified in 1997.[2] 
### info :
* [LENRAN ABOUT RSA ](https://en.wikipedia.org/wiki/Encryption)
-------------------------------------------------------------------------------
## RSA_GENKEY Features

* support Symmetric and  asymmetric encryption
* Key is encryption
* out put encryption file format "Base64 or HEX"
* RAS_GENKEY allow user to hidden the "data" ,key and message ,in image
* EXrict data from image and Decrytipt
* auto create file for each Message and named
### how to use 
* git clone https://www.github.com/jac11/RAS_GENKEY.git
* cd RSA_GENKEY
* chmod +x rsa_alg.py
-----------------------------------------------------------------------------------------------------------
## RSA_GENKEY option 
    
```usage: rsa.py [-h] [-M] [-D] [-E] ct [-H] [-S] [-B] [-K] [-F] [-p] [-P] [-I] [-N] [-e]

Usage: [OPtion] [arguments] [ -w ] [arguments]

options:
  -h, --help       show this help message and exit
  -M , --message   Path of Plaintext message to Decrypt
  -D, --decrypt    Decrypt Mode
  -E, --enctypt    Enctypt Mode
  -H, --hex        Output Message Encrypt Hex Format
  -S , --secret    Private key To Decrypt Cihper Text
  -B, --base64     Output Message Encrypt Base64 Format
  -K , --key       Genreagte Key public-key , Private-Key
  -F , --file      Encrypt Cihper Text file To Decrypt
  -p , --public    Encrypt or Decrypt use Symmetric Key public key
  -P , --private   Encrypt or Decrypt use Symmetric Key private key
  -I , --image     Image to write matadata into
  -N, --hiden      write hiden data into the image the Encrypt message and key for Decrypt the message
  -e, --exif       exif the data from image

```
-------------------------------------------------------------------------------------------
## Encryption  Command 
-------------------------------------
 *  ### Encryption Message Different key
       ###  *  THE TOOL WILL GENERATE DIFFERENT KEY FOR EACH TIME USE EVEN IT SAME MESSAGE  
       * rsa_alg.py -M "Message path" -B "For Base64 format" -E "Encrption mode"
       * rsa_alg.py -M /home/user/Message -B -E
       * for Hex Format use  -H instead of  -B
       * rsa_alg.py -M /home/user/Message -H -E
   * ###  - Encryption With Same Pravite KEY nad Public Key 
       * Generate Private key and public key use
       * rsa_alg.py  -K "Nmae of the Keys"
       * rsa_alg.py  -K Test
       * by use this command you have private and public keys so you can use  to encryption the message by any one
       * so if you encrypt the message by private key you will Decrypt the message use public key
       * Captila "P" for private key
       * Smaill "p" For public Key
       * rsa_alg.py -P name-Private-Key.pem   --message  Cryto.txt  --hex or --base64 --encrypt
       * rsa_alg.py -P  name-Private-Key.pem  -M Cryto.txt " -H or -B "-E
       * rsa_alg.py -P name-Public-Key.pem    --message  Cryto.txt  --hex or --base64 --encrypt
       * rsa_alg.py -p  name-Public-Key.pem -M Cryto.txt " -H or -B "-E
       * by defult the tool will greate folder  genrate the put key  
         * ### RECOMMANDED 
           * ### KEEP  PUT OF THE KEYS "PRIEVATE AND PUBLIC" AT SAME ONE FOLDER SO THE TOOL CAN DEDECTIT THE ENCRYPT KEY AND DECRYPT KEY
   * ###  -Encryption Message hidden in Images 
       * To hidden Message in the Image
       * Get iMage you wish to Hidden Message in the side it any exsstion 
       * The RSA_GENKEY with hidden the Key For Decrypt the Meaasge auto with Message 
       * output  Image "PNG" exsstion
       * user he specifies the path mssage and specifies the Image path
       * if you will you Symmetric Key you will specifies the key User will use For Encrypt
       * ### Command Image
          * rsa_alg.py --image "Image Path" --message "Message Path" --encyrpt --hidden "--base46 or --hex" 
          * rsa_alg.py --image Image.jpeg --message Cryto --encyrpt --hidden "--base46 or --hex" 
          *  rsa_alg.py -I Image.jpeg -M Cryto -E -H " -B or -H"


