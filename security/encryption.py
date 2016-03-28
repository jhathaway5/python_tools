import base64
import os.path 

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc))

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def encode_file(key, fname):
    file1 = open(fname, 'r')
    text = file1.read()
    file1.close()
    enc_text = encode(key,text)

    fname_new = os.path.basename(fname).split('.')[0]+'.enc'
    dirname = os.path.dirname(fname)

    file2 = open(os.path.join(dirname,fname_new), 'w')
    file2.write(enc_text)
    file2.close()

    return enc_text


def decode_file(key, fname):
    file1 = open(fname, 'r')
    text = file1.read()
    file1.close()
    dec_text = decode(key,text)

    fname_new = os.path.basename(fname).split('.')[0]+'.txt'
    dirname = os.path.dirname(fname)

    file2 = open(os.path.join(dirname,fname_new), 'w')
    file2.write(dec_text)
    file2.close()

    return dec_text


