import sys 
import os 

def reform_file(file_name):
    with open(file_name, "r", encoding="utf8") as f: 
        lst = f.readlines()
    with open(file_name, "w", encoding="utf8") as g :
        for line in lst:
            g.write("|")
            g.write(line.strip())
            g.write("|")
            g.write("\n")
    g.close()
    f.close()
    print("*--- Done : ", file_name)


def main():
    dir_name = sys.argv[1]
    lst = os.listdir(dir_name)
    for i in lst:
        file_name = os.path.join(dir_name, i)
        reform_file(file_name)

if __name__=="__main__":
    main()