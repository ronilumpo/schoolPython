import sys
#file's each row has the form "team\twins\tties\tlosses\tscored-allowed"
#each field is separated by tabulator character
filename = sys.argv[1]
teams = []
table = []
width = 0

with open(filename) as f:
  for line in f:
    teams.append(line)
    
for team in teams:
  team = team.strip('\n')
  parts = team.split('\t')
  name = parts[0]
  games = int(parts[1]) + int(parts[2]) + int(parts[3])
  wins = parts[1]
  ties = parts[2]
  losses = parts[3]
  ratio = parts[4]
  points = 3 * int(parts[1]) + 1 * int(parts[2])
  
  subTable = []
  subTable.append(name)
  subTable.append(str(games))
  subTable.append(wins)
  subTable.append(ties)
  subTable.append(losses)
  subTable.append(ratio)
  subTable.append(str(points))
  
  table.append(subTable)

for i in range(0,len(table)):
  if len(table[i][0]) > width:
    width = len(table[i][0])

table.sort(key=lambda x: x[0])
table.sort(key=lambda x: x[5][0], reverse=True)
table.sort(key=lambda x: int(x[5][0]) - int(x[5][2]), reverse=True)
table.sort(key=lambda x: x[6], reverse=True)

for obj in table:
  print("{:<{width1}}{:>3}{:>3}{:>3}{:>3}{:>6}{:>3}".format(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6], width1=width))
  