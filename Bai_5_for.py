# Ex 5.5
# n = int(input('Enter n:\n'))
# A, B, C, D, E = 0, 0, 1, 1, 0
# strA, strB, strC, strD, strE = '', '', '', '',''
# if n >= 1:
#     for i in range(1, n+1):
#         if i % 2 != 0:
#             A += i
#             strA += str(i)+'+'
#         else:
#             B += i
#             strB += str(i)+'+'
#         C *= i
#         strC += str(i)+'*'
#         if i % 3 == 0:
#             D *= i
#             strD += str(i)+'*'
#         count = 0
#         for j in range(1, i+1):
#             if i % j == 0:
#                 count = count + 1
#         if count == 2:
#             E = E+is
#             strE += str(i)+'+'
# print('A = %s = %d'%(strA,A))
# print('B = %s = %d'%(strB,B))
# print('C = %s = %d'%(strC,C))
# print('D = %s = %d'%(strD,D))
# print('E = %s = %d'%(strE,E))
# else: print("pls enter a number greater than 1")
# # Ex 5.4
# solution1
# count = 0
# for i in range(1, x+1):
#     if x % i == 0:
#         count = count + 1
# if count == 2:
#     print('%d is an integer' % x)
# else:
#     print('%d is not an integer' % x)
# solution 2
# x = int(input('Enterx:'))
# if x <= 1:
#     print('%d is an integer' % x)
# else:
#     j = 2
#     while x % j != 0:
#         j += 1
#     if j == x:
#         print('%d is an integer' % x)
#         else:
#             print('%d is not an integer' % x)
# Ex 5.3
# n = int(input('Nhập n:\n'))
# x = eval(input('Nhập x:\n'))
# if x == 0:
#     A = 2
# else:
#     A1 = 1
#     A2 = 2
#     for i in range(0,n):
#           A1 = A1*(x*x+x+1)
#           A2 = A2*(x*x-x+1)
#     A=A1+A2
# print('A=',A)

# Ex 5.2
# n = int(input('Nhập n:\n'))
# x = eval(input('Nhập x:\n'))
# if n==0:
#     S = 1
# else:
# S = 1
# for i in range(0,n):
# S = S * (x * x + 1)
# print('S = (x*x + 1)^n=', S)

# Duyệt từng phần tử.

# chuoi= "information"
# for x in chuoi:    # sequence là 1 chuỗi (chuỗi là 1 tập hợp các ký tự)
#   print(x)

# Duyệt chạy theo số lần xác định
# for x in range(6):  #chạy từ 0 -> 5
#   print(x)

# for x in range(2, 6):  #chạy từ 2 -> 5
#   print(x)

# for i in range(1, 11):  #in bảng cửu chương 2
#   print("2 * {} = {}".format(i,2*i))

# for x in range(2, 30, 3):   #chạy từ 2 -> 29, nhảy 1 lần 3 bước
#   print(x)

# for i in range(1, 11,2):  #in bảng cửu chương 2 lẻ
#   print("2 * {} = {}".format(i,2*i))

# tính tổng các số lẻ từ 1 đến 100
# tong = 0
# for x in range(1, 101, 2):
#     tong+=x

# for x in range(1, 101):
#   if x%2 != 0:
#     tong+=x
# print("Tổng lẻ: ", tong)

# Sử dụng else
# for i in range(1, 11):  #in bảng cửu chương 2
#   print("2 * {} = {}".format(i,2*i))
#   tbao = "xong"
# else:
#     print(tbao)

# for i in range(1, 11):  #in bảng cửu chương 2
#   print("2 * {} = {}".format(i,2*i))
#   tbao = "xong"

# print(tbao)

# Sử dụng pass
# for i in range(1, 11):  #in bảng cửu chương 2 lẻ
#   if i%2==0:
#     pass
#   else:
#     print("2 * {} = {}".format(i,2*i))

# Minh họa break: tìm 1 số nguyên lớn nhất trong[1,100] chia hết cho n
n = int(input("Nhập n: "))
max = 1
# for i in range(1, 101):
#   if i%n==0:
#     max= i

# cách sau hay hơn
for i in range(100, 0, -1):
    if i % n == 0:
        max = i
        break  # thoát ngang vòng lặp

print("max = ", max)

# Minh họa continue :
tong = 0
# for x in range(1, 101, 2):   #tính tổng các số lẻ từ 1 đến 100
#   tong += x

# for x in range(1, 101):   #tính tổng các số lẻ từ 1 đến 100
#   if x%2!=0:
#     tong += x

# for x in range(1, 101):   #tính tổng các số lẻ từ 1 đến 100
#   if x%2==0:
#     continue  #Quay lên đầu vòng lặp, bỏ qua các lệnh đứng sau nó
#   tong+=x

# print("Tổng lẻ: ", tong)

'''Nhận xét:
- break và continue chỉ xuất hiện kèm theo điều kiện
'''
