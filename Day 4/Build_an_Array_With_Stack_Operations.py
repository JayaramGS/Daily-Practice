import json
input_string = str(input())
test_string = ''
for element in input_string[:-2]:
    if element.isdigit() == True:
        test_string += element
test_list = list(test_string)
test_list2 = []
identity = 0
for number in test_list:
    difference = int(number) - identity - 1
    if difference:
        test_list2 += ["Push","Pop"] * difference
    test_list2 += ["Push"]
    identity = int(number)
dump_list = json.dumps(test_list2)
output_list = dump_list.replace(", ",",")
print(output_list)