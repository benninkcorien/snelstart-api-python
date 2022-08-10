import http.client, urllib.request, urllib.parse, urllib.error, base64

"""
>python3 get-artikelen.py 

Laat JSON output met alle artikelen uit Snelstart zien in de console.

"""

# Let op! Bearer is 1 uur geldig!
SNELSTART_BEARER_ACCESS_KEY = "PLAK HELE LANGE BEARER KEY HIER (zie get-bearer-key om die makkelijk te krijgen)"

SNELSTART_PRIMARY_API_KEY = (
    "VUL JE PRIMARY KEY VAN SNELSTART HIER IN, INLOGGEN OP API DOCUMENTATIE EN DAN STAAT HIJ ONDER PROFIEL"
)

# Bearer woord moet voor de key in de Authorization header
headers = {
    "Ocp-Apim-Subscription-Key": SNELSTART_PRIMARY_API_KEY,
    "Authorization": "Bearer" + " " + SNELSTART_BEARER_ACCESS_KEY,
}

try:
    conn = http.client.HTTPSConnection("b2bapi.snelstart.nl")
    conn.request("GET", "/v2/artikelen/", "", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
