hour = int(input("ป้อนจำนวนชั่วโมงที่ยืม : "))
moto_rent = int(input("ป้อนจำนวนรถจักรยานยนต์ : "))
car_rent = int(input("ป้อนจำนวนรถยนต์ : "))
if moto_rent and car_rent <= 2:
    rate_per_moto = hour * moto_rent * 50
    rate_per_car = hour * car_rent * 100
    all_rate_rent = rate_per_moto + rate_per_car
    discount_moto = 0.05
    if rate_per_car <= 1000:
        discount_car = rate_per_car * 0.10
    else:
        discount_car = 0
    print("ค่าเช่ารถรวมทั้งหมด : ", all_rate_rent)
    print("ส่วนลดค่าเช่ารถจักรยานยนต์ : ", discount_moto)
    print("ส่วนลดค่าเช่ารถยนต์ : ", discount_car)
    print("ส่วนลดรวม : ", discount_moto + discount_car)
    print("เงินค่าเช่ารถยนต์ที่ต้องชำระ : ", rate_per_car - discount_car)
    print("เงินค่เช่ารถจักรยานยนต์ที่ต้องชำระ : ", rate_per_moto - discount_moto)
else:
    print("สามารถเช่ารถได้ไม่เกิน 2 คัน")
