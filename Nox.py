import requests
import threading
import time

# CONFIGURATION
id = "ReplaceMe!" # The id of the Lockee
THREADS = 50 # the number of threads
limit = 10000 # The limit of digit searching. It needs to be a multiple of the value of variable THREADS otherwise it won't be precise
            # and will take longer time
start = 0 # The start digit 0
length = 4 # The length of digit code EXAMPLE if 4: 0 -> 0000, 12 -> 0012, 310 -> 0310

# ACTUAL CODE
threads = []
found = False
range_ = round(limit / THREADS)
current = 0
headers = {
    "referer": f"https://lockee.fr/{id}",
    "x-requested-with": "XMLHttpRequest"
}
def req(start_, amount_):
    global found
    global current
    for i in range(start_, amount_):
        if found:
            quit()
        code = add(i)
        url = f"https://lockee.fr/ajax-open.php?id={id}&code={code}"
        response = requests.get(url, headers=headers).json()
        current += 1
        percentage = str(round(current/limit*100))+"%"
        if response.get("content"):
            found = True
            sec = round(time.time() - first)
            print(f"Found code \"{code}\" by trying {percentage} of possibilities and performing {current} requests in a time of {sec} s.")
            break
        print(percentage)
    



def add(code):
    code +=1
    return str(code).zfill(length)


first = time.time()

for i in range(THREADS):
    if not found:
        x = threading.Thread(target=req, args=(start, start+range_,), daemon=True)
        threads.append(x)
        #print(start, start+range_)
        start += range_
        
for t in threads:
    t.start()


for t in threads:
    t.join()
