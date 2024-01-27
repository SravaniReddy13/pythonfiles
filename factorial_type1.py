def factorial():
    out=1
    a=int(input('enter any value'))
    for i in range(1,a+1):
        out*=i
    print(out)
factorial()