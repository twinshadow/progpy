#!/usr/bin/env python2
import readline
import sqlite3
import sys

QUIT = False

def main(sqlfile):
    con = sqlite3.connect(':memory:')
    cur = con.executescript(open(sqlfile).read())

    try:
        print "Enter your SQL commands to execute in sqlite3."

        buffer = ""
        while True:
            line = raw_input('>> ')
            buffer += line
            if sqlite3.complete_statement(buffer):
                try:
                    buffer = buffer.strip()
                    cur.execute(buffer)

                    if buffer.lstrip().upper().startswith("SELECT"):
                        print "\n".join([str(f) for f in cur.fetchall()])
                except sqlite3.Error, e:
                    print "An error occurred:", e.args[0]
                buffer = ""
    finally:
        con.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("USAGE: %s SQLite_file" % sys.argv[0])
