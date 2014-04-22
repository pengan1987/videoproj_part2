# -*- coding: utf-8 -*-
import csv
import argparse
from xml.etree import ElementTree as et
from distutils.sysconfig import project_base
import codecs
import sys
def toHex(s):
    res = ""
    for c in s:
        codedChar = "%04x" % ord(c)
        if codedChar.startswith("5c"):
            codedChar = "5c"+codedChar
        res += codedChar #at least 2 hex digits, can be more
    return res

def processXMLFile(datafile,outputfile,replaceDict):
    projFile = codecs.open(datafile,'r','utf-8')
    newProjFile = codecs.open(outputfile,'w','utf-8')
    for line in projFile:
        newProjFile.write(processBData(line, replaceDict))
    projFile.close()
    newProjFile.close()
        
def parseCSVfile(textfile):
    replaceDict = {}
    txtfile = codecs.open(textfile,'r','utf-8')
      # next(f) # skip headings
    reader=csv.reader(txtfile,delimiter='\t')
    for lineTag,content in reader:
        replaceDict[toHex(lineTag.strip())]= toHex(content.strip())
    txtfile.close()
    return replaceDict        
    
def processBData(bdata,replaceDict):
    newBData = bdata
    for key,value in replaceDict.items():
        if key in bdata:
            print ("replace "+key+" with "+value)
            newBData = bdata.replace(key,value)
    return newBData


def main():
    reload(sys)
    sys.setdefaultencoding("utf-8")
    cmdParser = argparse.ArgumentParser(description='Replace string in AEPX file with TAB seprated CSV file.')
    cmdParser.add_argument('--inputfile','-i',type=str)
    cmdParser.add_argument('--outputfile','-o',type=str)
    cmdParser.add_argument('--csvfile','-c',type=str)
    if len(sys.argv)==1:
        cmdParser.print_help()
        sys.exit(1)
    args = cmdParser.parse_args()
    
    
    replaceDict = parseCSVfile(args.csvfile)
    processXMLFile(args.inputfile,args.outputfile,replaceDict)
    
main()