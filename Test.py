'''ticket_ubon = int(input("ตั๋วอุบล : "))
ticket_nong_khai = int(input("ตั๋วหนองคาย : "))
ticket_khon_khan = int(input("ตั๋วขอนแก่น : "))
ubon_pay = ticket_ubon * 521
nong_khai_pay = ticket_nong_khai * 494
khon_khan_pay = ticket_khon_khan * 365
discount = 0
all_money_pay = ubon_pay + nong_khai_pay + khon_khan_pay
all_ticket = ticket_ubon + ticket_nong_khai + ticket_khon_khan
if all_ticket > 5:
    discount = all_ticket * 30
if all_money_pay > 1500:
    discount = all_money_pay * 0.05
else:
    discount = 0
all_discount_pay = all_money_pay - discount
print("จำนวนเงินที่ต้องชำระก่อนหักส่วนลด : ", all_money_pay, "บาท")
print("เงินส่วนลด : %0.2f" % discount, "บาท")
print("เงินที่ต้องชำระ : %0.2f" % all_discount_pay, "บาท")'''

'''###############################################################################'''

'''member_type = input("ป้อนประเภทสมาชิก ไม่เป็นเป็นสามาชิก = u,U และ เป็นสมาชิก = m,M : ")
if member_type in ('u', 'U', 'm', 'M'):
    cargo_amount = int(input("ป้อนจำนวนสินค้า : "))
    cargo_price = int(input("ป้อนราคาสินค้า : "))
    cargo_per_price = cargo_price * cargo_amount
    discount = 0
    if member_type in ('u', 'U',):
        if cargo_per_price > 1500:
            discount = cargo_per_price * 0.05
    else:
        if cargo_per_price <= 1500:
            discount = cargo_per_price * 0.05
        else:
            discount = cargo_per_price * 0.10
    pay_discount = cargo_per_price - discount
    vat_7_percent = pay_discount * 0.07
    pay_discount_vat = pay_discount + vat_7_percent
    print("ราคาสินค้าทั้งหมด : ", cargo_per_price, "บาท")
    print("จำนวนเงินส่วนลด : : ", discount, "บาท")
    print("ราสินค้าหลังหักส่วนลด : ", pay_discount, "บาท")
    print("จำนวนภาษีมูลค่าเพิ่ม : %0.2f" % vat_7_percent, "บาท")
    print("จำนวนเงินที่ต้องชำระ : ", pay_discount_vat, "บาท")
else:
    print("ป้อนประเภทสมาชิกไม่ถูกต้อง")'''

'''##########################################################################'''





'''member_type = input("ป้อนประเภทลูกค้า N=สมาชิกปกติ และ U=ไม่เป็นสมาชิก : ")
if member_type in ('N','n', 'U', 'n'):
    rent_day_book = int(input('จำนวนวันที่เช่าหนังสือ: '))
    rent_money = 0
    discount = 0
    pay = 0
    if member_type in ('N','n'):
        rent_money = rent_day_book
        pay = rent_money
        if rent_money > 20:
            discount = rent_money * 0.15
            pay = rent_money - discount
    else:
        rent_money = 3 * rent_day_book
        pay = rent_money
        if rent_money > 50:
            discount = rent_money * 0.10
            pay = rent_money - discount
    print("ค่าเช่าหนังสือก่อนหักส่วนลด : ", rent_money)
    print("ส่วนลด : ", discount)
    print("ค่าเช่าหนังสือหลังหักส่วนลด : ", pay)
else:
    print("กรุณากรอกประเภทลูกค้าให้ถูกต้อง")'''

'''##########################################################################'''

"""member_type = input("กรอกประเภทลูกค้า R=สมาชิก และ G=ทั่วไป : ")
if member_type in ("R", "G"):
    rent_day = int(input('กรอกจำนวนวันที่เช่า: '))
    pay_money = 300 * rent_day
    discount = 0
    if member_type in ("R"):
        discount = pay_money * 0.10
    else:
        if pay_money > 1000:
            discount = pay_money * 0.05
    print('ค่าเช่ารถจักยานยนต์ก่อนหักส่วนลด: ', pay_money)
    print('ส่วนลด: ', discount)
    print('ค่าเช่ารถจักยานยนต์หลังหักส่วนลด: ', pay_money - discount)
else:
    print('กรุณากรอกประเภทลูกค้าให้ถูกต้อง')"""

'''##########################################################################'''

'''position_type = input('กรอกตำแหน่ง L=ลูกจ้าง และ E=พนักงาน: ')
if position_type in("L","E"):
    income = int(input('กรอกเงินเดือน: '))
    over_time = int(input('จำนวนชั่วโมงทำงานล่วงเวลา: '))
    salary = 0
    if position_type in("L"):
        tax = income * 0.02
        money_time = 200 * over_time
        salary = income + money_time - tax
    else:
        tax = income * 0.03
        money_time = 300 * over_time
        salary = income + money_time - tax
    print("จำนวนเงินภาษี : ", tax)
    print("จำนวนเงินค่าล่วงเวลา : ", money_time)
    print("รายได้สุทธิ : ", salary)
else:
    print("กรุณากรอกตำแหน่งให้ถูกต้อง")'''

'''##########################################################################'''

"""kind = input("ป้อนประเภทลูกค้า < N = สมาชิกปกติ, U = ไม่เป็นสมาชิกก> ==> : ")
if kind.lower() in ("n", "u"):
    print("T")
else:
    print("F")"""

