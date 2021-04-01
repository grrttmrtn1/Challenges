import collections
import sys, getopt

#tested on Python 2.7.16

def main(argv):
    inputFile = ''
    percentVariance = float(90)
    #read in and parse arguments
    try:
      opts, args = getopt.getopt(argv,"hi:p:")
    except getopt.GetoptError:
      print 'occurrences.py -i <inputfile> -p <percentVariance>'
    for opt, arg in opts:
        if opt == '-h':
            print 'occurrences.py -i <inputfile> -p <percentVariance>'
            sys.exit()
        if opt == '-p':
            percentVariance = float(arg)
        elif opt in ("-i"):
            inputFile = arg
    #read in file
    f = open(inputFile, "r")
    #f = open("occurrences.txt", "r")
    text = f.read()
    f.close()
    #utilize library to count occurrences of each character
    results = collections.Counter(text)
    #convert back to a dict
    results = dict(results)
    #calculate an average
    average = sum(results.values())/len(results)
    #cast as a float. dividing by an integer otherwise results with 0
    
    #print all occurences with a variance greater than the percentage passed
    print(dict((k, v) for k, v in results.items() if v < (average * (1 - percentVariance/100))))


if __name__ == "__main__":
   main(sys.argv[1:])
