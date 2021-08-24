import os

raw_list = os.listdir("./")
list_of_files = []

for x in raw_list:
    list_of_files.append(x.lower())
        
if "lib.pyger" in list_of_files:
    file = open("lib.pyger", "r")
    content = file.readlines()
    file.close()
    if len(content) > 0:
        for x in content:
            command = f"pip install {x.strip()}"
            try:
                os.system(command)
                print("===============================================")
                print(f"{x.strip()} installed")
                print("===============================================")
            except:
                print("Error")
    else:
        print("=================================================")
        print("No library names are mentioned in the pyger file.")
        print("=================================================")
else:
    print("=============================================================================")
    print("lib.pyger is not there in the directory. We generated one pyger file for you.")
    print("=============================================================================")
    open("lib.pyger", "w")
    
    
print()
print()
input("Press ENTER to exit")