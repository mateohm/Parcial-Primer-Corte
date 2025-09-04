%{
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int yylex(void);
void yyerror(const char *s);
%}

%union {
    double num;
}

%token <num> NUM
%token CBRT

%type <num> expr

%%

input:
      /* vacío */
    | input line
    ;

line:
      '\n'
    | expr '\n'   { printf("Resultado: %lf\n", $1); }
    ;

expr:
      NUM              { $$ = $1; }
    | CBRT '(' expr ')' { $$ = cbrt($3); }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
