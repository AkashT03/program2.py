def generate_series(a):
    if a < 1 :
        return "input value must be greater than or equal to 1. "
    series =[]
    for i in range(1,a*2,2):
        series.append(str(i))
    return ",".join(series)
a= int(input("ENTER THE VALUE OF A :"))
series = generate_series(a)
print("Output" ,series)
