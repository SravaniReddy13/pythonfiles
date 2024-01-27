def seq_of_numbers(start,stop,step):
    out=[]
    while start<=stop :
        out+=[start]
        start+=step
    print(out)
seq_of_numbers(1,100,1)
