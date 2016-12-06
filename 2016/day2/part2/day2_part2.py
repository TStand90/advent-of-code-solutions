import sys


def main(file_arg):
    keypad = [
        [None, None, None, None, None, None, None],
        [None, None, None, '1',  None, None, None],
        [None, None, '2',  '3',  '4',  None, None],
        [None, '5',  '6',  '7',  '8',  '9', None],
        [None, None, 'A',  'B',  'C',  None, None],
        [None, None, None, 'D',  None, None, None],
        [None, None, None, None, None, None, None]
    ]

    keypad_string = ''

    with open(file_arg) as f:
        for line in f:
            line = line.strip()

            current_x = 3
            current_y = 3

            for character in line:
                temp_x = current_x
                temp_y = current_y

                if character == 'U':
                    temp_y -= 1
                elif character == 'D':
                    temp_y += 1
                elif character == 'L':
                    temp_x -= 1
                elif character == 'R':
                    temp_x += 1

                if keypad[temp_y][temp_x] is not None:
                    current_x = temp_x
                    current_y = temp_y

            keypad_string += keypad[current_y][current_x]

    print(keypad_string)


if __name__ == '__main__':
    main(sys.argv[1])

