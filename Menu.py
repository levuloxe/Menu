print(" ~~~~~~~~~~~~~~~~~~~~~~~ ")
print("|    อาหารอีสานแซ่บนัว    |")
print("|    ระบบสั่งอาหารออนไลน์    |")
print(" ~~~~~~~~~~~~~~~~~~~~~~~ ")
print("")
print("ยินดีต้อนรับสู่ร้านอาหารอีสานแซบนัวครับ✪ ω ✪")
print("พิมพ์ X เพื่อออกจากระบบ")

code = input("พิมพ์โค้ดอาหารที่ต้องการใส่ลงมาได้เลยครับ")

file = open("food-menu.txt","r")

totalCost = 0
while(code!="X"):
  for line in file:
    data = line.split(";")
    itemCode = data[0]
    itemDescription = data[1]
    itemPrice = float(data[2])
    if itemCode == code:
      print(itemCode + " - " + itemDescription + " - ฿ " + str(itemPrice))
      totalCost = totalCost + itemPrice
  code = input("สั่งอาหารเพิ่มหรือพิมพ์ X เพื่อเสร็จสิ้นการสั่งซื้อ")

print("ยอดราคาอาหารรวมทั้งสิ้นราคา: ฿" + str(totalCost))
print("ขอบคุณที่ใช้บริการครับ !o(^▽^)o!")
file.close() 
