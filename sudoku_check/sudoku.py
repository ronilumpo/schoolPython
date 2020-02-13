import sys
import os
from os.path import dirname, join

def checkSudoku(filename):
  illegal_rows = []
  illegal_columns = []
  illegal_subgrids = []
  
  stripped = []
  row_index = 1
  column_index = 1
  grid = []
  added = 0
  
  with open(filename) as f:
    for line in f:
     string = ''.join(i for i in line if i.isdigit())
     if len(string) != 0:
      stripped.append(string)
  f.close()
  
  ### check if row has duplicates ###
  
  #row
  for i in range(9):
    string = stripped[i]
    string = "".join(set(string))
    if len(string) != len(stripped[i]):
      illegal_rows.append(row_index)
    row_index += 1
    string = ""
    
  ### check if column has duplicates ###  
  
  #column
  for i in range(9):
    string = ""
    #row
    for j in range(9):
      string = string + stripped[j][i]
    string = "".join(set(string))
    if len(string) != 9:
      illegal_columns.append(column_index)
    column_index += 1
    
  ### check if subgrid has duplicates ### 
  
  for i in range(9):
    grid = []
    string=""
    if i < 3:
      for j in range(3):
        if (i == 0):
          for k in range(3):
            string = string + stripped[j][k]
        
        elif(i == 1):
          for k in range(3,6):
            string = string + stripped[j][k]
        elif(i == 2):
          for k in range(6,9):
            string = string + stripped[j][k]
            
      string = "".join(set(string))
      if len(string) != 9:
        grid.append(1)
        grid.append(i+1)
        illegal_subgrids.append(grid)
    
    if i > 2 and i < 6:
      for j in range(3,6):
        if (i == 3):
          for k in range(3):
            string = string + stripped[j][k]
        
        elif(i == 4):
          for k in range(3,6):
            string = string + stripped[j][k]
        elif(i == 5):
          for k in range(6,9):
            string = string + stripped[j][k]
            
      string = "".join(set(string))
      if len(string) != 9:
        grid.append(2)
        grid.append(i-2)
        illegal_subgrids.append([])
        illegal_subgrids[added] = grid
        added += 1
    
    if i > 5:
      for j in range(6,9):
        if (i == 6):
          for k in range(3):
            string = string + stripped[j][k]
        
        elif(i == 7):
          for k in range(3,6):
            string = string + stripped[j][k]
        elif(i == 8):
          for k in range(6,9):
            string = string + stripped[j][k]
            
      string = "".join(set(string))
      if len(string) != 9:
        grid.append(3)
        grid.append(i-5)
        illegal_subgrids.append([])
        illegal_subgrids[added]=grid
        added += 1
       
  
  if len(illegal_rows) != 0 or len(illegal_columns) != 0 or len(illegal_subgrids) != 0:
    print("Illegal rows: ",end="")
    print(' '.join(map(str,illegal_rows)))
    print("Illegal columns: ",end="")
    print(' '.join(map(str,illegal_columns)))
    print("Illegal subgrids: ",end="")
    print(' '.join(map(str,illegal_subgrids)))
  else:
    print("The sudoku solution is legal")

if __name__ == "__main__":
  checkSudoku("sudoku1.txt")    
  checkSudoku("sudoku2.txt")
  checkSudoku("sudoku3.txt")    