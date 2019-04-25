lines = []
with open("customer_ids.txt") as file:
    for line in file:
        line = line.strip()
        lines.append("'" + line + "'")

lines_length = len(lines)

count = 0
upper_limit = 499
query = ''
if lines_length < 1000:
    while(count <= (lines_length - 1)):
        query = query + ',' + lines[count]
        count = count + 1
else:
    print(lines_length % (upper_limit + 1))
    for x in lines:

        query = query + ',' + lines[count]

'''
    while (count <= lines_length):
        count_a = 0
        while (count_a <= upper_limit):
            query = query + ',' + lines[count]
            count_a = count_a + 1
            count = count + 1
        print('ended')


    while(count <= (lines_length - 1)):
        while(count <= (upper_limit - 1)):
            query = query + ',' + lines[count]
            count = count + 1
            print(query)
        print("Upper Limit Reached")
    upper_limit = upper_limit + 500
'''

