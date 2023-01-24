#[“name512”, “same1example”, “joy18full”] replace the digits from string inside list

vals= ["name512","same1example", "joy18full"]

valsnew=["".join(filter(lambda char: char.isalpha(),word)) for word in vals]

print(valsnew)