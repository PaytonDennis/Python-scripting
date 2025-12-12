def tests ():
    "variable"
    name = "bill"

    "number"
    Int = 2
    float = 2.6

    text: str = "Hello World"
    list = [1, 2, 3]
    tuple = (1, 1, 1), "duplicates, not mutable"

    set = {1, 2, 3}, "no dublicates, mutable"
    dict = {1: "one", 2: "two", 3: "three"}
    "key value pairs"
    return name,int,float,str,list,tuple,set,dict

print(*tests(), sep="\n")

#ternary
i = 7
print("i should be greater than 5" if i > 5 else "i should be less than 5")