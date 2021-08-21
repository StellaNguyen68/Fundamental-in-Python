import os 
os.system('cls')    #xóa màn hình trên windows 

s = "Chào các bạn"
print(s)

#Chuỗi nhiều dòng: dùng 3 dấu """" hoặc 3 nháy '

s2 = """Thiện căn ở tại lòng ta 
Chữ Tâm kia mới bằng ba chữ Tài"""
 
print(s2)

#chuỗi được xem như 1 mảng 1 ký tự
s3 = "Chữ Tài liền với chữ Tai một vần"
print(s3[2])
print(s3[2:5])   # từ vị trí 2 đến 5 (nhưng không tính 5)
print(s3[-6:-2]) # Tính từ cuối lên, từ vị trí 2 đến 5 (nhưng không tính 6)

#lặp lại chuỗi
print("="*20)
s4 = "Hello! "
print(s4*4)

#Chiều dài chuỗi
print(len(s4))

# Định dạng chuỗi
name = "Pham Thiên Thanh"
age = 16
height = 1.5
weight = 45

print("1. Tôi tên là %s, tôi %d tuổi, cao %.3f(m) và cân nặng %d(kg)" %(name, age, height, weight))

#cách khác: dùng hàm format, cách này hay hơn
print("2. Tôi tên là {}, tôi {} tuổi, cao {:,.3f}(m) và cân nặng {}(kg)".format(name,age,height,weight))

#{} : placeholder

chuoi ="Trung Tâm Tin học \n ĐH KHTN"
print(chuoi)

