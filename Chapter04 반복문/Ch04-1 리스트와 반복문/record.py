records = [90, 85, 70, 55, 95, 60, 80, 90, 85, 70, 55, 95, 60, 80, 90, 85, 70, 55, 95, 60, 80]
total = 0
for score in records:
    total += score
max_result = 0
min_result = 0
for i in range(len(records)):
    if i == 0:
        max_result = records[i]
        min_result = records[i]
    if max_result < records[i]:
        max_result = records[i]
    if min_result > records[i]:
        min_result = records[i]

print("최고값", max_result)
print("최저값", min_result) 
print("총점", total)
print("평균", total/int(len(records)))