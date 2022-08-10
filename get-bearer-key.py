import http.client, urllib.request, urllib.parse, urllib.error, base64

"""
Dit script haalt de Bearer Key op die nodig is om verbinding te maken met de Snelstart B2B API.
Maak in je boekhouding een nieuwe Koppeling met "Maatwerk" en vul die key hieronder in.

> python3 get-bearer-key.py

De Bearer key staat dan in bearerkey.json
Bearer key is 1 uur geldig (!)

"""


SNELSTART_MAATWERK_KOPPELING_KEY = "VUL HIER DE MAATWERK KOPPELING KEY IN"


headers = {"Content-Type": "application/x-www-form-urlencoded"}

print(headers.items())

body = f"grant_type=clientkey&clientkey={SNELSTART_MAATWERK_KOPPELING_KEY}"


try:
    conn = http.client.HTTPSConnection("auth.snelstart.nl")
    conn.request("POST", "/b2b/token", body, headers)
    response = conn.getresponse()
    data = response.read()
    data = data.decode("utf-8")

    with open("bearerkey.json", "w") as file:
        file.write(data)
    conn.close()
except Exception as e:
    print(e)
