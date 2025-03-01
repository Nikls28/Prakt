def convert(n, p):
    if n < p:
        return str(n)
    else:
        return convert(n // p, p) + str(n % p)
