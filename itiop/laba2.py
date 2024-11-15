
import struct

def float_to_hex(number):
    # Преобразование в 32-битное представление (четырехбайтное)
    packed_32 = struct.pack('!f', number)
    hex_32 = ''.join(f'{byte:02X}' for byte in packed_32)

    # Преобразование в 64-битное представление (восьмибайтное)
    packed_64 = struct.pack('!d', number)
    hex_64 = ''.join(f'{byte:02X}' for byte in packed_64)

    return hex_32, hex_64

# Пример использования
number = -146.836
hex_32, hex_64 = float_to_hex(number)

print(f"Число: {number}")
print(f"32-битное представление: {hex_32}")
print(f"64-битное представление: {hex_64}")
