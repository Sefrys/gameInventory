# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
import csv
from collections import OrderedDict
from operator import itemgetter

# Displays the inventory.
def display_inventory(inventory):

    count = 0
    for key, value in inventory.items():
        count = count + value
        print(value, key)
    print("Total number of items: " + str(count) + "\n")


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):

    counter = 0
    for x in added_items:
        if x in inventory:
            inventory[x] += 1
        else:
            inventory[x] = 1
    return inventory


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):

    count = 0
    print("\n" + "Inventory: ")
    print("{0:>4} {1:>12}".format("count", "item name"))
    print("-"*17)
    if order == "desc":
        for key, value in sorted(inventory.items(), key=itemgetter(1), reverse=True):
            print("{0:>4} {1:>12}".format(value, key))
            count = count + value

    elif order == "asc":
        for key, value in sorted(inventory.items(), key=itemgetter(1), reverse=False):
            print("{0:>4} {1:>12}".format(value, key))
            count = count + value

    else:
        for key, value in inventory.items():
            print("{0:>4} {1:>12}".format(value, key))
            count = count + value

    print("-"*17)
    print("Total number of items: " + str(count))



# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    added_items = list(csv.reader(open(filename, 'r')))
    added_items = added_items[0]
    add_to_inventory(inventory, added_items)
    return(added_items)



# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    exported_file = open(filename, 'w')
    exported_string = ''
    for key in inventory:
        exported_string += ((key + ',') * inventory[key]) + ','
        exported_string = exported_string[:len(exported_string)- 1]
    exported_string = exported_string[:len(exported_string) - 1]
    exported_file.write(exported_string)
    exported_file.close()


# Main function sets initial variables and stores rest of the functions
def main():
    inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    display_inventory(inventory)

    inventory = add_to_inventory(inventory, dragon_loot)
    display_inventory(inventory)

    print_table(inventory, "desc")

    imported_items = import_inventory(inventory, "inventory_import.csv")

    inventory = add_to_inventory(inventory, imported_items)

    print_table(inventory, "desc")
    export_inventory(inventory)

main()
