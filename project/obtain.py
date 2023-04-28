
def go ():
    import random
    ans={}
    set=['a','b']
    random.randint(0,1)

    for i in range(1,72):
        v = random.randint(0, 1)
        #ans[i-1]=set[v]

        ans[i - 1] = 'b'

    print('ans=',ans)

    return ans






