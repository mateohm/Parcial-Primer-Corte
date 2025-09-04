%{
#include "calc.tab.h"
#include <stdio.h>
%}

%%
[0-9]+(\.[0-9]+)?    { yylval.num = atof(yytext); return NUM; }
"cbrt"               { return CBRT; }
\n                   { return '\n'; }
[ \t]                ;   // ignorar espacios y tabs
.                    { return yytext[0]; }
%%

int yywrap() { return 1; }
