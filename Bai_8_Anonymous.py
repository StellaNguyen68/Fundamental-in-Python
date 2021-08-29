
'''
Ghi chú:
- Lambda có thể có một hoặc nhiều tham số đầu vào nhưng chỉ trả về một giá trị duy nhất
- Chỉ được phép chứa 1 dòng lệnh 
- Không được phép sử dụng các biến khác, ngoài các tham số 
'''
def tinh_tong(x,y):
	return x+y

tong = lambda x, y: x+y
print(tong(5, 10))

#tính s = (x*x + 1)^n
def tinh_s(x, n):
	s= pow(pow(x, 2)+1, n)
	return s

s = lambda x, n : pow(pow(x, 2)+1, n)
print(s(3, 2))