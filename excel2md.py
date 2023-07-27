import csv
import sys

def csv2md(filename):
    i = 0
    with open("output.md", 'w', encoding='utf8') as x:
        x.write("# 問題集サンプル\n")
        with open(filename, encoding='utf8', newline='') as f:
            csvreader = csv.reader(f)
            next(csvreader)
            for row in csvreader:
                x.write("\n---\n\n")
                x.write("## 問"+str(i)+"\n\n")
                x.write(str(row[0]) + "\n")
                x.write("\n---\n\n")
                x.write("## 問"+str(i)+"\n\n")
                x.write(str(row[0]) + "\n\n")
                x.write("**" + str(row[i]) + "**" + "\n\n")
                x.write(str(row[2]) + "\n")
                print(row)
                i += 1

if __name__ == '__main__' :
    filename = 'sample.csv'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    csv2md(filename)