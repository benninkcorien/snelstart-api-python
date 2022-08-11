import json
import sqlite3
import pandas as pd

# pd.set_option("display.max_columns", None)


def get_landcode(land_id):
    landcode = landcodes.query(f"id=='{land_id}'")["landcode"]
    result = landcode.iloc[0]
    return result


# run get-relaties.py  om relaties.json te krijgen
with open("relaties.json", "r") as f:
    data = json.load(f)

df3 = pd.json_normalize(data)

# print alle column namen
# print(df3.columns)

# alleen houden wat je nodig hebt
df3 = df3[
    [
        "relatiecode",
        "naam",
        "email",
        "vestigingsAdres.straat",
        "vestigingsAdres.postcode",
        "vestigingsAdres.plaats",
        "vestigingsAdres.land.id",
    ]
]

landcodes = pd.read_json("landen.json")

for index, row in df3.iterrows():
    landid = df3.loc[index, "vestigingsAdres.land.id"]
    # print(landid)
    # print(get_landcode(landid))1
    df3.loc[index, "landcode"] = get_landcode(landid)

# alleen houden wat je nodig hebt
df3 = df3[
    [
        "relatiecode",
        "naam",
        "email",
        "vestigingsAdres.straat",
        "vestigingsAdres.postcode",
        "vestigingsAdres.plaats",
        "landcode",
    ]
]
# en alles een leesbare naam geven
df = df3.rename(
    columns={
        "vestigingsAdres.straat": "straat",
        "vestigingsAdres.postcode": "postcode",
        "vestigingsAdres.plaats": "plaats",
    }
)

# als je in de console wilt zien hoe dit eruit ziet:
# print(df.head())

# Dit zijn de overgebleven Column Names :
# relatiecode, naam, email, straat, postcode, plaats, landcode

# Stop alles in een klanten.sqlite database

connection = sqlite3.connect("klanten.sqlite")
cursor = connection.cursor()

df.to_sql("klanten", connection, if_exists="replace", index=False)

connection.commit()
connection.close()
