import random
import os
import sys

def getByteArrayFromFile(path):
    with open(path, 'rb') as f:
        bajty = bytearray(f.read())
        f.close()
        return [i for i in bajty]


def saveByteArrayInFile(path, array):
    bajty = bytearray(array)
    with open(path, 'wb') as f:
        f.write(bajty)
        f.close()


def saveKey(nameFile, key):
    keystr = ""
    for k in key:
        keystr += str(k) + "\n"
    with open(nameFile, 'w') as f:
        f.write(keystr)
        f.close()


def encoder(array):
    newArray = []
    key = []
    for byte in array:
        maks = 256 - byte
        int = random.randint(0, maks-1)
        key.append(int)
        newArray.append(byte + int)
    return newArray, key


def decoder(pathKey, pathFile):
    keys = None
    decodeFile = []
    with open(pathKey, 'r') as f:
        keys = [int(key.strip()) for key in f.readlines()]
        f.close()
    file = getByteArrayFromFile(pathFile)
    i = 0
    for byte in file:
        decodeFile.append(byte - keys[i])
        i = i + 1
    return decodeFile


def Encode(fileName = "output", pathToFile = '', keyFileName = "key"):
    if os.path.isfile(pathToFile):
        print("[OK]\tFile does exist.")
        file = getByteArrayFromFile(pathToFile)
        print("[OK]\tLoad bytes from file.")
        newFile, key = encoder(file)
        print("[OK]\tEncode bytes.")
        if keyFileName != "":
            saveKey(keyFileName, key)
            print("[OK]\tSave key to file '{0}'".format(keyFileName))
        else:
            print("[Error]\tKey file name is not correct")

        if fileName != "":
            saveByteArrayInFile(fileName, newFile)
            print("[OK]\tCreate new encode file '{0}'".format(fileName))
        else:
            print("[Error]\tFile name is not correct")
    else:
        print("[Error]\tFile does not exist.")


def Decode(fileName = "output", pathToFile = '', pathToKeyFile = ''):
    if os.path.isfile(pathToFile) and os.path.isfile(pathToKeyFile):
        print("[OK]\tFiles does exist.")
        decodeFile = decoder(pathToKeyFile, pathToFile)
        print("[OK]\tDecode file")
        if fileName != "":
            saveByteArrayInFile(fileName, decodeFile)
            print("[OK]\tCreate new decode file '{0}'".format(fileName))
        else:
            print("[Error]\tFile name is not correct")
    else:
        print("[Error]\tFiles does not exist.")


def info():
    n = 60
    print("=" * n)
    print("Autor: Hubert Koloska")
    print("Version: v1.0.0")
    print("=" * n)
    print("Commands:")
    print("[+]\tencode <fileName> <pathToFile> <keyFileName>")
    print("[+]\tdecode <fileName> <pathToFile> <pathToKeyFile>")
    print("[+]\thelp")
    print("=" * n)


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == "info":
        info()
    elif cmd == "encode":
        fileName = sys.argv[2]
        pathToFile = sys.argv[3]
        keyFileName = sys.argv[4]
        print("Start Encoding...")
        Encode(fileName, pathToFile, keyFileName)
    elif cmd == "decode":
        fileName = sys.argv[2]
        pathToFile = sys.argv[3]
        pathToKeyFile = sys.argv[4]
        print("Start decoding...")
        Decode(fileName, pathToFile, pathToKeyFile)
    else:
        print("[TIP]\tNext time use 'info'")
        print("[Error]\tCommand not found.")

