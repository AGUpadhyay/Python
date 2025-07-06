def vowel(n):
    c=0
    b='aeiouAEIOU'
    for x in n:
        if x in b:
            c=c+1
    return c
Name=input("Enter your name\t")          
Result=vowel(Name)
print("Vowel is",Result)