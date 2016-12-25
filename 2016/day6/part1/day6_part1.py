import sys


def main(file_arg):
    decoded_string = ''

    with open(file_arg) as f:
        # Read the first line just to get the number of columns
        first_line = f.readline().strip()

        number_of_columns = len(first_line)

        column_dictionaries = [{} for x in range(number_of_columns)]

        # Reset the file to the beginning so that the first line is iterated over
        f.seek(0)

        for line in f:
            line = line.strip()

            for x, letter in enumerate(line):
                if letter in column_dictionaries[x].keys():
                    column_dictionaries[x][letter] += 1
                else:
                    column_dictionaries[x][letter] = 1

        for column_dictionary in column_dictionaries:
            sorted_column_dictionary = sorted(column_dictionary.items(), key=lambda x: x[1], reverse=True)

            decoded_string += sorted_column_dictionary[0][0]

    print(decoded_string)


if __name__ == '__main__':
    main(sys.argv[1])

