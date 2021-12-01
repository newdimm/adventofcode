def check(i):
  last_digit = 10
  seen_double = False
  seen_double_ctr = 0
  
  while (i):
    new_i = i // 10
    digit = i - new_i * 10
    #print ("%d -> %d + %d (%d)" % (i, new_i, digit, last_digit))
    if digit > last_digit:
      return False
    if digit == last_digit:
      seen_double_ctr += 1
    else:
      if seen_double_ctr == 1:
        seen_double = True
      seen_double_ctr = 0
    last_digit = digit
    i = new_i
  
  return seen_double or seen_double_ctr == 1

with open("input") as f:
  params = f.readline().split("-")
  start = int(params[0])
  stop = int(params[1])
  counter = 0
  for i in range(start, stop):
    if (check(i)):
      counter += 1
  print("[%d:%d]: %d" % (start, stop, counter))
  