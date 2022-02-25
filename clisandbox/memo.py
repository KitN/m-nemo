# Some functions for handling the data

phoneticfile = "memodict.dict"
codedict = {}


def readpairs(filepath):
    # Read the data from the csv into a dictionary.
    with open(filepath, 'r') as reader:
        for line in reader.readlines():
            word, code = line.strip().split(',')
            codedict[word] = code
            pass

def findmnemonics(numerals: str) -> list:
    """ Given some decimal digits, find every word that fits"""
    words = codedict.keys()
    numbers = codedict.values()
    pairs = codedict.items()
    for pair in pairs:
        if pair[1] == numerals:
            print(pair)

readpairs(phoneticfile)
findmnemonics("69")
