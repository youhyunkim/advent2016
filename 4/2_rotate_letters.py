import re

pattern = '(.*)-([0-9]*)\[(.*)\]'

with open("input.txt") as f:
    room_names = f.read().splitlines()
    for room_name in room_names:
        result = re.match(pattern, room_name)
        letters = result.group(1).replace('-', ' ')
        sector_id = int(result.group(2))
        checksum = result.group(3)
        
        rotate_count = sector_id % 26

        new_letters = ''
        for letter in letters:
            if letter == '':
                new_letters+= ' '

            new_ascii = ord(letter) + (rotate_count % 26)

            if new_ascii > 122:
                new_ascii-= 26
            new_letters+= str(unichr(new_ascii))

        if new_letters == "northpole'object'storage":
            print sector_id
