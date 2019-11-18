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


# Create NG label (3 labels)
label_50 = Label(root, text='X')
label_50.place(x=50, y=100)  # ตำแหน่ง จากมุมซ้ายบน

label_100 = Label(root, text='X')
label_100.place(x=100, y=100)  # ตำแหน่ง จากมุมซ้ายบน

label_200 = Label(root, text='X')
label_200.place(x=200, y=100)  # ตำแหน่ง จากมุมซ้ายบน


# Create Player label with image
# สร้าง Player label พร้อมรูปภาพ
# ตั้งชื่อและตำแหน่งของภาพ (ไฟล์ airplane.png ในโฟลเดอร์ img)
image_path = os.path.join(os.path.dirname(__file__), 'img/airplane.png')
# ขนาดของภาพ (ความกว้าง=50 ความสูง=50)
image_object = Image.open(image_path).resize((50, 50), Image.ADAPTIVE)
image_object = ImageTk.PhotoImage(image=image_object)
# สร้าง label ด้วยภาพ
label_player = Label(root, image=image_object)
label_player.place(x=240/2-50/2, y=240-50)


# get keyboard input
def keyboard_input(event):
    # move player
    input.key(event, label_player)

    # Check
    result = check.check_position(label_player, label_50, label_100, label_200)
    if (result < 0):
        messagebox.showinfo("INFORMATION", "Don't Touch X!")
        label_player.place(x=240/2-50/2, y=240-50)

    if (result > 0):
        messagebox.showinfo("INFORMATION", "Game Clear!")
        label_player.place(x=240/2-50/2, y=240-50)


root.bind("<Key>", keyboard_input)

# This is an also necessary line for GUI program.
# (This line must be placed at the end of GUI program)
# นี่เป็นบรรทัดที่จำเป็นสำหรับโปรแกรม GUI
# (บรรทัดนี้ควรอยู่ที่ท้ายโปรแกรม GUI)
root.mainloop()
