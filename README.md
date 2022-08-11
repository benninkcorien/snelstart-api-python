# Python scripts voor Snelstart B2B API

Python scripts waarmee je verschillende info uit de Snelstart API kan ophalen.
(en die info lokaal kan opslaan als JSON bestanden of een sqlite database etc)

# How to

Maak een maatwerk koppeling aan in je boekhouding, je krijgt dan een key. (maatwerk key)

Vul de maatwerk key in bij SNELSTART*MAATWERK_KOPPELING_KEY in \_get-bearer-key.py*

    python get-bearer-key.py
    # slaat de response van de server als lokaal json bestand op zodat je de bearer key daar uit kan halen

**Let op ! De Bearer Key is maar 1 uur geldig**

Haal je Primary Key op uit je profiel op https://b2bapi-developer.snelstart.nl/developer

De Bearer key en de Primary key heb je nodig om info uit de API te halen.

    in de scriptjes moet je die zelf nog invullen.

    SNELSTART_BEARER_ACCESS_KEY = "PLAK HELE LANGE BEARER KEY HIER (zie get-bearer-key om die makkelijk te krijgen"

    SNELSTART_PRIMARY_API_KEY = "VUL JE PRIMARY KEY VAN SNELSTART HIER IN, INLOGGEN OP API DOCUMENTATIE EN DAN STAAT HIJ ONDER PROFIEL"
