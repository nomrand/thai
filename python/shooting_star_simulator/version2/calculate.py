import math

meter_per_pixel = 100*1000
earth_kilogram = 6E24
earth_position = (400/2 * meter_per_pixel, 400/2 * meter_per_pixel)
#  constant of gravitation
G = 6.67E-11

star_kilogram = 100E3
star_position = (0, 0)
star_velocity = (0, 0)
star_accelation = (0, 0)


def init(position, velocity):
    global star_accelation
    global star_velocity
    global star_position
    star_position = (position[0] * meter_per_pixel,
                     position[1] * meter_per_pixel)
    star_velocity = (velocity[0] * 1000, velocity[1] * 1000)
    star_accelation = (0, 0)


def calc():
    global star_accelation
    global star_velocity
    global star_position

    distance_x = earth_position[0] - star_position[0]
    distance_y = earth_position[1] - star_position[1]

    distance = math.sqrt(distance_x**2 + distance_y**2)

    # F = G (m1 * m2)/ r**2
    force = G * (earth_kilogram * star_kilogram) / (distance ** 2)

    degree = math.atan2(distance_y, distance_x)
    force_x = force * math.cos(degree)
    force_y = force * math.sin(degree)

    # F=ma -> a=F/m
    accel_x = force_x/star_kilogram
    accel_y = force_y/star_kilogram

    star_accelation = (star_accelation[0] + accel_x,
                       star_accelation[1] + accel_y)

    star_velocity = (star_velocity[0] + star_accelation[0]*1,
                     star_velocity[1] + star_accelation[1]*1)

    star_position = (star_position[0] + star_velocity[0]*1,
                     star_position[1] + star_velocity[1]*1)

    screen_position = (int(star_position[0] / meter_per_pixel),
                       int(star_position[1] / meter_per_pixel))

    screen_velocity = (int(star_velocity[0] / 1000),
                       int(star_velocity[1] / 1000))

    result = (screen_position, screen_velocity)
    return result
