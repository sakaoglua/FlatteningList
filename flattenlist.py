liste=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
i=0
while i<len(liste):
    if type(liste[i])==list:
        a=liste[i]
        liste.pop(i)
        j=0
        while j<len(a):
            liste.insert(i+j,a[j])
            j=j+1
    else: i=i+1
print(liste)
