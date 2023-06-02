## Creating  an empty set
b = set()
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(4) # Set is a collection of non repetative elements
b.add(5)
b.add(5) # Adding a value repeatadly does not changes a set
b.add((4,5,6))  # we can insert in tuple

## Accessing Elements
# b.add({4:5})  # we cannot add list or dictionary in sets
print(b)

## Length of the set
print(len(b))  # Prints the length of this set

## Removal of an item
b.remove(5) # Removes 5 from set b
# b.remove(15) # Throws an error while trying to remove 15 (Which is not present in the set)
print(b)

  
print(b.pop()) # Removes any arbitary element from set and returns element removed
print(b)
 





















