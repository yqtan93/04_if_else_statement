# Welcome message with condition explanation (e.g.: weight unit, max weight of item, enter 0 to terminate program)
print("""Welcome to the Package Loading System!

You'll need to enter the number of items to be shipped at the beginning.
Afterwards, pack your item by entering the weight of the item, note that the allowed range of weight is 1-10kg.

Each package would be sent off with a limit of 20kg. 

The process will be terminated when you enter an item of 0kg or the number of items has been reached.""")


# Prompt user to enter max number of items
while True:
    try:
        max_items = int(input("\nPlease enter the number of items to be shipped: "))
    except ValueError:
        print("\nInvalid input. Please enter a valid integer.")
        continue
    else:
        break

# Empty list to save individual package weight
pack_list = []

# Start a new empty package
pack = 0

# For loop: program continues before max number of packages and items weight != 0, terminate loop if item weight = 0 or when length of list > max number of packages
for i in range(max_items):

# Enter item weight (loop)
    try:
        item = float(input("\nPlease enter the weight of the item to be packed (1-10kg): ") )
    
# Error message for if input item weight not within 1-10kg range
        if item < 1 or item > 10:
            print("\nItem weight not within allowed range. Please only enter item within the range of 1-10 kg\n")
            continue

# Break the loop if item == 0
        if item == 0:
            if pack > 0:
                pack_list.append(pack)
                print(f"\nA package is shipped at {pack} kg! This is the last package.")
            else:
                print(f"\nEnding packing process.")
            break

# If item weight + package weight > 20, append current package weight to list, start a new package, and add current item to new package
        if pack + item > 20:
            pack_list.append(pack)
            print(f"\nA package is shipped at {pack} kg! Put current item in a new package.")
            pack = 0
            pack += item
            print(f"\nItem added. Current package is at {pack} kg.")
            i += 1
            

# Add item to package weight
        else:
            pack += item
            print(f"\nItem added. Current package is at {pack} kg.")

# Except ValueError if wrong value type has been entered for item weight
    except ValueError:
        print("\nInvalid input. Please enter a valid number for the weight of the item (1-10kg).")
        continue

else:
    print("\nLast item packed. Ending program...")


print(pack_list)

# Calculate unused capacity of each package
num_pack = len(pack_list)
weight_pack = sum(pack_list)
unused_cap = (num_pack * 20) - weight_pack

# Enumerate package list and apply min() function to obtain package with lowest weight, lambda function specified as key to
min_wpack_index, min_pack = min(enumerate(pack_list), key=lambda x:x[1])
most_unused = 20 - min_pack

print(f"""\nSummary:
	A total of {num_pack} packages were shipped with a total weight of {weight_pack} kg.
	A total of {unused_cap} capacity were left unused with package number {min_wpack_index + 1} with the most unused capacity of {most_unused}.""")