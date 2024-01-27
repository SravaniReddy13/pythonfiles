def filter(str):
    vowels='aeiouAEIOU'
    out=[]
    for i in vowels:
        if i in str:
            out+=i
    return out
def extract(st):
    res=[]
    for j in 'aeiouAEIOU':
        if j not in st:
            res+=j
    return res
print(extract(filter('sravani')))       
         