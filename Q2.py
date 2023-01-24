# [1, “a”, 2, “b”, 3, “c”] filter digits and alphabets separately using inbuilt functions like map, filter or reduce

data = [1,"a",2,"b",3,"c"]

chars =list(filter(lambda char: str(char).isalpha(),data))
nums=list(filter(lambda num: str(num).isnumeric(),data))

print(chars,nums)