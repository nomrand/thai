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
root = Tk(className='shooting star simulator')
root.geometry("400x400")  # ความกว้าง=400 ความสูง=400


# ##########################
# ###  Create GUI Parts  ###
# ##########################
# สร้าง label
label_earth = Label(root, text="●")
label_earth.place(x=400/2, y=400/2)

label_shooting_star = Label(root, text="★")
label_shooting_star.place(x=0, y=400/2)

label_x = Label(root, text="velocity X:")
label_x.place(x=0, y=0)
velocity_x = Entry(root)
velocity_x.place(x=60, y=0)
unit_x = Label(root, text="km/s")
unit_x.place(x=160, y=0)

label_y = Label(root, text="velocity Y:")
label_y.place(x=0, y=25)
velocity_y = Entry(root)
velocity_y.place(x=60, y=25)
unit_7 = Label(root, text="km/s")
unit_7.place(x=160, y=25)


def set_velocity(v_x, v_y):
    velocity_x.delete(0, END)
    velocity_x.insert(0, v_x)
    velocity_y.delete(0, END)
    velocity_y.insert(0, v_y)


def loop_start():
    position = (label_shooting_star.winfo_x(), label_shooting_star.winfo_y())
    velocity = (float(velocity_x.get()), float(velocity_y.get()))

    calculate.init(position, velocity)
    move()


def move():
    result = calculate.calc()
    position = result[0]
    velocity = result[1]
    label_shooting_star.place(x=position[0], y=position[1])

    set_velocity(velocity[0], velocity[1])

    if(position[0] < 400 and position[1] < 400 and position[0] >= 0 and position[1] >= 0):
        root.after(10, move)
    else:
        label_shooting_star.place(x=0, y=400/2)
        set_velocity(10, 15)


start_button = Button(root, text="START", command=loop_start)
start_button.place(x=0, y=50)


set_velocity(10, 15)


# This is an also necessary line for GUI program.
# (This line must be placed at the end of GUI program)
# นี่เป็นบรรทัดที่จำเป็นสำหรับโปรแกรม GUI
# (บรรทัดนี้ควรอยู่ที่ท้ายโปรแกรม GUI)
root.mainloop()
