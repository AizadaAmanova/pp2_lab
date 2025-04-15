a = [19, 4, -3, 23, -83, 2, 43, 77]
min_element = a[0]
for i in a:
    if a[i]>0:
        if a[i]< a[i+1]:
            min_element == a[i]

print(min_element)