#!/usr/bin/python

DEBUG = True

class IntComp:
  def __init__(self, orig_mem,
               orig_in_dev = [],
               orig_out_dev = [],
               mem_size = 1024*1024):
    self.mem = [0xfe] * mem_size
    self.mem[0:len(orig_mem)] = orig_mem[:]
    self.in_dev = orig_in_dev
    self.out_dev = orig_out_dev
    
    self.opcodes = {
      1 : self.command_add,
      2 : self.command_mult,
      3 : self.command_input,
      4 : self.command_output,
      5 : self.command_jump_if_true,
      6 : self.command_jump_if_false,
      7 : self.command_less_than,
      8 : self.command_equals,
      9 : self.command_adjust_base,
      99: self.command_halt
    }
    
    self.base = 0
    self.pc = 0
    self._is_running = True
    
  def output(self):
    return str(self.out_dev)
    
  def is_running(self):
    return self._is_running

  def step(self):
    opcode = self.mem[self.pc] % 100
    command = self.opcodes[opcode]
    print("[%03d]OPCODE: %d - %s" % (self.pc, opcode, command.__name__));
    command()
  
  def load_parameters(self, spec):
    count = len(spec)
    mem = self.mem
    pos = self.pc
    
    modes = mem[pos] // 100
    pos += 1
    params = []
    for i in range(0, count):
      mode = modes % 10
      modes = modes // 10
      param = mem[pos]
      if spec[i] == 'i':
        ## input parameter - return value
        if mode == 0:
          # position mode
          param = mem[param]
        elif mode == 1:
          # immediate mode
          param = param
        elif mode == 2:
          # relative mode
          param = mem[self.base + param]
      else:
        ## output parameter - return index
        if mode == 0:
          # position mode
          param = param
        elif mode == 1:
          # immediate mode
          raise
        elif mode == 2:
          # relative mode
          param = self.base + param

      params.append(param)
      pos += 1
      
    return params

  def command_add(self):
    mem = self.mem
    pc = self.pc
    
    [a,b,c] = self.load_parameters("iio")
    if DEBUG:
      print("ADD[%d] %d + %d = %d ==> %d + %d -> mem[%d]" %(
        mem[pc] // 100,
        mem[pc + 1],
        mem[pc + 2],
        mem[pc + 3],
        a,b,c))
    mem[c] = a + b
    
    self.pc += 4

  def command_mult(self):
    mem = self.mem
    pc = self.pc
    
    [a,b,c] = self.load_parameters("iio")
    mem[c] = a * b
    
    self.pc += 4
    
  def command_input(self):
    mem = self.mem
    pc = self.pc
    
    [a] = self.load_parameters("o")
    
    input_data = self.in_dev.pop()
    print("INPUT: %d -> mem[%d] (%d)" % (input_data, a, mem[pc+1]))
    
    mem[a] = input_data
    self.pc += 2

  def command_output(self):
    [a] = self.load_parameters("i")
    print("OUTPUT: %d" % a)
    self.out_dev.append(a)

    self.pc += 2

  def command_halt(self):
    self._is_running = False
    self.pc += 1
 
  def command_jump_if_true(self):
    mem = self.mem
    pc = self.pc
    
    [a, b] = self.load_parameters("ii")
    if a:
      new_pc = b
    else:
      new_pc = pc + 3

    if DEBUG:
      print("JUMP_IF_TRUE[%d] %d -> %d :: %d -> %d :: PC(%d) -> PC(%d)" % (
        mem[pc] // 100, mem[pc+1], mem[pc+2], a, b, pc, new_pc))

    self.pc = new_pc

  def command_jump_if_false(self):
    mem = self.mem
    pc = self.pc
    
    [a, b] = self.load_parameters("ii")
    if not a:
      new_pc = b
    else:
      new_pc = pc + 3
      
    self.pc = new_pc

  def command_less_than(self):
    mem = self.mem
    pc = self.pc

    [a, b, c] = self.load_parameters("iio")
    if a < b:
      result = 1
    else:
      result = 0
      
    mem[c] = result
    
    self.pc += 4

  def command_equals(self):
    mem = self.mem
    pc = self.pc

    [a, b, c] = self.load_parameters("iio")
    if a == b:
      result = 1
    else:
      result = 0

    if DEBUG:
      print("EQUALS[%d] %d ? %d -> %d :: %d ? %d == %d -> %d" % (
        mem[pc] // 100, mem[pc+1], mem[pc+2], mem[pc+3], a,b, result, c))
    mem[c] = result
    
    self.pc += 4
    
  def command_adjust_base(self):
    [a] = self.load_parameters("i")
    self.base += a
    
    self.pc += 2

with open("input") as f:
  mem = [int(i) for i in f.readline().split(",")]
  
  if DEBUG:
    for i in range(0, len(mem)):
      print("[%02d] = %d" % (i, mem[i]))
  
  c = IntComp(mem, [2])
  while c.is_running():
    c.step()
  print("Result: ", c.output())
