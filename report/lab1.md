# Lab1: Scanning

## Language Design

for this lab I created a language called Nova. Nova is based on Lox from Crafting Interpreters, but I changed several of the keywords to make the language different while keeping the scanner simple.

some of the main changes are :

Nova            Lox
let             var
when            if
otherwise       else
loop            while
func            fun
null            nil

Nova also uses the keywords return, print, true, and false.

i kept most of the operators similar to Lox because they are common and easy to understand. Nova supports:

+ - * / ! != = == < <= > >=

and it also supports this punctuation

( ) { } , . ;

Single-line comments begin with //. Everything after // on the same line is ignored by the scanner. Spaces, tabs, and carriage returns are also ignored. Newlines are not made into tokens, but they are counted so that lexical errors can display the correct line number.

## Lexical Grammar

### Number Literals

Regular expression:

[0-9]+(\.[0-9]+)?

A number must contain one or more digits. It can optionally contain a decimal point followed by one or more additional digits.

Examples of valid numbers:

10
123
3.14
0.5
123.50

A value such as 123. is scanned as the number 123 followed by a DOT token because Nova requires at least one digit after a decimal point.

### String Literals

Regular expression:

"[^"]*"

Strings begin and end with double quotation marks. The quotation marks are included in the lexeme but are removed from the literal value.

Examples:

"Hello"
"Hello world!"
""

Nova allows strings to continue across multiple lines. If the end of the source is reached without finding a closing quotation mark, the scanner reports an unterminated string error.

### Literals

Regular expression:

[a-zA-Z_][a-zA-Z0-9_]*

An identifier must begin with a letter or underscore. After the first character, it can contain letters, numbers, or underscores.

Examples:

score
player1
_player
player_score

After an identifier is scanned, Nova checks whether it matches one of the language's keywords. If it does, the appropriate keyword token is created. Otherwise, an IDENTIFIER token is created.

## Differences from Lox

Nova's scanner follows the general scanning approach shown for Lox in Chapter 4 of Crafting Interpreters, but Nova has its own keyword choices. For example, Nova uses let instead of var, when instead of if, and otherwise instead of else.

I chose these keywords because their meanings are still easy to understand while making Nova different from Lox. I kept the common arithmetic and comparison operators because changing them would make the language less familiar without adding much benefit to the scanner.

This lab only implements scanning. Nova does not currently parse or execute the tokens produced by the scanner.

## Setup and Running Nova

### Requirements

Nova is implemented in Python. Python 3 is required to run the scanner. No additional libraries or dependencies are required.

The implementation files are located in the src/ directory.

### Interactive Mode

To start Nova in interactive mode, run the following command from the root directory of the repository:

python src/main.py

The program will display the Nova prompt:

 >

Code can then be entered directly into the terminal. The scanner prints the token type, lexeme, and literal value for each token it finds.

For example:

let score = 10;

produces:

LET let None
IDENTIFIER score None
EQUAL = None
NUMBER 10 10.0
SEMICOLON ; None
EOF  None

Type exit to leave interactive mode.

Interactive mode also continues running after a lexical error. This allows the user to correct the input or enter another line without restarting Nova.

### Source File Mode

Nova can also scan code stored in a source file. Run:

python src/main.py <file>

For example, the basic test file can be run with:

python src/main.py test/lab1/basic.txt

The scanner reads the entire file and prints the tokens it finds.

### Running the Tests

The test files for Lab 1 are located under test/lab1/.

The file tests can be reproduced with the following commands:

python src/main.py test/lab1/basic.txt
python src/main.py test/lab1/operators.txt
python src/main.py test/lab1/literals.txt
python src/main.py test/lab1/keywords.txt
python src/main.py test/lab1/errors.txt

## Test Results

### Test 1: Basic Program

#### Purpose:
This test checks that Nova can scan a basic program containing variables, numbers, strings, keywords, comparison operators, punctuation, and a comment.

#### Source Input:

// Basic Nova program

let score = 10;
let name = "Tobin";

when (score >= 5) {
    print "You win!";
}

#### Expected Result:
The scanner should recognize all keywords, identifiers, literals, operators, and punctuation. The comment and whitespace should be ignored.

#### Actual Output

LET let None
IDENTIFIER score None
EQUAL = None
NUMBER 10 10.0
SEMICOLON ; None
LET let None
IDENTIFIER name None
EQUAL = None
STRING "Tobin" Tobin
SEMICOLON ; None
WHEN when None
LEFT_PAREN ( None
IDENTIFIER score None
GREATER_EQUAL >= None
NUMBER 5 5.0
RIGHT_PAREN ) None
LEFT_BRACE { None
PRINT print None
STRING "You win!" You win!
SEMICOLON ; None
RIGHT_BRACE } None
EOF  None

#### Result: Passed. 
The actual output matched the expected result.

### Test 2: Operators and Punctuation

#### Purpose:
This test checks every operator and punctuation token supported by Nova.

#### Source Input:

( ) { }
, . ;
+ - * /
! !=
= ==
< <=
> >=

#### Expected Result:
Each operator and punctuation symbol should produce its correct token type.

#### Actual Output:

LEFT_PAREN ( None
RIGHT_PAREN ) None
LEFT_BRACE { None
RIGHT_BRACE } None
COMMA , None
DOT . None
SEMICOLON ; None
PLUS + None
MINUS - None
STAR * None
SLASH / None
BANG ! None
BANG_EQUAL != None
EQUAL = None
EQUAL_EQUAL == None
LESS < None
LESS_EQUAL <= None
GREATER > None
GREATER_EQUAL >= None
EOF  None

#### Result: Passed.
All operators and punctuation were recognized correctly.

### Test 3: Literals and Identifiers

#### Purpose:
This test checks identifiers, numbers, decimal numbers, strings, an empty string, comments, and number edge cases.

#### Source Input:

score
player1
_player
player_score

10
123
3.14
0.5
123.50

"Hello"
"Hello world!"
""

let x = 10; // This comment should be ignored.

123.

#### Expected Result:
Identifiers should be recognized correctly, numbers should contain their numeric literal values, and strings should contain their values without quotation marks. The comment should be ignored. 123. should be scanned as the number 123 followed by a DOT.

#### Actual Output

IDENTIFIER score None
IDENTIFIER player1 None
IDENTIFIER _player None
IDENTIFIER player_score None
NUMBER 10 10.0
NUMBER 123 123.0
NUMBER 3.14 3.14
NUMBER 0.5 0.5
NUMBER 123.50 123.5
STRING "Hello" Hello
STRING "Hello world!" Hello world!
STRING ""
LET let None
IDENTIFIER x None
EQUAL = None
NUMBER 10 10.0
SEMICOLON ; None
NUMBER 123 123.0
DOT . None
EOF  None

#### Result: Passed. 
All literals and identifiers matched the expected behavior.

### Test 4: Keywords

#### Purpose:
This test checks every keyword defined in Nova.

#### Source Input:

let
when
otherwise
loop
func
return
print
true
false
null

#### Expected Result:
Each word should be recognized as its specific keyword token instead of as an identifier.

#### Actual Output:

LET let None
WHEN when None
OTHERWISE otherwise None
LOOP loop None
FUNC func None
RETURN return None
PRINT print None
TRUE true None
FALSE false None
NULL null None
EOF  None

#### Result: Passed. 
All Nova keywords were recognized correctly.

### Test 5: Lexical Errors

#### Purpose:
This test checks unexpected-character errors, line numbers, error recovery, and unterminated strings.

#### Source Input:

let good = 10;

@
######
$

let stillGood = 20;

"This string never ends

#### Expected Result:
The scanner should report errors for @, #, and $ with their correct line numbers. It should continue scanning after these errors and recognize let stillGood = 20;. The final unfinished string should produce an unterminated string error.

#### Actual Errors:

[line 3] Error: Unexpected character '@'.
[line 4] Error: Unexpected character '#'.
[line 5] Error: Unexpected character '$'.
[line 9] Error: Unterminated string.

The scanner also successfully produced tokens for both let good = 10; and let stillGood = 20;.

#### Result: Passed. 
All expected errors were reported with the correct line numbers, and scanning continued after the unexpected characters.

### Test 6: Interactive Error Recovery

#### Purpose:
This test checks that interactive mode remains usable after lexical errors.

#### Source Input:

@
let score = 10;
"unfinished
print "Still working!";

Each line was entered separately into interactive mode.

#### Expected Result:
The @ character should produce an unexpected-character error, but Nova should return to the prompt. The unfinished string should also produce an error without closing the interactive session. Valid input entered after each error should still be scanned normally.

#### Actual Result:

Nova reported:

[line 1] Error: Unexpected character '@'.

and returned to the prompt. It then successfully scanned:

let score = 10;

The unfinished string produced:

[line 1] Error: Unterminated string.

Nova again returned to the prompt and successfully scanned:

print "Still working!";

#### Result: Passed. 
Interactive mode remained usable after both types of lexical errors.

## Known Limitations

All of the current test cases passed, but Nova's scanner has some limitations.

Nova does not support escape sequences inside strings. For example, quotation marks cannot currently be escaped with \".

Nova only supports single-line comments beginning with //. Block comments are not supported.

Numbers support integers and basic decimals, but scientific notation such as 1.5e10 is not supported.

A decimal point must have digits after it to be considered part of a number. For example, 123. is scanned as the number 123 followed by a DOT token.

Nova currently only performs scanning. Parsing and execution are not implemented as part of this lab.

There are currently no known failing tests.