# Dictionaries: A dictionary is a collection of key-value pairs.
# Fast because they use hashing.
# Keys must be unique and immutable (like strings, numbers, or tuples).

capitals = {
    'India': 'New Delhi', 
    'USA': 'Washington, D.C.', 
    'Japan': 'Tokyo'
}
print(capitals) # {'India': 'New Delhi', 'USA': 'Washington, D.C.', 'Japan': 'Tokyo'}

print(capitals['India']) # New Delhi
# print(capitals['Karnataka']) #ERROR: KeyError 'Karnataka'

print(capitals.get('India')) # New Delhi
print(capitals.get('Karnataka')) # None

print(capitals.keys()) # dict_keys(['India', 'USA', 'Japan'])
print(capitals.values()) # dict_values(['New Delhi', 'Washington, D.C.', 'Tokyo'])
print(capitals.items()) # dict_items([('India', 'New Delhi'), ('USA', 'Washington, D.C.'), ('Japan', 'Tokyo')])

for key,value in capitals.items():
    print(key , ":" , value)
# India : New Delhi
# USA : Washington, D.C.
# Japan : Tokyo


capitals.update({'Karnataka': 'Bengalore'}) # New
print(capitals) # {'India': 'New Delhi', 'USA': 'Washington, D.C.', 'Japan': 'Tokyo', 'Karnataka': 'Bengalore'}

capitals.update({'Karnataka': 'Bengaluru'}) # Existing
print(capitals) # {'India': 'New Delhi', 'USA': 'Washington, D.C.', 'Japan': 'Tokyo', 'Karnataka': 'Bengaluru'}

capitals.clear()
print(capitals) # {}
