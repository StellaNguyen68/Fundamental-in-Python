#import Bai_8_function    ==> khi dùng phải Bai_8_function.cong_hai_so
import Bai_8_function as tv		#đặt bí danh  ==> tv.Tên_hàm

#from Bai_8_function import tru_hai_so      # ==> khi dùng tru_hai_so

# dai = int(input("Nhập chiều dài: "))
# rong = int(input("Nhập chiều rộng: "))
# dt = tv.dien_tich_hcn(dai, rong)  	#cú pháp gọi hàm TRẢ về giá trị, dai, rong: là tham số thực
# print("Diện tích HCN: ", dt)

# tv.dien_tich_hcn_2(dai, rong)		#cú pháp gọi hàm KHÔNG TRẢ về giá trị

# bientc = tv.bien_toan_cuc
# print(bientc)

#tham trị
# x = 5
# y = 10
# print("x trước khi gọi hàm: ", x)
# z = tv.cong_hai_so(x, y)
# print("x sau khi gọi hàm: ", x)	# x= ?
# print("z = ", z)		# z =?

#Muốn truyển số nguyên kiểu tham chiếu, phải truyền list (thủ thuật)
# x = [5]
# y = 10
# print("x trước khi gọi hàm: ", x[0])
# z =  tv.tru_hai_so(x, y)
# print("x sau khi gọi hàm: ", x[0])
# print("z = ", z)

#truyền tham chiếu
# lst = ["Đào", "Tử Đằng"]
# print("Trước: ",lst)
# tv.ds_hoa(lst)
# print("Sau: ",lst)

#Hàm trả về nhiều giá trị
chuoi, so = tv.fun1()   #trả về tuple
print(chuoi, ' - ', so)

list_ham = tv.fun2()    #trả về list
print(list_ham)

dict_ham = tv.fun3()    #trả về dictionary
print(dict_ham)

