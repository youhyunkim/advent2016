import re


pattern = "\([0-9]*x[0-9]*\)"
pattern_2 = "\(([0-9]*)x([0-9]*)\)"

with open("input.txt") as f:
    line = f.read()

    indices = [(m.start(0), m.end(0)) for m in re.finditer(pattern, line)]

    current_loc = 0
    decrypted = ""
    for idx in indices:
        if current_loc > idx[0]:
            continue

        operation = line[idx[0]:idx[1]]

        m = re.match(pattern_2, operation)
        counter = int(m.group(1))
        multiplier = int(m.group(2))

        current_loc += len(operation)
        
        chars_to_multiply = line[current_loc:current_loc+counter]
        for _ in range(0, multiplier):
            decrypted+= chars_to_multiply

        current_loc+= counter

    print len(decrypted)