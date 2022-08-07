def fizz(number):

    for fi in range(0, number):
        fi += 1
        print(fi)

        if fi / 2 == 0:
            print(fi.replace(fi, 'fizz'))

print(fizz(25))
