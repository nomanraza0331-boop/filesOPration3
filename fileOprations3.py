import os 
os.chdir("D:\\sales.3")
with open("data.txt","a+") as f1:
    # f1.seek(0)
    # print(f1.read())
    # f1.write("added one line !")
    
    f1.seek(0)
    print(f1.read())
    f1.write("cabinet  2200  2  4400\n")
    f1.seek(0)
    print(f1.read())
    f1.write("proccer  12000  1  12000\n")
    f1.seek(0)
    print(f1.read())
    f1.write("moniter  7000  1  7000\n")





