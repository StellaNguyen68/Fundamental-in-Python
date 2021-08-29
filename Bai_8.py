# Bai_8_4_thuvien
# tạo file module
# bài 7.2
import Bai_8_3_thuvien as tv
import Bai_8_4_thuvien as tv


def them_vao_list(list_original):
    tl = 1
    while tl == 1:
        gt = eval(input("Nhập giá trị: "))
        list_original.append(gt)
        tl = eval(input("Tiếp tục nhập giá trị? 1: Có, 0: Không "))
    return list_original


def tinh_tong_list(list_original):
    return sum(list_original)
# bài 7.4


def tim_dem_slxh(tuple_original, x):
    return tuple_original.count(x)
# bài 7.6


def in_dictionary(dictionary):
    print('Key \t Value')
    for key, value in dictionary.items():
        print(key, ' -- ', value)


def tim_kiem_dictionary(dictionary, key_search):
    if dictionary.get(key_search) != None:
        return dictionary.get(key_search)
    else:
        return "Không tìm thấy keysearch"


def them_dictionary(dictionary, key_insert, value_insert):
    dictionary[key_insert] = value_insert
    return dictionary


# Tạo file sử dụng module (Chương trình)
# Bài 7.2
list_int = []
tv.them_vao_list(list_int)
print("List: ", list_int)

print("Tổng các giá trị trong list: ", tv.tinh_tong_list(list_int))
# Đếm số lần - tuple
tuple_strings = ('red', 'green', 'yellow', 'blue', 'black',
                 'white', 'pink', 'orange', 'red', 'blue')
s_find = input("Nhập chuỗi cần tìm: ")
print(s_find, " xuất hiện trong tuple ",
      tv.tim_dem_slxh(tuple_strings, s_find), " lần")
# Tạo file sử dụng module (Chương trình)
danh_ba = {'Johnny': '0989741258', 'Katherine': '0903852147', 'Misu': '0913753951', 'Jack':
           '0933753654'}
tl = 1
while tl == 1:
    v = int(input('Bạn muốn làm gì? 1: Xem danh bạ; 2: Tìm kiếm, 3: Thêm mới\t'))
    if cv == 1:
        print('Danh bạ điện thoại:')
        tv.in_dictionary(danh_ba)
    elif cv == 2:
        name_search = input('Nhập tên cần tìm:\n')
        print(tv.tim_kiem_dictionary(danh_ba, name_search))
    elif cv == 3:
        ten = input('Nhập tên:\n')
        fone = input('Nhập số điện thoại:\n')
        tv.them_dictionary(danh_ba, ten, fone)
        tv.in_dictionary(danh_ba)
    tl = int(input("Bạn có muốn tiếp tục không?, 1: có, 0 : Không - "))
# Bai_8_3_thuvien
# tạo file module


def tinh_S(n, x):
    s = 0
    if n == 0:
        s = 1
    else:
        s = pow((x * x + 1), n)
    return s


def tinh_A(n, x):
    A = pow((pow(x, 2) + x + 1), n) + pow((pow(x, 2) - x + 1), n)
    return A


def kiem_tra_so_ngyen_to(x):
    count = 0
    for i in range(1, x+1):
        if x % i == 0:
            count = count + 1
    if count == 2:
        return True
    else:
        return False


# Tạo file sử dụng module (Chương trình)
# bài 5.2
# S = (x^2 + 1)^n
n = int(input('Nhập n:\n'))
x = eval(input('Nhập x:\n'))
S = tv.tinh_S(n, x)
print('S = (x*x + 1)^n=', S)
# bài 5.3 tính A = (x^2 + x + 1)^n + (x^2 - x + 1)^n
n = eval(input("Nhập n: "))
x = eval(input("Nhập x: "))
A = tv.tinh_A(n, x)
print("A = (x^2 + x + 1)^n + (x^2 - x + 1)^n = ", A)
# bài 5.4 Kiểm tra số ng.tố

x = eval(input("Nhập x: "))
if tv.kiem_tra_so_ngyen_to(x):
    print("%d là số nguyên tố" % x)
else:
    print("%d KHÔNG là số nguyên tố" % x)
# #Ex8_2
# # module file
# import math
# def calculate_bmi(weight, height):
#     bmi = weight / pow(height,2)
#     return bmi
# def evaluate(bmi):
#     result = ''
#     if bmi < 18.5:result = 'thin'
#     elif bmi < 25:result = 'normal'
#     else:result = 'fat'
#     return result
# #program file
# import Ex8_2 as tv
# weight = int(input('Enter weight (kg):\n'))
# height = int(input('Enter height (m):\n'))
# bmi = tv.calculate_bmi(weight, height)
# print('Your BMI: %.2f'%bmi)

# print('Result: You are', tv.evaluate(bmi))


# # Ex 8.1
# nam = int(input('Year of birth:\n'))
# chuoi_can = ('Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Kỷ')
# can = chuoi_can[nam % 10]
# chuoi_chi = ('Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu',
#              'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi')
# chi = chuoi_chi[nam % 12]
# print('Năm ', nam, ' âm lịch là năm ', can, chi)
