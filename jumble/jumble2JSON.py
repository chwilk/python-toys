#! /usr/bin/env python

import json

def lensort(x,y):
    c=cmp(len(x),len(y))
    if c != 0:
        return(c)
    else:
        return(cmp(x,y))

def divide(jumb):
    """Recursive function to search for substrings in dictionary"""
    words=[]
    if len(jumb) > 3:
	for i in range(0,len(jumb)):
            words.extend(divide(jumb[:i]+jumb[i+1:]))
    if alpha.has_key(jumb):
        words.extend(alpha[jumb])
    return(sorted(list(set(words)),lensort))
    


if __name__ == "__main__":
    alpha=dict()
    with open('TWL.json', 'r') as dict:
        alpha = json.load(dict)
    print "Type 'q' to exit\n"
    jumb=''
    while(jumb != 'q'):
        try:
            jumb = str(raw_input("Jumble> ")).rstrip()
            for i in divide(''.join(sorted(jumb))):
                print i
        except KeyboardInterrupt:
            print "Exiting"
            break
        except EOFError:
            break
