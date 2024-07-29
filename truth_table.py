def binary_numbers_generator():
    # Iterate through the numbers 0 to 15
    for number in range(16):  # 16 is not included, so we get 0 to 15
        # Convert number to binary, remove the '0b' prefix, and pad with zeros to ensure 4 digits
        binary_number = format(number, '04b')
        yield binary_number  # Yield the binary number as a string

def truth_table_tester():
    for i, binary_number in enumerate(binary_numbers_generator()):
        object2 = two_s_complement(binary_number)
        output = object2.whole_network()
        if i<=9:
            print(i,' -  ',binary_number , "===> Our 2's complement network ===>",output )
        else:
            print(i,'-  ',binary_number , "===> Our 2's complement network ===>",output )


truth_table_tester()