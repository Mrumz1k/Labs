def is_point_in_circle(x, y, r):
    distance_squared = x**2 + y**2
    return distance_squared <= r**2

x, y = 3, 4
r = 5
if is_point_in_circle(x, y, r):
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")