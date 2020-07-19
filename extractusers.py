#!/usr/bin/env python3

import ldap3
import json
from record import record

def findUser(user,group,conn,base,search):
    ret=conn.search(base,search,search_scope=ldap3.SUBTREE,attributes=['member'])
    entry=conn.entries[0]
    members=json.loads(entry.entry_to_json())['attributes']['member']
#    print(members)
    for member in members:
#        print(member)
        if "User" in member:
            r=record(member)
            print(r.CN)
            user.append(r.CN)

        if "Groups" in member:
            print("Recurssion")
            r=record(member)
            search='(&(objectCategory=GROUP)(cn=%s))'%r.CN
            user=findUser(user,r.CN,conn,base,search)
#            print(users,r.CN,conn,base,search)
    return user
if __name__ == "__main__":
    server=ldap3.Server('adserver.com')
	conn=ldap3.Connection(server,auto_bind=True)
    grp='ADGroupWithRecursiveGroup'
    base='dc=ad,dc='<domainname/CompanyName>",dc=com'
    search='(&(objectCategory=GROUP)(cn=%s))'%grp
    users=[]

    users=findUser(users,grp,conn,base,search)
    print(set(users))
    conn.unbind()
