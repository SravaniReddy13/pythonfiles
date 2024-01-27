def occurance(string,char):
    i=0
    count=0
    while i<len(string):
        if string[i]==char:
            count+=1
        i+=1
    print(count)
occurance('sravani reddy','d')