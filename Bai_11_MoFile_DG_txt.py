''' 
"a+": Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. 
The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
'''
#Mở file
f = open("baihat.txt","a+", encoding="utf-8")  #lưu ý quan trọng, phải lưu tập tin chọn chế độ utf-8 (lưu chế độ nào thì mở chế đó, nếu k nó sẽ báo lỗi )
print("Xem thuộc tính: ")
print(f.closed,'\t', f.mode,'\t', f.name)    #xem các thuộc tính

f.seek(0)
print("Vị trí hiện hành của con trỏ: " , f.tell())
chuoi = f.read()
print(chuoi) # không có dữ liệu vì mở chế độ này con trỏ này nằm cuối file, nếu muốn đọc từ đầu phải dùng lệnh f.seek(0)

noidung = """LÃNG DU
Âm thanh ngây ngất vui
cho đôi ta lớn lên cùng nhau
Thênh thang trong nắng mai
đôi ta vui bước trong tự do"""

f.write(noidung)    #Ghi vào cuối file
f.close()

