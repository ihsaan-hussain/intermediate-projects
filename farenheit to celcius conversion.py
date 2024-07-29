def conversion(celsius):
    farenheit = celsius * (9/5) + 32
    return farenheit

temperatures = [31, 28, 13, 14, 12]

print(list(map(conversion, temperatures)))