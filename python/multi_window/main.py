# This line is needed to use GUI
# ↓ บรรทัดนี้จำเป็นต้องใช้ GUI
from tkinter import *
# This line is needed to get random numbers
# ↓ บรรทัดนี้จำเป็นสำหรับการรับตัวเลขแบบสุ่ม
import random


# This is main part of program

# These 2 lines are making screen outline.
# These are necessary for GUI program.
# 2 บรรทัดเหล่านี้กำลังสร้างเค้าโครงหน้าต่าง GUI
# สิ่งเหล่านี้จำเป็นสำหรับโปรแกรม GUI
root = Tk(className='main')
root.geometry("240x240")

# Preparation
# การจัดเตรียม
label_main = Label(root, text="0")
label_main.pack()
click_count = 0


def change_main():
    global click_count
    click_count = click_count + 1
    label_main["text"] = click_count


# "root" (=made by "Tk" function) is a special window
# If the user closes "root" window, application will finish
# But closing a sub-window (=made by "Toplevel" function) just close the window
# application will keep continue to work

# "root" (= ทำโดยฟังก์ชั่น "Tk") เป็นหน้าต่างพิเศษ
# หากผู้ใช้ปิดหน้าต่าง "root"  แอปพลิเคชันจะเสร็จสิ้น
# แต่ ปิดหน้าต่างย่อย (= ทำโดยฟังก์ชั่น "Toplevel") เพียงปิดหน้าต่าง
# แอปพลิเคชั่นจะทำงานต่อไป

# สร้าง หน้าต่างย่อย โดยฟังก์ชั่น "Toplevel"
sub = Toplevel()
# ต้องให้ชื่อ โดยฟังก์ชั่น "title"
sub.title("sub")
# สามารถให้ขนาด เหมือนกับหน้าต่างหลัก
sub.geometry("300x100")

# สามารถสร้างชิ้นส่วน GUI เหมือนกับหน้าต่างหลัก
# แต่ระวัง อาร์กิวเมนต์ที่ 1 ของฟังก์ชั่น ไม่ใช่ "root"
button_sub = Button(sub, text="In Sub Window", command=change_main)
button_sub.pack()


# This is an also necessary line for GUI program.
# (This line must be placed at the end of GUI program)
# นี่เป็นบรรทัดที่จำเป็นสำหรับโปรแกรม GUI
# (บรรทัดนี้ควรอยู่ที่ท้ายโปรแกรม GUI)
root.mainloop()
