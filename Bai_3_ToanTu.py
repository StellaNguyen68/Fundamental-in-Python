a = 5
b = 7
c = 10
a = b
print(a)

z = 7 % 3  # mod  => modulo
print("z = ", z)

print("a**b = ", 2**3)
print("7 //3  = ", 7//3)

c += b   # c= c+b
print(c)

c -= b  # c= c-b
print(c)

c /= b  # c= c/b
print(c)

c *= b  # c= c*b
print(c)

c **= b  # c mũ b
print(c)

c //= b  # Thực hiện phép chia, làm tròn cận dưới (Floor Division)
print(c)

# toán tử is
n = 10
m = 5
n = m  # cùng trỏ đến đ.tượng
d = n is m
print("n= ", n, ", m= ", m)
print("d = ", d)

m = 15
print("n= ", n, ", m= ", m)
print("d = ", d)

# Lưu ý:
x = 3*10+9-10/2
y = 3*(10+9)-(10/2)
z = (3*10)+(9-10)/2

print("x= ", x)
print("y= ", y)
print("z= ", z)
