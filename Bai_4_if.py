
# Ex 4.5
room = eval(input("Enter room type (from 1 to 8): "))
night = eval(input("number of night:"))
UnitPrice = (1260, 1550, 1830, 1830, 2120, 2120, 2540, 4800)
Price = UnitPrice[room-1]*night

if night <= 1:
    print('Total Price:', Price)
elif night <= 3:
    print('Total Price:', Price*0.75)
else:
    print('Total Price:', Price*0.7)

# Ex 4.4
# kw = eval(input("Enter consumption (kw): "))
# if kw <= 50:
#     Elecfee = kw*1.484
# elif kw <= 100:
#     Elecfee = 50*1.484+(kw-50)*1.533
# elif kw <= 200:
#     Elecfee = 50*1.484+50*1.533+(kw-100)*1.786
# elif kw <= 300:
#     Elecfee = 50*1.484+50*1.533+100*1.786+(kw-200)*2.242
# elif kw <= 400:
#     Elecfee = 50*1.484+50*1.533+100*1.786+100*2.242+(kw-300)*2.503
# else:
#     Elecfee = 50*1.484+50*1.533+100*1.786+100*2.242+100*2.503+(kw-400)*2.587
# print('Total fee', Elecfee)

# Ex 4.2
# car = eval(input('Type of car (4 or 7):'))
# dis = eval(input("Enter distance (km): "))
# time = eval(input("Waiting time (min): "))

# if time <= 5:
#     Waitingfee = 0
# else:
#     Waitingfee = (time-5)*0.750
# print('Waiting fee = ({} - 5)*750d ='.format(time), Waitingfee)

# if car == 4:
#     if dis <= 0.8:
#         Cost = 11
#     elif dis <= 30:
#         Cost = 11 + 15.3*(dis-0.8)
#     else:
#         Cost = 11 + 15.3*(30-0.8) + (dis-30)*12.1
# else:
#     if dis <= 0.8:
#         Cost = 12
#     elif dis <= 30:
#         Cost = 12 + 16.1*(dis-0.8)
#     else:
#         Cost = 12 + 16.1*(30-0.8) + (dis-30)*13.8

# print("Cost =", Cost)
# Totalfee = Waitingfee + Cost
# print('Totalfee = {} + {} = {}'.format(Waitingfee, Cost, Totalfee))

# dtb = eval(input("Nhập điểm trung bình: "))

# #1 điều kiện
# # if dtb >=5:
# #     print("Đậu")

# #2 điều kiện
# if dtb >=5:
#     print("Đậu")
# else:
#     print("Rớt")
