# Lab 2: AST Printer

## Expression Grammar

for this lab, I continued developing my programming language from Lab 1. I created an expression grammar based on Lox that defines how different expressions are structured.

The grammar supports arithmetic, comparison, and equality operators, along with unary expressions, literals, and grouping.

The grammar follows the same basic operator precedence as Lox.

My programming language, Nova,  uses its own keywords, such as let, when, otherwise, and func, instead of some of the keywords used in Lox. However, these keywords are not part of the expression grammar implemented in this lab.

The supported literal types are numbers, strings, booleans, and null.

## implementaion and Setup

### AST Implementaion

For this lab, I created four expression classes in expr.py: Literal, Unary, Binary, and Grouping.

I reused the Token and TokenType classes from Lab 1 to represent the operators.

### AST Printer

I created an AstPrinter class in ast_printer.py that converts expression trees into readable strings.

The printer uses a visit() method to determine which type of expression it is working with. It then calls the correct method for that expression type.

The printer also uses recursion to handle nested expressions. This allows it to print more complicated expressions while keeping their structure.

For example, the expression (5 + 3) * 2 produces: (* (group (+ 5 3)) 2)

### Setup and Running Tests

The project was developed using Python and does not require any additional libraries.

The files are organized into three main folders:

src/ contains the implementation files, including the AST classes, printer, and reused scanner components.
test/lab2/ contains the AST printer tests.
report/ contains the Lab 2 report.

To run the tests, open a terminal in the repository's main directory and enter: python test/lab2/test_printer.py

The test program creates hard-coded AST expressions and prints their results. It also uses Python assert statements to compare the actual output with the expected output.

## Test Cases and Results

### Test 1: Basic Expressions

Purpose: Test the basic AST classes, including literals, unary expressions, binary expressions, grouping, and nested expressions.

#### Hard-coded ASTs:

Literal(5)
Literal(True)
Literal(None)

Unary(Token(TokenType.MINUS, "-", None, 1), Literal(5))

Binary(
    Literal(5),
    Token(TokenType.PLUS, "+", None, 1),
    Literal(3)
)

Binary(
    Grouping(
        Binary(
            Literal(5),
            Token(TokenType.PLUS, "+", None, 1),
            Literal(3)
        )
    ),
    Token(TokenType.STAR, "*", None, 1),
    Literal(2)
)

#### Expected Output:

5
true
null
(- 5)
(+ 5 3)
(* (group (+ 5 3)) 2)

#### Actual Output: Matched the expected output.

#### Result: PASS

### Test 2: Binary Operators

Purpose: Verify that the AST printer correctly handles all ten supported binary operators.

#### Hard-coded AST: 

Each test uses a Binary expression with Literal(10) on the left and Literal(5) on the right. The operator changes for each test.

Example:

Binary(
    Literal(10),
    Token(TokenType.PLUS, "+", None, 1),
    Literal(5)
)

Operator    Expected Output     Actual Output   Result
+           (+ 10 5)            (+ 10 5)        PASS
-           (- 10 5)            (- 10 5)        PASS
*           (* 10 5)            (* 10 5)        PASS
/           (/ 10 5)            (/ 10 5)        PASS
==          (== 10 5)           (== 10 5)       PASS
!=          (!= 10 5)           (!= 10 5)       PASS
>           (> 10 5)            (> 10 5)        PASS
>=          (>= 10 5)           (>= 10 5)       PASS
<           (< 10 5)            (< 10 5)        PASS
<=          (<= 10 5)           (<= 10 5)       PASS

#### Result: PASS

All ten binary operators produced the expected output.

### Test 3: Literal Types

Purpose: Verify that the printer correctly handles numbers, strings, booleans, and null values.

#### Hard-coded ASTs:

Literal(42)
Literal(3.14)
Literal("Hello, World!")
Literal(True)
Literal(False)
Literal(None)

Literal     Expected Output     Actual Output   Result
integer     42                  42              PASS
decimal     3.14                3.14            PASS
string      Hello, World!       Hello, World!   PASS
True        true                true            PASS
False       false               false           PASS
Null        null                null            PASS

#### Result: PASS

All literal types produced the expected output.

### Test 4: Unary Operators

Purpose: Verify that the printer correctly handles unary minus (-) and logical NOT (!).

#### Hard-coded ASTs:

Unary(
    Token(TokenType.MINUS, "-", None, 1),
    Literal(10)
)

Unary(
    Token(TokenType.BANG, "!", None, 1),
    Literal(True)
)

Expected Output:

(- 10)
(! true)

Actual Output:

(- 10)
(! true)

#### Result: PASS

### Testing Summary

All the tests passed successfully. The AST printer correctly handled every expression class, supported operator, and literal type. The nested expression test also showed that the printer preserves the structure of the expression tree.

## Known Limitations

The AST printer passed all the tests, but there are a few limitations to the current implementation.

### Manual AST creation: 

The expression trees are created manually in the test file. Nova does not automatically convert source code into ASTs yet.

### No expression evaluation: 

The printer only displays the structure of expressions. It does not calculate or execute them.

### String formatting: 

String literals are printed without quotation marks, which can make them harder to distinguish from other values.

### Limited expression support: 

The AST currently supports literals, unary expressions, binary expressions, and grouping. Other language features, such as variables, functions, and statements, are not represented yet.

These limitations are expected because this lab focuses on representing and printing ASTs rather than parsing or executing code.

All the implemented tests passed, and there are no known failing tests.