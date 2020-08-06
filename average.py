num = int(input("Enter How Many Number you want:"))
total_sum = 0

for i in range(num):
    input = (input("Enter The Number:"))
    total_sum += input
    ans = total_sum/num

line = f"Total Average of {total_sum}is{ans}"
print(line)




