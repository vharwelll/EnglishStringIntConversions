from asyncio.subprocess import Process
from concurrent.futures import as_completed, ThreadPoolExecutor


class IntToEnglishString:
    def __init__(self):
        self.first_twenty = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen",]
        self.twenty_to_ninety = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]

    def decode(self, source):
        if source < 0:
            return "Negative " + self.decode(-1 * source)
        elif source < 20:
            return self.first_twenty[source]
        elif source < 100:
            tens = source // 10
            remainder = source -(10*tens)
            return self.twenty_to_ninety[tens] + ' ' + (self.decode(remainder) if remainder > 0 else "")
        elif source < 1000:
            hundreds = source // 100
            remainder = source - (100*hundreds)
            return self.decode(hundreds) + ' Hundred' + (" " + self.decode(remainder) if remainder > 0 else "")
        elif source < 1000000:
            thousands = source // 1000
            remainder = source - (1000*thousands)
            return self.decode(thousands) + ' Thousand' + (" " + self.decode(remainder) if remainder > 0 else "")
        elif source < 1000000000:
            millions = source // 1000000
            remainder = source - (1000000*millions)
            return self.decode(millions) + ' Million' + (" " + self.decode(remainder) if remainder > 0 else "")
        elif source < 1000000000000:
            millions = source // 1000000000
            remainder = source - (1000000000 * millions)
            return self.decode(millions) + ' Billion' + (" " + self.decode(remainder) if remainder > 0 else "")
        else:
            return f"Source: {source} is too large for processing"

    def check(self, number, string):
        result = self.decode(number)
        print(f"in: {number:16}, match: {result == string}, result: {result}, expected: {string}")

def worker(value, processor):
    string = processor.decode(value)
    return value, string

def main():
    t = IntToEnglishString()

    t.check(9, "Nine")
    t.check(-9, "Negative Nine")
    t.check(19, "Nineteen")
    t.check(99, "Ninety Nine")
    t.check(100, "One Hundred")
    t.check(999, "Nine Hundred Ninety Nine")
    t.check(1000, "One Thousand")
    t.check(9999, "Nine Thousand Nine Hundred Ninety Nine")
    t.check(10000, "Ten Thousand")
    t.check(999999, "Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine")
    t.check(1000000, "One Million")
    t.check(1000001, "One Million One")
    t.check(9999999, "Nine Million Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine")
    t.check(99999999, "Ninety Nine Million Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine")
    t.check(100000000, "One Hundred Million")
    t.check(100000001, "One Hundred Million One")
    t.check(999999999, "Nine Hundred Ninety Nine Million Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine")
    t.check(1000000000, "One Billion")
    t.check(9999999999, "Nine Billion Nine Hundred Ninety Nine Million Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine")
    t.check(10000000000, "Ten Billion")
    t.check(100000000000, "One Hundred Billion")
    t.check(100000000001, "One Hundred Billion One")
    t.check(100000000010, "One Hundred Billion Ten")
    t.check(100000000100, "One Hundred Billion One Hundred")
    t.check(100000001000, "One Hundred Billion One Thousand")
    t.check(100000010000, "One Hundred Billion Ten Thousand")
    t.check(100000100000, "One Hundred Billion One Hundred Thousand")
    t.check(100001000000, "One Hundred Billion One Million")
    t.check(100010000000, "One Hundred Billion Ten Million")
    t.check(100100000000, "One Hundred Billion One Hundred Million")
    t.check(101000000000, "One Hundred One Billion")
    t.check(110000000000, "One Hundred Ten Billion")
    t.check(999999999999, "Nine Hundred Ninety Nine Billion Nine Hundred Ninety Nine Million Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine")
    t.check(-999999999999, "Negative Nine Hundred Ninety Nine Billion Nine Hundred Ninety Nine Million Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine")
    t.check(1000000000000, "Source: 1000000000000 is too large for processing")

    #with open("IntTOEnglishString.txt", mode="wt", encoding="utf8") as stream:
    #    with ThreadPoolExecutor() as executor:
    #        items = range(-999999999, 1000000000)
    #        #items = range(0,10)
    #        results = executor.map(worker,items, (t for _ in items))
    #        for value, string in results:
    #            stream.write(f"{value}:{string}\n")

    with open("IntTOEnglishString.txt", mode="wt", encoding="utf8") as stream:
        items = range(-999999999, 1000000000)
        #items = range(0,10)
        for item in items:
            value, string = worker(item, t)
            stream.write(f"{value}:{string}\n")


if __name__ == "__main__":
    main()

