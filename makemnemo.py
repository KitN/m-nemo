sm_dict_read = "./smalldict.dict"
sm_dict_write = "./smallmemodict.dict"
lg_dict_read = "./cmudict.dict"
lg_dict_write = "./memodict.dict"

phones = {
    "B":  "9",
    "CH": "6",
    "D":  "1",
    "F":  "8",
    "G":  "7",
    "JH": "6",
    "K":  "7",
    "L":  "5",
    "M":  "3",
    "N":  "2",
    "P":  "9",
    "R":  "4",
    "ER0": "4",
    "ER1": "4",
    "ER2": "4",
    "S":  "0",
    "SH": "6",
    "T":  "1",
    "V":  "8",
    "Z":  "0"
    }

testwords = """
    diekman D IY1 K M AH0 N
    donaghy D AA1 N AH0 G IY0
    earthy ER1 TH IY0
    encumber EH0 N K AH1 M B ER0
    excellency EH1 K S L EH1 N S IY0
    fermi F ER1 M IY0 """
testwords = testwords[1:]

def phone_to_num(cmuline) -> tuple:
    ortho = ""
    memo = ""
    words = cmuline.split()
    ortho = words[0]
    memo = "".join(phones.get(key, '') for key in words[1:])
    return (ortho, memo)

mnemonic_tuples = []
for line in testwords.split("\n"):
    mnemonic_tuples.append(phone_to_num(line))
print(mnemonic_tuples)

# Now try with the small dictionary
smallmemos = []
with open(lg_dict_read, 'r') as reader:
    smallmemos = reader.readlines()

with open(lg_dict_write, 'w') as writer:
    for line in smallmemos:
        memotuple = phone_to_num(line)
        finalline = memotuple[0] + ',' + memotuple[1] + '\n'
        writer.write(finalline)
