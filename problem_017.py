"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example,
342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.

The use of "and" when writing out numbers is in compliance with British usage.
"""
import re

from utils import measure_execution_time


UNDER_TWENTY_TO_WORD = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

TEENS_TO_WORDS = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

LIMIT = 1000


def main() -> None:
    print("Problem 17")
    with measure_execution_time():
        words = [three_digit_number_written_as_word(n)
                 for n in range(1, LIMIT)]
        cleaned_words = [clean_word(word) for word in words]
        result = sum(len(w) for w in cleaned_words) + len("onethousand")
    print(f"the number of letters used to write 1 to {LIMIT} in words is {result}")


def three_digit_number_written_as_word(n: int) -> str:
    assert n >= 1 and n <= 999
    two_digit_number = two_digit_number_written_as_word(n % 100)
    if n < 100:
        return two_digit_number
    hundreds = UNDER_TWENTY_TO_WORD[n // 100] + " hundred"
    if two_digit_number:
        return f"{hundreds} and {two_digit_number}"
    else:
        return hundreds


def two_digit_number_written_as_word(n: int) -> str:
    assert n >= 0 and n <= 99
    if n == 0:
        return ""
    if n < 20:
        return UNDER_TWENTY_TO_WORD[n]
    result = TEENS_TO_WORDS[n // 10]
    ones = n % 10
    if ones:
        result += "-" + UNDER_TWENTY_TO_WORD[ones]
    return result


def clean_word(w: str) -> str:
    return re.sub(r"-|\s", repl="", string=w)


if __name__ == '__main__':
    main()
