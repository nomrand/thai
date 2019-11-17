from tkinter import *
import textset


# This is main part of program

# These 2 lines are making screen outline.
# These are necessary for GUI program.
# 2 บรรทัดเหล่านี้กำลังสร้างเค้าโครงหน้าต่าง GUI
# สิ่งเหล่านี้จำเป็นสำหรับโปรแกรม GUI
root = Tk(className='Fruit Info')
root.geometry("240x240")  # ความกว้าง=240 ความสูง=240

# From now, making inside elements of screen.
# 1st line in screen = Input elements for "Fruit Name"
# จากนี้ไปสร้างชิ้นส่วน ภายในของหน้าต่าง
# บรรทัดที่ 1 ในหน้าต่าง = ชิ้นส่วนอินพุต สำหรับ"ชื่อผลไม้"
label0 = Label(root, text='Fruit Name:')
label0.grid(row=0, column=0)
entry0 = Entry(root)  # Entry คือชิ้นส่วนอินพุต
entry0.grid(row=0, column=1)

# 2nd line in screen = Output elements for "Fruit Color"
# บรรทัดที่ 2 ในหน้าต่าง = ชิ้นส่วนเอาท์พุต สำหรับ"สีผลไม้"
label1_0 = Label(root, text='Color:')
label1_0.grid(row=1, column=0)
label1_1 = Label(root, text='')
label1_1.grid(row=1, column=1)

# 3rd line = Output elements for Fruit Price
# บรรทัดที่ 3 ในหน้าต่าง = ชิ้นส่วนเอาท์พุต สำหรับ"ราคาผลไม้"
label2_0 = Label(root, text='Price:')
label2_0.grid(row=2, column=0)
label2_1 = Label(root, text='')
label2_1.grid(row=2, column=1)
label2_2 = Label(root, text='Baht')
label2_2.grid(row=2, column=2)


# Make a function which will work when button pressed
def when_button_pressed():
    textset.set_text(entry0, label1_1, label2_1)


# At last, add button next to input element at 1st line
# (If "button0" is pushed, "set_text" function in "textset" module will be called)
# ในที่สุดเพิ่มปุ่มถัด ชิ้นส่วนอินพุต ที่บรรทัดที่ 1
# หากกด "button0" ระบบจะเรียกใช้ ฟังก์ชัน"when_button_pressed",
# ในฟังก์ชัน"when_button_pressed", เรียกใช้ ฟังก์ชัน"set_text" ในโมดูล"textset"
button0 = Button(root, text='SET', command=when_button_pressed)
button0.grid(row=0, column=2)

# This is an also necessary line for GUI program.
# (This line must be placed at the end of GUI program)
# นี่เป็นบรรทัดที่จำเป็นสำหรับโปรแกรม GUI
# (บรรทัดนี้ควรอยู่ที่ท้ายโปรแกรม GUI)
root.mainloop()
