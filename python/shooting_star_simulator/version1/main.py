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
root = Tk(className='shooting star simulator ver1')
root.geometry("400x400")  # ความกว้าง=400 ความสูง=400


# ##########################
# ###  Create GUI Parts  ###
# ###  (สร้างส่วน GUI)     ###
# ##########################
# สร้างดาว เป็น ★ label
label_shooting_star = Label(root, text="★")
# default positon is top-left
# ตำแหน่งเริ่มต้น เป็นด้านซ้ายบน
label_shooting_star.place(x=0, y=0)


# ########################################
# ###  The Core of Animation Structure ###
# ###  (โครงสร้างภาพเคลื่อนไหว)           ###
# ########################################
# This function repeats every 10 milliseconds
# ฟังก์ชันนี้จะทำซ้ำทุก ๆ 10 มิลลิวินาที
def move():
    # Move the star to right-down side (x-axis +3, y-axis +3)
    # เลื่อนดาวไปทางด้านขวาลง
    # winfo_x() และ winfo_y() คือตำแหน่งปัจจุบันของดาว
    position = (label_shooting_star.winfo_x() + 3,
                label_shooting_star.winfo_y() + 3)
    label_shooting_star.place(x=position[0], y=position[1])

    # Check if the star is out of screen
    # ตรวจสอบว่า ดาวอยู่นอกหน้าต่าง หรือไม่
    if position[0] > 400 or position[1] > 400:
        # If the star is out of screen, reset it to a random position
        # หากดาวอยู่นอกหน้าต่าง ให้รีเซ็ตดาวนั้นเป็นตำแหน่งสุ่ม
        random_y = random.randint(0, 200)
        label_shooting_star.place(x=0, y=random_y)

    # After 10 milliseconds, "move" function will be called again
    # หลังจาก 10 มิลลิวินาทีฟังก์ชัน "move" จะถูกเรียกอีกครั้ง
    root.after(10, move)


# Need to manually call the “move” function once to start the “after” loop
# ต้องเรียกใช้ฟังก์ชั่น "move" หนึ่งครั้ง เพื่อเริ่มต้นวนซ้ำ "after"
move()

# This is an also necessary line for GUI program.
# (This line must be placed at the end of GUI program)
# นี่เป็นบรรทัดที่จำเป็นสำหรับโปรแกรม GUI
# (บรรทัดนี้ควรอยู่ที่ท้ายโปรแกรม GUI)
root.mainloop()
