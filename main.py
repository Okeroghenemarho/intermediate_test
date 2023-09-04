# A fibonacci sequence uses the first two numbers to calculate consecutive numbers in the sequence
first_num = int(input("Enter the first number you would like in the Fibonacci series "))
second_num = int(input("Enter the second number you would like in the Fibonacci series "))
number_of_terms = int(input("How many terms would you like in this series?"))


fibonacci_series = [first_num, second_num]
series_sum = sum(fibonacci_series)

for num in range(2, number_of_terms):
    new_term = fibonacci_series[num-1] + fibonacci_series[num-2]
    fibonacci_series.append(new_term)
    series_sum += new_term

print(fibonacci_series)
