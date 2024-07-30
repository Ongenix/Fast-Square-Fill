def square_fill(top_left_x, bottom_right_x, top_left_y, bottom_right_y, time):
  x = top_left_x + (time % (bottom_right_x - top_left_x + 1))
  y = top_left_y + (time // (bottom_right_y - top_left_y - 1))
  return x, y

top_left_x = 0
bottom_right_x = 10
top_left_y = 0
bottom_right_y = -10

area = abs((bottom_right_x - top_left_x) * (bottom_right_y - top_left_y))
for time in range(area):
  print(square_fill(top_left_x, bottom_right_x, top_left_y, bottom_right_y, time))
