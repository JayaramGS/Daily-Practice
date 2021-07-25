from collections import Counter

No_of_elements = int(input())
values = input().split()
To_int = [int(value) for value in values]

occurrences = Counter(To_int)

res =  [key for key in occurrences if all(occurrences[temp] >= occurrences[key] for temp in occurrences)] 

sort_res = sorted(res)

occur_once = ' '.join(map(str, sort_res))

print(occur_once)