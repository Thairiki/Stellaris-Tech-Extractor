grammar stellaris;

content
    : (expr | SPACE | NL)* EOF
    ;

expr
    : keyval+
    ;

keyval
    : key ('=' | '>' | '<')* val
    ;

key
    : id_
    | attrib
    ;

val
    : id_
    | attrib
    | array
    | group
    ;

attrib
    : id_ accessor (attrib | id_)
    ;

accessor
    : '.'
    | '@'
    | ':'
    ;

array
    : '{' array_elements? '}'
    ;

array_elements
    : id_ (id_ | NL | SPACE)*
    ;

group
    : '{' (expr* | id_) '}'
    ;

id_
    : IDENTIFIER
    | STRING
    | INTEGER
    ;

IDENTIFIER
    : IDENTIFIERHEAD IDENTIFIERBODY*
    ;

INTEGER
    : [+-]? INTEGERFRAG
    ;

fragment INTEGERFRAG
    : [0-9]+
    ;

fragment IDENTIFIERHEAD
    : [a-zA-Z/@]
    ;

fragment IDENTIFIERBODY
    : IDENTIFIERHEAD
    | [0-9_]
    ;

STRING
    : '"' (~["\\] | '\\' .)* '"'
    ;

COMMENT
    : '#' ~[\r\n]* -> channel(HIDDEN)
    ;

SPACE
    : [ \t\f] -> channel(HIDDEN)
    ;

NL
    : [\r\n] -> channel(HIDDEN)
    ;