"""canned_fish = int(input("ป้อนจำนวนปลากระป๋อง : "))
fish = 3
tomato = 4
over_All = (fish + tomato) * canned_fish
print("จำนวนวัตถุดิบทั้งหมดที่ต้องใช้ทั้งหมด : ", over_All," ชิ้น")"""
"""##################################################################"""
"""room_rate = int(input("ป้อนอัตราค่าเช่าห้อง : ")) #อัตรค่าเช่าหอพัก
month = int(input("ป้อนจำนวนเดือนที่เช้า : "))
water_const = eval(input("ป้อนปริมาณน้ำ : "))
power_const = eval(input("ป้อนปริมาณไฟฟ้า : "))
rate_month = room_rate * month
water_const = water_const * month
power_const = power_const * month
print("อัตราค่าเช่าต่อเดือน : ",rate_month)
print("ปริมาณค่าน้ำที่ใช้ไป : ", water_const)
print("ปริมาณค่าไฟที่ใช้ไป : ", power_const)"""
"""#####################################################################"""
"""amount_cargo = int(input("ป้อนจำนวนสินค้า : ")) #ราคาสินค้ารวม #และเงินภาษี
price_cargo = int(input("ป้อนราคาสินค้า : "))
all_cargo_price = price_cargo * amount_cargo
vat_7_percent = all_cargo_price * 0.07
print("ราคาสินค้าทั้งหมด : %d " % all_cargo_price, "บาท")
print("เงินภาษี 7 เปอร์เซ็นต์ : %0.2f" % vat_7_percent, "บาท")"""
"""###################################################################"""
"""salary = int(input("ป้อนเงินเดือน : "))  #เงินเดือนสุทธิ #เงินภาษี #โบนัส
amount = int(input("ป้อนยอดขาย : "))   
tax_7_percent = salary * 0.07
bonus = amount * 0.1
salary_net = salary + bonus - tax_7_percent
print("รายรับสุทธิ : %0.2f" % salary_net, "บาท")
print("โบนัส : %0.2f" % bonus, "บาท")
print("เงินภาษี 7 เปอร์เซ็นต์ : %0.2f", "บาท")"""
"""###################################################################"""
"""amount_cargo = int(input("ป้อนจำนวนสินค้า : ")) #ราคาสินค้าทั้งหมด #ส่วนลด #ราคาสินค้าที่ต้องจ่าย 
cargo_price = int(input("ป้อนราคาสินค้า : "))
all_cargo_price = cargo_price * amount_cargo
discount_price = all_cargo_price * 0.05
end_cargo_price = all_cargo_price - discount_price
print("ราคาสินค้าทั้งหมด : %d" % all_cargo_price, "บาท")
print("ส่วนลดจากราคาสินค้า : %0.2f" % discount_price, "บาท")
print("ราคาสินค้าที่ต้องจ่ายทัังหมด : %0.2f" % end_cargo_price, "บาท")"""
"""##################################################################"""
"""salary = int(input("เงินเดือน : ")) #เงินเดือนสุทธิ #เงินค่าล่วงเวลา #เงินภาษี
over_hour = eval(input("จำนวนชั่วโมง : "))
money_per_hour = eval(input("อัตราค่าล่วงเวลา : "))
over_hour_money = money_per_hour * over_hour
tax_7_percent = salary * 0.07
salary_net = salary + over_hour_money - tax_7_percent
print("รายได้สุทธิ : %d" % salary_net, "บาท")
print("เงินค่าล่วงเวลา : %0.2f" % over_hour_money, "บาท")
print("เงินภาษี : %0.2f" % tax_7_percent, "บาท")"""
"""###################################################################"""
""""amount_book = int(input("ป้อนจำนวนหนังสือ : "))
price_borrow_book = int(input("ป้อนอัตราค่าเช่า : "))
discount_price = int(input("ป้อนส่วนลด : "))
borrow_book_day = eval(input("จำนวนเวลาการยืม : "))
all_price_book = (price_borrow_book * amount_book) * borrow_book_day
all_price_book = all_price_book - discount_price
print("อัตราค่าเช่าหนังสือทั้งหมด : %0.2f" % all_price_book)"""
"""####################################################################"""
"""length_dis = int(input("ป้อนระยะทาง : "))
use_oli = eval(input("ป้อนอัตราน้ำมัน : "))
length_dis = length_dis * 2
total_oli_use = length_dis / use_oli
print("ปริมาณการใช้นำมันทั้งหมด : %0.2f" % total_oli_use, "ลิตร")"""
"""###################################################################"""
"""price = int(input("ป้อนราคาสินค้า : "))
vat_7_percent = price * 0.07
price_after_vat = price - vat_7_percent
print("จำนวนเงินที่ต้องจ่าย : %d" % price_after_vat, "บาท")"""
"""###################################################################"""




