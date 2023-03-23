print("เป็นสมาชิก VIP = 1 , เป็นสมาชิก = 2 , ไม่เป็นเป็นสมาชิก = 3 ")
member_type = int(input("ป้อนประเภทลูกค้า : "))
amount_product = int(input("ป้อนจำนวนสินค้า : "))
price_per_amount = int(input("ป้อนราคาสินค้าต่อชิ้น : "))
all_price = amount_product * price_per_amount
if member_type == 1:
    discount = all_price * 0.10
elif member_type == 2 and all_price <= 500:
    discount = all_price * 0.02
elif member_type == 2 and all_price <= 1500:
    discount = all_price * 0.05
elif member_type == 2 and all_price > 1500:
    discount = all_price * 0.10
elif member_type == 3 and all_price > 1500:
    discount = all_price * 0.05
else:
    discount = 0
pay_discount = all_price - discount
vat = pay_discount * 0.07
net = pay_discount + vat
print("ราคาสินค้า : ", all_price)
print("เงินส่วนลด : ", discount)
print("ราคาหลังหักส่วนลด : ", pay_discount)
print("เงินภาษีมูลค่าเพิ่ม : %0.2f " % vat)
print("เงินที่ต้องชำระ : ", net)




