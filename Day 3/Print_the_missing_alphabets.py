import string
str_input = input()
miss_alp = ""
for alp in string.ascii_lowercase:
    if alp not in str_input:
        miss_alp = miss_alp + alp
test = str_input.isalpha()
if test == True:
    print(miss_alp)
else :
    miss_num = ""
    for num in "0123456789":
        if num not in str_input:
            miss_num = miss_num + num
    miss_alpnum = miss_alp + miss_num
    print(miss_alpnum)