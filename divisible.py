lst= [45,22,14,65,97,72,90,33]
for i in range(0,len(lst)):
    if (lst[i]%3==0 and lst[i]%5==0):
        lst[i]='pppqqq'
    elif(lst[i]%3==0):
        lst[i]='ppp'
    elif(lst[i]%5==0):
       lst[i]='qqq'
    else:
        continue
print(lst)
    
        