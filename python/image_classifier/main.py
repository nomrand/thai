from tkinter import filedialog
from tkinter import font
from tkinter import *
from PIL import Image, ImageTk

# import calltf.py ใน โฟลเดอร์ tf
from tf import calltf

# requirements (ความต้องการ)
# ต้องติดตั้งโมดูล "tensorflow (vesion 1.15)"

# This is main part of program

# 2 บรรทัดเหล่านี้กำลังสร้างเค้าโครงหน้าต่าง GUI
# สิ่งเหล่านี้จำเป็นสำหรับโปรแกรม GUI
root = Tk(className='Image Classifier')
root.geometry("300x400")  # ความกว้าง=400 ความสูง=400


# ##########################
# ###  Create GUI Parts  ###
# ###  (สร้างส่วน GUI)     ###
# ##########################
# สร้าง label ด้วยภาพ
# ภาพจะถูกตั้งค่า หลังจากที่กดปุ่ม
image_label = Label(root)
image_label.place(x=0, y=50)
# สร้าง label สำหรับการแสดงผล
# ข้อความผลลัพธ์ถูกตั้งค่า หลังจากที่กดปุ่ม
text_label = Label(root)
text_label.place(x=0, y=350)
text_label["font"] = font.Font(size=20, slant='italic')


def check_image():
    # This line is needed to search image file, and get the path of the image
    # บรรทัดนี้จำเป็นสำหรับการค้นหาไฟล์รูปภาพและรับเส้นทางของรูปภาพ
    # สามารถเลือกได้เฉพาะไฟล์ "jpg" & "png"
    image_path = filedialog.askopenfilename(
        filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))

    # Show image on the Screen (This opereations are not related to AI, Image Classifier)
    # แสดงภาพบนหน้าต่าง (ตัวเลือกนี้ไม่เกี่ยวข้องกับ AI, Image Classifier (จัดหมวดหมู่ภาพ))
    image_object = Image.open(image_path)
    image_object.thumbnail((295, 295), Image.ANTIALIAS)
    image_object = ImageTk.PhotoImage(image=image_object)
    image_label.configure(image=image_object)
    image_label.image = image_object

    # เริ่มต้น Image Classifier (จัดหมวดหมู่ภาพ)
    result = calltf.predict(image_path)

    # result คือรายการที่มี 1,000 สมาชิก
    # result[0] คือหมวดหมู่ที่คล้ายกัน มากที่สุด
    # result[999] คือหมวดหมู่ที่คล้ายกัน น้อยที่สุด
    # result[0][0] คือชื่อหมวดหมู่, result[0][1] คือร้อยละ(0...1.0 -> 0%...100%)
    text_label["text"] = result[0][0] + \
        "(" + str(int(result[0][1] * 100)) + "%)"


# สร้าง Button
button = Button(root, text="Select Image", command=check_image)
button.place(x=0, y=0)
button["font"] = font.Font(size=15, weight="bold")

# นี่เป็นบรรทัดที่จำเป็นสำหรับโปรแกรม GUI
# (บรรทัดนี้ควรอยู่ที่ท้ายโปรแกรม GUI)
root.mainloop()
