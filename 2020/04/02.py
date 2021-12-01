#!/usr/bin/python

import re

fields = {
        "byr" : (True, [("(\d\d\d\d)", 1920, 2002)]), # (Birth Year)
        "iyr" : (True, [("(\d\d\d\d)", 2010, 2020)]), # (Issue Year)
        "eyr" : (True, [("(\d\d\d\d)", 2020, 2030)]), # (Expiration Year)
        "hgt" : (True, [("(\d+)cm", 150, 193), ("(\d+)in", 59, 76)]), # (Height)
        "hcl" : (True, [("#([0-9a-f]{6}$)", 0, 0)]), # (Hair Color)
        "ecl" : (True, [("amb|blu|brn|gry|grn|hzl|oth", 0, 0)]), # (Eye Color)
        "pid" : (True, [("[0-9]{9}$", 0, 0)]), # (Passport ID)
        "cid" : (False,[(".*", 0, 0)]) # (Country ID)
        }

required = 0
for (mandatory, rules) in fields.values():
    if mandatory:
        required += 1


test = 0

if test:
    input_file = "simple_input2.txt"
else:
    input_file = "input.txt"

with open(input_file, "r") as f:

    valid = 0

    p = {}
    counter = 0

    for line in f:
        line = line.strip()

        #print("<%s>" % line)


        if not line:
            if counter:
                print("is valid: %s fields %d" % (str(counter == required), counter))

                if counter == required:
                    valid += 1
            p = {}
            counter = 0
            continue

        records = line.split(" ")
        #print("records: <%s>" % str(records));
        for record in records:
            #print("record <%s>" % str(record))
            (field, value) = record.split(":")

            if field not in fields:
                print("unknown field: %s" % field)
                continue

            if field not in p:
                p[field] = True
                (mandatory, rules) = fields[field]

                if mandatory:
                    matched = False

                    #print("field %s rules: %s" % (field, str(rules)))

                    for rule in rules:
                        #print("rule: %s" % str(rule))
                        (pattern, value_min, value_max) = rule
                        match_result = re.match(pattern, value)
    
                        if match_result is None:
                            continue

                        if value_min == value_max:
                            matched = True
                            break

                        if not match_result.groups(0):
                            continue

                        match_value_str = match_result.groups(0)[0]

                        try:
                            match_value = int(match_value_str)
                        except ValueError:
                            match_value = None

                        if match_value is None:
                            continue

                        #print("match_value: %d", match_value)
                        if match_value >= value_min and match_value <= value_max:
                             matched = True
                             break
                        

                    if matched:
                        counter += 1 
                    print("mandatory: <%s>:<%s> (%s,%d,%d) -> %s" % (field, value, pattern, value_min, value_max, str(matched)))

    if counter:
        print("is valid: %s fields %d" % (str(counter == required), counter))
        if counter == required:
            valid += 1

    print("Valid paasports: %d" % valid)


