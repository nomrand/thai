# This line is needed to use GUI
from tkinter import *
# This line is needed to show messagebox
from tkinter import messagebox
# These 2 lines are needed to use image
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
# (หากจำนวน NG label เปลี่ยนเป็น 3 จาก 2 จะสามารถกำหนดเองได้ง่าย)
# (ลิสต์ สามารถปรับแต่งได้ง่าย ถ้าจำนวน NG label เปลี่ยนจาก 2 เป็น 3)
nglabel_list = []
# NG Label1
label1 = Label(root, image=image_box)
label1.place(x=50, y=100)  # ตำแหน่ง จากมุมซ้ายบน
nglabel_list.append(label1)  # ตั้งในลิสต์ ตำแหน่ง(index)=0
# NG Label2
label2 = Label(root, image=image_box)
label2.place(x=150, y=100)  # ตำแหน่ง จากมุมซ้ายบน
nglabel_list.append(label2)  # ตั้งในลิสต์ ตำแหน่ง(index)=1


# ##########################################
# ### 1-2. Create Plane label with image ###
# ###    (สร้าง Plane label พร้อมรูปภาพ)    ###
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


# ######################################
# ### 2. Keyboard Input Check ###
# ######################################
# keyboard input check function
def keyboard_input(event):
    # move plane
    input.key(event, label_plane)

    # Check (Game Lose? Game Win?)
    result = check.check_position(label_plane, nglabel_list)
    if (result < 0):
        # if Game Lose, result is -1
        messagebox.showinfo("info", "Game Lose... Don't Touch X")
        label_plane.place(x=240/2, y=240-50)

    if (result > 0):
        # if Game Win, result is 1
        messagebox.showinfo("info", "Game Win!")
        label_plane.place(x=240/2, y=240-50)


# If keyboard pressed, function "keyboard_input" called
root.bind("<Key>", keyboard_input)


# This is an also necessary line for GUI program.
# (This line must be placed at the end of GUI program)
# นี่เป็นบรรทัดที่จำเป็นสำหรับโปรแกรม GUI
# (บรรทัดนี้ควรอยู่ที่ท้ายโปรแกรม GUI)
root.mainloop()
