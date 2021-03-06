import zipfile
import optparse
import os
from threading import *

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Password = ' + password + '\n'
        os._exit(1)
    except:
        pass


def main():
    parser = optparse.OptionParser("usage%prog "+\
    "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string',\
    help='specify zip file')
    parser.add_option('-d', dest='dname', type='string',\
    help='specify dictionary file')
    (options, args) = parser.parse_args()
    if(options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    with open(dname) as f:
        for line in f:
            password = line.strip('\n')
            t = Thread(target=extractFile, args=(zFile,password))
            t.start()

if __name__ == '__main__':
    main()
