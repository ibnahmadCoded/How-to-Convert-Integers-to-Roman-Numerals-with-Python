def int_to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX",
           "V", "IV", "I"]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num




print("2661 = ",int_to_roman(2661))
print("3789 = ",int_to_roman(3789))
print("379 = ",int_to_roman(379))
print("67 = ",int_to_roman(67))
print("39 = ",int_to_roman(39))
print("1 = ",int_to_roman(1))

    
