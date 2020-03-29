# N-Queens Class

class nQueenBoard:
    
    def __init__(self, n):
        
        # board is n x n
        self.n = n
        # for maintaining the placed queens
        self.col = []
        
    def QueensCount(self):
        x=len(self.col)
        return x
 
    def getSize(self):
        return self.n
 
    def MoveToNextRow(self, column):
        self.col.append(column)
 
    def RemoveFromCurrentRow(self):
        return self.col.pop()
 
    def isSafe(self, column):
 
        # check column
        for qCol in self.col:
            if(column == qCol):
                return False
            
        # index of next row
        row =self.QueensCount()
        
        # check diagonal
        for qRow, qCol in enumerate(self.col):
            
            if(qCol-qRow == column-row):
                
                return False
 
        # check other diagonal
        for queen_row, queen_column in enumerate(self.col):
            
            if((self.n-queen_column)-queen_row==(self.n-column)-row):
                
                return False
 
        return True
 
    def display(self):
        
        #to display the the board in the form of nxn matrix
        
        for i in range(self.n):
            
            for j in range(self.n):
                
                if j != self.col[i]:
                    print('0', end=' ')   
                else:
                    print('X', end=' ')
                    
            print("\n")
 