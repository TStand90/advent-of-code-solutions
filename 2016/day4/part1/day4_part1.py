import sys
import collections


def main(file_arg):
    sector_id_sum = 0

    with open(file_arg) as f:
        for line in f:
            room_string_and_sector_id, checksum = line.strip().split('[')
            checksum = checksum[:-1]

            room_string = ''.join(room_string_and_sector_id.split('-')[:-1])
            sector_id = int(room_string_and_sector_id.split('-')[-1])

            letters = collections.Counter(room_string)

            sorted_letters = sorted(letters.items(), key=lambda x: (-x[1], x[0]))

            five_most_common_letters = ''.join([letter[0] for letter in sorted_letters[:5]])

            if five_most_common_letters == checksum:
                sector_id_sum += sector_id

    print(sector_id_sum)


if __name__ == '__main__':
    main(sys.argv[1])

