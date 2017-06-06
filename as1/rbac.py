#!/usr/bin/python
"""
sp00ky skelet0n
"""
import sys, collections

def main():
    with open(sys.argv[1],'rb') as g:
        g = parse_groups(g)

    with open(sys.argv[2],'rb') as acl:
        acl = parse_acl(acl)

    with open(sys.argv[3],'rb') as a:
        print_result(a,acl,g)

def print_result(a,acl,g):
    for l in a:
        user, action, direc = l.split(" ")
        dir_access = acl[direc.strip()]
        for x in g[user.strip()]:
            if x in dir_access:
                if action in dir_access[x]:
                    print "ALLOW %s %s %s" %(user, action, direc)
                    break
        else:
            print "DENY %s %s %s" %(user, action, direc)

def parse_acl(acl):
    d = collections.defaultdict(lambda: collections.defaultdict(list))
    for l in acl:
        if not l.startswith(' '):
            key = l.strip().strip(':')
        else:
            l = l.strip()
            if any(l):
                group, perms = clean_line(l)
                d[key][group] = perms
    return d

def parse_groups(g):
    d = collections.defaultdict(list)
    for l in g:
        l = l.strip()
        if any(l):
            group, members = clean_line(l)
            d[group] = members
    inv_d = collections.defaultdict(list)
    for key, values in d.iteritems():
        for value in values:
            inv_d[value].append(key)
    return inv_d

def clean_line(line):
    group, members = line.split(":")
    members = members.split(",")
    members = [x.strip() for x in members]
    return group, members

def usage(script):
    print("USAGE: %s groups resources actions" % script)
    sys.exit()

if __name__=="__main__":
    if len(sys.argv) != 4:
        usage(sys.argv[0])
    main()
