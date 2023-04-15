lexer grammar IOLexer;

TYPE : 'int' | 'float' | 'double' | 'string' ;

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

// Boolean operators.
NOT : '~' ;
AND : '&' ;
OR : '|' ;

// Comparison operators.
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

FLOAT : INT '.' ( '0'..'9' )+ ;

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
