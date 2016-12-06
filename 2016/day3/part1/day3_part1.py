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
        for line in f:
            tokens = [int(token) for token in line.split()]

            if is_triangle(tokens[0], tokens[1], tokens[2]):
                number_of_triangles += 1

    print(number_of_triangles)


if __name__ == '__main__':
    main(sys.argv[1])
