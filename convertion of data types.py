list1=[1,2.7,3,"hike",6]
tuple1=(4,7,8.1,"chat")
set1={5,7,9,"way"}
#covert list[] to tuple()
output=tuple(list1)
print(output)#output=(1, 2.7, 3, 'hike', 6)
#covert list[] to set{}
output=set(list1)
print(output)#output={1, 3, 6, 'hike', 2.7}
#covert tuple() to list[]
output=list(tuple1)
print(output)#output=[4, 7, 8.1, 'chat']
#covert tuple to set
output=set(tuple1)
print(output)#output={'chat', 8.1, 4, 7}
#covert set to list
output=set(list1)
print(output)#output={1, 3, 6, 'hike', 2.7}
#covert set to tuple
output=set(tuple1)
print(output)#output={'chat', 8.1, 4, 7}
