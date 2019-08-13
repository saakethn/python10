# SET
a = {1,2,3,4,5,6}
print(a)
# print(a[0])  #Throws error

# NOTE - there is no indexing in SET, NO order There shouldnt be any duplicates in set.
a = {1,2,2,2,3,4,5,6}
print(a)      # Will not show the duplicates
a = {1,2,3,5,6}
a.add(4)
print(a)  # Added after 3 - but will not have order
a.add("a")
print(a)  #Added at last ---*****
a.remove(3)
print(a)


#SET functions
a = {1,2,3,5,6}
b = {5,6,7,8,9}

print(a.difference(b))
print(b.difference(a))   # NOTE - WE CAN SEE not printing in order.
print(a.intersection(b))
print(a.union(b))
print(a.symmetric_difference(b))