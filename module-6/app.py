#!/usr/bin/env python3

def main():
    while True:
        try:
            amount = float(input("Enter a numeric amount: "))
            if amount <= 0:
                raise ValueError("Amount cannot be negative or zero.")
            if amount > 1000000000000:  # Check for numbers exceeding or equal to a trillion
                raise ValueError("Amount must be less than a trillion.")
            break
        except ValueError as e:
            print("Invalid input:", e)

    dollars, cents = divmod(amount, 1)
    dollars = int(dollars)
    cents = round(cents * 100)

    dollar_words = convert_to_words(dollars)
    cent_words = convert_to_words(cents)

    print(format_check_text(dollar_words, cent_words))


def convert_to_words(number):
    under_20 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]

    if number < 20:
        return under_20[number]
    elif number < 100:
        return tens[number // 10] + ("-" + under_20[number % 10] if number % 10 != 0 else "")
    elif number < 1000:
        return under_20[number // 100] + " hundred" + (" " + convert_to_words(number % 100) if number % 100 != 0 else "")
    else:
        for idx, word in enumerate(thousands):
            if number < 1000 ** (idx + 1):
                return convert_to_words(number // (1000 ** idx)) + " " + word + (" " + convert_to_words(number % (1000 ** idx)) if number % (1000 ** idx) != 0 else "")
        return "Number too large"


def format_check_text(dollars, cents):
    return f"{dollars.capitalize()} dollars and {cents} cents only."


if __name__ == "__main__":
    main()
