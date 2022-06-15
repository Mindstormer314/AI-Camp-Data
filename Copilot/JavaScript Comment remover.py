jsText = ""

with open('C#Data-1.1.txt') as fp:
    jsText = fp.read()

comIndex = jsText.find('//')

while comIndex != -1:
    closeIndex = comIndex + 2 + jsText[comIndex + 2:].find('\n')
    jsText = jsText[:comIndex] + jsText[closeIndex:]
    comIndex = jsText.find('//')

    #print(str(comIndex)+ " : " + str(closeIndex))



with open("C#Data-1.2.txt", 'w') as fp:
    fp.write(jsText)
