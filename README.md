# GetUsersFromADGroups
 Recursively resolve AD groups to get users

Input - groupwithrecursivegroups
output- unique usernames after resolving all the groups in the given input.


Example:
input given :
groupwithrecursivegroups 
 -username1
 -group1
    -username2
    -username3
    -group2
 -group3
    -username4
    -username5
    -group3
      -username6
      -username7
      -group4
         -group5
           -username8
      -username9
         
 output:
 (username1,username2,username3,username4,username5,username6,username7,username8,username9)
