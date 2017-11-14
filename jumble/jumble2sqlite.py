#! /usr/bin/env python

import sqlite3

def lensort(x,y):
    c=cmp(len(x),len(y))
    if c != 0:
        return(c)
    else:
        return(cmp(x,y))

def divide(jumb, count):
    """Recursive function to search for substrings in dictionary"""
    words=[]
    c.execute("select word from words where hash=?", (jumb,))
    words.extend((w[0] for w in c.fetchall()))
    count += len(words)
    if count < 20 and len(jumb) > 3:
	for i in range(0,len(jumb)):
            words.extend(divide(jumb[:i]+jumb[i+1:],count))
    return(sorted(list(set(words)),lensort))
    


if __name__ == "__main__":
    conn = sqlite3.connect('TWL06.db')
    c = conn.cursor()
    print "Type 'q' to exit\n"
    jumb=''
    while(jumb != 'q'):
        try:
            jumb = str(raw_input("Jumble> ")).rstrip()
            divide(''.join(sorted(jumb)), 0)
        except KeyboardInterrupt:
            print "Exiting"
            break
        except EOFError:
            break
    conn.close()
