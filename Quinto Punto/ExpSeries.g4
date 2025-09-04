grammar ExpSeries;

prog: 'exp' '(' x=NUMBER ',' n=NUMBER ')' EOF ;

NUMBER: [0-9]+ ('.' [0-9]+)? ;
WS: [ \t\r\n]+ -> skip ;
