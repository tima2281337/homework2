import math
import struct 
def to_base_r(n, r, precision=8):
    if n == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Перевод целой части
    integer_part = int(n)
    result = ""
    while integer_part > 0:
        remainder = integer_part % r
        result = digits[remainder] + result
        integer_part //= r

    # Перевод дробной части
    if n - int(n) > 0:
        result += "."
        fractional_part = n - int(n)
        for i in range(precision):
            fractional_part *= r
            remainder = int(fractional_part)
            result += digits[remainder]
            fractional_part -= remainder

    return result

def from_baser(s, r=4):
    iop = float(s)
    packed_32 = struct.pack('!f', iop)
    hex_32 = ''.join(f'{byte:02X}' for byte in packed_32)
    return hex_32
def frombase_r(s, r=6):
    iop = float(s)
    packed_64 = struct.pack('!d', iop)
    hex_64 = ''.join(f'{byte:02X}' for byte in packed_64)
    return hex_64
def from_base_r(s, r):
    parts = s.split(".")

    # Перевод целой части
    integer_part = 0
    for i, digit in enumerate(reversed(parts[0])):
        integer_part += int(digit, r) * (r ** i)

    # Перевод дробной части
    fractional_part = 0
    if len(parts) > 1:
        for i, digit in enumerate(parts[1]):
            fractional_part += int(digit, r) * (r ** (-i - 1))

    return integer_part + fractional_part

def float_to_hex8(number):
    iop = float(number)
    if number[0] == "-":
        number = number[1:]
        number = float(number)
        number = to_base_r(number, 2)
        zap = number.find(".")
        number = list(number)
        number.pop(zap)
        number.pop(0)
        number = "".join(number)
        exp = (zap - 2) + 1023
        exp = to_base_r(exp, 2)
        number = "1" + exp + number
        mantis = len(number)
        zero = '0'
        mantis = 64 - mantis
        mantis = zero * mantis
        number = number + mantis
        a = int(from_base_r(iop, 2))
        hex8 = frombase_r(iop)
        
    elif number[0] != "-":
        number = float(number)
        number = to_base_r(number, 2)
        zap = number.find(".")
        number = list(number)
        number.pop(zap)
        number.pop(0)
        number = "".join(number)
        exp = (zap - 1) + 1023
        exp = to_base_r(exp, 2)
        number = "0" + exp + number
        mantis = len(number)
        zero = '0'
        mantis = 64 - mantis
        mantis = zero * mantis
        number = number + mantis
        a = int(from_base_r(number, 2))
        hex8 = frombase_r(iop)
        
    return hex8

def float_to_hex4(number):
    
    iop = float(number)
    if number[0] == "-":
        number = number[1:]
        number = float(number)
        number = to_base_r(number, 2)
        zap = number.find(".")
        number = list(number)
        number.pop(zap)
        number.pop(0)
        number = "".join(number)
        exp = (zap - 1) + 127
        exp = to_base_r(exp, 2)
        number = "1" + exp + number
        mantis = len(number)
        zero = '0'
        mantis = 32 - mantis
        mantis = zero * mantis
        number = number + mantis 
        hex4= from_baser(iop)
    elif number[0] != "-":
        number = float(number)
        number = to_base_r(number, 2)
        zap = number.find(".")
        number = list(number)
        number.pop(zap)
        number.pop(0)
        number = "".join(number)
        exp = (zap - 1) + 127
        exp = to_base_r(exp, 2)
        number = "0" + exp + number
        mantis = len(number)
        zero = '0'
        mantis = 32 - mantis
        mantis = zero * mantis
        number = number + mantis
        a = int(from_base_r(number, 2))
        a = to_base_r(a, 16)
        packed_32 = struct.pack('!f', iop)
        hex4= from_baser(iop)
    return hex4

def from_hex_to_float8(hex_num):
    
    f_n = hex_num[0]
    hex_num = from_base_r(hex_num, 16)
    hex_num = to_base_r(hex_num, 2)
    if len(hex_num) == 63:
        hex_num = "0" + hex_num
    mantis = ""
    mantis = str(hex_num[12:])
    mantis = mantis[:mantis.rfind("1") + 1]
    exp = hex_num[1:12]
    exp = from_base_r(exp, 2)
    exp = exp - 1023
    bin_num = "1" + mantis 
    bin_num = bin_num[:exp + 1] + "." + bin_num[exp + 1:]
    if f_n == "C":
        dec_num = -1 * from_base_r(bin_num, 2)
    else: 
         dec_num = from_base_r (bin_num, 2)
    return dec_num

def from_hex_to_float4(hex_num):
    f_n = hex_num[0]
    
    hex_num = from_base_r(hex_num, 16)
    hex_num = to_base_r(hex_num, 2)
    if len(hex_num) == 31:
        hex_num = "0" + hex_num
    mantis = ""
    
    mantis = str(hex_num[9:])
    mantis = mantis[:mantis.rfind("1") + 1]
    exp = hex_num[1:9]
    exp = from_base_r(exp, 2)
    exp = exp - 127
    bin_num = "1" + mantis 
    bin_num = bin_num[:exp + 1] + "." + bin_num[exp + 1:]
    if f_n == "C":
        dec_num = -1 * from_base_r(bin_num, 2)
    else: 
         dec_num = from_base_r (bin_num, 2)
    return dec_num

b="0.05"
print(float_to_hex4(b))
print(float_to_hex8(b))
