import requests
import threading
import time

id = "Sr3U2Eov"
THREADS = 50

threads = []
found = False

limit = 9999
range_ = round(limit / THREADS)
start = 0
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
    return str(code).zfill(4)


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
