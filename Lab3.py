''''money_per_hour = 100
hour_work_1 = int(input("ชั่วโมงการทำงานของพนักงานคนที่ 1 : "))
hour_work_2 = int(input("ชั่วโมงการทำงานของพนักงานคนที่ 2 : "))
hour_work_3 = int(input("ชั่วโมงการทำงานของพนักงานคนที่ 3 : "))
p1_per_hour = hour_work_1 * money_per_hour
p2_per_hour = hour_work_2 * money_per_hour
p3_per_hour = hour_work_3 * money_per_hour
all_money_pay = p1_per_hour + p2_per_hour + p3_per_hour
social_sec = all_money_pay * 0.015
last_money_pay = all_money_pay - social_sec
print("จำนวนที่ต้องจ่ายแก่พนักงานคนแรก 1 : ", p1_per_hour, "บาท")
print("จำนวนที่ต้องจ่ายแก่พนักงานคนแรก 2 : ", p2_per_hour, "บาท")
print("จำนวนที่ต้องจ่ายแก่พนักงานคนแรก 3 : ", p3_per_hour, "บาท")
print("จำนวนเงินค่าประกันสังคมทั้งหมด : ", social_sec, "บาท")
print("จำนวนเงินททั้งหมดที่บริษัทต้องจ่าย : ", last_money_pay, "บาท")'''
'''num = int(input("ป้อนตัวเลข : "))
if 100 <= num <= 500:
    print("You Value Between 100 - 500 ")'''
'''num = int(input("ป้อนตัวเลข : "))
if num < 100 or num > 500:
    print("Valid")'''
'''num = int(input("ป้อนตัวเลข : "))
if 50 <= num <= 100:
    print("Your Value Between 50 - 100")'''
'''num = int(input("ป้อนจำนวนแพคเกจ : "))
if num == 1:
    services_charge = 784 * num
    print(services_charge, "บาท")
if num == 2:
    services_charge_1 = 437 * num
    print(services_charge_1)
if num == 3:
    services_charge_2 = 437 * num
    print(services_charge_2)
if num == 4:
    service_charge_3 = 437 + 784 * num
    print(service_charge_3)'''
'''num = int(input("ติดตั้งแพคเกจจำนวน : "))
if num >= 1 and num <= 4:
    if num == 1:
        print(784*num)
    if num > 1:
        print(784+(437*(num - 1)))'''
'''quantity = int(input("ป้อนจำนวนสินค้า : "))
price = int(input("ป้อนราคาสินค้า : "))
type = int(input("ประเภทลูกค้า : "))
const = price * quantity
discount = 0
if type == 1:
    discount = const * 0.2
print("ราคาสินค้ารวม : ", const)
print("จำนวนเงินส่วนลด : ", discount)'''
'''total_book = int(input("ป้อนจำนวนหนังสือ : "))
borrow_day = int(input("ป้อนจำนวนวันยืม : "))
pay_money = total_book * (borrow_day * 5)
discount = 0
if pay_money > 50:
    discount = pay_money * 0.10
print("จำนวนเงินที่ต้องจ่ายก่อนหักส่วนลด : ", pay_money)
print("จำนวนเงินส่วนลด : ", discount )
print("จำนวนเงินที่ต้องจ่ายสุทธิ : ", pay_money - discount)'''
'''salary = int(input("ป้อนจำนวนเงินเดือน : "))
social_sec = 0
if salary > 10000:
    social_sec = salary * 0.02
print("จำนวนเงินเดือน : ", salary)
print("จำนวนเงินค่าประกันสังคม : ", social_sec)
print("จำนวนรายรับสุทธิ : ", salary - social_sec)'''
'''minute_car = int(input("ป้อนจำนวนนาที : "))
hour = minute_car // 60
if minute_car % 60 >= 1:
    hour = hour + 1
pay_money = hour * 20
print("จำนวนเงินที่ต้องจ่าย : ", pay_money)'''
'''county_num = int(input("ป้อนหมายเลขจังหวัด : "))
ticket_amount = int(input("ป้อนจำนวนตั๋ว : "))
ubon_pay_1 = 521
nong_khai_pay_2 = 494
khon_kaen_pay_3 = 365
discount = 0
if county_num == 1 and ticket_amount <=5:
   money_pay = ubon_pay_1 * ticket_amount
   print(money_pay)
if county_num == 2 and ticket_amount <=5:
   money_pay = nong_khai_pay_2 * ticket_amount
   print(money_pay)
if county_num == 3 and ticket_amount <=5:
   money_pay = khon_kaen_pay_3 * ticket_amount
   print(money_pay)'''
ubon=int(input('จำนวนตั๋วอุบลราชธานี :'))
nongkhai=int(input('จำนวนตั๋วหนองคาย :'))
khonkaen=int(input('จำนวนตั๋วขอนแก่น :'))
money_ubon=ubon*521
money_nongkhai=nongkhai*494
money_khonkaen=khonkaen*365
discount=0
all_ticket=ubon+nongkhai+khonkaen
pay=money_ubon+money_nongkhai+money_khonkaen
if all_ticket>5:
   discount=all_ticket*50
pay_discount=pay-discount
print('จำนวนเงินค่าโดยสารก่อนหักส่วนลด: ',pay)
print('ส่วนลด: ',discount)
print('เงินที่ต้องชำระสุทธิ์: ',pay_discount)



