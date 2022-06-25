class Solution:
    def defangIPaddr(self, address: str) -> str:
        '''
        or we could simply use replace function :/
        '''

        address = address.split(".")
        return "[.]".join(address)
        
