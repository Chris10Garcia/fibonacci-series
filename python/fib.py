

# fib sequence
'''
0 1 1 2 3 5 8 + 13
  + + + + + + + 
0 1 2 3 4 5 6   7
  
n n-1 = nth position 

[ 0, 1 ]

2   1     0


n = n_1 + n_0



'''


def main(n):
    fib = [0, 1]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # since the array covers the 0, and 1nth elements, anything past that needs to take into consideraiton
    n = n - 1
    for i in range(1, n + 1):
        value = fib[i] + fib[i-1]
        fib.append(value)
    return value



if __name__ == "__main__":
    
    test_values = [
        0,
        10,
        1,
        7,
        14
    ]

    test_answers = [
        0,
        55,
        1,
        13,
        377
    ]
    
    for value, answer in zip(test_values, test_answers):
        result = main(value)

        assert result == answer, f"Test for {value} failed, expected {answer}, got {result}"
        print(f"Successful result for {value}")
    
    