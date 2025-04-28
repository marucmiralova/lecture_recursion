
def recursive_nth_fibo(idx):
    posloupnost = [0,1]
    if idx == 0:
        return posloupnost[idx]
    elif idx  == 1:
        return posloupnost[idx]
    else:
        return recursive_nth_fibo(idx-1) + recursive_nth_fibo(idx-2) #vrati to finalni cislo

def main():
    n = int(5)
    seq = [recursive_nth_fibo(num) for num in range(n+1)]
    print(seq)


if __name__ == "__main__":
    main()
