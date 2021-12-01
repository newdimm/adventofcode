width = 25
height = 6
layer_size = width * height

with open("input") as f:
  for line in f:
    pos = 0
    min_number = layer_size + 1
    min_layer = -1
    number = 0
    while pos < len(line):
      if line[pos] == '0':
        number += 1
      if pos % layer_size == layer_size - 1:
        if number < min_number:
          min_number = number
          min_layer = pos - layer_size
        number = 0
      pos += 1
      
    ones = 0
    twos = 0
    for i in range(layer_size):
      if line[min_layer + i] == '1':
        ones += 1
      elif line[min_layer + i] == '2':
        twos += 1
    print("Layer %d zeros %d answer: %d * %d = %d" % (min_layer, min_number, ones, twos, ones * twos))
    
    image = [2] * layer_size
    for i in range(layer_size):
        pos = i
        while pos < len(line):
          if line[pos] != '2':
            image[i] = line[pos]
            break
          pos += layer_size
    for i in range(layer_size):
      if image[i] == '0':
        image[i] = ' '
      else:
        image[i] = '@'
    for r in range(height):
      print("".join(image[r * width : (r+1) * width]))
      
      
      
      
      
