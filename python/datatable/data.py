# This is Fruit Data
# นี่คือข้อมูลผลไม้
data = [
    # 0,            1,          2
    # name,         color,      price
    # ชื่อ,            สี,          ราคา
    ['banana',      'yellow',   10],
    ['apple',       'red',      20],
    ['coconut ',    'white',    30],
    ['watermelon ', 'green',    40],
]


# This is a function to search for a Fruit by name
# argument1 = name = fruit name
# นี่คือฟังก์ชั่นในการค้นหาผลไม้ตามชื่อ
# อาร์กิวเมนต์ 1  = name = ชื่อผลไม้
def search(name):
    # Loop through all data
    # วนซ้ำข้อมูลทั้งหมด
    for fruit in data:
        if fruit[0] == name:
            # if fruit name is found
            # หากพบชื่อผลไม้
            return fruit
    return None
