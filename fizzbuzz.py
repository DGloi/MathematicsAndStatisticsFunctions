def fizzbuzz(n) :

    print(*map(lambda i : 'Fizz'*(not i%3) + 'Buzz'*(not i%5) + "Bazz"*(not i%7) or i, range(1,n)),sep='\n')