from pytest import mark

from problem_017 import clean_word, three_digit_number_written_as_word


@mark.parametrize('n, word', [
    (16, 'sixteen'),
    (27, "twenty-seven"),
    (82, "eighty-two"),
    (99, "ninety-nine"),
    (115, "one hundred and fifteen"),
    (342, "three hundred and forty-two"),
    (501, "five hundred and one"),
    (710, "seven hundred and ten"),
    (900, "nine hundred"),
])
def test_three_digit_number_written_as_word(n, word):
    assert three_digit_number_written_as_word(n) == word


@mark.parametrize('word, length', [
    ("three hundred and forty-two", 23),
    ("one hundred and fifteen", 20),
])
def test_clean(word, length):
    assert len(clean_word(word)) == length
