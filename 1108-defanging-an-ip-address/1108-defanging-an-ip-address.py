class Solution:
    def defangIPaddr(self, address: str) -> str:
        '''Since characters cannot be replaced 
        from a string, converting string to 
        list with delimiter "."
        '''

        address = address.split(".")
        return "[.]".join(address)
        