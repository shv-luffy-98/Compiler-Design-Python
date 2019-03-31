def printParseTable(terminals, nonTerminals, parseTable):
  f = open("./parse/parseTable.txt", "w")
  st = ("-"*40 + "+") * (len(terminals) + 1) + "\n"
  f.write(st + "Parse Table".center(40) + "|")
  for i in terminals:
    if(i != "\'\'"):
      f.write(i.center(40))
    else:
      f.write("$".center(40))
    f.write("|")
  f.write("\n"+st+"\n")
  for i in range(len(nonTerminals)):
    f.write(nonTerminals[i].center(40) + "|")
    for j in range(len(terminals)):
        f.write(" ".join(parseTable[i][j]).center(40) + "|")
    f.write("\n\n")


terminals =  [ 'type',
  'id',
  '(',
  ')',
  'begin',
  'end',
  'return',
  ';',
  '$',
  ',',
  'operator',
  'number',
  'while',
  'relop',
  '+' ]
nonTerminals =  [ 'Start',
  'Functions',
  'Return',
  'Body',
  'Declarations',
  'List',
  'I\'',
  'AID',
  'AID\'',
  'Loops',
  'Es',
  'E',
  'E\'',
  'Op',
  'X' ]
parseTable = [
[["Functions"],"","","","","","","","sync","","","","","","" ]
,
[["type","id","(",")","begin","Body","Return","end"],"","","","","","","","sync","","","","","","" ]
,
["","","","","",["''"],["return","id",";"],"","","","","","","","" ]
,
[["Declarations","Body"],["Es","Body"],"","","",["''"],["''"],"","","","",["Es","Body"],["Loops","Body"],"",["Es","Body"] ]
,
[["type","List",";"],"sync","","","","sync","sync","","","","","sync","sync","","sync" ]
,
["",["AID","I'"],"","","","","","sync","","","","","","","" ]
,
["","","","","","","",["''"],"",[",","AID","I'"],"","","","","" ]
,
["",["id","AID'"],"","","","","","sync","","sync","","","","","" ]
,
["","","","","","","",["''"],"",["''"],["operator","number"],"","","","" ]
,
["sync","sync","","","","sync","sync","","","","","sync",["while","(","E",")","begin","Body","end","while"],"","sync" ]
,
["sync",["E",";"],"","","","sync","sync","","","","",["E",";"],"sync","",["E",";"] ]
,
["",["X","E'"],"","sync","","","","sync","","","",["X","E'"],"","",["X","E'"] ]
,
["","","",["''"],"","","",["''"],"","",["Op","X","E'"],"","",["Op","X","E'"],"" ]
,
["","sync","","","","","","","","",["operator"],"sync","",["relop"],"sync" ]
,
["",["id"],"","sync","","","","sync","","","sync",["number"],"","sync",["+","+","id"] ]
]


printParseTable(terminals, nonTerminals, parseTable)