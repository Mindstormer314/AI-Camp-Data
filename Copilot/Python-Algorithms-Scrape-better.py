import os

directories = os.listdir(path = None)
fixFolders = []
for item in directories:
    if "." not in item:
        fixFolders.append(item)

output = ""

for name in fixFolders:
    list = os.listdir(name)


    for item in list:
        if ".js" in item:
            with open(name+"/"+item) as fp:
                output += fp.read()
        elif "." not in item:
            for file in os.listdir(name+"/"+item):
                if ".js" in file:
                    with open(name+"/"+item+"/"+file) as it:
                              output+=it.read()
                elif "." not in file:
                    for thing in os.listdir(name+"/"+item + "/" + file):
                        if ".js" in thing:
                            with open(name+"/"+item+"/"+file + "/" + thing) as it:
                                output+=it.read()
                        elif "." not in file:
                            for b in os.listdir(name+"/"+item + "/" + file + "/" + thing):
                                if ".js" in b:
                                    with open(name+"/"+item+"/"+file + "/" + thing + "/" + b) as it:
                                        output+=it.read()
                                elif "." not in file:
                                    print("spooky additional directory"+ name + "/" + item + "/" + thing + "/" + b)
                              
                

    print(list)
    
print("".join(output))

with open("final.txt", 'w') as fp:
    fp.write("".join(output))

