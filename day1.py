####
# Day 1
####

def main():
    print('Solution for part one is: ', part1())
    print('Solution for part two is: ', part2())

####
# Part 1
####
# The newly-improved calibration document consists of lines of text;
# each line originally contained a specific calibration value that the Elves now need to recover.
# On each line, the calibration value can be found by
# combining the first digit and the last digit (in that order) to form a single two-digit number.
#---------------
# For example:  |
# 1abc2         |
# pqr3stu8vwx   |
# a1b2c3d4e5f   |
# treb7uchet    |
#---------------
# In this example, the calibration values of these four lines are 12, 38, 15, and 77.
# Adding these together produces 142.
# Consider your entire calibration document. What is the sum of all of the calibration values?
def part1():
    num_arr = []
    with open("day1.txt") as text:
        for line in text:
            line_arr = []
            for char in line:
                if char.isdigit():
                    line_arr.append(char)
            num_arr.append(line_arr)

    all_numbers_sum = 0
    for num_list in num_arr:
        first = num_list[0]
        last = num_list[-1]
        all_numbers_sum += int(first + last)
    return all_numbers_sum


def has_spelled_out_numbers(string):
    """Returns a List of numbers up to 9 that are spelled out in the string"""
    spelled_out_numbers = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    ]
    found_numbers = []

    for start_index in range(len(string)):
        for number, spelled_out_number in enumerate(spelled_out_numbers):
            if string[start_index:].startswith(spelled_out_number):
                found_numbers.append(number)

    return found_numbers

assert has_spelled_out_numbers('seven') == [7], has_spelled_out_numbers('seven')
assert has_spelled_out_numbers('seveneight') == [7, 8], has_spelled_out_numbers('seveneight')
assert has_spelled_out_numbers('twone') == [2, 1], has_spelled_out_numbers('twone')
assert has_spelled_out_numbers('sevenkrrlnbzggtwofourtwo') == [7, 2, 4, 2], has_spelled_out_numbers('sevenkrrlnbzggtwofourtwo')


def split_text_on_digits(text):
    temp_check_if_number_string = ""
    split_on_digits = []
    for char in text:
        if char.isdigit():
            if len(temp_check_if_number_string) > 0:
                split_on_digits.append(temp_check_if_number_string)
                temp_check_if_number_string = ""
            split_on_digits.append(char)
        else:
            temp_check_if_number_string += char
    if len(temp_check_if_number_string) > 0:
        split_on_digits.append(temp_check_if_number_string)
    return split_on_digits

assert split_text_on_digits('dlslthree1sevenkrrlnbzggtwofourtwo') == ['dlslthree', '1', 'sevenkrrlnbzggtwofourtwo'], split_text_on_digits('dlslthree1sevenkrrlnbzggtwofourtwo')
assert split_text_on_digits('seven1twothree4five6') == ['seven', '1', 'twothree', '4', 'five', '6'], split_text_on_digits('seven1twothree4five6')
assert split_text_on_digits('two1nine') == ['two', '1', 'nine'], split_text_on_digits('two1nine')
assert split_text_on_digits('eightwothree') == ['eightwothree'], split_text_on_digits('eightwothree')
assert split_text_on_digits('abcone2threexyz') == ['abcone','2','threexyz'], split_text_on_digits('abcone2threexyz')
assert split_text_on_digits('xtwone3four') == ['xtwone','3','four'], split_text_on_digits('xtwone3four')
assert split_text_on_digits('4nineeightseven2')== ['4','nineeightseven','2'], split_text_on_digits('4nineeightseven2')
assert split_text_on_digits('zoneight234') == ['zoneight','2','3','4'], split_text_on_digits('zoneight234')
assert split_text_on_digits('7pqrstsixteen') == ['7','pqrstsixteen'], split_text_on_digits('7pqrstsixteen')

def convert_spelled_out_numbers_into_numbers(arr):
    just_digits = []
    for text in arr:
        if text.isdigit():
            just_digits.append(int(text))
        else:
            spelled_out_numbers = has_spelled_out_numbers(text)
            if len(spelled_out_numbers) > 0:
                just_digits = just_digits + spelled_out_numbers
    return just_digits

assert convert_spelled_out_numbers_into_numbers(['eighthree']) == [8, 3], convert_spelled_out_numbers_into_numbers(['eighthree'])
assert convert_spelled_out_numbers_into_numbers(['seven', '1', 'eightwo', '4', 'five', '6']) == [7, 1, 8, 2, 4, 5, 6], convert_spelled_out_numbers_into_numbers(['seven', '1', 'eightwo', '4', 'five', '6'])
assert convert_spelled_out_numbers_into_numbers(['two', '1', 'nine']) == [2, 1, 9], convert_spelled_out_numbers_into_numbers(['two', '1', 'nine'])
assert convert_spelled_out_numbers_into_numbers(['eightwothree']) == [8, 2, 3], convert_spelled_out_numbers_into_numbers(['eightwothree'])
assert convert_spelled_out_numbers_into_numbers(['abcone','2','threexyz']) == [1, 2, 3], convert_spelled_out_numbers_into_numbers(['abcone','2','threexyz'])
assert convert_spelled_out_numbers_into_numbers(['xtwone','3','four']) == [2, 1, 3, 4], convert_spelled_out_numbers_into_numbers(['xtwone','3','four'])
assert convert_spelled_out_numbers_into_numbers(['4','nineeightseven','2']) == [4, 9, 8, 7, 2], convert_spelled_out_numbers_into_numbers(['4','nineeightseven','2'])
assert convert_spelled_out_numbers_into_numbers(['zoneight','2','3','4']) == [1, 8, 2, 3, 4], convert_spelled_out_numbers_into_numbers(['zoneight','2','3','4'])
assert convert_spelled_out_numbers_into_numbers(['7','pqrstsixteen']) == [7, 6], convert_spelled_out_numbers_into_numbers(['7','pqrstsixteen'])
assert convert_spelled_out_numbers_into_numbers(['dlslthree', '1', 'sevenkrrlnbzggtwofourtwo']) == [3, 1, 7, 2, 4, 2], convert_spelled_out_numbers_into_numbers(['dlslthree', '1', 'sevenkrrlnbzggtwofourtwo'])

def test_part2(text_arr):
    all_numbers_sum = 0
    for line in text_arr:
        split_on_digits = split_text_on_digits(line)
        just_digits = convert_spelled_out_numbers_into_numbers(split_on_digits)
        first, last = just_digits[0], just_digits[-1]
        total_num_str = str(first) + str(last)
        all_numbers_sum += int(total_num_str)
    return all_numbers_sum

assert test_part2(['two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen', ]) == 281, test_part2(['two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen', ])

assert test_part2(['nineight']) == 98, test_part2(['nineight'])
assert test_part2(['eightwone']) == 81, test_part2(['eightwone'])
assert test_part2(['five']) == 55, test_part2(['five'])
assert test_part2(['oneighthree']) == 13, test_part2(['oneighthree'])
assert test_part2(['eightwo']) == 82, test_part2(['eightwo'])
assert test_part2(['twone']) == 21, test_part2(['twone'])
assert test_part2(['three28jxdmlqfmc619eightwol']) == 32, test_part2(['three28jxdmlqfmc619eightwol'])
assert test_part2(['rfour4qkvcxsbjnveightwogm']) == 42, test_part2(['rfour4qkvcxsbjnveightwogm'])
assert test_part2(['dlslthree1sevenkrrlnbzggtwofourtwo']) == 32, test_part2(['dlslthree1sevenkrrlnbzggtwofourtwo'])

###
# Part 2
#
# It looks like some of the digits are actually spelled out with letters:
# one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
# Equipped with this new information, you now need to find the real first and last digit on each line. For example:
#-------------------
# two1nine          |
# eightwothree      |
# abcone2threexyz   |
# xtwone3four       |
# 4nineeightseven2  |
# zoneight234       |
# 7pqrstsixteen     |
#-------------------
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
# Adding these together produces 281.
# What is the sum of all of the calibration values?
def part2():
    all_numbers_sum = 0
    with open("day1.txt") as text:
        for line in text:
            split_on_digits = split_text_on_digits(line)
            just_digits = convert_spelled_out_numbers_into_numbers(split_on_digits)
            first, last = just_digits[0], just_digits[-1]
            total_num = str(first) + str(last)
            all_numbers_sum += int(total_num)
    return all_numbers_sum

if __name__ == "__main__":
    main()