'''
* Có 2 dạng hàm:
    - Hàm không trả về giá trị
    - Hàm trả về giá trị: Phải có dòng return nằm cuối hàm
'''
#hàm trả về giá trị, cd, cr: tham số hình thức
def dien_tich_hcn(cd, cr):
    dt = cd*cr
    return dt

#hàm KHÔNG trả về giá trị
def dien_tich_hcn_2(cd, cr):
    dt = cd*cr
    print("Diện tích hình chữ nhật = ", dt)

#Khai báo biến toàn cục
bien_toan_cuc ="Biến toàn cục"

#demo tham trị
def cong_hai_so(a, b):
    a = 15
    return a+b

def tru_hai_so(x, y):   #nếu muốn trả về tham chiếu, truyền list 1 p.tử (thủ thuật)
    x[0] = 15
    return x[0]+y

#truyền tham chiếu
def ds_hoa(list_hoa):
    list_hoa.append("Hồng")
    list_hoa.append("Cát tường")

#trả về nhiều gía trị
#1. t.hợp 1: trả về 1 tuple
def fun1(): 
    str = "Ăn quả nhớ kẻ trồng cây"
    x   = 20
    return str, x  #hoặc (str, x) 
#2. t.hợp 2: trả về 1 list
def fun2(): 
    str = "Ăn quả nhớ kẻ trồng cây"
    x   = 20
    return [str, x]

#3. t.hợp 3: trả về 1 dictionary
def fun3(): 
    d = dict()
    d[1] = "Ăn quả nhớ kẻ trồng cây"
    d[2] = 20
    return d

