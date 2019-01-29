from pip._vendor.distlib.compat import raw_input
from scapy.layers.inet import ICMP, IP
from scapy.sendrecv import sr1
import socket
import sys
import signal
import time

#build packets
ipPaket = IP()
icmpPAKET = ICMP()

#build attiributes
timeOutSeconds = 0.8769
ipList = []

def Start():
    print("starting now, please be patient^^")
    CheckForParameters()

def CheckForParameters():
    if len(sys.argv) >= 2:
        if sys.argv[1] is not None:
            if sys.argv[1] == "auto" or sys.argv[1] == "manuel":
                if sys.argv[1] == "auto":
                    startAutoProgress()
                if sys.argv[1] == "manuel":
                    if len(sys.argv) >= 6:
                        if sys.argv[2] == "-iprange" and sys.argv[4] == "-t":
                            if "/" in sys.argv[3]:
                                full = str(sys.argv[3]).split("/")
                                part1 = full[0]
                                part2 = full[1]
                                if validateIPv4Adress(part1):
                                    startManuelProgress(str(sys.argv[3]), int(sys.argv[5]))
                                else:
                                    print("Please specify a valid IPv4 Adress")
                                    printUsage()
                            else:
                                printUsage()
                        else:
                            printUsage()
                    else:
                        printUsage()
            else:
                printUsage()
        else:
            printUsage()
    else:
        printUsage()

def validateIPv4Adress(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

def printUsage():
    print("Useage:","\n")
    print("auto     set mode automatic")
    print("manuel   set mode manuel")
    print("-iprange n     set an Ip adress range")
    print("-t n     set ICMP timeout", "\n")
    print("useage: python findUpDevices.py auto")
    print("useage: python findUpDevices.py manuel -iprange <IPRange> -t <timeout>","\n")
    print("example: python findUpDevices.py manuel -iprange 192.168.1.0/24 -t 5","\n")

def startManuelProgress(iprange, timeoutsec):
    global timeOutSeconds
    timeOutSeconds = timeoutsec
    splitedIP = iprange.split(".")
    splitedIPlastpart = splitedIP[3].split("/")
    ipPart4 = splitedIPlastpart[0]
    ipPartFirst3 = splitedIP[0] + "." + splitedIP[1] + "." + splitedIP[2] + "."
    SetIpListManuel(ipPartFirst3, ipPart4)

def startAutoProgress():
    AutoDetectLocalIpAdress()

def AutoDetectLocalIpAdress():
    myipv4 = socket.gethostbyname(socket.gethostname())
    splitedIP = myipv4.split(".")
    ipv4First3Part = splitedIP[0] + "." + splitedIP[1] + "." + splitedIP[2] + "."
    SetIpListAuto(ipv4First3Part)

def SetIpListManuel(ipPartFirst3, ipPart4):
    if str(ipPart4) == "0":
        ipPart4 = 1
    global ipList
    for i in range(int(ipPart4), 255):
        ipList.append(ipPartFirst3 + str(i))
    #for item in ipList:
    #    print(item)
    SendPacket()

def SetIpListAuto(ipPartFirst3):
    global ipList
    for i in range(int(1), 255):
        ipList.append(ipPartFirst3 + str(i))
    #for item in ipList:
    #    print(item)
    SendPacket()

def SendPacket():
    global ipPaket
    for ipadressv4 in ipList:
        ipPaket.dst = ipadressv4
        response = sr1(ipPaket / icmpPAKET, timeout=timeOutSeconds, verbose=False)
        if not response is None:
            print(ipadressv4, "is ONLINE")
        else:
            print(ipadressv4, "is OFFLINE, UNREACHABLE or DO NOT ANSWER ICMP")

def sigint_handler(signum, frame):
    print("please wait 1 moment...^^")
    time.sleep(1)
    print('okay, bye!')
    sys.exit(1)

signal.signal(signal.SIGINT, sigint_handler)
Start()
