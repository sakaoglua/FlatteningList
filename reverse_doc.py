liste=[[1, 2], [3, 4], [5, 6, 7]]
liste.reverse()
i=0
while i<len(liste):
        a=liste[i]
        a.reverse()
        liste.pop(i)
        liste.insert(i,a)
        i=i+1
print(liste)
