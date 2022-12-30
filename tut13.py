# # loops
# list1 = [["samyak", 21], ["rishi", 20], ["samik", 21], ["yash",20], ["janhvi", 80]]
# # print(list1[0])
#
# for person, age in list1:
#     print(person, age)

list2 = [1, 3, 5, 7, 9, "a", "bcd", '+', 'e']
for num in list2:
    if str(num).isnumeric() and num > 6:
        print(num)
