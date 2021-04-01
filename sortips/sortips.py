import socket
import sys, getopt

#tested on Python 2.7.16

def main(argv):
    inputFile = ''
    outputFile = 'results.txt'
    #read in and parse arguments
    try:
      opts, args = getopt.getopt(argv,"hi:o:")
    except getopt.GetoptError:
      print 'iplist.py -i <inputfile> -o <outputfile>'
    for opt, arg in opts:
        if opt == '-h':
            print 'iplist.py -i <inputfile> -p <outputfile>'
            sys.exit()
        if opt == '-o':
            outputFile = arg
        elif opt in ("-i"):
            inputFile = arg
    #read in file
    f = open(inputFile, "r")
    #f = open("iplist.txt", "r")
    text = f.read()
    f.close()
    iplist = text.split('\r\n')
    iplist= list(set(iplist))
    iplist = sorted(iplist,key=socket.inet_aton)
    with open(outputFile, 'w') as f:
        for item in iplist:
            f.write("%s\n" % item)
    f.close()

if __name__ == "__main__":
   main(sys.argv[1:])
