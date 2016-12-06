import sys


def main(file_arg):
    keypad_string = ''

    with open(file_arg) as f:
        for line in f:
            line = line.strip()

            current_x = 1
            current_y = 1

            for character in line:
                if character == 'U':
                    if current_y > 0:
                        current_y -= 1
                elif character == 'D':
                    if current_y < 2:
                        current_y += 1
                elif character == 'L':
                    if current_x > 0:
                        current_x -= 1
                elif character == 'R':
                    if current_x < 2:
                        current_x += 1

            keypad_character = str(current_x + (current_y * 3) + 1)

            keypad_string += keypad_character

    print(keypad_string)



if __name__ == '__main__':
    main(sys.argv[1])

