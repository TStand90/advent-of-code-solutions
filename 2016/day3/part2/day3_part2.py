import sys


def is_triangle(first_number, second_number, third_number):
    if (first_number + second_number) <= third_number:
        return False
    if (first_number + third_number) <= second_number:
        return False
    if (second_number + third_number) <= first_number:
        return False

    return True


def main(file_arg):
    number_of_triangles = 0

    with open(file_arg) as f:
        lines = f.readlines()

        for line_set_one, line_set_two, line_set_three in zip(lines[0::3], lines[1::3], lines[2::3]):
            token_set_one = [int(token) for token in line_set_one.split()]
            token_set_two = [int(token) for token in line_set_two.split()]
            token_set_three = [int(token) for token in line_set_three.split()]

            if is_triangle(token_set_one[0], token_set_two[0], token_set_three[0]):
                number_of_triangles += 1
            if is_triangle(token_set_one[1], token_set_two[1], token_set_three[1]):
                number_of_triangles += 1
            if is_triangle(token_set_one[2], token_set_two[2], token_set_three[2]):
                number_of_triangles += 1

    print(number_of_triangles)


if __name__ == '__main__':
    main(sys.argv[1])
