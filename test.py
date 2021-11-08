def countdown(i):
    if i <= 0:
        return 0
    else:
        print(i)
        countdown(i - 1)

# recursive countdown test 
countdown(5)