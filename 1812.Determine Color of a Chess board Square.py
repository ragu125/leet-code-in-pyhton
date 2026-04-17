class Solution(object):
    def squareIsWhite(self, coordinates):
        row=ord(coordinates[0])-ord("a")+1
        col=int(coordinates[1])

        if(row+col)%2==0:
            return False
        else:
            return True

       
