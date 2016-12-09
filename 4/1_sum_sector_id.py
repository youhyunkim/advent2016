import re

def is_room_real(letters_with_dash, checksum):

    letters = letters_with_dash.replace('-', '')

    print letters
    letter_to_count = {}
    for letter in letters:
        if letter in letter_to_count:
            letter_to_count[letter]+= 1
        else:
            letter_to_count[letter] = 1

    ordered_letter_cand = []
    for n in range (15, 0, -1):
        letter_for_n = []
        for letter, cnt in letter_to_count.items():
            if cnt == n:
                letter_for_n.append(letter)
        sorted_letter_for_n = ''.join(sorted(letter_for_n))
        ordered_letter_cand.extend(sorted_letter_for_n)

    checksum_should_be = ''.join(map(str, ordered_letter_cand[0:5]))
    return checksum_should_be == checksum

pattern = '(.*)-([0-9]*)\[(.*)\]'

real_sector_id_sum = 0

with open("input.txt") as f:
    room_names = f.read().splitlines()
    for room_name in room_names:
        result = re.match(pattern, room_name)
        letters_with_dash = result.group(1)
        sector_id = int(result.group(2))
        checksum = result.group(3)
        if is_room_real(letters_with_dash, checksum):
            real_sector_id_sum += sector_id

    print real_sector_id_sum