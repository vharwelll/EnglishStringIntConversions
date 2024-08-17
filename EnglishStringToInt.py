
class EnglishStringToInt:
    def __init__(self):
        self.multipliers = {
            "billion":(1000000000, True),
            "million":(1000000, True),
            "thousand":(1000, True),
            "hundred":(100, False),
        }

        self.concrete = {
            "ninety": 90,
            "eighty":80,
            "seventy":70,
            "sixty":60,
            "fifty":50,
            "forty":40,
            "thirty":30,
            "twenty":20,
            "nineteen":19,
            "eighteen":18,
            "seventeen":17,
            "sixteen":16,
            "fifteen":15,
            "fourteen":14,
            "thirteen":13,
            "twelve":12,
            "eleven":11,
            "ten":10,
            "nine":9,
            "eight":8,
            "seven":7,
            "six":6,
            "five":5,
            "four":4,
            "three":3,
            "two":2,
            "one":1,
            "zero":0
        }

    def decode(self, source):
        working = 0
        final = 0
        sign = 1
        found = False
        words = source.split(' ') #chop0
        words = [w.lower() for w in words] # sanitize
        words = [w for w in words if not w.isspace() and w != '' and w != "and"] # filter

        for word in words:
            if word == "negative":
                sign = -1
            elif word in self.concrete.keys():
                found = True
                working += self.concrete[word]
            elif word in self.multipliers.keys():
                working *=  self.multipliers[word][0]
                if self.multipliers[word][1]:
                    final += working
                    working = 0
            else:
                raise ValueError(f"word: '{word}' is not valid ")

        if found:
            final += working
            return sign * final
        else:
            raise ValueError(f"source: '{source}' is not a valid number")

    def check(self, string, number):
        result = self.decode(string)
        passed = result == number
        if not passed:
            print(f"in: {number:16}, match: {passed}, result: {result}, source: {string}")
        return passed

testdata = [
    "",
    "unmatched",
    "Zero",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen",
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety",
    "Hundred",
    "Thousand",
    "Million",
    "Billion",
    "Four Hundred",
    "Five Thousand",
    "Six Million",
    "Seven Billion",
    "Sixty            two",
    "Sixty and two",
    "Sixty Thousand And and Two"
]

def main():
    t = EnglishStringToInt()

    t.check("Eight Hundred Five Thousand Eight Hundred Eighty Eight",805888)
    #return

    for test in testdata:
        try:
            print(f"in: {test}, out: {t.decode(test)}")
        except ValueError as e:
            print(f"in: {test}, out: {e}")

    count = 1
    with open("IntTOEnglishString.txt", mode="rt", encoding="utf8") as stream:
        for record in stream:
            if count % 1000000 == 0:
                print(f"processed {count} records...")
            parts = record.replace('\n', '').split(":")
            if not t.check(parts[1], int(parts[0])):
                print(f"failure at record: {count}")
                raise ValueError()
            count+=1
        print("finished file processing...")





if __name__ == "__main__":
    main()

