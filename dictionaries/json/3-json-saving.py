# We need to import module 'json'

import json


# This is Python dictionary, not JSON!
address = {
    'street': 'Ovčí hájek',
    'city': 'Hlavní Město Praha',
    'country': 'Česká Republika'
}

# Converting Dictionary to JSON string
json_string = json.dumps(address)
print('\nConverting to json with no further parameters:')
print(json_string)

# For special characters we need ensure_ascii=False
json_string_special_chars = json.dumps(address, ensure_ascii=False)
print('\nThis is json with special characters:')
print(json_string_special_chars)

# Indentation sets number of spaces eg. indent=2
json_string_special_chars_indented = json.dumps(address, ensure_ascii=False, indent=2)
print('\nThis json is also nicely formatted and indented:')
print(json_string_special_chars_indented)