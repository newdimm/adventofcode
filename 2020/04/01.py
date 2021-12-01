#!/usr/bin/python


fields = {
        "byr" : True, # (Birth Year)
        "iyr" : True, # (Issue Year)
        "eyr" : True, # (Expiration Year)
        "hgt" : True, # (Height)
        "hcl" : True, # (Hair Color)
        "ecl" : True, # (Eye Color)
        "pid" : True, # (Passport ID)
        "cid" : False # (Country ID)
        }

required = 0
for v in fields.values():
    if v:
        required += 1


test = 0

if test:
    input_file = "simple_input.txt"
else:
    input_file = "input.txt"

with open(input_file, "r") as f:

    valid = 0

    p = {}
    counter = 0

    for line in f:
        line = line.strip()


        print("<%s>" % line)

        if not line:
            print("is valid: %s fields %d" % (str(counter == required), counter))

            if counter == required:
                valid += 1
            # handle passport
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
                if fields[field]:
                    #print("required field")
                    counter += 1

    if counter:
        print("is valid: %s fields %d" % (str(counter == required), counter))
        if counter == required:
            valid += 1

    print("Valid paasports: %d" % valid)


