class IntegerToRoman:
    def __init__(self, i):
        self.i = i

    def to_roman(self):
        num = self.i
        roman_numerals = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }

        result = ''
        for value in roman_numerals:
            while num >= value:
                result += roman_numerals[value]
                num -= value
        return result
number = int(input("Enter an integer (1 to 3999): "))

if 1 <= number <= 3999:
    converter = IntegerToRoman(number)
    print("Roman numeral:", converter.to_roman())
else:
    print("Please enter a number between 1 and 3999.")
