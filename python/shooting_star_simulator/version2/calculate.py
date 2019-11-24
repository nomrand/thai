# This line is needed to use mathematical function
# ↓ บรรทัดนี้จำเป็นต้องใช้ ฟังก์ชันทางคณิตศาสตร์
import math

# ตัวแปรส่วนกลาง (global variable)
# แต่ละพิกเซลมีจำนวนกี่เมตร? (1pixel = 100km)
METER_PER_PIXEL = 100*1000
# ค่าคงตัวโน้มถ่วงสากล (constant of gravitation)
G = 6.67E-11
# มวลของโลก (6 * (10 ยกกำลัง 24) kg)
EARTH_KILOGRAM = 6E24
# ตำแหน่งของโลก
EARTH_POSITION = (400/2 * METER_PER_PIXEL, 400/2 * METER_PER_PIXEL)

# มวล ของดาวเคราะห์น้อย (100kg)
STAR_KILOGRAM = 100E3
# Following 3 variables are set dummy data
# ↓ ตัวแปร 3 ตัวต่อไปนี้ถูกตั้งค่าข้อมูลเท็จ  (หากกดปุ่มระบบจะตั้งค่าจริง)
# ตำแหน่ง ของดาวเคราะห์น้อย
STAR_POSITION = (0, 0)  # แกน x, แกน y
# ความเร็ว ของดาวเคราะห์น้อย (m/s)
STAR_VELOCITY = (0, 0)  # แกน x, แกน y
# ความเร่ง ของดาวเคราะห์น้อย
STAR_ACCELERATION = (0, 0)  # แกน x, แกน y


# กำหนดค่าความเร็วเริ่มต้น
# สะท้อนค่าความเร็ว เริ่มต้น จากหน้าต่าง
def set_init(velocity_x, velocity_y):
    # ในฟังก์ชันนี้ ต้องการเปลี่ยน ตัวแปรส่วนกลาง (global variable)
    # ดังนั้นใช้คำสั่ง global ก่อน
    global STAR_ACCELERATION
    global STAR_VELOCITY
    global STAR_POSITION

    # ค่ามาจากหน้าต่างเป็นพิกเซล  ดังนั้นเปลี่ยนจากพิกเซล เป็นเมตร
    STAR_POSITION = (0, 400/2 * METER_PER_PIXEL)
    # ค่ามาจากหน้าต่างเป็น km/s  ดังนั้นเปลี่ยนจาก km/s เป็น m/s
    STAR_VELOCITY = (velocity_x * 1000, velocity_y * 1000)
    STAR_ACCELERATION = (0, 0)


def calc():
    # ในฟังก์ชันนี้ ต้องการเปลี่ยน ตัวแปรส่วนกลาง (global variable)
    # ดังนั้นใช้คำสั่ง global ก่อน
    global STAR_ACCELERATION
    global STAR_VELOCITY
    global STAR_POSITION

    # 1. Calculate distance between the earth and asteroid
    # คำนวณ ระยะทางระหว่างโลกกับดาวเคราะห์น้อย
    distance_x = EARTH_POSITION[0] - STAR_POSITION[0]
    distance_y = EARTH_POSITION[1] - STAR_POSITION[1]
    distance = math.sqrt(distance_x**2 + distance_y**2)

    # 2. Calculate "Force of Attraction"
    # คำนวณ แรงดึงดูดระหว่างมวล
    # F = G (m1 * m2)/ r**2
    force = G * (EARTH_KILOGRAM * STAR_KILOGRAM) / (distance ** 2)
    # แยกแรง แกน x และแกน y
    degree = math.atan2(distance_y, distance_x)
    force_x = force * math.cos(degree)
    force_y = force * math.sin(degree)

    # 3. Calculate Acceleration
    # คำนวณ ความเร่งที่ดาวเคราะห์น้อยได้รับ
    # F=ma -> a=F/m
    accel_x = force_x/STAR_KILOGRAM
    accel_y = force_y/STAR_KILOGRAM
    # เพิ่มลง ในความเร่งปัจจุบัน
    STAR_ACCELERATION = (STAR_ACCELERATION[0] + accel_x,
                         STAR_ACCELERATION[1] + accel_y)

    # 4. Calculate Velocity
    # เพิ่มความเร็ว ในการเปลี่ยนต่อวินาที เป็นค่าปัจจุบัน
    # acceleration * (1 second) = velocity change
    STAR_VELOCITY = (STAR_VELOCITY[0] + STAR_ACCELERATION[0]*1,
                     STAR_VELOCITY[1] + STAR_ACCELERATION[1]*1)

    # 5. Calculate Position of Asteroid
    # เพิ่มตำแหน่ง ในการเปลี่ยนต่อวินาที เป็นค่าปัจจุบัน
    # velocity * (1 second) = position change
    STAR_POSITION = (STAR_POSITION[0] + STAR_VELOCITY[0]*1,
                     STAR_POSITION[1] + STAR_VELOCITY[1]*1)

    # ค่าไปยังหน้าต่างเป็นพิกเซล  ดังนั้น เปลี่ยนจากเมตร เป็นพิกเซล
    screen_position = (int(STAR_POSITION[0] / METER_PER_PIXEL),
                       int(STAR_POSITION[1] / METER_PER_PIXEL))
    # ค่าไปยังหน้าต่างเป็น km/s  ดังนั้นเปลี่ยนจาก m/s เป็น km/s
    screen_velocity = (int(STAR_VELOCITY[0] / 1000),
                       int(STAR_VELOCITY[1] / 1000))
    result = (screen_position, screen_velocity)

    # ส่งค่ากลับ ตำแหน่งของดาวเคราะห์ & ความเร็ว
    return result
