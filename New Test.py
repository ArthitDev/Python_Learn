hour = int(input("ป้อนจำนวนชั่วโมงที่ยืม : "))
moto_rent = int(input("ป้อนจำนวนรถจักรยานยนต์ : "))
car_rent = int(input("ป้อนจำนวนรถยนต์ : "))
rate_per_moto = hour * moto_rent * 50
rate_per_car = hour * car_rent * 100
if moto_rent and car_rent <= 2:
    discount = 0.05

