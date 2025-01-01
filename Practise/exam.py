""" # range example
for i in range(0,100):
    print(i)
    
    

# range with step
for i in range(0,50,5):
    print(i)
 """

""" flowers = ["lilly","rose","jasmine","marigold"]
f1 = []
f2 = []
f3 = []
f4 = []

for flower in flowers:
    f1.append(flowers[0])
    f2.append(flowers[1])
    f3.append(flowers[2])
    f4.append(flowers[3])
print(f1,f2,f3,f4) """

# range using step
""" for i in range(0,100,5):
    print(i) """

# dictionary --- Nested loop dictionary

biodata = {"name":"gousiya",
           "rollno":"22"}
        
education = {"education":"BSC",
             "group":"CSC"}

""" new_biodata = {"a":biodata["name"],"b":education["group"]}
print(new_biodata) """

for key,value in biodata.items():
    print(f"{key},{value}")
    