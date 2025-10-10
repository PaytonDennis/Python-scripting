def tests ():
    "variable"
    name = "bill"

    "number"
    Int = 2
    float = 2.6

    text: str = "Hello World"
    list = [1, 2, 3]
    tuple = (1, 2, 3), "duplicates, not mutable"

    set = {1, 2, 3}, "no dublicates, mutable"
    dict = {1: "one", 2: "two", 3: "three"};
    "key value pairs"
    return name,int,float,str,list,tuple,set,dict

print(*tests(), sep="\n")