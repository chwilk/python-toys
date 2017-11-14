#! /usr/bin/env python
import os
import sys

myrange = 5

def lensort(x,y):
    c=cmp(len(x),len(y))
    if c != 0:
        return(c)
    else:
        return(cmp(x,y))

def divide(req, jumb, limit):
    """Recursive function to search for substrings in dictionary"""
    words=[]
    if len(jumb) > limit:
	for i in range(0,len(jumb)):
            words.extend(divide(req, jumb[:i]+jumb[i+1:], limit))
    key = ''.join(sorted(jumb+req))
    if alpha.has_key(key):
        words.extend(alpha[key])
    return(sorted(list(set(words)),lensort))
    


if __name__ == "__main__":
    alpha=dict()
    wordlist=os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'TWL06.db')
    #wordlist="/usr/share/dict/words"
    with open(wordlist, 'r') as dict:
        for word in dict:
	    word=word.rstrip().lower()
            if word.islower():
                key=''.join(sorted(word))
                if alpha.has_key(key):
                    alpha[key].append(word)
                else:
                    alpha[key]=[word]
    print "Read {} words\n".format(len(alpha))
    print "Type 'q' to exit. Use a space to separate must-have letters\n"
    jumb=''
    while(jumb != 'q'):
        try:
            jumb = str(raw_input("Jumbl3> ")).rstrip()
            """Handle a space"""
            jumbs = jumb.split()
            if len(jumbs) > 1:
                req = jumbs[0]
                jumb = jumbs[1]
                limit = max(0, len(jumb)-myrange)
            else:
                req = ""
                limit = max(3, len(jumb)-myrange)
            for i in divide(req, ''.join(sorted(jumb)), limit):
                print i
        except KeyboardInterrupt:
            print "Exiting"
            break
        except EOFError:
            break
