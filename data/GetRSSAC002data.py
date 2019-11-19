import sys
import datetime
import requests


def readLetters(x):
    letters=dict()

    try:

        with open(x,'r') as f:
            lines=f.readlines()
            for l in lines:
                if "#" not in l:
                    sp=l.split(",")
                    letters[sp[0]]=l.strip()
    except:
        print('error input file')

    return letters

def downloadSimple(d):

    for k, v in d.items():
        if k!='g' and k!="h":

            if k=='e':
                print('z')
            letter=k
            path=v.split(",")[-2]
            minDate=v.split(",")[-1]
            minDateD=datetime.datetime(int(minDate[0:4]),int(minDate[4:6]),int(minDate[6:8]))
            minYear=minDate[0:4]
            minMonth=minDate[4:6]
            minDay=minDate[6:8]

            today=datetime.datetime.now()

            #queries
            udpv4=dict()
            tcpv4=dict()
            udpv6=dict()
            tcpv6=dict()

            intStart=int(minDate)
            intEnd=int(str(today).split(" ")[0].replace("-",''))
            diff= (today-minDateD).days

            for i in range(0, diff):
                currentDate= minDateD + datetime.timedelta(days=i)
                currentStrDate = str(currentDate).split(" ")[0].replace("-", '')
                print(k + "," + currentStrDate)

                base2 = v.split(',')[1]
                fullPath = base2 + currentStrDate[0:4] + "/" + currentStrDate[
                                                               4:6] + "/traffic-volume/" + k + "-root-" + currentStrDate + "-traffic-volume.yaml"
                fullPath=fullPath.strip()
                data = requests.get(fullPath)
                data = data.text
                data = data.split("\n")
                for i in data:
                    if 'dns-udp-queries-received-ipv4' in i:
                        udpv4[currentStrDate] = int(i.split(":")[1])
                    elif 'dns-udp-queries-received-ipv6' in i:
                        udpv6[currentStrDate] = int(i.split(":")[1])
                    elif 'dns-tcp-queries-received-ipv4' in i:
                        tcpv4[currentStrDate] = int(i.split(":")[1])
                    elif 'dns-tcp-queries-received-ipv6' in i:
                        tcpv6[currentStrDate] = int(i.split(":")[1])


            with open(k+"-"+ str(intEnd)+'.csv', 'w') as f:
                f.write("#date,udpv4,updv6,tcpv4,tcp6,ratiotcpv4,ratiotcpv6\n")

                sortedKeys=sorted(udpv4)

                for k in sortedKeys:
                    v=udpv4[k]
                    tcpv4ratio="NA"
                    try:
                        tcpv4ratio=float(float(tcpv4[k])/float(udpv4[k])+ float(tcpv4[k]))
                        tcpv4ratio = round(100 * tcpv4ratio, 2)
                    except:
                        pass
                    t4=str(tcpv4ratio)
                    tcpv6ratio="NA"
                    try:

                        tcpv6ratio = float(float(tcpv6[k]) / float(udpv6[k]) + float(tcpv6[k]) )
                        tcpv6ratio = round(100 * tcpv6ratio, 2)
                    except:
                        pass
                    t6=str(tcpv6ratio)

                    f.write(k+","+str(v)+","+str(udpv6[k])+","+str(tcpv4[k])+","+ str(tcpv6[k])+","+t4+","+t6+"\n")


def main():

    lettersPath=readLetters(sys.argv[1])
    downloadSimple(lettersPath)



if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Wrong number of parameters\n")
        print(str(len(sys.argv)))
        print("Usage:  python getRSAAC002data.py $inputFile")

    else:

        main()

'''
def downloadIt(d):
    for k, v in d.items():

        if k != 'g':

            letter = k
            path = v.split(",")[-2]
            minDate = v.split(",")[-1]
            minDateD = datetime.datetime(int(minDate[0:4]), int(minDate[4:6]), int(minDate[6:8]))
            minYear = minDate[0:4]
            minMonth = minDate[4:6]
            minDay = minDate[6:8]

            today = datetime.datetime.now()

            # queries
            udpv4 = dict()
            tcpv4 = dict()
            udpv6 = dict()
            tcpv6 = dict()

            intStart = int(minDate)
            intEnd = int(str(today).split(" ")[0].replace("-", ''))
            diff = (today - minDateD).days

            for i in range(0, 2):
                currentDate = minDateD + datetime.timedelta(days=i)
                currentStrDate = str(currentDate).split(" ")[0].replace("-", '')

                path = v.split(',')[-2]
                if k == 'a' or k == 'j':

                    base2 = v.split(',')[1]
                    fullPath = base2 + currentStrDate[0:4] + "/" + currentStrDate[
                                                                   4:6] + "/traffic-volume/" + k + "-root-" + currentStrDate + "-traffic-volume.yaml"
                    data = requests.get(fullPath)
                    data = data.text
                    data = data.split("\n")
                    for i in data:
                        if 'dns-udp-queries-received-ipv4' in i:
                            udpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-udp-queries-received-ipv6' in i:
                            udpv6[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv4' in i:
                            tcpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv6' in i:
                            tcpv6[currentStrDate] = int(i.split(":")[1])
                    print(k + "," + currentStrDate)
                elif k == 'b':
                    base2 = v.split(',')[1]
                    # https://b.root-servers.org/rssac/2015/12/traffic-volume/b-root-20151215-traffic-volume.yaml
                    fullPath = base2 + currentStrDate[0:4] + "/" + currentStrDate[
                                                                   4:6] + "/traffic-volume/b-root-" + currentStrDate + "-traffic-volume.yaml"
                    data = requests.get(fullPath)
                    data = data.text
                    data = data.split("\n")
                    for i in data:
                        if 'dns-udp-queries-received-ipv4' in i:
                            udpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-udp-queries-received-ipv6' in i:
                            udpv6[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv4' in i:
                            tcpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv6' in i:
                            tcpv6[currentStrDate] = int(i.split(":")[1])
                    print(k + "," + currentStrDate)
                elif k == 'c':
                    base2 = v.split(',')[1]
                    # https://c.root-servers.org/rssac002-metrics/2015/01/traffic-volume/c-root-20150106-traffic-volume.yaml,20150106
                    fullPath = base2 + currentStrDate[0:4] + "/" + currentStrDate[
                                                                   4:6] + "/traffic-volume/c-root-" + currentStrDate + "-traffic-volume.yaml"
                    data = requests.get(fullPath)
                    data = data.text
                    data = data.split("\n")
                    for i in data:
                        if 'dns-udp-queries-received-ipv4' in i:
                            udpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-udp-queries-received-ipv6' in i:
                            udpv6[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv4' in i:
                            tcpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv6' in i:
                            tcpv6[currentStrDate] = int(i.split(":")[1])
                    print(k + "," + currentStrDate)

                elif k == 'd':
                    base2 = v.split(',')[1]
                    # https://c.root-servers.org/rssac002-metrics/2015/01/traffic-volume/c-root-20150106-traffic-volume.yaml,20150106
                    fullPath = base2 + currentStrDate[0:4] + "/" + currentStrDate[
                                                                   4:6] + "/traffic-volume/d-root-" + currentStrDate + "-traffic-volume.yaml"
                    data = requests.get(fullPath)
                    data = data.text
                    data = data.split("\n")
                    for i in data:
                        if 'dns-udp-queries-received-ipv4' in i:
                            udpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-udp-queries-received-ipv6' in i:
                            udpv6[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv4' in i:
                            tcpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv6' in i:
                            tcpv6[currentStrDate] = int(i.split(":")[1])
                    print(k + "," + currentStrDate)


                elif k == 'e':
                    base2 = v.split(',')[1]
                    fullPath = base2 + currentStrDate[0:4] + "/" + currentStrDate[
                                                                   4:6] + "/traffic-volume/e-root-" + currentStrDate + "-traffic-volume.yaml"
                    # print(fullPath)
                    data = requests.get(fullPath)
                    data = data.text
                    data = data.split("\n")
                    for i in data:
                        if 'dns-udp-queries-received-ipv4' in i:
                            udpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-udp-queries-received-ipv6' in i:
                            udpv6[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv4' in i:
                            tcpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv6' in i:
                            tcpv6[currentStrDate] = int(i.split(":")[1])
                    print(k + "," + currentStrDate)

                elif k == 'f':
                    base2 = v.split(',')[1]
                    fullPath = base2 + currentStrDate[0:4] + "/" + currentStrDate[
                                                                   4:6] + "/traffic-volume/f-root-" + currentStrDate + "-traffic-volume.yaml"
                    # print(fullPath)
                    data = requests.get(fullPath)
                    data = data.text
                    data = data.split("\n")
                    for i in data:
                        if 'dns-udp-queries-received-ipv4' in i:
                            udpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-udp-queries-received-ipv6' in i:
                            udpv6[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv4' in i:
                            tcpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv6' in i:
                            tcpv6[currentStrDate] = int(i.split(":")[1])
                    print(k + "," + currentStrDate)
                elif k == 'g':
                    print("update later, g is broken")
                elif k == 'h':
                    # h blacklist access
                    print('h blocks scarping')

                elif k == 'i':
                    base2 = v.split(',')[1]
                    fullPath = base2 + currentStrDate[0:4] + "/" + currentStrDate[
                                                                   4:6] + "/traffic-volume/i-root-" + currentStrDate + "-traffic-volume.yaml"
                    # print(fullPath)
                    data = requests.get(fullPath)
                    data = data.text
                    data = data.split("\n")
                    for i in data:
                        if 'dns-udp-queries-received-ipv4' in i:
                            udpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-udp-queries-received-ipv6' in i:
                            udpv6[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv4' in i:
                            tcpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv6' in i:
                            tcpv6[currentStrDate] = int(i.split(":")[1])
                    print(k + "," + currentStrDate)
                elif k == 'k':
                    base2 = v.split(',')[1]
                    fullPath = base2 + currentStrDate[0:4] + "/" + currentStrDate[
                                                                   4:6] + "/traffic-volume/k-root-" + currentStrDate + "-traffic-volume.yaml"
                    # print(fullPath)
                    data = requests.get(fullPath)
                    data = data.text
                    data = data.split("\n")
                    for i in data:
                        if 'dns-udp-queries-received-ipv4' in i:
                            udpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-udp-queries-received-ipv6' in i:
                            udpv6[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv4' in i:
                            tcpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv6' in i:
                            tcpv6[currentStrDate] = int(i.split(":")[1])
                    print(k + "," + currentStrDate)
                elif k == 'l':
                    base2 = v.split(',')[1]
                    fullPath = base2 + currentStrDate[0:4] + "/" + currentStrDate[
                                                                   4:6] + "/traffic-volume/l-root-" + currentStrDate + "-traffic-volume.yaml"
                    # print(fullPath)
                    data = requests.get(fullPath)
                    data = data.text
                    data = data.split("\n")
                    for i in data:
                        if 'dns-udp-queries-received-ipv4' in i:
                            udpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-udp-queries-received-ipv6' in i:
                            udpv6[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv4' in i:
                            tcpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv6' in i:
                            tcpv6[currentStrDate] = int(i.split(":")[1])
                    print(k + "," + currentStrDate)
                elif k == 'm':
                    base2 = v.split(',')[1]
                    fullPath = base2 + currentStrDate[0:4] + "/" + currentStrDate[
                                                                   4:6] + "/traffic-volume/m-root-" + currentStrDate + "-traffic-volume.yaml"
                    # print(fullPath)
                    data = requests.get(fullPath)
                    data = data.text
                    data = data.split("\n")
                    for i in data:
                        if 'dns-udp-queries-received-ipv4' in i:
                            udpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-udp-queries-received-ipv6' in i:
                            udpv6[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv4' in i:
                            tcpv4[currentStrDate] = int(i.split(":")[1])
                        elif 'dns-tcp-queries-received-ipv6' in i:
                            tcpv6[currentStrDate] = int(i.split(":")[1])
                    print(k + "," + currentStrDate)

            with open(k + "-" + str(intEnd) + '.csv', 'w') as f:
                f.write("#date,udpv4,updv6,tcpv4,tcp6,ratiotcpv4,ratiotcpv6\n")
                for k, v in udpv4.items():
                    tcpv4ratio = "NA"
                    try:
                        tcpv4ratio = float(int(tcpv4[k]) / int(udpv4[k]))
                        tcpv4ratio = round(100 * tcpv4ratio, 2)
                    except:
                        pass
                    t4 = str(tcpv4ratio)
                    tcpv6ratio = "NA"
                    try:

                        tcpv6ratio = float(int(tcpv6[k]) / int(udpv6[k]))
                        tcpv6ratio = round(100 * tcpv6ratio, 2)
                    except:
                        pass
                    t6 = str(tcpv6ratio)

                    f.write(k + "," + str(v) + "," + str(udpv6[k]) + "," + str(tcpv4[k]) + "," + str(
                        tcpv6[k]) + "," + t4 + "," + t6 + "\n")




'''