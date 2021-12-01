def check(i):
  last_digit = 10
  seen_double = False
  while (i):
    new_i = i // 10
    digit = i - new_i * 10
    #print ("%d -> %d + %d (%d)" % (i, new_i, digit, last_digit))
    if digit > last_digit:
      return False
    if digit == last_digit:
      seen_double = True   
    last_digit = digit
    i = new_i
  
  return seen_double

with open("input") as f:
  params = f.readline().split("-")
  start = int(params[0])
  stop = int(params[1])
  counter = 0
  for i in range(start, stop):
    if (check(i)):
      counter += 1
  print("[%d:%d]: %d" % (start, stop, counter))
  