from concurrent.futures import ProcessPoolExecutor
import time

def square_num(num):
    time.sleep(2)
    return f"Square:{num*num}"

numbers=[1,2,3,4,5,6,7,8,9,10,11,12]
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square_num,numbers)

    for result in results:
        print(result)