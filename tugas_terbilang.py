# satuan
# belasan
# puluhan
# ratusan
# jutaan
# milyar

# 1 = satu -> satuan
# 17 = tujuh belas -> belasan
# 23 = dua puluh tiga -> puluhan
# 234 = dua ratus tiga puluh empat -> ratusan
# 202 = dua ratus dua
# 101 = seratus satu
# 121 = seratus dua puluh satu
# 1000 = seribu -> ribuan
# 2500 = dua ribu lima ratus
# 2345 = dua ribu tiga ratus empat puluh lima
# 999999 = ...
# 1000000 = satu juga -> jutaan 
# 1000000000 = satu milyar -> milyar

kata = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def terbilang(n):
    if n < 10:
        return kata[n]
    elif n >= 1_000_000_000:
        return terbilang(n // 1_000_000_000) + ' billion ' + (terbilang(n % 1_000_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000_000:
        return terbilang(n // 1_000_000) + ' million ' + (terbilang(n % 1_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000:
        if n // 1_000 == 1:
            return " one thousand " + (terbilang(n % 1_000) if n % 1_000 != 0 else '')
        else:
            return terbilang(n // 1_000) + " thousand " + (terbilang(n % 1_000) if n % 1_000 != 0 else '')
    elif n >= 100:
        if n // 100 == 1:
            return ' one hundred ' + (terbilang(n % 100) if n % 100 != 0 else '')
        else:
            return terbilang(n // 100) + ' hundred ' + (terbilang(n % 100) if n % 100 != 0 else '')
    elif n >= 20:
        if n//10 == 2:
            return 'twenty ' + (terbilang(n % 10) if n % 10 != 0 else ' ')
        elif n//10 == 3:
            return 'thirty ' + (terbilang(n % 10) if n % 10 != 0 else ' ')
        elif n//10 == 4:
            return 'fourty ' + (terbilang(n % 10) if n % 10 != 0 else ' ')
        elif n//10 == 5:
            return 'fifty ' + (terbilang(n % 10) if n % 10 != 0 else ' ')
        else:
            return terbilang(n//10) + 'ty ' + (terbilang(n % 10) if n % 10 != 0 else ' ')
    else:
        if n == 10:
            return ' ten'
        elif n == 11:
            return ' eleven'
        elif n == 12:
            return ' twelve'
        elif n == 13:
            return ' thirteen'
        elif n == 14:
            return ' fourteen'
        elif n == 15:
            return ' fifteen'
        else:
            return terbilang(n%10) + 'teen'

# test
import os
while True:
    os.system('cls')
    try:
        n = int(input('Number ? '))
        print(f'{n:,} = {terbilang(n)}')
    except:
        print('numbers only pls? ')
    os.system('pause')