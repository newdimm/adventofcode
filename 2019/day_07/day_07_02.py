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

def command_add(mem, pc, dev_input, dev_output):
  [a,b] = load_parameters(mem, pc, 2)
  c = mem[pc + 3]
  if DEBUG:
    print("ADD[%d] %d + %d = %d ==> %d + %d -> mem[%d]" %(
      mem[pc] // 100, mem[pc+1], mem[pc+2], mem[pc+3],a,b,c))
  mem[c] = a + b
  return pc + 4

def command_mult(mem, pc, dev_input, dev_output):
  [a,b] = load_parameters(mem, pc, 2)
  c = mem[pc + 3]
  mem[c] = a * b
  return pc + 4

class IO_Dev_Interrupt(BaseException):
  pass

def command_input(mem, pc, dev_input, dev_output):
  if not dev_input:
    raise IO_Dev_Interrupt
  input_data = dev_input.pop()
  print("INPUT: %d" % input_data)
  mem[mem[pc + 1]] = input_data
  return pc + 2

def command_output(mem, pc, dev_input, dev_output):
  [a] = load_parameters(mem, pc, 1)
  print("OUTPUT: %d" % a)
  dev_output.insert(0, a)
  return pc + 2

def command_halt(mem, pc, dev_input, dev_output):
  return len(mem)

def command_jump_if_true(mem, pc, dev_input, dev_output):
  [a, b] = load_parameters(mem, pc, 2)
  if a:
    new_pc = b
  else:
    new_pc = pc + 3

  if DEBUG:
    print("JUMP_IF_TRUE[%d] %d -> %d :: %d -> %d :: PC(%d) -> PC(%d)" % (
      mem[pc] // 100, mem[pc+1], mem[pc+2], a, b, pc, new_pc))

  return new_pc

def command_jump_if_false(mem, pc, dev_input, dev_output):
  [a, b] = load_parameters(mem, pc, 2)
  if not a:
    return b
  return pc + 3

def command_less_than(mem, pc, dev_input, dev_output):
  [a, b] = load_parameters(mem, pc, 2)
  if a < b:
    result = 1
  else:
    result = 0
  mem[mem[pc + 3]] = result
  return pc + 4

def command_equals(mem, pc, dev_input, dev_output):
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

def phases_increment(phases):
  for i in range(len(phases)):
    if phases[i] == 4:
      phases[i] = 0
    else:
      phases[i] += 1
      return phases
  return []

def phases_ok(phases):
  for i in range(len(phases)):
    for g in range(i+1, len(phases)):
      #print ("p[%d](%d) ?= p[%d](%d)" % (i,phases[i], g,phases[g]))
      if phases[i] == phases[g]:
        return False
  return True
  
def get_next_phases(phases):
  phases = phases_increment(phases)
  
  while phases and not phases_ok(phases):
    phases = phases_increment(phases)
    
  return phases

def phases_iterate(phases):
  counter = 0
  phases = get_next_phases(phases)
  while phases:
    counter += 1
    print (counter, phases)
    phases = get_next_phases(phases)
  
with open("input") as f:
  orig_mem = [int(i) for i in f.readline().split(",")]
  
  if DEBUG:
    for i in range(0, len(mem)):
      print("[%02d] = %d" % (i, mem[i]))
  
  best_output = 0
  best_phases = []
  
  phases = [0,0,0,0,0]
  
  phase_values = [5,6,7,8,9]

  phases = get_next_phases(phases)

  while phases:
    
    print("Check", [phase_values[x] for x in phases])
    
    mems = []
    dev_inputs = []
    dev_outputs = []
    pcs = []
    for phase in phases:
      mems.append(orig_mem[:])
      dev_inputs.append([])
      dev_outputs.append([])
      pcs.append(0)
    
    dev_inputs[1] = dev_outputs[0]
    dev_inputs[2] = dev_outputs[1]
    dev_inputs[3] = dev_outputs[2]
    dev_inputs[4] = dev_outputs[3]
    dev_inputs[0] = dev_outputs[4]
    dev_inputs[0].append(0)
    
    for i in range(len(phases)):
      phase = phase_values[phases[i]]
      dev_inputs[i].append(phase)
    
    def all_off(mems, pcs):
      for i in range(len(pcs)):
        mem = mems[i]
        pc = pcs[i]
        if pc < len(mem):
          return False
      return True
      
    while not all_off(mems, pcs):      
      for i in range(len(phases)):
        mem = mems[i]
        pc = pcs[i]
        dev_input = dev_inputs[i]
        dev_output = dev_outputs[i]

        print("Running: dev %d PC=%d" % (i, pc))
        while pc < len(mem):
          opcode = mem[pc] % 100
          command = opcodes[opcode]
          print("[%03d]OPCODE: %d - %s" % (pc, opcode, command.__name__));
          try:
            pc = command(mem, pc, dev_input, dev_output)
          except IO_Dev_Interrupt:
            print ("IO Interrupt: dev %d PC=%d" % (i, pc))
            break
        pcs[i] = pc
        
    output = dev_inputs[0][0]
    print("\n\nStoped, phases %s output %d\n\n" % ([phase_values[p] for p in phases], output))
    if output > best_output:
      best_output = output
      best_phases = phases[:]
    phases = get_next_phases(phases)
        
  
  print("Best output %d for phase %s" % (best_output, [phase_values[x] for x in best_phases]))
    
