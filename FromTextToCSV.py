import json

def create():
    inputFile = open("mails.txt", "rt")
    emails = []
    outputFile = open("out.csv", "wt")
        
    for line in inputFile:
        firstComma = line.replace(',', '\n')
        removeFirstSign = firstComma.replace(' <', ', ')
        removeSecondSign = removeFirstSign.replace('>', '')
        arrValue = str(removeSecondSign)
        for x in arrValue.split("\n"):
            emails.append(str(x))
    subArr = []
    for i in emails:
       if i not in subArr:
          subArr.append(i)
    for line in subArr:
        outputFile.write(str(line+'\n'))
    outputFile.close() #close file


if __name__ == '__main__':
    create()
