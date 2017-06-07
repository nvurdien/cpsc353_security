#!/usr/bin/env python
"""
This program implements a simple RBAC system

Input:
    groups [1]
        a file describing groups, where each line is in the following format:
            GROUP: (USER)+
            seperated by newlines
    acl [2]
        a file containing an acl table, each line being:
            /INSERT/DIR/HERE:
                GROUP: (USER)+
                  .       .
                  .       .
    actions [3]
        a file of actions to be authorized like:
            USER ACTION DIR


    Outputs either DENY or ACCEPT for each action, given the group and acl tables
            
"""
import sys, collections

__author__ = "Christopher Grant and Navie Vurdien"

def main():
    """
    driver function
    """
    with open(sys.argv[1],'rb') as g:
        g = parse_groups(g)

    with open(sys.argv[2],'rb') as acl:
        acl = parse_acl(acl)

    with open(sys.argv[3],'rb') as a:
        print_result(a,acl,g)

def print_result(a,acl,g):
    """
    prints out formatted string expressing the authorization result
    :param a: a file object pointing to a file of given actions 
    :param acl: dictionary of dictionaries mapped as 'dir: dict' where the 
        inside dict is mapped as 'user: group(s)' which gives permissions 
        of each group given a directory
    :param g: dictionary of lists describing group membership 
        mapped as 'user: group(s)'
    :return: N/A
    
    """
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
    """Create a defaultdict that stores the permissions each group has in a directory
    key -- directory
    values -- key = group
                values = permissions
    """
    d = collections.defaultdict(lambda: collections.defaultdict(list))
    for l in acl:
        if not l.startswith(' '):
            key = l.strip().strip(':') #key is the directory
        else:
            l = l.strip()
            if any(l):
                group, perms = clean_line(l)
                d[key][group] = perms
    return d

def parse_groups(g):
    """Create a defaultdict that stores the members in each group
    key -- group
    values -- members in group
    """
    d = collections.defaultdict(list)
    for l in g:
        l = l.strip()
        if any(l):
            group, members = clean_line(l)
            d[group] = members
    inv_d = collections.defaultdict(list)
    # invert dictionary
    for key, values in d.iteritems():
        for value in values:
            inv_d[value].append(key)
    return inv_d

def clean_line(line):
<<<<<<< HEAD
    """Splits the lines between colons and commas and strips spaces from the lines
=======
    """
    Removes colons from groups and splits each element into a list
    :param line: line of group to user, seperated with a colon 
        and delimited by commas
    :return group: string of group
    :return members: list of members
>>>>>>> origin/master
    """
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
