import os
from os import path
import csv

#Mở đọc file csv
# dd = os.getcwd() + "\\danhba.csv"
# if path.exists(dd):
#     f = open(dd, encoding="utf-8")
#     for row in csv.reader(f):
#         # print(row)  #hoặc đọc từng cột 
#         #print(row[0], "\t", row[1])
#         chuoi = ""
#         for col in range(0,len(row)):
#             chuoi += row[col] + "\t"

#         print(chuoi)
#     f.close()
# else:
#     print("Không có tập tin này")

#Mở ghi file csv
dd = os.getcwd() + "\\danhba.csv"
f = open(dd,'a', newline='', encoding="utf-8")      
listContent = [['Thiên Thanh', '0913 753852'], ['Hoạ Mi', '0989 753951'], ['Tường Vy','0903 123456']]
for item in listContent:        
    csv.writer(f).writerow(item)

f.close()        