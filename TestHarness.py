from IntToEnglishString import IntToEnglishString
from EnglishStringToInt import EnglishStringToInt

def main():
    to_string = IntToEnglishString()
    from_string = EnglishStringToInt()

    items = range(-999999999, 1000000000)
    print(f"start test")
    for item in items:
        test_value = to_string.decode(item)
        parsed = from_string.decode(test_value)
        if item != parsed:
            print(f"item: {item} failed - testValue: {test_value}, parsed: {parsed}")
        if item % 1000000 == 0:
            print(f"processing: {item}")

    print(f"finish test")



if __name__ == "__main__":
    main()

