#!/usr/bin/env python

# ---- Kelvins to Celsius and Fahrenheit converter ----
kelvins = [100, 253, 273, 283, 295]


def kelv_to_celc(degrees):
    celc = degrees - 273.15
    return round(celc, 1)


def kelv_to_fahr(degrees):
    fahr = degrees * 9/5 - 459.67
    return round(fahr, 1)

print 'Celsius    :', map(kelv_to_celc, kelvins)
print 'Fahrenheits:', map(kelv_to_fahr, kelvins)
# > Celsius    : [-173.1, -20.1, -0.1, 9.9, 21.9]
# > Fahrenheits: [-279.7, -4.7, 31.3, 49.3, 71.3]


# ---- Filtering ----

print filter(lambda x: x % 2, range(0, 10))
print filter(lambda x: x % 2 == 0, range(0, 10))
# > [1, 3, 5, 7, 9]
# > [0, 2, 4, 6, 8]


# ---- Reducing a List ----
print reduce(lambda x, y: x + y, range(1, 11))
# > 55

print reduce(lambda x, y: x * y, range(1, 11))
# > 3628800

i = [47, 11, 42, 102, 13]
print reduce(
    lambda a, b: a if (a > b) else b,
    i
)
# > 102
