from time import time_ns

def square_fill(top_left_x, bottom_right_x, top_left_y, bottom_right_y, time):
  x = top_left_x + (time % (bottom_right_x - top_left_x + 1))
  y = top_left_y + (time // (bottom_right_y - top_left_y - 1))
  return x, y

def slow_square_fill(top_left_x, bottom_right_x, top_left_y, bottom_right_y):
  out = []
  for y in range(top_left_y, bottom_right_y + 1):
    for x in range(top_left_x, bottom_right_x + 1):
        out.append((x, y))
  return out

def test_square_fill(top_left_x, bottom_right_x, top_left_y, bottom_right_y):
  area = abs((bottom_right_x - top_left_x) * (bottom_right_y - top_left_y))
  
  out = []
  for time in range(area):
    out.append((square_fill(top_left_x, bottom_right_x, top_left_y, bottom_right_y, time)))
  return out

def main():
  top_left_x = 0
  bottom_right_x = 10
  top_left_y = 0
  bottom_right_y = -10
  
  first_start = time_ns()
  first = test_square_fill(top_left_x, bottom_right_x, top_left_y, bottom_right_y)
  first_end = time_ns()

  second_start = time_ns()
  second = slow_square_fill(top_left_x, bottom_right_x, top_left_y, bottom_right_y)
  second_end = time_ns()

  return (first_end - first_start), (second_end - second_start)

first_times = []
second_times = []
for _ in range(10000):
  first, second = main()
  first_times.append(first)
  second_times.append(second)

print(sum(first_times) / len(first_times))
print(sum(second_times) / len(second_times))
print((sum(first_times) / len(first_times)) / (sum(second_times) / len(second_times)))
