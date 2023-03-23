"""num = int(input("ป้อนตัวเลข : "))#1
a = 10
if num == 1:
    a += 10
elif num == 2:
    a **= 2
elif num == 3:
    a -= 5
else:
    a = a
print("ค่าของ a : ", a)"""


"""num = int(input("ป้อนตัวเลข : "))#2
if num >= 1 and num <= 5:
    print("Low")
elif num >=6 and num <= 10:
    print("Middle")
elif num >=11 and num <=13:
    print("Normal")
elif num >=14 and num <=20:
    print("High")
else:
    print("invalid")"""


"""count = int(input("ป้อนจำนวนสินค้า : "))#3
cost = eval(input("ป้อนราคาสินค้า : "))
pay = count * cost
discount = 0
if pay > 15000:
    discount = pay * 0.15
elif pay >= 10001:
    discount = pay * 0.10
elif pay >= 5000:
    discount = pay * 0.05
print("เงินที่ต้องชำระ : ", pay, "บาท")
print("ส่วนลด : ", discount, "บาท")
print("เงินที่ต้องชำระสุทธิ : ", pay - discount, "บาท")"""

"""count = int(input("ป้อนจำนวนสินค้า : "))#3
cost = eval(input("ป้อนราคาสินค้า : "))
pay = count * cost
discount = 0
if pay >= 1:
    if pay > 15000:
        discount = pay * 0.15
    elif pay >= 10001:
        discount = pay * 0.10
    elif pay >= 5000:
        discount = pay * 0.05
    print("เงินที่ต้องชำระ : ", pay, "บาท")
    print("ส่วนลด : ", discount, "บาท")
    print("เงินที่ต้องชำระสุทธิ : ", pay - discount, "บาท")
else:
    print("ป้อนจำนวนไม่ถูกต้อง")"""

count = int(input("ป้อนจำนวนสินค้า : "))#3 เขียนโฟล
cost = eval(input("ป้อนราคาสินค้า : "))
pay = count * cost
if pay < 5000:
    discount = 0
elif pay <= 10000:
    discount = pay * 0.05
elif pay <= 15000:
    discount = pay * 0.10
else:
    discount = pay * 0.15
print("เงินที่ต้องชำระ : ", pay, "บาท")
print("ส่วนลด : ", discount, "บาท")
print("เงินที่ต้องชำระสุทธิ : ", pay - discount, "บาท")


"""hour = int(input("ป้อนจำนวนชั่วโมง : "))#4
if hour in range(1, 6):
    over_time_money = hour * 100
elif hour in range(6, 11):
    over_time_money = hour * 200
elif hour in range(11, 21):
    over_time_money = hour * 300
else:
    over_time_money = hour * 400
print("เงินค่าล่วงเวลา : ", over_time_money)"""


"""hour = int(input("ป้อนจำนวนชั่วโมง : "))#4
if hour <= 0:
    print("ป้อนค่าไม่ถูกต้อง")
else:
    if hour <= 5:
        rate = 100
    elif hour <= 10:
        rate = 200
    elif hour <= 20:
        rate = 300
    else:
        rate = 400
    over_time_money = hour * rate
    print("เงินค่าล่วงเวลา : ", over_time_money)"""

"""hour = int(input("ป้อนจำนวนชั่วโมง : "))#4
if hour <= 0:
    print("ป้อนค่าไม่ถูกต้อง")
else:
    if hour > 20:
        rate = 400
    elif hour > 10:
        rate = 300
    elif hour > 5:
        rate = 200
    else:
        rate = 100
    over_time_money = hour * rate
    print("เงินค่าล่วงเวลา : ", over_time_money)"""


"""over_time_hour = int(input("ป้อนจำนวนชั่วโมงทำงานล่วงเวลา : "))#5
position = int(input("ป้อนตำแหน่งงาน : "))
salary = int(input("ป้อนจำนวนเงินเดือน : "))
money_per_hour = 0
tax = 0
if position == 1:
    money_per_hour = over_time_hour * 200
    tax = salary * 0.03
elif position == 2:
    money_per_hour = over_time_hour * 300
    tax = salary * 0.05
elif position == 3:
    money_per_hour = over_time_hour * 400
    tax = salary * 0.07
else:
    print("invalid")
salary_net = salary + money_per_hour - tax
print("เงินเดือน : ", salary, "บาท")
print("ค่าตอบแทนล่วงเวลา : ", money_per_hour, "บาท")
print("ภาษี : ", tax, "บาท")
print("รายรับสุทธิ : ", salary_net, "บาท")"""

over_time_hour = int(input("ป้อนจำนวนชั่วโมงทำงานล่วงเวลา : "))#5
position = int(input("ป้อนตำแหน่งงาน : "))
salary = int(input("ป้อนจำนวนเงินเดือน : "))
rot = 0
rt = 0
if position == 1:
    rot = 200
    rt = 0.03
if position == 2:
    rot = 300
    rt = 0.05
if position == 3:
    rot = 400
    rt = 0.07
if position < 1 or position > 3:
    print("invalid")
money_per_hour = rot * over_time_hour
tax = salary * rt
salary_net = money_per_hour + salary - tax
print("เงินเดือน : ", salary, "บาท")
print("ค่าตอบแทนล่วงเวลา : ", money_per_hour, "บาท")
print("ภาษี : ", tax, "บาท")
print("รายรับสุทธิ : ", salary_net, "บาท")





print("VIP = 1 , Member1 = 2 , Member2 = 3 , General = ค่าทั้งหมดที่ไม่ใช่ 1 - 3")
member_type = int(input("ป้อนประเภทลูกค้า : "))
if member_type > 0:
    hour_moto = int(input("ป้อนจำนวนชั่วโมงเช่ารถมอเตอร์ไซค์ : "))
    hour_car = int(input("ป้อนจำนวนชั่วโมงเช่าโมงรถยนต์ : "))
    moto_rent_amount = int(input("ป้อนจำนวนรถมอเตอร์ไซค์ที่เช่า : "))
    car_rent_amount = int(input("ป้อนจำนวนรถยนต์ที่เช่า : "))
    rate_per_moto = (hour_moto * moto_rent_amount) * 100
    rate_per_car = (hour_car * car_rent_amount) * 300
    all_rent = rate_per_moto + rate_per_car
    if member_type != 1 and member_type != 2 and member_type != 3:
        discount = 0
    elif member_type == 1:
        discount = all_rent * 0.20
    elif member_type == 2:
        discount = all_rent * 0.10
    elif member_type == 3 and all_rent <= 500:
        discount = all_rent * 0.05
    else:
        discount = all_rent * 0.10
    net_money = all_rent - discount
    print("จำนวนค่าเช่ารถ : ", all_rent, "บาท")
    print("ส่วนลด : ", discount, "บาท")
    print("จำนวนที่ต้องจ่าย : ", net_money, "บาท")
else:
    print("ประเภทลูกค้าไม่ถูกต้อง")


"""print("VIP = 1 , Member1 = 2 , Member2 = 3 , General = ค่าทั้งหมดที่ไม่ใช่ 1 - 3")
member_type = int(input("ป้อนประเภทลูกค้า : "))
if member_type > 0:
    hour_moto = int(input("ป้อนจำนวนชั่วโมงเช่ารถมอเตอร์ไซค์ : "))
    hour_car = int(input("ป้อนจำนวนชั่วโมงเช่าโมงรถยนต์ : "))
    moto_rent_amount = int(input("ป้อนจำนวนรถมอเตอร์ไซค์ที่เช่า : "))
    car_rent_amount = int(input("ป้อนจำนวนรถยนต์ที่เช่า : "))
    rate_per_moto = hour_moto * moto_rent_amount
    rate_per_car = hour_car * car_rent_amount
    rate_moto = rate_per_moto * 100
    rate_car = rate_per_car * 300
    all_rent = rate_car + rate_moto
    if member_type != 1 and member_type != 2 and member_type != 3:
        discount = 0
    elif member_type == 1:
        discount = all_rent * 0.20
    elif member_type == 2:
        discount = all_rent * 0.10
    elif member_type == 3 and all_rent <= 500:
        discount = all_rent * 0.05
    else:
        discount = all_rent * 0.10
    net_money = all_rent - discount
    print("จำนวนค่าเช่ารถ : ", all_rent, "บาท")
    print("ส่วนลด : ", discount, "บาท")
    print("จำนวนที่ต้องจ่าย : ", net_money, "บาท")
else:
    print("ไม่มีประเภทสมาขิกนี้")"""
