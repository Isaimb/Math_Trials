# Creating a hashmap using a dictionary
hashmap = {}

# Adding key-value pairs to the hashmap
hashmap['key1'] = 'value1'
hashmap['key2'] = 'value2'
hashmap['key3'] = 'value3'

# Accessing values using keys
print("Value for key 'key1':", hashmap['key1'])
print("Value for key 'key2':", hashmap['key2'])
print("Value for key 'key3':", hashmap['key3'])

# Checking if a key exists in the hashmap
key_to_check = 'key2'
if key_to_check in hashmap:
    print(f"'{key_to_check}' exists in the hashmap.")
else:
    print(f"'{key_to_check}' does not exist in the hashmap.")

# Iterating through the keys and values in the hashmap
print("Iterating through the hashmap:")
for key, value in hashmap.items():
    print(f"Key: {key}, Value: {value}")
