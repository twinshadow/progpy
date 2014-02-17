#!/usr/bin/env python2

from socket import socket, AF_UNIX, SOCK_STREAM, SOMAXCONN
from sys import argv, stdin, stdout
from stat import S_ISSOCK
from os import stat, unlink
from errno import ENOENT
from cStringIO import StringIO

def sosend(sockpath):
    s = socket(AF_UNIX, SOCK_STREAM)
    s.connect(sockpath)
    try:
        while True:
            line = stdin.readline()
            if not line.strip():
                break
            s.sendall(line)
    finally:
        s.close()


def sorecv(sockpath):
    s1 = socket(AF_UNIX, SOCK_STREAM)
    s1.bind(sockpath)
    s1.listen(SOMAXCONN)
    try:
        s2, _ = s1.accept()
    finally:
        s1.close()
    try:
        while True:
            data = s2.recv(4096)
            if not data:
                break
            stdout.write(data)
    finally:
        s2.close()


def main():
    if argv[1] == "-l":
        transmit = False
        sockpath = argv[2]
    else:
        transmit = True
        sockpath = argv[1]

    st = None
    try:
        st = stat(sockpath)
    except OSError as ex:
        if ex.errno not in (ENOENT,):
            raise

    if st and S_ISSOCK(st.st_mode):
        pass
        #unlink(sockpath)

    if transmit:
        return sosend(sockpath)

    try:
        return sorecv(sockpath)
    finally:
        unlink(sockpath)


if __name__ == "__main__":
    main()
