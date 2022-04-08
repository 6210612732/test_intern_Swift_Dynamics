# test3.py

line_input = input("input array number : ")

array_str = line_input.split(" ")

max_value = int(array_str[0])
index_of_max = 0

for i in range(len(array_str)):
	if(max_value < int(array_str[i])):
		max_value = int(array_str[i])
		index_of_max = i 


print("index of max value is : " + str(index_of_max))

"""
	- รับอินพุตทั้งบรรทัดเป็นstring
	- ใช้ method split ให้เป็น list
	- ลูปไล่ค่าทุกตัวในlist โดยเก็บค่าindexค่ามากสุดและค่าmax
	  เพื่อเปรียบเทียบและอัปเดต
"""