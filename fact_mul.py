import multiprocessing
import math
import sys 
import time

sys.set_int_max_str_digits(100000)
    
##function to computre factorials of given number
def compute_f(num):
    print(f"factorial is {num}")
    result=math.factorial(num)
    print(f"factoril of {num} is {result}")

if __name__=="__main__":
    number=[5000,6000,7000,8000]

    start_time=time.time()

    with multiprocessing.Pool() as pool:
        results=pool.map(compute_f,number)
    end_time=time.time()

    print(f"timetaken:{end_time-start_time}seconds")