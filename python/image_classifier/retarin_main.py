# Requirements on Your Computer (ความต้องการ ในคอมพิวเตอร์ของคุณ)
# ต้องติดตั้งโมดูล "tensorflow (vesion 1.15)"
# ต้องติดตั้งโมดูล "tensorflow_hub"

# import calltf.py ใน โฟลเดอร์ tf
from tf import calltf


# ในโฟลเดอร์ "train_images"  ต้องมี บางโฟลเดอร์ย่อย
# ในโฟลเดอร์ย่อย  ต้องมี ไฟล์ภาพมากมาย (มาก 20 ไฟล์ขึ้นไป)
# ตัวอย่างเช่น
# โฟลเดอร์ "train_images"
#   |
#   --> โฟลเดอร์ "cat"  (ประเภทที่ 1)
#   |     |
#   |     --> cat1.jpg (ไฟล์ภาพแมว)
#   |     --> cat2.jpg (ไฟล์ภาพแมว)
#   |     |     :
#   |     --> cat20.jpg (ไฟล์ภาพแมว)
#   |
#   --> โฟลเดอร์ "dog"  (ประเภทที่ 2)
#   |     |
#   |     --> dog1.jpg (ไฟล์ภาพสุนัข)
#   |     --> dog2.jpg (ไฟล์ภาพสุนัข)
#   |     |     :
#   |     --> dog20.jpg (ไฟล์ภาพสุนัข)
#   |
#   --> โฟลเดอร์ "bird" (ประเภทที่ 3)
#         |
#         --> bird1.jpg (ไฟล์ภาพนก)
#         --> bird2.jpg (ไฟล์ภาพนก)
#         |     :
#         --> bird20.jpg (ไฟล์ภาพนก)

calltf.retain()
# after run this file,
# "calltf.predict" function will return YOUR OWN categories as above
# หลังจาก run ไฟล์นี้  ฟังก์ชั่น "calltf.predict" จะส่งคืนหมวดหมู่ของคุณเอง ดังกล่าว
