

from beautifultable import BeautifulTable
import random
from annealing_class import annealing
obj=annealing()

ip = []
output = []
expected_output = []

for i in range(0,100):
    ip.append(int(random.randint(0,100)))

#print("Random input generated: " +str(ip))
expected_output = obj.expOpgenerator(ip)
#print("The Expected values: "+str(expected_output))
output = obj.annealing(ip, expected_output)
#print("The annealing values: "+str(output))
count = 0
for i in range(0, 100):
    if expected_output[i] == output[i]:
        count += 1
print("Number of values match: "+str(count))
table = BeautifulTable()
table.column_headers = ["Input ", "Expected output", "Output"]
print("------------")
for row in zip(ip, expected_output, output):
    table.append_row([row[0], row[1], row[2]])
print(table)




