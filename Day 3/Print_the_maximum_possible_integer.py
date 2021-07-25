def sumofdigits(N):
    int_to_string = str(N)
    test_list = list(map(int, int_to_string.strip()))
    return (sum(test_list))
    
N = int(input())
sum_of_digits = sumofdigits(N)
for num in range(N-1, 10, -1):
    if(sumofdigits(num) > sum_of_digits):
        print(num)
        break
    else:
        if(num == 11):
            print(N)
            break
    