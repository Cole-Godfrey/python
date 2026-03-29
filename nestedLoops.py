# nested loops = The inner loop will finish all of it's iterations before finishing one iteration of the outer loop

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol: ")

for i in range(rows):
    for i in range(cols):
        print(symbol, end="")
    print()
