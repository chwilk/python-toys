#! /usr/bin/env python

import sqlite3


if __name__ == "__main__":
    conn = sqlite3.connect('TWL06.db')
    c = conn.cursor()
    c.execute("drop table if exists words")
    c.execute("create table words (hash text, word text)")
    with open('/home/cw5/src/dictionary/TWL06.txt', 'r') as wordlist:
        for word in wordlist:
	    word=word.rstrip().lower()
            tuple = (''.join(sorted(word)), word)
            #print "adding %s pointing to %s" % tuple
            c.execute("insert into words values (?, ?)", tuple)
    conn.commit()
