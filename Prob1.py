#prob1
    def main():
    try:
        numbers = []
        for i in range (3):
            num = int(input(f"enter the number {i+1}"))
            numbers.append(num)

        greatestNum = max(numbers)
        print("the largest number is: ", greatestNum)
    except ValueError:
        print("invalid input, please enter valid numbers")

if __name__=__main__