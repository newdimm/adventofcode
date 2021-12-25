#!/usr/bin/python

test = False
if test:
    f_input = open("input.test")
else:
    f_input = open("input")

a,b,c,d,e,f,g = 0,1,2,3,4,5,6

disp = [
    [a,b,c,e,f,g], # 0
    [c,f],  # 1
    [a,c,d,e,g], # 2
    [a,c,d,f,g], # 3
    [b,c,d,f], # 4
    [a,b,d,f,g], # 5
    [a,b,d,e,f,g], # 6
    [a,c,f], # 7
    [a,b,c,d,e,f,g], # 8
    [a,b,c,d,f,g] # 9
]

seg_decode = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5,
    'g' : 6,
}



def process(decoder, codes, variants):
    for index in range(len(decoder)):
        if index in codes:
            decoder[index] = [x for x in decoder[index] if x in variants]
        else:
            decoder[index] = [x for x in decoder[index] if x not in variants]
    
def print_decoder(d):
    for x in range(len(d)):
        print("[%d]: %s" % (x, d[x]))

def find_common(digits):
    all_segments = []
    for digit in digits:
        for d in digit:
            if d not in all_segments:
                all_segments.append(d)
    common_segments = all_segments[:]
    for digit in digits:
        for s in all_segments:
            if s not in digit:
                common_segments = [x for x in common_segments if x != s]

    return common_segments

final_answer = 0
for line in f_input:
    # maps segments 
    decoder = []
    for digit in range(7):
        decoder.append([x for x in range(10)])
    
    print_decoder(decoder)


    codes, output = line.strip().split(" | ")
    code = codes.split(" ")
    output = output.split(" ")

    fives = []
    sixes = []

    for digit in code:
        digit = [seg_decode[seg] for seg in digit]

        matches = []
        for m in disp:
            if len(m) == len(digit):
                matches.append(m)

        if len(matches) == 1:
            print("digit: %s matches %s" % (digit, matches[0]))
            process(decoder, digit, matches[0])
            print_decoder(decoder)
        elif len(digit) == 5:
            fives.append(digit)
            print("digit: %s is fives" % digit)
        elif len(digit) == 6:
            sixes.append(digit)
            print("digit: %s is sixes" % digit)
        
    codes = find_common(fives)
    variants = find_common([disp[2], disp[3], disp[5]])   

    print("fives %s match %s", codes, variants)
    process(decoder, codes, variants)
    print_decoder(decoder)

    codes = find_common(sixes)
    variants = find_common([disp[0], disp[6], disp[9]])   

    print("sixes %s match %s", codes, variants)
    process(decoder, codes, variants)
    print_decoder(decoder)

    for index in range(len(decoder)):
        decoder[index] = decoder[index][0]

    answer = 0
    for digit in output:
        s = [seg_decode[seg] for seg in digit]
        s = [decoder[d] for d in s]
        s.sort()

        for index in range(len(disp)):
            if s == disp[index]:
                break
        answer = (answer * 10 + index)
    
    print("output %s -> %d" % (output, answer))
    final_answer += answer

print("Final answer: %d" % final_answer)
