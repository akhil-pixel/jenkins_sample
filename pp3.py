#i am loving python bcoz of jenkins
def prime(n):
    count = 0:
    for i in range (2,n):
        if n % i == 0:
            count = count + i
        if count == 0:
            return (True)
        else:
            return (false)


a=prime(7)
print(a)