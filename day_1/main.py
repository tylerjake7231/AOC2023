import itertools
import operator

def puzzle1():
    #read input text file
    input = open("day_1/input_1.txt", "rt").read()

    #split by lines
    input = input.splitlines()

    #map each line to its number
    line_nums = map(extract_number1, input)

    #sum the numbers
    answer_1 = sum(line_nums)

    print(answer_1)

def puzzle2():
    #read input text file
    input = open("day_1/input_1.txt", "rt").read()


    #split by lines
    input = input.splitlines()

    #map each line to its number
    line_nums = map(extract_number2, input)

    #sum the numbers
    answer_2 = sum(line_nums)

    print(answer_2)


def extract_number1(line : str) -> int:
    '''
    Turns each line into a number
    '''

    #keeps only the digits
    numbers = "".join([ele for ele in line if ele.isdigit()])

    #keep only the first and last digit
    first_digit = numbers[0]
    last_digit = numbers[-1]

    #parse to a number and return
    return int(first_digit)*10+int(last_digit)

def extract_number2(line : str) -> int:
    '''
    Turns each line into a number
    '''

    #digit list
    digit_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    #first digit
    #find which digits are in line
    digits_present = [digit for digit in digit_list if digit in line]

    if digits_present != []:
        #find the first position of each digit
        first_digit_pos = min([line.index(digit) for digit in digits_present])
        #find the digit
        first_digit = [digit for digit in digits_present if line.index(digit) == first_digit_pos][0]

        #insert that specific digit
        if(first_digit == "one"):
            line = line[:first_digit_pos] + "1" + line[first_digit_pos:]
        elif(first_digit == "two"):
            line = line[:first_digit_pos] + "2" + line[first_digit_pos:]
        elif(first_digit == "three"):
            line = line[:first_digit_pos] + "3" + line[first_digit_pos:]
        elif(first_digit == "four"):
            line = line[:first_digit_pos] + "4" + line[first_digit_pos:]
        elif(first_digit == "five"):
            line = line[:first_digit_pos] + "5" + line[first_digit_pos:]
        elif(first_digit == "six"):
            line = line[:first_digit_pos] + "6" + line[first_digit_pos:]
        elif(first_digit == "seven"):
            line = line[:first_digit_pos] + "7" + line[first_digit_pos:]
        elif(first_digit == "eight"):
            line = line[:first_digit_pos] + "8" + line[first_digit_pos:]
        elif(first_digit == "nine"):
            line = line[:first_digit_pos] + "9" + line[first_digit_pos:]
            
    #last digit
    #find which digits are in line
    digits_present = [digit for digit in digit_list if digit in line]

    if digits_present != []:
        #find the last position of each digit
        first_digit_pos = max([line.rindex(digit) for digit in digits_present])
        #find the digit
        first_digit = [digit for digit in digits_present if line.rindex(digit) == first_digit_pos][0]

        #replace that specific digit
        if(first_digit == "one"):
            line = line[:first_digit_pos] + "1" + line[first_digit_pos:]
        elif(first_digit == "two"):
            line = line[:first_digit_pos] + "2" + line[first_digit_pos:]
        elif(first_digit == "three"):
            line = line[:first_digit_pos] + "3" + line[first_digit_pos:]
        elif(first_digit == "four"):
            line = line[:first_digit_pos] + "4" + line[first_digit_pos:]
        elif(first_digit == "five"):
            line = line[:first_digit_pos] + "5" + line[first_digit_pos:]
        elif(first_digit == "six"):
            line = line[:first_digit_pos] + "6" + line[first_digit_pos:]
        elif(first_digit == "seven"):
            line = line[:first_digit_pos] + "7" + line[first_digit_pos:]
        elif(first_digit == "eight"):
            line = line[:first_digit_pos] + "8" + line[first_digit_pos:]
        elif(first_digit == "nine"):
            line = line[:first_digit_pos] + "9" + line[first_digit_pos:]

    #extract number same way as in part 1
    return extract_number1(line)

if __name__ == "__main__":
    puzzle1()
    puzzle2()