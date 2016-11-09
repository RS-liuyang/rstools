import sys, getopt
from netaddr import *

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "hF:f:")

    File1 = ""
    File2 = ""
    for opt, value in opts:
        if opt == "-F":
            File1 = value
        if opt == "-f":
            File2 = value

    #print File1
    #print File2

    f1 = open(File1, 'r')
    f2 = open(File2, 'r')

    ipset1=IPSet()
    ipset2=IPSet()
    for line in f1:
        #print line
        ipset1.add(line)

    for line in f2:
        ipset2.add(line)

    ipset3 = ipset1 ^ ipset2

    for cidr in ipset3.iter_cidrs():
        print cidr

