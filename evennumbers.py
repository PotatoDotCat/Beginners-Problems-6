def getEven(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even
integers = []
for i in range(0,5):
    ans = int(input("Enter number: "))
    integers.append(ans)
print("Even numbers in the list:", getEven(integers))
