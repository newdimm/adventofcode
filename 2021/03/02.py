#!/usr/bin/python

test = False
if test:
    f = open("input.test")
else:
    f = open("input")

bitmask = []

lines = []
for line in f:
    lines.append(line.strip())

bitlen = len(lines[0])

pattern = ""
for pos in range(0, bitlen+1):
    result = 0
    counter = 0
    print("[%d] =====> <%s>" % (pos, pattern))
    for line in lines:
        if line[0:pos] != pattern:
            continue

        last_line = line
        counter += 1

        print("%s" % line)

        if pos == bitlen:
            break

        if line[pos] == '0':
            result -= 1
        else:
            result += 1

    if counter == 1:
        oxigen = last_line
        break

    if result >= 0:
        pattern += '1'
    else:
        pattern += '0'

pattern = ""
for pos in range(0, bitlen+1):
    result = 0
    counter = 0
    print("[%d] =====> <%s>" % (pos, pattern))
    for line in lines:
        if line[0:pos] != pattern:
            continue

        last_line = line
        counter += 1

        print("%s" % line)

        if pos == bitlen:
            break

        if line[pos] == '0':
            result -= 1
        else:
            result += 1

    if counter == 1:
        co2 = last_line
        break

    if result >= 0:
        pattern += '0'
    else:
        pattern += '1'

pos = bitlen - 1
oxi_rate = 0
for bit in oxigen:
    if bit == '1':
        oxi_rate += 1 << pos
    pos -= 1

pos = bitlen - 1
co2_rate = 0
for bit in co2:
    if bit == '1':
        co2_rate += 1 << pos
    pos -= 1

print("oxi_rate %d * co2_rate %d = %d" % (oxi_rate, co2_rate, oxi_rate * co2_rate))



    
    



