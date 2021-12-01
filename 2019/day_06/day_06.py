orbits = {}

with open("input") as f:
  for line in f:
    (parent,child) = line.strip().split(")")
    print("%s orbits %s" % (child,parent))
    orbits[child] = parent
    
  counter = 0
  for (child,parent) in orbits.items():
    counter += 1
    
    while parent:
      try:
        child = parent
        parent = orbits[child]
        counter += 1
      except:
        parent = ""
    
  print("Result:",counter)

  # part 2
  you_list = []
  parent = "YOU"
  while parent:
      try:
        child = parent
        parent = orbits[child]
        you_list.append(parent)
      except:
        parent = ""
  san_list = []
  parent = "SAN"
  while parent:
      try:
        child = parent
        parent = orbits[child]
        san_list.append(parent)
      except:
        parent = ""
  print ("YOU:", you_list)
  print ("SAN:", san_list)
  for planet in you_list:
    if planet in san_list:
      print("Part 2:", you_list.index(planet) + san_list.index(planet))
      break
      
  