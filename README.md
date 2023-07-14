#  $$\color{red}{\textsf{RSA-GENKEY}}$$
# $\color{red}{\textsf{RSA algorithm Decrypt Encrypt}}$
## $\color{yellow}{\textsf{ what is "RSA"}}$
* RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem, one of the oldest, that is widely used for secure data transmission. The acronym "RSA" comes from the surnames of Ron Rivest, Adi Shamir, and Leonard Adleman, who publicly described the algorithm in 1977. An equivalent system was developed secretly in 1973 at Government Communications Headquarters (GCHQ) (the British Signals intelligence agency) by the English mathematician Clifford Cocks. That system was declassified in 1997
###  $\color{red}{\textsf{ Learn about RSA :}}$
* [wiki-Encryption ](https://en.wikipedia.org/wiki/Encryption)
* [techtarget](https://www.techtarget.com/searchsecurity/definition/RSA)
* [tutorialspoint](https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_understanding_rsa_algorithm.htm)
-------------------------------------------------------------------------------
## $\color{red}{\textsf{RSA-GENKEY Features}}$
* support Symmetric and  asymmetric encryption
* Key is encryption
* output encryption file format "Base64 or HEX"
* RAS_GENKEY allows the user to hide the "data", key, and message, in the image
* EXrict data from image and Decrytipt
* auto create a file for each Message and named
### How to use 
* git clone https://www.github.com/jac11/RAS_GENKEY.git
* cd RSA_GENKEY
* chmod +x rsa_alg.py
-----------------------------------------------------------------------------------------------------------
## RSA_GENKEY option 
    
```
usage: rsa_alg.py [-h] [-M] [-D] [-E] ct [-H] [-S] [-B] [-K] [-F] [-p] [-P] [-I] [-N] [-e]

options:
  -h, --help       show this help message and exit
  -M, --message   Path of Plaintext message to Decrypt
  -D, --decrypt    Decrypt Mode
  -E, --encrypt    Encrypt Mode
  -H, --hex        Output Message Encrypt Hex Format
  -S, --secret    Private key To Decrypt Cipher Text
  -B, --base64     Output Message Encrypt Base64 Format
  -K, --key       Genreagte Key public-key, Private-Key
  -F, --file      Encrypt Cihper Text file To Decrypt
  -p, --public    Encrypt or Decrypt use Symmetric Key public key
  -P, --private   Encrypt or Decrypt use Symmetric Key private key
  -I, --image     Image to write metadata into
  -N, --hidden      write hidden data into the image the Encrypt message and key for Decrypt the message
  -e, --Exif       EXIF the data from the image

```
-------------------------------------------------------------------------------------------
 # $\textcolor{blue}{Encryption -Mathed}$
-------------------------------------
 *  ### $\color{yellow}{\textsf{Encryption Message Different key}}$
      **User Will Decrypt the Message using the public key generated for the Cipher Message**  
       * rsa_alg.py -M "Message path" -B "For Base64 format" -E "Encrption mode"
       * rsa_alg.py -M /home/user/Message -B -E
       * for Hex Format use  -H instead of  -B
       * rsa_alg.py -M /home/user/Message -H -E
   * ### $\color{yellow}{\textsf{Encryption With  Same Pravite KEY and Public Key each time}}$
       * Generate Private key and public key use
       * rsa_alg.py  -K "name of the Keys"
       * rsa_alg.py  -K Test
       * by using this command you have private and public keys so you can use  them to encryption the message by anyone
       * so if you encrypt the message with the private key you will Decrypt the message using the public key
       * Capital "P" for the private key
       * Small   "p" For public key
       * rsa_alg.py -P name-Private-Key.pem   --message  Cryto.txt  --hex or --base64 --encrypt
       * rsa_alg.py -P  name-Private-Key.pem  -M Cryto.txt " -H or -B "-E
       * rsa_alg.py -P name-Public-Key.pem    --message  Cryto.txt  --hex or --base64 --encrypt
       * rsa_alg.py -p  name-Public-Key.pem -M Cryto.txt " -H or -B "-E
       * by default the tool will create a folder  to generate the put key  
       ## $\textcolor{red}{RECOMMANDED}$
     *  ##### $\color{yellow}{\textsf{ KEEP  PUT OF THE KEYS "PRIVATE AND PUBLIC" AT SAME ONE.FOLDER }}$
        ##### $\color{yellow}{\textsf{ SO THE TOOL CAN DEDECTIT THE ENCRYPT KEY AND DECRYPT KEY}}$
     * ### $\color{yellow}{\textsf{Encryption Message hidden in Images }}$    
       * To hide Message in the Image
       * Get the image you wish to Hidden Message on the side it any extension 
       * The RSA_GENKEY with hidden the Key For Decrypt the Meaasge auto with Message 
       * output  Image "PNG" exception
       * user specifies the path message and sets the Image path
       * if the User will use  the same Key code  specify the key  For Encrypt
       * RSA_GENKEY  will Create a Folder by message name and  all output files we store in this folder include the image ".png" 
       * Keep  Put Of The Keys "PRIVATE AND PUBLIC" in Same One Folder so The Tool Can Dedecit The Encrypt Key and  Decrypt Key

       * ## $\color{yellow}{\textsf{Hidden Message in Image Generate Key }}$
          * rsa_alg.py --image "Image Path" --message "Message Path" --encrypt --hidden "--base46 or --hex" 
       * by using this command you have private and public keys so you can use  them to encryption the message by anyone
       * so if you encrypt the message with the private key you will Decrypt the message using a public key
       * Capital "P" for the private key
       * Small   "p" For public key
       * rsa_alg.py -P name-Private-Key.pem   --message  Cryto.txt  --hex or --base64 --encrypt
       * rsa_alg.py -P  name-Private-Key.pem  -M Cryto.txt " -H or -B "-E
       * rsa_alg.py -P name-Public-Key.pem    --message  Cryto.txt  --hex or --base64 --encrypt
       * rsa_alg.py -p  name-Public-Key.pem -M Cryto.txt " -H or -B "-E
       * by default the tool will create a folder  to generate the put key  
       ## $\textcolor{red}{RECOMMANDED}$
     *  ##### $\color{yellow}{\textsf{ KEEP  PUT OF THE KEYS "PRIVATE AND PUBLIC" AT SAME ONE.FOLDER }}$
        ##### $\color{yellow}{\textsf{ SO THE TOOL CAN DEDECTIT THE ENCRYPT KEY AND DECRYPT KEY}}$
     * ### $\color{yellow}{\textsf{Encryption Message hidden in Images }}$    
       * To hide Message in the Image
       * Get the image you wish to Hidden Message on the side it any existing 
       * The RSA_GENKEY with hidden the Key For Decrypt the Meaasge auto with Message 
       * output  Image "PNG" exception
       * user specifies the path message and sets the Image path
       * if the User will use  the same Key should   specify the key  For Encrypt
       * RSA_GENKEY  will Create a Folder by message name and  all output files we store in this folder include the image ".png" 
       * Keep  Put Of The Keys "PRIVATE AND PUBLIC" in the Same One Folder so The Tool Can Dedecit The Encrypt Key and  Decrypt Key

       * ## $\color{yellow}{\textsf{Hidden Message in Image Generate Key }}$
          * rsa_alg.py --image "Image Path" --message "Message Path" --encyrpt --hidden "--base46 or --hex" 
          * rsa_alg.py --image Image.jpeg --message Cryto --encyrpt --hidden "--base46 or --hex" 
          *  rsa_alg.py -I Image.jpeg -M Cryto -E -H " -B or -H"
       * ### $\color{yellow}{\textsf{Encryption Message hidden in Images }}$
          *  rsa_alg.py --image "Image Path" --message "Message Path" --encyrpt --hidden "--base46 or --hex" --private name-private-key.pem 
          *  rsa_alg.py -I Image.jpeg -M Cryto -E -H " -B or -H" -P name-private-key. pem
          * rsa_alg.py --image Image.jpeg --message Cryto --encyrpt --hidden "--base46 or --hex" 
          *  rsa_alg.py -I Image.jpeg -M Cryto -E -H " -B or -H"
       * ### $\color{yellow}{\textsf{Encryption Message hidden in Images }}$
          *  rsa_alg.py --image "Image Path" --message "Message Path" --encyrpt --hidden "--base46 or --hex" --private name-private-key.pem 
          *  rsa_alg.py -I Image.jpeg -M Cryto -E -H " -B or -H" -P name-private-key. pem
-------------------------------------------------------------------------------------------
## $\color{blue}{\textsf{Decryption Mathed }}$
-------------------------------------        
 *  ### $\color{yellow}{\textsf{ Decryption Message}}$
       #### $\color{red}{\textsf{USER SHUDO HAVE A PUBLIC KEY TO CAN DECRYPT THE MEESSAGE}}$
       * "-F" For File Encrypt message
       * "-S" path of the public key to decrypt the message 
       * rsa_alg.py -F "File Encrypt Message  patchsets of the Public key" -B "For Base64 format" -D "Decrption mspecifya_alg.py --file EncryptB64-Cryto --secret  name-Public-key.pem  or  -base64 or --hex --decrypt 
       * rsa_alg.py -F EncryptB64-Cryto -S name-Public-key.pem   "-B or-H" -D
   * ### $\color{yellow}{\textsf{Deryption With  Same Pravite KEY nad Public}}$
     #### $\color{blue}{\textsf{ FOR THIS MOTHED IF ENCRYPTION DNE BE PRIVATE KEY }}$
     #### $\color{blue}{\textsf{"DECRYPTION HAVE TO DONE BY PUBLIC KEY" }}$
       * rsa_alg.py -P   name-Public-Key.pem   --file EncryptB64-Cryto --hex or --base64 --decrypt
       * rsa_alg.py -p   name-Public-Key.pem -M Cryto.txt " -H or -B "-D
       * rsa_alg.py -P   name-Private-Key.pem   --file EncryptB64-Cryto --hex or --base64 --decrypt
       * rsa_alg.py -P   name-Private--Key.pem -M Cryto.txt " -H or -B "-D
       * by default the tool will generate a folder to store all result file 
       ## $\textcolor{red}{RECOMMANDED}$
       *  ##### $\color{yellow}{\textsf{ KEEP  PUT OF THE KEYS "PRIVATE AND PUBLIC" AT SAME ONE.FOLDER }}$
          ##### $\color{yellow}{\textsf{ SO THE TOOL CAN DEDECTIT THE ENCRYPT KEY AND DECRYPT KEY}}$
   * ### $\color{blue}{\textsf{Decryption Message hidden in Images}}$
       * use the Image png have data hidden by the RSA_GENKEY tool
       * just use --EXIF
       * rsa_alg.py -I image.png -e -N
       * the tool with the make folder has all exit data "Message- Key- Decrypt Message"

