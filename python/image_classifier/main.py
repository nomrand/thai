from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk

from tf import calltf

# requires
# * tensorflow==1.x
# * tensorflow_hub

# This is main part of program

# 2 บรรทัดเหล่านี้กำลังสร้างเค้าโครงหน้าต่าง GUI
# สิ่งเหล่านี้จำเป็นสำหรับโปรแกรม GUI
root = Tk(className='Image Classifier')
root.geometry("300x400")  # ความกว้าง=400 ความสูง=400


# สร้าง label ด้วยภาพ
image_label = Label(root)
image_label.place(x=0, y=50)
text_label = Label(root)
text_label.place(x=0, y=350)


def check_image():
    image_path = filedialog.askopenfilename(filetypes=(
        ("jpeg files", "*.jpg"), ("png files", "*.png")))

    image_object = Image.open(image_path)
    image_object.thumbnail((295, 295), Image.ANTIALIAS)
    image_object = ImageTk.PhotoImage(image=image_object)
    image_label.configure(image=image_object)
    image_label.image = image_object

    result = calltf.predict(image_path)
    result_text = '{} ({:.1f}%)'.format(result[0][0], result[0][1] * 100)

    text_label["text"] = result_text

    print('----- result -----')
    for r in result[:5]:
        print(r[0], r[1])


button = Button(root, text="Select Image", command=check_image)
button.place(x=0, y=0)

# นี่เป็นบรรทัดที่จำเป็นสำหรับโปรแกรม GUI
# (บรรทัดนี้ควรอยู่ที่ท้ายโปรแกรม GUI)
root.mainloop()
