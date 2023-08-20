class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ''
        for s in address: 
            if s == '.': 
                res += '[.]'
            else: 
                res += s
        return res

#Exercise: https://leetcode.com/problems/defanging-an-ip-address/submissions/
#Given a valid (IPv4) IP address, return a defanged version of that IP address.
#A defanged IP address replaces every period "." with "[.]".