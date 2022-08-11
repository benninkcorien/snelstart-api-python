import http.client, urllib.request, urllib.parse, urllib.error, base64

# download alle relaties, en sla die op in een JSON bestand

# Let op! Bearer is 1 uur geldig!
SNELSTART_BEARER_ACCESS_KEY = "BEARER_KEY"

SNELSTART_PRIMARY_API_KEY = "PRIMARY_API_KEY"

headers = {
    "Ocp-Apim-Subscription-Key": SNELSTART_PRIMARY_API_KEY,
    "Authorization": "Bearer" + " " + SNELSTART_BEARER_ACCESS_KEY,
}


try:
    conn = http.client.HTTPSConnection("b2bapi.snelstart.nl")
    conn.request("GET", "/v2/relaties/", "", headers)
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    with open("relaties.json", "w", encoding="utf-8") as file:
        file.write(data)
    conn.close()
except Exception as e:
    print(e)
