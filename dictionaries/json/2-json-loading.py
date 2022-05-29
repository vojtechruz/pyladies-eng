# We need to import module 'json'
import json

json_cat = """ 
{
    "name": "Whiskers",
    "favoriteFood": "CatFood Premium Deluxe",
    "weight": 11,
    "race": "Who knows?",
    "color": "black and white"
}
"""

cat = json.loads(json_cat)
cat['hasFleas'] = True
print(cat)

