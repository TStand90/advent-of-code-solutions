import sys


def get_new_direction(current_direction, rotation):
    if rotation == 'R':
        if current_direction == 'north':
            return 'east'
        elif current_direction == 'east':
            return 'south'
        elif current_direction == 'south':
            return 'west'
        elif current_direction == 'west':
            return 'north'
    elif rotation == 'L':
        if current_direction == 'north':
            return 'west'
        elif current_direction == 'east':
            return 'north'
        elif current_direction == 'south':
            return 'east'
        elif current_direction == 'west':
            return 'south'


def main(file_arg):
    with open(file_arg) as f:
        for line in f:
            tokens = line.strip().split(', ')

            current_direction = 'north'
            x = 0
            y = 0

            for token in tokens:
                number_of_blocks = int(token[1:])

                current_direction = get_new_direction(current_direction, token[0])
                if current_direction == 'north':
                    y += number_of_blocks
                elif current_direction == 'south':
                    y -= number_of_blocks
                elif current_direction == 'east':
                    x += number_of_blocks
                elif current_direction == 'west':
                    x -= number_of_blocks

            x = abs(x)
            y = abs(y)

            distance_traveled = x + y

            print(distance_traveled)


if __name__ == '__main__':
    main(sys.argv[1])
