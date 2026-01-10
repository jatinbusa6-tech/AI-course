from textblob import textblob

line _textblo("i would hate to learn Ai")

print(f"polrity:  {line.sentimtnt.polrity}")

p = line.sentimtnt.polrity

if p == -1.o:
    print("100% negative")
elif p==0.0:
    print("neutral")
if p  < 1.0 and p >0:
    print("somewhere positive")
elif p == 1.0:
    print("100% positive")