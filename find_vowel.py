abc='Shefali love HimAni'
v=0
ch=0
word=len(abc.split())
# for i in abc:
#     if(i=='a'or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#         v=v+1
#     else:
#         ch=ch+1
# print("vowles",v)
# print("charachter",ch)

vowel=['a','e','i','o','u','A','E','I','O','U']
for i in abc:
    if i in vowel:
        v+=1
    ch+=1
print(f'The Number of Vowel is {v}')
print(f'The Number of character is {ch}')
print(f'The Number of word is {word}')