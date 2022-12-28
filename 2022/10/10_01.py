f = open("input.txt")

class regfile:
    def __init__(self, x = 1):
        self._x = x
    
    @property    
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
        
    
class oplib:
    def __init__(self, cpu):
        self._cpu = cpu
        
        self._cmds = {
            "addx" : self.addx,
            "noop" : self.noop
        }

    @property
    def cmds(self):
        return self._cmds

        
    def noop(self, params):
        self._cpu.tick()
    
    def addx(self, params):
        value = int(params)
        
        self._cpu.tick()
        self._cpu.regs.x += value
        self._cpu.tick()

class BasicCpu:
    def __init__(self):
        self._regs = regfile()
        self._clock = 1
                
        self._ops = oplib(self)
        
        self._senses = 0
        
        
    @property
    def regs(self):
        return self._regs
    
    @property
    def ops(self):
        return self._ops
    
    @property
    def clock(self):
        return self._clock
            
    def tick(self):
        self._clock += 1
        
        if ((self._clock - 20) % 40) == 0:
            self.do_sense()
            
    def do_sense(self):
        value = self.regs.x * self._clock
        
        print("CPU sensed %d at clock %d x %d" % (value, self._clock, self.regs.x))
        self._senses += value
        
    @property
    def senses(self):
        return self._senses

    def run(self, command, params):
        handler = self.ops.cmds[command]
        handler(params)
        
cpu = BasicCpu()

for line in f:
    line = line.strip()
    
    if " " in line:
        command, params = line.split(" ")
    else:
        command = line
        params = ""
    
    print("%s [%s]: cycle %d, x %d" % (command, line, cpu.clock, cpu.regs.x))
    cpu.run(command, params)
    
print("Result: %d" % cpu.senses)
