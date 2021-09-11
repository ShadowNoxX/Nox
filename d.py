import requests

id_ = "Sr3U2Eov"
url = f"https://lockee.fr/ajax-open.php?id={id_}&code=2366"

headers = {
    "referer": f"https://lockee.fr/{id_}",
    "x-requested-with": "XMLHttpRequest"
}

response = requests.get(url, headers=headers).json()
print(response)