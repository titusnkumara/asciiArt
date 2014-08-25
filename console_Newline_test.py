import Console

c = Console.getconsole()

c.title("Console Example")
str="here's some\n white text on white\n background"
txt=str.split("\n")
for i in range(0,len(txt)):
    c.text(0,i,txt[i],15*16)
c.text(10, 5, "line five, column ten")
