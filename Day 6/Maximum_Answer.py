qstns_diff = input().split()
diff_qstn = input().split()

qstn_no = int(qstns_diff[0])
diff_lvl = int(qstns_diff[1])

each_diff = [int(diff) for diff in diff_qstn]

max_lvl = 0
solv_qstn = 0

for qstn in each_diff:
    if(qstn > diff_lvl and max_lvl != 2):
        max_lvl += 1
    elif(qstn <= diff_lvl and max_lvl != 2):
        solv_qstn += 1
    elif(max_lvl == 2):
        break
print(solv_qstn)