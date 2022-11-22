class RomanNumbers:
# This function can convert any integer into its roman number, range of int : [0, +inf[

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

 # Function to convert integer to roman number values, range of possible int output : [0, 3999]
 
    def roman_to_int(s):

     rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
     int_val = 0

     for i in range(len(s)):

         if i > 0 and rom_dict[s[i]] > rom_dict[s[i - 1]]:

            int_val += rom_dict[s[i]] - 2 * rom_dict[s[i - 1]]
         else:
            int_val += rom_dict[s[i]]
            return int_val