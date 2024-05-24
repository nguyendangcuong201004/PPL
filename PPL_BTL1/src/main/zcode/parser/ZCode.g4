grammar ZCode;

@lexer::header {
  #2153594
from lexererr import *
}
options {
	language = Python3;
}

// declared
program: NEWLINE* list_declared EOF;
list_declared: declared list_declared | declared;
declared: function | variables ignore;

variables: implicit_var | keyword_var | implicit_dynamic;
// implicit_var 
implicit_var: VAR ID ASSIGNINIT expression;
// keyword_var, typ is BOOL, NUMBER, STRING
keyword_var:
	typ ID (LBRACKET list_NUMBER_LIT RBRACKET)? (
		ASSIGNINIT expression
	)?;
list_NUMBER_LIT: NUMBER_LIT COMMA list_NUMBER_LIT | NUMBER_LIT;
// implicit_dynamic
implicit_dynamic: DYNAMIC ID (ASSIGNINIT expression)?;

function:
	FUNC ID LPAREN parameters_list? RPAREN (
		ignore? return_statement
		| ignore? block_statement
		| ignore
	);

// prameters_list
parameters_list: parameter COMMA parameters_list | parameter;
//parameter, implicit can not be used for parameter declaration
parameter: typ ID (LBRACKET list_NUMBER_LIT RBRACKET)?;
typ: BOOL | NUMBER | STRING;
// ---------------------------Expression---------------------------------//
// ---------------------------Expression---------------------------------// list_expression
list_expression: expression COMMA list_expression | expression;
// expression
expression: expr1 STRING_CONCAT expr1 | expr1;
expr1:
	expr2 (
		EQUAL
		| STRING_EQUAL
		| NOT_EQUAL
		| LESS_THAN
		| GREATER_THAN
		| LESS_THAN_EQUAL
		| GREATER_THAN_EQUAL
	) expr2
	| expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: (SUB | ADD) expr6 | expr7;
//index expression
expr7: (ID | func_call) LBRACKET (list_expression) RBRACKET
	| expr8;
expr8: ID | literal | LPAREN expression RPAREN | func_call;

//! Value
literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal;
// array_literal
array_literal: LBRACKET list_expression RBRACKET;
// func_call
func_call: ID LPAREN list_expression? RPAREN;
// kí tự bỏ qua
ignore: NEWLINE+; // at least one new line character
// ---------------------------Statement---------------------------------//
statement:
	declaration_statement
	| assignment_statement
	| if_statement
	| for_statement
	| break_statement
	| continue_statement
	| return_statement
	| call_statement
	| block_statement;
//declaration_statement, the same at variables
declaration_statement: (
		implicit_var
		| keyword_var
		| implicit_dynamic
	) ignore;
//assignment_statement, ID hoac index operator khong bao gom ham
assignment_statement: lhs ASSIGNINIT expression ignore;
lhs: ID LBRACKET list_expression RBRACKET | ID;
//if_statement
if_statement:
	IF LPAREN expression RPAREN ignore? statement elif_list? (
		ELSE ignore? statement
	)?;
elif_list: elif_stmt elif_list | elif_stmt;
elif_stmt: ELIF LPAREN expression RPAREN ignore? statement;
//for_statement
for_statement:
	FOR ID UNTIL expression BY expression ignore? statement;
//break statement
break_statement: BREAK ignore;
//continue statement
continue_statement: CONTINUE ignore;
//return statement
return_statement: RETURN expression? ignore;
//call statement
call_statement: ID LPAREN list_expression? RPAREN ignore;
//block statement
block_statement: BEGIN ignore stmt_list END ignore;
stmt_list: statement stmt_list |;

//! --------------------------  Lexical structure ----------------------- //

// -----------------------------KeyWord------------------------------------//

TRUE: 'true';

FALSE: 'false';

NUMBER: 'number';

BOOL: 'bool';

STRING: 'string';

RETURN: 'return';

VAR: 'var';

DYNAMIC: 'dynamic';

FUNC: 'func';

FOR: 'for';

UNTIL: 'until';

BY: 'by';

BREAK: 'break';

CONTINUE: 'continue';

IF: 'if';

ELSE: 'else';

ELIF: 'elif';

BEGIN: 'begin';

END: 'end';

NOT: 'not';

AND: 'and';

OR: 'or';

// --------------------------------------End of KeyWord--------------------------------//

// --------------------------------------Operators------------------------------------//

ADD: '+';

SUB: '-';

MUL: '*';

DIV: '/';

MOD: '%';

EQUAL: '=';

NOT_EQUAL: '!=';

ASSIGNINIT: '<-';

LESS_THAN: '<';

LESS_THAN_EQUAL: '<=';

GREATER_THAN: '>';

GREATER_THAN_EQUAL: '>=';

STRING_EQUAL: '==';

STRING_CONCAT: '...';

// --------------------------------------End of Operators----------------------------//

// --------------------------------------Separators------------------------------------//

LBRACKET: '[';

RBRACKET: ']';

LPAREN: '(';

RPAREN: ')';

COMMA: ',';

// --------------------------------------End of Separators----------------------------//

// --------------------------------------Identifiers------------------------------------//

ID: [a-zA-Z_] [a-zA-Z_0-9]*;

// --------------------------------------End of Identifiers----------------------------//

// --------------------------------------Literal------------------------------------// LITERAL:

// NUMBER_LIT | STRING_LIT | BOOL_LIT;

NUMBER_LIT: INTERGER_PART DECIMAL_PART? EXPONENT_PART?;

fragment INTERGER_PART: DIGIT+;

fragment DECIMAL_PART: '.' DIGIT*;

fragment EXPONENT_PART: [eE] [+-]? DIGIT+;

fragment DIGIT: [0-9];

STRING_LIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1];};

// --------------------------------------End of Literal----------------------------//

NEWLINE: [\n];

COMMENTS: '##' ~[\n\r]* -> skip; // Comments
WS: [ \t\r\f\b]+ -> skip; // skip spaces, tabs

UNCLOSE_STRING:
	'"' STR_CHAR* ('\r\n' | '\n' | EOF) {
	if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
		raise UncloseString(self.text[1:-2])
	elif (self.text[-1] == '\n'):
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL {
    raise IllegalEscape(self.text[1:])
};

fragment ESC_ILLEGAL: '\\' (~[btnfr'\\]) | [\r];

fragment STR_CHAR: ~[\r\n\\"] | ESC_SEQ | [']["];

fragment ESC_SEQ: '\\' [btnfr'\\];

ERROR_CHAR: . {raise ErrorToken(self.text)};

//!  -------------------------- end Lexical structure ------------------- //