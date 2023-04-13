lexer grammar IOLexer;

SORTED : 'sorted' ;
ASC : 'asc' ;
DESC : 'desc' ;
STRICT : 'strict' ;
DISTINCT : 'distinct' ;
GRAPH : 'graph' ;
TREE : 'tree' ;
NODES : 'nodes' ;
EDGES : 'edges' ;
CONNECTED : 'connected' ;
LINE : 'line' ;
BIPARTITE : 'bipartite' ;
DAG : 'dag' ;

// Identifier (note that it cannot contain underscores).
IDENT : [a-zA-Z][a-zA-Z0-9]* ;

ARROW : '->' ;

// Boolean binary operators.
BOOL_BIN_OP
    : AND
    | OR
    ;

NOT : '~' ;
AND : '&' ;
OR : '|' ;

// Comparison operators.
COMP_OP
    : EQ
    | NOT_EQ
    | LT
    | LTE
    | GT
    | GTE
    ;

EQ : '==' ;
NOT_EQ : '!=' ;
LT : '<' ;
LTE : '<=' ;
GT : '>' ;
GTE : '>=' ;

// Arithmetic operators.
PLUS : '+' ;
MINUS : '-' ;
MULT : '*' ;
DIV : '/' ;
MOD : '%' ;

ASSIGN : '=' ;

// Integer literal (no leading zeros).
INT : '-'? ( '0' | '1'..'9' ( '0'..'9' )* ) ;

// String literal.
STR : '"' ~[\r\n]*? '"' ;

// Parentheses.
LPAREN : '(' ;
RPAREN : ')' ;
LBRACK : '[' ;
RBRACK : ']' ;
LBRACE : '{' ;
RBRACE : '}' ;

COMMA : ',' ;
COLUMN: ':' ;
UNDERSCORE : '_' ;
DOTS : '..' ;

NL : '\\n' ;
WS : [ \t\r\n] -> skip ;

INLINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;