import urllib2
import urllib
import os
from cookielib import CookieJar


def downloadPackage(username,password,loginUrl,downloadUrl,targetFile):
    cj = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    
    values = {'LoginForm[username]': username, 'LoginForm[password]': password}

    data = urllib.urlencode(values)
    request = urllib2.Request(loginUrl, data)
    result = urllib2.urlopen(request)
    
    print "login to system "+str(len(result.read()))+" bytes transfered"
    print "Start download"
    request = urllib2.Request(downloadUrl)
    result = urllib2.urlopen(request)
    local_file = open(targetFile, "wb")
    local_file.write(result.read())
    
    local_file.close()
    print str(os.stat(targetFile).st_size) +" bytes downloaded."

def main():
    username = 'admin'
    password = 'admin123'
    loginUrl = "http://www.palmstamp.net/videoproj/index.php?r=site/login"
    downloadUrl = "http://www.palmstamp.net/videoproj/index.php?r=job/download&id=30"
    targetFile = "d:\\test0000.zip"
    downloadPackage(username,password,loginUrl,downloadUrl,targetFile)
main()