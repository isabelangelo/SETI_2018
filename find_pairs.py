import numpy as np

def find_pairs(a,b,w):
    matches = []
    i=0
    while i < len(a):
        j=i
        while j < len(a):
            #print('i=',i,'j=',j)
            if abs(a[i]-b[j]) <= w:
                #print('match found',a[i],b[j])
                matches.append((a[i],b[j]))
            if b[j] >= a[i] + w:
                #print('STOP')
                j=len(a)
            else:
                #print('continue')
                j+=1
        j=i-1
        while j >= 0:
            #print('i=',i,'j=',j)
            if abs(a[i]-b[j]) <= w:
                #print('match found',a[i],b[j])
                matches.append((a[i],b[j]))
            if b[j] <= a[i] - w:
                #print('STOP')
                j=-1
            else:
                #print('continue')
                j-=1            
        i += 1
    print(len(matches),' matches found')
    return matches

def find_triples(matches,c,w): #note: c is an array
    triples = []
    for match in matches:
        min = np.max(match) - w
        max = np.min(match) + w
        triple_idx = np.where((min<=c)&(c<=max))[0]
        for i in triple_idx:
            triples.append((match+(c[i],)))
    print(len(triples),' triples found')
    return triples
















def find_pairs2(a,b,w):
    #bug: depends on the order, see what happens for b and a
    matches = []
    for i in range(len(a)):
        for j in range(len(a)-1):
            if abs(a[i]-b[j]) <= w:
                matches.append((a[i],b[j])) #store these as variables?
            if b[j] >= a[i]+w:
                break
    return matches

def find_pairs3(a,b,w):
    #gives bug for a[1] in while loop
    matches = []
    for i in range(len(a)):
        j=0
        while b[j]<=a[i]+2:
            if abs(i-b[j]) <= w:
                 matches.append((i,b[j]))
            print(a[i],b[j])
            j+=1
    return matches
    