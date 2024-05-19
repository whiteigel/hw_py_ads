start_num = int(input("Enter a number to start with: "))
end_num = int(input("Enter a number to end with: "))

even_list = []
while start_num <= end_num:
    if start_num % 2 == 0:
        even_list.append(start_num)
    start_num += 1
print(even_list)

counter = 0
while counter < len(even_list):
    even_list[counter] = even_list[counter] ** 2
    counter += 1
print(even_list)