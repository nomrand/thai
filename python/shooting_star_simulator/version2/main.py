# This line is needed to use GUI
# ↓ บรรทัดนี้จำเป็นต้องใช้ GUI
from tkinter import *

# import calculate.py
import calculate


# This is main part of program

# These 2 lines are making screen outline.
# These are necessary for GUI program.
# 2 บรรทัดเหล่านี้กำลังสร้างเค้าโครงหน้าต่าง GUI
# สิ่งเหล่านี้จำเป็นสำหรับโปรแกรม GUI
root = Tk(className='shooting star simulator ver2')
root.geometry("400x400")  # ความกว้าง=400 ความสูง=400


# ##########################
# ###  Create GUI Parts  ###
# ###  (สร้างส่วน GUI)     ###
# ##########################
# สร้างโลก เป็น ● Label
label_earth = Label(root, text="●")
label_earth.place(x=400/2, y=400/2)  # ศูนย์กลางของหน้าต่าง

# สร้างดาวเคราะห์น้อย เป็น ★ Label
label_star = Label(root, text="★")
# default positon is left edge, middle height
# ตำแหน่งเริ่มต้น เป็น ซ้ายสุด, ความสูงระดับกลาง
label_star.place(x=0, y=400/2)

# สร้างความเร็ว
# x-axis (แกน x)
label_x = Label(root, text="velocity X:")
label_x.place(x=0, y=0)
velocity_x = Entry(root)
velocity_x.place(x=60, y=0)
unit_x = Label(root, text="km/s")
unit_x.place(x=160, y=0)
# y-axis (แกน y)
label_y = Label(root, text="velocity Y:")
label_y.place(x=0, y=25)
velocity_y = Entry(root)
velocity_y.place(x=60, y=25)
unit_7 = Label(root, text="km/s")
unit_7.place(x=160, y=25)


# Show velocity in GUI window (="Entry"s above)
# แสดงความเร็ว ในหน้าต่าง
# (Because this action is often done in many places, make it a function)
# (เนื่องจากการกระทำนี้มักจะทำ ในหลาย ๆ ที่  ทำให้เป็นฟังก์ชัน)
def show_velocity(v_x, v_y):
    # clear the contents of Entry (ล้างเนื้อหาของ Entry)
    velocity_x.delete(0, END)
    velocity_y.delete(0, END)
    # set the value into Entry (ตั้งค่าไปยัง Entry)
    velocity_x.insert(0, v_x)
    velocity_y.insert(0, v_y)


# ########################################
# ###  The Core of Animation Structure ###
# ###  (โครงสร้างภาพเคลื่อนไหว)           ###
# ########################################
# "move" function will be called again & again,
# but this function is called only once by each pressing
# ฟังก์ชั่น "move" จะถูกเรียกหลายครั้ง
# แต่ ฟังก์ชั่นนี้เรียกว่าเพียงครั้งเดียว โดยการกดแต่ละครั้ง
def loop_start():
    # "get()" คือเนื้อหาของ Entry  แต่ค่านั้นเป็น สายอักษร (String)
    # ดังนั้นเราต้องเปลี่ยนมันเป็น ตัวเลขทศนิยม หรือจำนวนจริง (Floating-Point numbers)
    # โดยใช้ฟังก์ชั่น float
    v_float_x = float(velocity_x.get())
    v_float_y = float(velocity_y.get())

    # Initialization process
    # กระบวนการเริ่มต้น
    calculate.set_init(v_float_x, v_float_y)

    # Start Loop
    # เริ่มวนซ้ำ
    move()


# This function repeats every 10 milliseconds
# ฟังก์ชันนี้จะทำซ้ำทุก ๆ 10 มิลลิวินาที
def move():
    # Move the asteroid according to the calculation result
    # Result will be a 2 dimensional tuple (2 inner-tuples in 1 outer-tuple)
    # ย้ายดาวเคราะห์น้อย ตามผลการคำนวณ
    # ผลลัพธ์จะเป็น 2 มิติ ทัพเพิล (2 ทัพเพิลภายใน ใน 1 ทัพเพิลด้านนอก)
    result = calculate.calc()
    # result คือ 1 ทัพเพิลด้านนอก
    # ใน result มี 2 ทัพเพิลภายใน (ตำแหน่งของดาวเคราะห์ & ความเร็ว)
    position = result[0]
    velocity = result[1]
    label_star.place(x=position[0], y=position[1])

    # Show the velocity
    # แสดงความเร็ว
    show_velocity(velocity[0], velocity[1])

    # ตรวจสอบว่า ดาวเคราะห์น้อยอยู่นอกหน้าต่าง หรือไม่
    if(position[0] < 400 and position[1] < 400 and position[0] >= 0 and position[1] >= 0):
        # NO = call “move” again (ดาวเคราะห์น้อยอยู่ในหน้าต่าง = เรียก "move" อีกครั้ง)
        root.after(10, move)
    else:
        # YES = Stop Loop (ดาวเคราะห์น้อยอยู่นอกหน้าต่าง = หยุดวนซ้ำ)
        # หากเราไม่เรียกใช้ฟังก์ชัน "move"  วนซ้ำจะหยุดโดยอัตโนมัติ

        # กลับ ดาวเคราะห์น้อย และ ความเร็ว Entry สู่สถานะดั้งเดิม
        label_star.place(x=0, y=400/2)
        show_velocity(10, 15)


# สร้างปุ่ม START
start_button = Button(root, text="START", command=loop_start)
start_button.place(x=0, y=50)


# กำหนดค่าความเร็วเริ่มต้น
show_velocity(10, 15)


# This is an also necessary line for GUI program.
# (This line must be placed at the end of GUI program)
# นี่เป็นบรรทัดที่จำเป็นสำหรับโปรแกรม GUI
# (บรรทัดนี้ควรอยู่ที่ท้ายโปรแกรม GUI)
root.mainloop()
