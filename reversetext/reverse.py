import sys, getopt

#tested on Python 2.7.16

def main(argv):
    inputFile = ''
    #read in and parse arguments
    try:
      opts, args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError:
      print 'reverseme.py -i <inputfile>'
    for opt, arg in opts:
      if opt == '-h':
         print 'reverseme.py -i <inputfile>'
         sys.exit()
      elif opt in ("-i"):
         inputFile = arg
    #read in file
    f = open(inputFile, "r")
    text = f.read()
    f.close()
    #this prints out all the characters starting from the last and working backwards
    print(text [::-1])


if __name__ == "__main__":
   main(sys.argv[1:])
