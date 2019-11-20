import sys
import glob
import csv
from operator import itemgetter
import os


def calcAndWrite(singleFile):

    with open(singleFile, 'r') as f:
        lines=f.readlines()
        letter=singleFile.split("/")[-1].split('-')[0]
        date=singleFile.split("/")[-1].split('-')[2]
        #queries
        qUDPv4=0
        qUDPv6 = 0
        qTCPv4=0
        qTCPv6= 0
        for i in lines:
            if 'dns-udp-queries-received-ipv4' in i:
                qUDPv4 = int(i.split(":")[1])
            elif 'dns-udp-queries-received-ipv6' in i:
                qUDPv6 = int(i.split(":")[1])
            elif 'dns-tcp-queries-received-ipv4' in i:
                qTCPv4 = int(i.split(":")[1])
            elif 'dns-tcp-queries-received-ipv6' in i:
                qTCPv6 = int(i.split(":")[1])

        ratioTCPv4="NA"
        try:

            ratioTCPv4= round(100*float(qTCPv4)/(float(qTCPv4)+float(qUDPv4)),2)
        except:
            pass;
        ratioTCPv6="NA"
        try:
            ratioTCPv6= round(100*float(qTCPv6)/(float(qTCPv6)+float(qUDPv6)),2)
        except:
            pass

        with open(letter+"-tcp.csv", 'a') as out:
            fmt_line=str(qUDPv4)+","+str(qTCPv4)+","+str(qUDPv4+qTCPv4)+","+str(ratioTCPv4)
            fmt_line = fmt_line  +","  +str(qUDPv6) + "," + str(qTCPv6) + "," + str(qUDPv6 + qTCPv6) + "," + str(ratioTCPv6)

            out.write(date+","+fmt_line+"\n")
            out.close()

def sort_format():
    files=glob.glob('*-tcp.csv')
    path='tcp_udp'

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)

    for f in files:
        letter=f.split('-')[0]

        reader = csv.reader(open(f), delimiter=",")
        out=open(path+"/"+letter+".csv", 'w')
        out.write("#date,queriesUDP_IPV4,queriesTCP_IPv4,queriesTOTAL_IPv4,ratioTCP_IPv4,queriesUDP_IPV6,queriesTCP_IPv6,queriesTOTAL_IPv6,ratioTCP_IPv6\n")
        for line in sorted(reader, key=itemgetter(0)):
            out.write(' '.join(line).replace(" ", ",")+"\n")
            #out.write(str(line)+"\n")
        out.close()
        os.remove(f)
def main():

    #list files
    path=sys.argv[1]
    if path[-1]!="/":
        path=path+"/"
    path=path+"*/*/traffic-volume/*"
    print(path)
    yaml_files=glob.glob(path)
    for i in  yaml_files:
        calcAndWrite(i)
    sort_format()

    #RSSAC002-data/2013/10/traffic-volume/*.yaml





if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Wrong number of parameters\n")
        print(str(len(sys.argv)))
        print("Usage:  python tcpStats.py $INPUT_PATH")

    else:

        main()