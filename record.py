#!/usr/bin/env python3

class record():
    def __init__(self,string):
        self.OU=[]
        self.DC=[]
        for i in string.split(","):
            if "CN" in i:
                self.CN=i.split("=")[1]

            elif "OU" in i:
                self.OU.append(i.split("=")[1])

            elif "DC" in i:
                self.DC.append(i.split("=")[1])

if __name__ == "__main__":
    s="CN=username,OU=Users,OU=GWY,DC=ad,DC=CompanyName,DC=com"
    print(s)
    r=record(s)
    print(r.CN,r.OU,r.DC)