# Lab 4: Statements

## Overview

In this lab, I added support for print statements and expression statements to my interpreter. I also implemented panic-mode error recovery so the parser can continue processing statements after finding a syntax error.

## Implementation

I created a new `stmt.py` file with two classes: `Expression` and `Print`. I updated the parser to handle multiple statements and added a `synchronize()` method to recover from syntax errors.

I also updated `main.py` to execute the statements instead of printing their AST representations.

## Test Case 1: Error Recovery

Input:
```
"one"
true;
print 2 +
```

Output:
```
[line 2] Error at 'true': Expected ';' after expression.
[line 3] Error at end: Expected expression.
```

The parser correctly reported both syntax errors without crashing.

## Test Case 2: Valid Statements

Input:
```
4 + 2;
print "one";
print true;
print 1 + 2;
print null;
```

Output:
```
one
true
3
null
```

The interpreter successfully executed all the statements. The expression statement `4 + 2;` did not produce any output, which is expected.

## How to Run

From the repository's root directory, run:

```
python src/main.py test/lab4/test1.lox
python src/main.py test/lab4/test2.lox
```

## Conclusion

Both test cases produced the expected results. My interpreter can now execute multiple statements and recover from syntax errors while continuing to parse valid statements.