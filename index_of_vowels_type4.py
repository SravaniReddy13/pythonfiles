def vowel_index(string):
    i=0
    d=[]
    while i<len(string):
        if string[i] in 'aeiouAEIOU':
            d=d+[i]
        i+=1
    return d
print(vowel_index('sravani'))        

