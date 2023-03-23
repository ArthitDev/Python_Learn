"""point_1 = eval(input("ป้อนเกรดวิชาที่ 1 : "))
point_2 = eval(input("ป้อนเกรดวิชาที่ 2 : "))
point_3 = eval(input("ป้อนเกรดวิชาที่ 3 : "))
behavior_1 = eval(input("หน่วยกิตประจำวิชาที่ 1 : "))
behavior_2 = eval(input("หน่วยกิตประจำวิชาที่ 2 : "))
behavior_3 = eval(input("หน่วยกิตประจำวิชาที่ 3 : "))
grade_1 = point_1 * behavior_1
grade_2 = point_2 * behavior_2
grade_3 = point_3 * behavior_3
garde_all = grade_1 + grade_2 + grade_3
behavior_all = behavior_1 + behavior_2 + behavior_3
total_grade = garde_all / behavior_all
print("เกรดเฉลี่ยรวม คือ : %0.2f" % total_grade)"""

"""time_minute = eval(input("ป้อนนาที : "))
hour = time_minute / 60
if time_minute % 60 == 0:
    service_charge = int(hour) * 20
    print("ค่าบริการ : ", service_charge, "บาท")
if time_minute % 60 != 0:
    hour = int(hour) + 1
    service_charge = hour * 20
    print("ค่าบริการ : ", service_charge, "บาท",)"""

"""salary = int(input("ป้อนเงินเดือน : "))
if salary < 10000:
    social_sec = 0
    print("เงินเดือนสุทธิ : ", salary, "\n""เงินเดือน : ", salary, "\n""ค่าประกันสังคม : ", social_sec)
if salary >= 10000:
    social_sec = salary * 0.02
    total_salary = salary - social_sec
    print("เงินเดือนสุทธิ : ", total_salary, "\n""เงินเดือน : ", salary, "\n""ค่าประกันสังคม : ", social_sec)"""

"""cargo = int(input("ป้อนจำนวนสินค้า : "))
cargo_price = int(input("ป้อนราคาสินค้า : "))
all_cargo_price = cargo * cargo_price
if all_cargo_price >= 10000:
    discount = all_cargo_price * 0.1
    total_pay = all_cargo_price - discount
    print("ราคารวม : ", all_cargo_price, "\n""จำนวนเงินส่วนลด : ", discount, "\n""ราคาที่ต้องจ่าย : ", total_pay)
if all_cargo_price < 10000:
    discount = 0
    print("ราคารวม : ", all_cargo_price, "\n""จำนวนเงินส่วนลด : ", discount, "\n""ราคาที่ต้องจ่าย : ", all_cargo_price)"""

"""over_time = int(input("ป้อนชั่วโมงการทำงานล่วงเวลา : "))
if 1 <= over_time <= 5:
    over_time_money = over_time * 200
    print("เงินค่าล่วงเวลาที่ได้รับ : ", over_time_money, "บาท")
if 5 < over_time <= 24:
    over_time_money = 1000 + (over_time-5) * 100
    print("เงินค่าล่วงเวลาที่ได้รับ : ", over_time_money, "บาท")
if 1 < over_time > 24:
    print("กรุณาป้อนชั่วโมงให้ถูกต้อง เช่น 1 - 24 ชั่วโมง")"""
