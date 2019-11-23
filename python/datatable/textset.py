import data


# This is a function to show information in screen
# argument(name_edit)    = where input "Fruit Name"
# argument(fruit_label1) = where show "Fruit Color"
# argument(fruit_label2) = where show "Fruit Price"
# นี่คือฟังก์ชั่นเพื่อแสดงข้อมูลในหน้าต่าง GUI
# อาร์กิวเมนต์(name_edit)    = ชิ้นส่วนอินพุต สำหรับ"ชื่อผลไม้"
# อาร์กิวเมนต์(fruit_label1) = ชิ้นส่วนเอาท์พุต สำหรับ"สีผลไม้"
# อาร์กิวเมนต์(fruit_label2) = ชิ้นส่วนเอาท์พุต สำหรับ"ราคาผลไม้"
def set_text(name_edit, fruit_label1, fruit_label2):
    # get "Fruit Name" from screen by "get" function
    # รับ "ชื่อผลไม้" จากหน้าต่าง โดยฟังก์ชั่น "get"
    fruit_name = name_edit.get()

    # search the fruit information by using "Fruit Name"
    # ค้นหาข้อมูลผลไม้โดยใช้ "ชื่อผลไม้"
    fruit = data.search(fruit_name)
    if fruit is None:
        # if couldn't find fruit information (when "data.search" return None),
        # show empty in screen
        # หากไม่พบข้อมูลผลไม้ (เมื่อ "data.search" ส่งคืน None),
        # แสดงที่ว่างในหน้าต่าง
        fruit_label1['text'] = ''
        fruit_label2['text'] = ''
    else:
        # if found fruit information,
        # show "Color(=fruit[1])" & "Price(=fruit[2])"
        # หากพบข้อมูลผลไม้
        # แสดง "สี (=fruit[1])" & "ราคา (=fruit[2])"
        fruit_label1['text'] = fruit[1]
        fruit_label2['text'] = fruit[2]
