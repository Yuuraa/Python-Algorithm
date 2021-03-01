# A function that converts roman numeral to integer
def roman_to_integer(s):
    rom_int_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_symbol = s[-1]
    int_val = 0

    for roman_symbol in s[::-1]:
        curr_int = rom_int_dict[roman_symbol]
        if roman_symbol != prev_symbol:
            if curr_int < rom_int_dict[prev_symbol]:
                curr_int = -curr_int
        int_val += curr_int
        prev_symbol = roman_symbol
        
    return int_val

if __name__ == "__main__":
    assert(roman_to_integer("LVIII") == 58)
    assert(roman_to_integer("MCMXCIV") == 1994)
    print("All examples passed!")
