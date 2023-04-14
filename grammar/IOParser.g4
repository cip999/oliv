parser grammar IOParser;

options { tokenVocab=IOLexer; }

sequence : unit ( unit )* ;

unit
    : NL
    | literal
    | block ( UNDERSCORE repeat )? ( COLUMN LBRACE attributes RBRACE )?
    ;

block
    : IDENT
    | LBRACE sequence RBRACE
    ;

attributes : attribute ( COMMA attribute )* ;
attribute
    : SORTED ( LPAREN ( ASC | DESC | STRICT )+ RPAREN )?
    | DISTINCT
    | GRAPH LPAREN ( NODES ASSIGN interval | EDGES ASSIGN edge | CONNECTED | TREE | LINE | BIPARTITE | DAG )+ RPAREN
    | comparison
    ;

edge : reference ( MINUS MINUS | ARROW ) reference ;

comparison : COMP_OP arithExpr ;

repeat : LBRACE ( arithExpr | interval ) RBRACE ;
interval : arithExpr DOTS arithExpr ;

arithExpr
    : addend
    | arithExpr ( PLUS | MINUS ) addend
    ;

addend
    : term
    | addend ( MULT | DIV | MOD ) term
    ;

term
    : reference
    | INT
    | LPAREN arithExpr RPAREN
    ;

reference : IDENT ( LBRACK arithExpr RBRACK )* ;

literal
    : INT
    | STR
    ;