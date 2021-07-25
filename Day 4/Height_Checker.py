import string
students_height = str(input())
height_list = list(students_height)
sorted_list = sorted(height_list)
test_list = []
for height in range(len(sorted_list)):
        if height_list[height] != sorted_list[height]:
            test_list += height_list[height]
print(len(test_list))