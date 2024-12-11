import math
from datetime import datetime

student_name = '李元盛'
file_name = '113360132'

fname = f"{file_name}.txt"
fp = open(fname, "w", encoding = "utf-8")

for i in range(1, 21):
    factorial_result = math.factorial(i)
    fp.write(f"{i}! = {factorial_result}\n")

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
fp.write(f"{student_name} {current_datetime}\n")

fp.close()

print(f"File {fname} has been saved suuccessfully") 
