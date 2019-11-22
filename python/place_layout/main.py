# This line is needed to use GUI
# ↓ บรรทัดนี้จำเป็นต้องใช้ GUI
from tkinter import *
# This line is needed to show messagebox
# ↓ บรรทัดนี้จำเป็นต้องแสดง messagebox
from tkinter import messagebox
# These 2 lines are needed to use image
# ↓ 2 บรรทัดนี้จำเป็นสำหรับการใช้รูปภาพ
import os
from PIL import Image, ImageTk

# import input.py & check.py
import input
import check


# This is main part of program

# These 2 lines are making screen outline.
# These are necessary for GUI program.
# 2 บรรทัดเหล่านี้กำลังสร้างเค้าโครงหน้าต่าง GUI
# สิ่งเหล่านี้จำเป็นสำหรับโปรแกรม GUI
root = Tk(className='place layout')
root.geometry("240x240")  # ความกว้าง=240 ความสูง=240


# #######################################
# ### 1-1. Create NG label with image ###
# ###    (สร้าง NG label พร้อมรูปภาพ)    ###
# #######################################
# ตั้งชื่อและตำแหน่งของภาพ (ไฟล์ box.png ในโฟลเดอร์ img)
path_box = os.path.join(os.path.dirname(__file__), 'img/box.png')
# ขนาดของภาพ (ความกว้าง=20 ความสูง=20)
image_box = Image.open(path_box).resize((20, 20), Image.ADAPTIVE)
image_box = ImageTk.PhotoImage(image=image_box)

# Create NG label by images and set into list
# (The list can be easily customized if the number of NG labels is changed from 2 to 3)
# สร้าง NG label ด้วยภาพ และตั้ง label ที่สร้างในลิสต์
# (ลิสต์ สามารถปรับแต่งได้ง่าย ถ้าจำนวน NG label เปลี่ยนจาก 2 เป็น 3)
nglabel_list = []
# NG Label ที่1
nglabel_1 = Label(root, image=image_box)
nglabel_1.place(x=50, y=100)  # ตำแหน่ง จากมุมซ้ายบน
nglabel_list.append(nglabel_1)  # ตั้งในลิสต์ ตำแหน่ง(index)=0
# NG Label ที่2
nglabel_2 = Label(root, image=image_box)
nglabel_2.place(x=150, y=100)  # ตำแหน่ง จากมุมซ้ายบน
nglabel_list.append(nglabel_2)  # ตั้งในลิสต์ ตำแหน่ง(index)=1


# ##########################################
# ### 1-2. Create Plane label with image ###
# ###    (สร้างเครื่องบิน label พร้อมรูปภาพ)    ###
# ##########################################
# ตั้งชื่อและตำแหน่งของภาพ (ไฟล์ airplane.png ในโฟลเดอร์ img)
path_plane = os.path.join(os.path.dirname(__file__), 'img/airplane.png')
# สร้าง ภาพ(image)
# ขนาดของภาพ (ความกว้าง=50 ความสูง=50)
image_plane = Image.open(path_plane).resize((50, 50), Image.ADAPTIVE)
image_plane = ImageTk.PhotoImage(image=image_plane)
# สร้าง label ด้วยภาพ
label_plane = Label(root, image=image_plane)
label_plane.place(x=240/2, y=240-50)


# ###################################
# ### 2. Keyboard Input Check     ###
# ###    (ตรวจสอบอินพุตของแป้นพิมพ์) ###
# ###################################
# keyboard input check function
# ฟังก์ชั่นที่ตรวจสอบ อินพุตของแป้นพิมพ์
def keyboard_input(event):
    # check & move plane
    # ตรวจสอบ และ ย้าย เครื่องบิน
    input.key(event, label_plane)

    # check Lose or Win
    # ตรวจสอบเกมแพ้หรือชนะ
    result = check.check_position(label_plane, nglabel_list)
    if (result < 0):
        # if you lose, result of "check.check_position" is -1
        # ถ้าคุณแพ้  ผลลัพธ์ของ ฟังก์ชัน "check.check_position" คือ -1
        messagebox.showinfo("info", "You Lose...")
        label_plane.place(x=240/2, y=240-50)

    if (result > 0):
        # if you win, result of "check.check_position" is 1
        # ถ้าคุณแพ้  ผลลัพธ์ของ ฟังก์ชัน "check.check_position" คือ 1
        messagebox.showinfo("info", "You Win!")
        label_plane.place(x=240/2, y=240-50)


# If keyboard pressed, function "keyboard_input" will be called
# หากแป้นพิมพ์ถูกกด  ฟังก์ชัน "keyboard_input" จะถูกเรียก
root.bind("<Key>", keyboard_input)


# This is an also necessary line for GUI program.
# (This line must be placed at the end of GUI program)
# นี่เป็นบรรทัดที่จำเป็นสำหรับโปรแกรม GUI
# (บรรทัดนี้ควรอยู่ที่ท้ายโปรแกรม GUI)
root.mainloop()
