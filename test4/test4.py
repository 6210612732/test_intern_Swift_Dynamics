# test4.py
def re_factorial(num):
	if(num == 1):
		return 1;
	else:
		return num * re_factorial(num-1)

def count_zero(num2):
	temp_count = 0
	while(1):
		if(num2 % 10 == 0):
			num2 /= 10
			temp_count+=1
		else:
			return temp_count 

number_n = int(input("input n for factorial : "))

sum_fact = re_factorial(number_n)
sum_zero = count_zero(sum_fact)

print(str(number_n) + "! = " + str(sum_fact) + " have zero behind = " + str(sum_zero))


"""
	- รับค่า n จากผู้ใช้ 
	- หาค่า factorial โดยใช้ recursive function  ชื่อre_factorial()
	- นำผลลัพธ์จาก factorial เข้าฟังก์ชั่่น count_zero() เพื่อนับ 0
	- count_zero ใช้วิธีลูป %10 /10 จนถึงหลักที่ %10ไม่ลงตัว 
"""