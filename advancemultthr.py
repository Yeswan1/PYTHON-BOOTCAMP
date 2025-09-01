


from concurrent.futures import ThreadPoolExecutor
import time

def printnum(number):
    time.sleep(3)
    return f"nmber:{number}"

numbers=[1,2,3,4,5,6,7,8,9]

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(printnum,numbers)

for result in results:
    print(result)
