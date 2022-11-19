class RomanNumbers:
# Function to convert integer to roman number values

    def to_roman(number):

        base_num = [1, 4, 5, 9, 10, 40, 50, 90,
            100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
            "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        while number:
            f_div = number // base_num[i]
            number %= base_num[i]
            while f_div:
                print(str(sym[i], end = ""))
                f_div -= 1
            i -= 1

 # Function to convert integer to roman number values
 
    def from_roman(number:str)-> int:
        roman_dict=  {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        adding = 0
        for i in range(len(number)-1,-1,-1): 

            num = roman_dict[number[i]]
            if 3*num < adding:

                adding -= num
            else:
                adding += num
            return adding
