"""Examples of dictionary syntax with Ice Cream shop order tallies."""

# Dictionary type is dict[key_type, value_type]
# Dcitionary literals are curly brackets
# that surround with key: value pairs
ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evaluated to number of key-value pairs
print(f"{len(ice_cream)} flavors")

# add key-value entries using subscription notation
ice_cream["mint"] = 3

# access values by their key using subscription
print(ice_cream["chocolate"])

# re-assign values by their key using assignment
ice_cream["vanilla"] += 10

# remove items by key using the pop method
ice_cream.pop("strawberry")

# loop through items using for-in loops
total_orders: int = 0
# the variable (e.g. flavor) iterates over
# each key one-by-one in the dictionary.
for flavor in ice_cream:
    print(f"{flavor}: {ice_cream[flavor]}")
    total_orders += ice_cream[flavor]

print(f"Total orders: {total_orders}")
