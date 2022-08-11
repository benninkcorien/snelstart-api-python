import http.client, urllib.request, urllib.parse, urllib.error, base64

# Haalt alle landen/landcodes op vanuit Snelstart.
# Slaat landen.json op - wordt gebruikt door script dat sqlite database van alle klanten maakt
# zodat land-ID  d17c442b-0016-44da-8d1d-84ab8c63e726 wordt omgezet in 2 letter landcode NL

# Let op! Bearer is 1 uur geldig!
SNELSTART_BEARER_ACCESS_KEY = "BEARER KEY HIER"

SNELSTART_PRIMARY_API_KEY = "PRIMARY API KEY HIER"

headers = {
    "Ocp-Apim-Subscription-Key": SNELSTART_PRIMARY_API_KEY,
    "Authorization": "Bearer" + " " + SNELSTART_BEARER_ACCESS_KEY,
}

try:
    conn = http.client.HTTPSConnection("b2bapi.snelstart.nl")
    conn.request("GET", "/v2/landen/", "", headers)
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    with open("landen.json", "w", encoding="utf-8") as file:
        file.write(data)
    conn.close()
except Exception as e:
    print(e)
