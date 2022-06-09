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
        if item[-3:] == ".py":
            with open(name+"/"+item) as fp:
                output += fp.read()
        elif "." not in item:
            for file in os.listdir(name+"/"+item):
                if item[-3:] == ".py":
                    with open(name+"/"+item+"/"+file) as it:
                              output+=it.read()
                elif "." not in file:
                    print("spooky additional directory"+ name + "/" + item)
                              
                

    print(list)
    
print("".join(output))

with open("final.txt", 'w') as fp:
    fp.write("".join(output))

