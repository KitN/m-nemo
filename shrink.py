# Make a script to take just 1% of the cmudict dictionary's lines
# Take one in one hundred

shrinkfactor = 2000
datapath     = "./cmudict.dict"
smallpath    = "./smalldict.dict"
with open(datapath, 'r') as reader:
    smallerdata = []
    try:
        for line in enumerate(reader):
            if line[0] % shrinkfactor == 0:
                smallerdata.append(line[1])
    finally:
        reader.close()

with open(smallpath, 'w') as writer:
    for line in smallerdata:
        writer.write(line)
