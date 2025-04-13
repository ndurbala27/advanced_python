def word_adder(word1: str, word2: str):
    numbers = { "zero" : 0, "one" : 1, "two" : 2, "three" : 3,
                "four" : 4, "five" : 5, "six" : 6, "seven" : 7,
                "eight" : 8, "nine" : 9, "ten" : 10, "eleven" : 11,
                "twelve" : 12, "thirteen" : 13, "fourteen": 14, "fifteen" : 15,
                "sixteen" : 16, "seventeen" : 17, "eighteen" : 18, "nineteen" : 19,
                "twenty" : 20
    }

    try:
        if (numbers[word1] < 11) and (numbers[word2] < 11):
            total = numbers[word1] + numbers[word2]
        else:
            return "The arguments should be words between zero and ten"
    except KeyError:
        return "The arguments should be words between zero and ten"
    else:
        for key, value in numbers.items():
            if total == value:
                return key