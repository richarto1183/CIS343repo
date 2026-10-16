# Lab 3: Parser

## 1. Introduction and Design

For this lab, I continued developing my programming language called Nova. The goal was to create a parser that takes the tokens from my scanner and converts them into an Abstract Syntax Tree (AST).

I reused my scanner, AST classes, and AST printer from the previous labs. I also created a new Parser class that handles different expressions, including arithmetic, comparisons, equality, unary operators, and parentheses.

My parser uses recursive descent, similar to the approach used in Lox. Nova uses `null` instead of Lox's `nil` keyword. The parser also follows operator precedence and associativity rules to make sure expressions are grouped correctly.

I added error handling so the program can detect invalid expressions without crashing. The program supports both interactive input and reading expressions from source files.

## 2. Expression Grammar

Nova uses a recursive descent parser to process expressions. The grammar is similar to Lox and uses different rules to handle operator precedence and associativity.

### Expression Grammar

```text
expression  → equality ;
equality    → comparison ( ( "!=" | "==" ) comparison )* ;
comparison  → term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
term        → factor ( ( "-" | "+" ) factor )* ;
factor      → unary ( ( "/" | "*" ) unary )* ;
unary       → ( "!" | "-" ) unary | primary ;
primary     → NUMBER | STRING | "true" | "false"
            | "null" | "(" expression ")" ;
```

### Operator Precedence

The operators in Nova follow this precedence order, from highest to lowest:

1. Parentheses and literals
2. Unary operators (`!`, `-`)
3. Multiplication and division (`*`, `/`)
4. Addition and subtraction (`+`, `-`)
5. Comparison (`>`, `>=`, `<`, `<=`)
6. Equality (`==`, `!=`)

### Associativity

Binary operators in Nova are left-associative. This means operators with the same precedence are grouped from left to right.

For example, `10 - 5 - 2` is parsed as `(10 - 5) - 2`.

Unary operators use right recursion, allowing expressions such as `--5` to be parsed correctly.

### Design Choices and Differences from Lox

Nova's expression grammar is mostly based on Lox. Both languages use recursive descent parsing and follow the same basic operator precedence rules.

One difference is that Nova uses the keyword `null` instead of Lox's `nil`. Nova also includes keywords such as `let`, `when`, `otherwise`, `loop`, and `func` in its scanner.

For this lab, I focused on parsing expressions rather than statements or function declarations. Logical `and` and `or` operators are not implemented.

## 3. Setup and Running Tests

Nova is implemented in Python and uses only the Python standard library. No additional libraries or dependencies are required.

### Setup

1. Make sure Python 3 is installed.
2. Clone or download the GitHub repository.
3. Open a terminal in the repository's root directory.

### Interactive Mode

To run Nova in interactive mode, use:

```bash
python src/main.py
```

The program will display a prompt where the user can enter expressions.

Example:

```text
> 5 + 3 * 2
(+ 5.0 (* 3.0 2.0))
```

Type `exit` to close the program.

### Source-File Mode

Nova can also read an expression from a source file.

Run:

```bash
python src/main.py test/lab3/valid_expression.nova
```

Expected output:

```text
(* (group (+ 5.0 3.0)) 2.0)
```

Each source file should contain one expression.

### Automated Tests

I created a Python test script that checks the parser using different expressions and invalid inputs.

To run the automated tests, use:

```bash
python test/lab3/test_parser.py
```

The script compares the actual AST output with the expected output for each test.

All 29 automated tests passed.

```text
Results: 29/29 tests passed
```

The tests cover arithmetic, comparisons, equality, unary operators, literals, grouping, precedence, associativity, and error handling.

## 4. Test Results

I created 29 automated tests to check that my Nova parser correctly handles different expressions and errors. All 29 tests passed.

Each test compares the actual output from my parser with the expected output.

### Arithmetic, Precedence, and Grouping

| Test | Input | Expected and Actual Output | Result |
|---|---|---|---|---|
| Addition | `5 + 3` | `(+ 5.0 3.0)` | PASS |
| Subtraction | `10 - 5` | `(- 10.0 5.0)` | PASS |
| Multiplication | `4 * 3` | `(* 4.0 3.0)` | PASS |
| Division | `20 / 4` | `(/ 20.0 4.0)` | PASS |
| Precedence | `5 + 3 * 2` | `(+ 5.0 (* 3.0 2.0))` | PASS |
| Associativity | `10 - 5 - 2` | `(- (- 10.0 5.0) 2.0)` | PASS |
| Grouping | `(5 + 3) * 2` | `(* (group (+ 5.0 3.0)) 2.0)` | PASS |
| Nested Grouping | `((2 + 3) * (4 - 1))` | `(group (* (group (+ 2.0 3.0)) (group (- 4.0 1.0))))` | PASS |

These tests check that arithmetic operators work and that the parser follows the correct precedence and associativity rules.

### Comparison and Equality

| Test | Input | Expected and Actual Output | Result |
|---|---|---|---|---|
| Greater Than | `10 > 5` | `(> 10.0 5.0)` | PASS |
| Greater Equal | `10 >= 5` | `(>= 10.0 5.0)` | PASS |
| Less Than | `5 < 10` | `(< 5.0 10.0)` | PASS |
| Less Equal | `5 <= 10` | `(<= 5.0 10.0)` | PASS |
| Equal | `5 == 5` | `(== 5.0 5.0)` | PASS |
| Not Equal | `5 != 3` | `(!= 5.0 3.0)` | PASS |

These tests verify that the parser recognizes all supported comparison and equality operators.

### Unary Operators and Literals

| Test | Input | Expected and Actual Output | Result |
| Unary Minus | `-5` | `(- 5.0)` | PASS |
| Logical Not | `!true` | `(! true)` | PASS |
| Multiple Unary | `!-5` | `(! (- 5.0))` | PASS |
| Integer | `42` | `42.0` | PASS |
| Decimal | `3.14` | `3.14` | PASS |
| String | `"Hello Nova"` | `Hello Nova` | PASS |
| True | `true` | `true` | PASS |
| False | `false` | `false` | PASS |
| Null | `null` | `null` | PASS |

These tests check that Nova correctly parses unary expressions and all supported literal types.

### Syntax and Lexical Errors

| Test | Input | Expected and Actual Result | Status |
| Missing Parenthesis | `(5 + 3` | `[line 1] Error at end: Expected ')' after expression.` | PASS |
| Missing Operand | `5 +` | `[line 1] Error at end: Expected expression.` | PASS |
| Unexpected Operator | `5 + * 3` | `[line 1] Error at '*': Expected expression.` | PASS |
| Trailing Token | `5 3` | `[line 1] Error at '3': Unexpected token after expression.` | PASS |
| Invalid Character | `5 + @` | `Lexical Error` | PASS |
| Unterminated String | `"Hello` | `Lexical Error` | PASS |

The missing parenthesis error occurs because the expression starts with `(` but never closes it. The missing operand error happens because the `+` operator does not have a right operand. The unexpected operator error occurs because `*` appears where an expression should begin. The trailing token error occurs because the parser finds another number after an expression has already finished.

The lexical errors occur when the scanner encounters an unsupported character or a string without a closing quotation mark. In both cases, the program reports the error without printing an AST. The test helper returns `Lexical Error`, while the scanner prints a more specific diagnostic.

### Interactive and Source-File Testing

I also tested Nova in both interactive mode and source-file mode.

For interactive mode, I entered invalid expressions followed by valid expressions without restarting the program. Nova continued accepting input after both syntax and lexical errors.

For source-file mode, I tested a valid expression and an invalid expression using `.nova` files. The valid expression produced the correct AST, and the invalid expression produced an error without crashing.

### Test Summary

- Total automated tests: 29
- Passed: 29
- Failed: 0

All automated tests passed, and both interactive and source-file modes worked correctly.

## 5. Concrete Syntax Tree and Abstract Syntax Tree

For this section, I used the expression:

```text
(5 + 3) * 2
```

### Concrete Syntax Tree (CST)

The concrete syntax tree follows Nova's expression grammar. It includes the grammar rules and symbols needed to produce the original expression.

```text
expression
└── equality
    └── comparison
        └── term
            └── factor
                ├── unary
                │   └── primary
                │       ├── "("
                │       ├── expression
                │       │   └── equality
                │       │       └── comparison
                │       │           └── term
                │       │               ├── factor
                │       │               │   └── unary
                │       │               │       └── primary
                │       │               │           └── NUMBER (5)
                │       │               ├── "+"
                │       │               └── factor
                │       │                   └── unary
                │       │                       └── primary
                │       │                           └── NUMBER (3)
                │       └── ")"
                ├── "*"
                └── unary
                    └── primary
                        └── NUMBER (2)
```

### Abstract Syntax Tree (AST)

The AST removes unnecessary grammar rules and focuses on the structure of the expression.

```text
        Binary (*)
        /        \
   Grouping     Literal (2)
       |
    Binary (+)
    /        \
Literal (5)  Literal (3)
```

The AST printer produces:

```text
(* (group (+ 5.0 3.0)) 2.0)
```

### Comparison

The CST contains all the grammar rules used to construct the expression, while the AST only contains the nodes needed to represent the expression.

The AST is simpler because it removes intermediate grammar rules such as `term`, `factor`, and `unary`.

Both trees show that `5 + 3` is grouped together before being multiplied by `2`.

## 6. Changes from Lab 2 and Known Limitations

### Changes from Lab 2

In Lab 2, I created the AST classes and AST printer to represent and display expressions. However, the expressions were created manually in Python.

For Lab 3, I added a recursive descent parser that automatically converts tokens from my scanner into an AST. This allows users to type expressions directly instead of having to manually create AST objects.

I also updated `main.py` to connect the scanner, parser, and AST printer. The program now supports both interactive mode and reading expressions from files.

Another improvement was adding better error handling. The scanner now tracks lexical errors, and the parser reports syntax errors with line numbers and token locations. This prevents the program from printing an AST when the input is invalid.

### Known Limitations

Nova currently supports basic expressions, including arithmetic, comparisons, equality, unary operators, literals, and grouping.

However, there are still some limitations:

- The parser does not support variable declarations, assignments, or statements yet.
- Keywords such as `let`, `when`, and `loop` are recognized by the scanner but are not handled by the expression parser.
- Logical operators such as `and` and `or` are not implemented.
- The parser accepts only one expression per input rather than a complete program.
- Nova currently builds ASTs but does not evaluate expressions.

These features could be added in future versions of Nova.

### Conclusion

Overall, this lab helped me understand how a recursive descent parser works and how a programming language converts source code into an AST.

I also learned more about operator precedence, associativity, and handling syntax errors. All 29 automated tests passed, and both interactive and source-file modes worked correctly.
