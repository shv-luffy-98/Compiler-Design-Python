terminals =  [ 'type',
  'id',
  '(',
  ')',
  'begin',
  'return',
  ';',
  'end',
  '\'\'',
  ',',
  'operator',
  'number',
  'while',
  'relop',
  '+' ]
nonTerminals =  [ 'Start',
  'Functions',
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
[["type","id","(",")","begin","Body","return","id",";","end"],"","","","","","","","sync","","","","","","" ]
,
[["Declarations","Body"],["Es","Body"],"","","",["''"],"",["''"],"","","",["Es","Body"],["Loops","Body"],"",["Es","Body"] ]
,
[["type","List",";"],"sync","","","","sync","","sync","","","","sync","sync","","sync" ]
,
["",["AID","I'"],"","","","","sync","","","","","","","","" ]
,
["","","","","","",["''"],"","",[",","AID","I'"],"","","","","" ]
,
["",["id","AID'"],"","","","","sync","","","sync","","","","","" ]
,
["","","","","","",["''"],"","",["''"],["operator","number"],"","","","" ]
,
["sync","sync","","","","sync","","sync","","","","sync",["while","(","E",")","begin","Body","end","while"],"","sync" ]
,
["sync",["E",";"],"","","","sync","","sync","","","",["E",";"],"sync","",["E",";"] ]
,
["",["X","E'"],"","sync","","","sync","","","","",["X","E'"],"","",["X","E'"] ]
,
["","","",["''"],"","",["''"],"","","",["Op","X","E'"],"","",["Op","X","E'"],"" ]
,
["","sync","","","","","","","","",["operator"],"sync","",["relop"],"sync" ]
,
["",["id"],"","sync","","","sync","","","","sync",["number"],"","sync",["+","+","id"] ]
]