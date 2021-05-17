def square_root(n):
    root = n / 2 # initial guess
    for k in range(20):
        root = (1 / 2) * (root + (n / root))
    return root


print(square_root(9))
print(square_root(4563))

