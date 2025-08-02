def func(n):
    if n == 0:
        return
    print(n)
    func(n-1)
    



# Print from 1 - n.
x = int(input("Enter a number"))
func(x)
                                                                                