stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print(f"Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
    print(f"\nTotal number of items: {str(item_total)}")

def addToInventory(inventory, addedItems):
    for loot in addedItems:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1
    return(inventory)

addToInventory(stuff, dragonLoot)
displayInventory(stuff)