#!/usr/bin/env python3

def mult_by_base(array, power):
    while power > 0:
        array.append(0)
        power -= 1
    return array

def even_pad(array):
    if len(array)%2 == 1:
        array.insert(0,0)
    return array

## Trim leading zeroes
def trim_leading_zeroes(array):
    while len(array) > 1 and array[0] == 0:  # leave last element, even if it is a zero
        array.pop(0)
    return array

## consolidate negative signs in front of positive numbers (execute borrows down)
def execute_borrows(array, base = 10):
    for i in range(len(array)-1):
        while array[i] < 0 and array[i+1] >0:
            array[i] += 1
            array[i+1] -= base
    return array


def normalize_array(array, base = 10):
    array = execute_borrows(array)
    array = trim_leading_zeroes(array)
    return array

def add(x_array, y_array, sub_factor=1, base = 10):
    # x_array.reverse()
    # y_array.reverse()
    ### Create return araray with all zeroes to simplify carry logic
    return_length = max(len(x_array), len(y_array)) + 1

    return_array = [0] * return_length

    for i in range(0,return_length-1):   # We don't have to loop over the carry byte
        if i + 1 > len(y_array):  ## x array is longer
            x = x_array[-1 -i]  ## Get ith element from the end
            z = return_array[-1 -i]  # Add in current value
            sum = z + x 
        elif i + 1 > len(x_array):   ### y array is longer
            y = y_array[-1 -i]  ## Get ith element from the end
            z = return_array[-1 -i]  # Add in current value
            sum = z + sub_factor * y
        else:
            x = x_array[-1 -i]  ## Get ith element from the end
            y = y_array[-1 -i]  ## Get ith element from the end
            z = return_array[-1 -i]  # Add in current value
            sum = z + x + sub_factor * y
        # if sum >= 0:
        return_array[-1 -i] = sum % base
        if sum < 0:
            borrow = 1
            return_array[-1 -i - 1] -=  borrow  # borrow
        else:
            return_array[-1 -i - 1] += (sum // base)  # carry
        # else:
        #     return_array[-1 -i] = -1* ((-1 * sum) % base)
        #     if i != 0:
        #         return_array[-1 -i - 1] = sum // base  # borrow

    return_array = normalize_array(return_array)
    return return_array

def sub(x_array, y_array):
    return add(x_array, y_array, sub_factor=-1)
    
def convert_string_number_to_byte_array(num_string):
    byte_array = [int(ch) for ch in num_string]
    return byte_array

def convert_byte_array_to_string_number(byte_array):
    return_string = "".join(map(str,byte_array))
    return return_string

def mult_strings(x_string, y_string):
    x = convert_string_number_to_byte_array(x_string)
    y = convert_string_number_to_byte_array(y_string)
    product = mult(x,y)
    product_string = convert_byte_array_to_string_number(product)
    return product_string

def mult(x_array, y_array, base = 10):
    return_array = []
    if len(x_array) < 1 or len(y_array) < 1:
        return None
    
    if len(x_array) == 1 and len(y_array) == 1:
        factor1 = x_array[0]
        factor2 = y_array[0]
        product = factor1 * factor2
        if product >= base:
            return_array = [product // base, product %base]
        else:
            return_array = [product % base]
  
    if len(x_array) == 1 or len(y_array) == 1:
        return_array_length = len(x_array) + len(y_array)
        return_array = [0] * return_array_length
        for i in range(0, len(x_array)):
            for j in range(0, len(y_array)):
                x = x_array[-1 - i]
                y = y_array[-1 - j]
                product = x * y
                return_array[-1 - (i + j)] += product % base
                if product >= base:
                    return_array[-1 - (i + j) - 1] += product // base
        
    
    if len(x_array) >= 2 and len(y_array) >= 2:
        x_array = even_pad(x_array)
        y_array = even_pad(y_array)
        power = len(x_array)  ## assumes no leading zeros

        x_mid = len(x_array) // 2
        y_mid = len(y_array) // 2

        x_high = x_array[:x_mid]
        x_low= x_array[x_mid:]
        y_high= y_array[:y_mid]
        y_low = y_array[y_mid:]

        ### e = (xh + xl)*(yh+yl) - a - d
        ### product = ab^2 + eb + d
        a = mult(x_high, y_high)
        d = mult(x_low, y_low)
        add1 = add(x_high, x_low)
        add2 = add(y_high,y_low)
        prod = mult(add1, add2)
        e = sub(sub(mult(add(x_high, x_low),  add(y_high,y_low)),a), d)
        return_array = add(add(mult_by_base(a,power), mult_by_base(e,power//2)), d)
    
    if return_array == []:
        print("panic")
    return normalize_array(return_array)

def main():
    product = mult_strings("3141592653589793238462643383279502884197169399375105820974944592", 
        "2718281828459045235360287471352662497757247093699959574966967627")
    print(f"product: {product}")

main()