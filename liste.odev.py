#1

list = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]
list.index("3")
print(list.index("3"))
list.index("Hi-Kod")
print(list.index("Hi-Kod"))
list.index(4.7)
print(list.index(4.7))
print(list[2:6])
print(list[4:len(list)+1])


#2
list = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]
yeni_list=[]
for eleman in list:
    if (eleman,str):
        yeni_list.append(eleman)
print(yeni_list)

#3
meyveler=["armut","ayva","elma","cilek","mandalina","muz","portakal"]
for index, meyve in enumerate(meyveler):
    print(f"Index: {index}., Değer: {meyve}")