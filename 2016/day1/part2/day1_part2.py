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
    visited_locations = [(0, 0)]

    with open(file_arg) as f:
        for line in f:
            tokens = line.strip().split(', ')

            current_direction = 'north'
            x = 0
            y = 0

            for token in tokens:
                number_of_blocks = int(token[1:])

                current_direction = get_new_direction(current_direction, token[0])

                for each_block in range(1, number_of_blocks + 1):
                    if current_direction == 'north':
                        y += 1
                    elif current_direction == 'south':
                        y -= 1
                    elif current_direction == 'east':
                        x += 1
                    elif current_direction == 'west':
                        x -= 1
                    
                    new_location = (x, y)

                    if new_location in visited_locations:
                        x = abs(x)
                        y = abs(y)

                        distance = x + y

                        print(distance)

                        return
                    else:
                        visited_locations.append(new_location)


if __name__ == '__main__':
    main(sys.argv[1])
