DEBUG = False

def load_parameters(mem, pos, count):
  modes = mem[pos] // 100
  pos += 1
  params = []
  for i in range(0, count):
    new_modes = modes // 10
    mode = modes - new_modes * 10
    modes = new_modes
    param = mem[pos]
    if mode == 0:
      param = mem[param]
    params.append(param)
    pos += 1
  return params

def command_add(mem, pc):
  [a,b] = load_parameters(mem, pc, 2)
  c = mem[pc + 3]
  if DEBUG:
    print("ADD[%d] %d + %d = %d ==> %d + %d -> mem[%d]" %(
      mem[pc] // 100, mem[pc+1], mem[pc+2], mem[pc+3],a,b,c))
  mem[c] = a + b
  return pc + 4

def command_mult(mem, pc):
  [a,b] = load_parameters(mem, pc, 2)
  c = mem[pc + 3]
  mem[c] = a * b
  return pc + 4

def command_input(mem, pc):
  input_str = input("INPUT> ")
  mem[mem[pc + 1]] = int(input_str)
  return pc + 2

def command_output(mem, pc):
  [a] = load_parameters(mem, pc, 1)
  print("OUTPUT: %d" % a)
  return pc + 2

def command_halt(mem, pc):
  return len(mem)

def command_jump_if_true(mem, pc):
  [a, b] = load_parameters(mem, pc, 2)
  if a:
    new_pc = b
  else:
    new_pc = pc + 3

  if DEBUG:
    print("JUMP_IF_TRUE[%d] %d -> %d :: %d -> %d :: PC(%d) -> PC(%d)" % (
      mem[pc] // 100, mem[pc+1], mem[pc+2], a, b, pc, new_pc))

  return new_pc

def command_jump_if_false(mem, pc):
  [a, b] = load_parameters(mem, pc, 2)
  if not a:
    return b
  return pc + 3

def command_less_than(mem, pc):
  [a, b] = load_parameters(mem, pc, 2)
  if a < b:
    result = 1
  else:
    result = 0
  mem[mem[pc + 3]] = result
  return pc + 4

def command_equals(mem, pc):
  [a, b] = load_parameters(mem, pc, 2)
  if a == b:
    result = 1
  else:
    result = 0
    
  if DEBUG:
    print("EQUALS[%d] %d ? %d -> %d :: %d ? %d == %d -> %d" % (
      mem[pc] // 100, mem[pc+1], mem[pc+2], mem[pc+3], a,b, result, mem[pc+3]))
  mem[mem[pc + 3]] = result
  return pc + 4

opcodes = {
  1 : command_add,
  2 : command_mult,
  3 : command_input,
  4 : command_output,
  5 : command_jump_if_true,
  6 : command_jump_if_false,
  7 : command_less_than,
  8 : command_equals,
  99: command_halt
}

with open("input") as f:
  mem = [int(i) for i in f.readline().split(",")]
  pc = 0
  
  if DEBUG:
    for i in range(0, len(mem)):
      print("[%02d] = %d" % (i, mem[i]))
  
  while pc < len(mem):
    opcode = mem[pc] % 100
    command = opcodes[opcode]
    print("[%03d]OPCODE: %d - %s" % (pc, opcode, command.__name__));
    pc = command(mem, pc)
    
  