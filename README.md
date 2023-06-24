# RSA_GENKEY
## RSA algorithm {Decrypt-Encrypt}
## what is "RSA"
* RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem, one of the oldest, that is widely used for secure data transmission. The acronym "RSA" comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, who publicly described the algorithm in 1977. An equivalent system was developed secretly in 1973 at Government Communications Headquarters (GCHQ) (the British signals intelligence agency) by the English mathematician Clifford Cocks. That system was declassified in 1997.[2] 
### info :
* [RSA](https://en.wikipedia.org/wiki/Encryption)
## RSA_GENKEY option 
    
```usage: rsa.py [-h] [-M] [-D] [-E] [-H] [-S] [-B] [-K] [-F] [-p] [-P] [-I] [-N] [-e]

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
