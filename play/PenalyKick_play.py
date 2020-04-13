from random import choice
print("choice one side to shoot:\nleft center right")
you = input()
print("you kicked:" + you)
com = choice(["left", "center", "right"])
print("computer saved:" + com)
if you != com:
    print("goal!")
else:
    print("oops...")
