import urllib
import urllib.request
import random
import string
import multiprocessing.dummy as mp
import time
import threading


req = urllib.request.Request("https://www.poptropica.com/reguser.php")

userfile = open("popusers.txt","a+") 

def randomString(stringLength=10):
    return ''.join([random.choice(string.ascii_letters) for n in range(stringLength)])

def randomNum(numLength=10):
    return ''.join([random.choice(string.digits) for n in range(numLength)])

generatedaccs = 0

def printit():
  threading.Timer(0.1, printit).start()
  global generatedaccs
  print("Generated Accounts : " + str(generatedaccs)) 

printit()

def do_gen(s):
    req.add_header("Connection", "keep-alive")
    req.add_header("Origin", "https://www.poptropica.com")
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    req.add_header("Accept", "*/*")
    req.add_header("X-Requested-With", "ShockwaveFlash/32.0.0.303")
    req.add_header("Sec-Fetch-Site", "cross-site")
    req.add_header("Sec-Fetch-Mode", "no-cors")
    req.add_header("Referer", "https://static.poptropica.com/game/Shell.swf")
    req.add_header("Accept-Encoding", "gzip, deflate, br")
    req.add_header("Accept-Language", "en-US,en;q=0.9")
    req.add_header("Cookie", "ssltest=1; Apache=10.0.11.50.1578287215828284; pop_uid=1578287217.5493-69.167.11.14-10.0.11.173-3856-20539908")

    # MadeByProto Og-Pass

    name = str(randomString(30))
    num = str(randomNum(10))


    body = b"inv=&pass%5Fhash=cbb2986487eb946596ad86b86357c7b2&look=1%2C9724985%2C5518629%2C2171950%2C100%2C1%2C1%2Cchar27%2C4%2Cchar34%2Cchar31%2Cpfool%2C1%2C1%2C1%2C1%2C1%2Cnone%3A&picked=&island=Hub%5Fas3&lname=Gen&num=" + num.encode('utf-8') + b"&age=14&lastx=1650&events%5Flist=&scores=&gender=M&lasty=790%2E3888888888889&user%5Fdata=%7B%7D&fname=Pop&lastroom=Town&login=" + name.encode('utf-8')

    response = urllib.request.urlopen(req, body)

    if response.code == 200:
        # print("Success!")
        # print(name + num + ":" + "MadeByProto")

        userfile.write(name + num + ":" + "MadeByProto\n")

        global generatedaccs
        generatedaccs += 1
    
    else:
        print("Unsuccessful! : " + str(response.code) + " " + response.reason)


if __name__=="__main__":
    p=mp.Pool(500)
    p.daemon = True
    p.map(do_gen,range(0,1000000)) # range(0,1000) if you want to replicate your example
    p.close()
    p.join()
