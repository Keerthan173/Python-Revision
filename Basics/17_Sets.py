# set - collection which is unordered,unindexed.{}
# No duplicate values.
# Faster than list. 

utensils={"fork","spoon","knife","spoon"}
print(utensils)  #{'knife', 'spoon', 'fork'}
print(utensils)  #{'spoon', 'fork', 'knife'}         # Order is not guaranteed.

utensils.add("napkin")
utensils.remove("fork")

dishes={"towl","cup"}
utensils.update(dishes)     # Update a set with the union of itself and others
print(utensils)   #{'towl', 'napkin', 'knife', 'cup', 'spoon'}
utensils.clear()
dishes.clear()



setA={1,2,"abc"}
setB={1,"2","xyz"}
print(setA.union(setB))  #{1, 2, 'xyz', 'abc', '2'}
print(setA.intersection(setB))  #{1}
print(setA.difference(setB))  #{'abc', 2}
print(setB.difference(setA))  #{'xyz', '2'}
print(setB.difference(setB))  #set()
