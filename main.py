print("welcome")

score = 0

answer = input("what language we usuing? ")

if answer.lower() == "python":
    print("bravo")
    score += 1
else:
    print("wrong")

print("your score is:", score)