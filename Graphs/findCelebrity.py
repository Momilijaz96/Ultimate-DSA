'''
    This is signature of helper function 'knows'.
    You should not implement it, or speculate about its implementation.

    def knows(int A, int B); 
    Function 'knows(A, B)' will returns "true" if the person having
    id 'A' knows the person having id 'B' in the party, "false" otherwise.
'''

def findCelebrity(n, knows):

    celeb = [i for i in range(n)]
    while(len(celeb)>1):
        a = celeb[0]
        b = celeb[1]
        
        if knows(a,b):
            celeb.pop(0)            
        else:
            celeb.pop(1) 
        
    if len(celeb)==1:
        i_m_known = 0
        i_know = 0
        for i in range(n):
            if knows(i,celeb[0]): i_m_known+=1
            if knows(celeb[0],i): i_know+=1
        if i_m_known==n-1 and i_know==0:
            return celeb[0]
        
    return -1