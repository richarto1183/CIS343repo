# Lab 5: Variables

## Overview

In this lab, I added support for variable declarations, variable access, variable assignment, and block scope to my Nova interpreter. I also added error handling for invalid assignments, undefined variables, and unmatched braces.

## Implementation

I created a new `environment.py` file that uses a dictionary to store variable names and their values. I updated `expr.py` to support variable access and assignment and updated `stmt.py` to support variable declarations and block statements.

I also updated the parser, AST printer, and main file to support these new features.

## Design Choices

### Variable Access Before Declaration

Variables must be declared before they can be accessed or assigned a value. If a variable does not exist in the current environment or any enclosing environment, a runtime error is displayed.

### Missing Initializer

If a variable is declared without an initializer, its value defaults to `null`.

### Redeclaration

Variables can be redeclared in the same scope. The new declaration replaces the previous value.

### Block Scope

Each block creates its own environment. Variables declared inside a block cannot be accessed outside of that block. Inner blocks can access variables from outer blocks and can also declare variables with the same name.

## Test Case 1: Variables

Input:

```java
let x = 10;
print x;

let y = x + 5;
print y;

x = 20;
print x;

x = x + 5;
print x;

let empty;
print empty;

let x = 100;
print x;

let a;
let b;
a = b = 50;
print a;
print b;
```

Output:

```
10
15
20
25
null
100
50
50
```

The interpreter successfully declared, accessed, and assigned variables. It also handled missing initializers, redeclaration, and chained assignments correctly.

## Test Case 2: Textbook Scope Example

Input:

```java
let a = "global a";
let b = "global b";
let c = "global c";
{
    let a = "outer a";
    let b = "outer b";
    {
        let a = "inner a";
        print a;
        print b;
        print c;
    }
    print a;
    print b;
    print c;
}
print a;
print b;
print c;
```

Output:

```
inner a
outer b
global c
outer a
outer b
global c
global a
global b
global c
```

The interpreter searches the current environment first. If a variable is not found, it searches the enclosing environment until the variable is found.

The inner block uses its own value of `a`, the outer block's value of `b`, and the global value of `c`. After each block finishes, its local variables are no longer accessible. This demonstrates variable shadowing and block scope.

The `var` keyword from the textbook was replaced with `let` to match Nova's syntax.

## Test Case 3: Block Scope and Assignment

Input:

```java
let x = 10;

{
    let x = 20;
    print x;
}

print x;

{
    x = 50;
}

print x;

{
    let x = 100;
    {
        print x;
    }
}

print x;
```

Output:

```
20
10
50
100
50
```

This test shows that declaring a variable inside a block does not change the outer variable. However, assigning a value to an existing outer variable updates that variable.

## Test Case 4: Syntax Errors

Input:

```java
5 = 10;
(5 + 2) = 10;
let = 10;
let x = ;
}
{ print 10;
```

Output:

```
[line 1] Error at '=': Invalid assignment target.
[line 2] Error at '=': Invalid assignment target.
[line 3] Error at '=': Expected variable name.
[line 4] Error at ';': Expected expression.
[line 5] Error at '}': Expected expression.
[line 7] Error at end: Expected '}' after block.
```

The interpreter correctly detected invalid assignment targets, missing variable names, missing initializer expressions, and unmatched braces.

I also updated the parser's error recovery to recognize opening braces as the beginning of a new statement.

## Test Case 5: Undefined Variable Access

Input:

```java
print unknown;
```

Output:

```
[line 1] Runtime error at 'unknown': Undefined variable.
```

## Test Case 6: Undefined Variable Assignment

Input:

```java
unknown = 10;
```

Output:

```
[line 1] Runtime error at 'unknown': Undefined variable.
```

## Test Case 7: Access Outside of Scope

Input:

```java
{
    let local = 10;
}
print local;
```

Output:

```
[line 4] Runtime error at 'local': Undefined variable.
```

## Test Case 8: Missing Semicolon

Input:

```java
let x = 10
```

Output:

```
[line 1] Error at end: Expected ';' after variable declaration.
```

## How to Run

From the repository's root directory, run the following commands:

```
python src/main.py test/lab5/variables.lox
python src/main.py test/lab5/scope.lox
python src/main.py test/lab5/block_scope.lox
python src/main.py test/lab5/syntax_errors.lox
python src/main.py test/lab5/undefined_access.lox
python src/main.py test/lab5/undefined_assignment.lox
python src/main.py test/lab5/scope_error.lox
python src/main.py test/lab5/missing_semicolon.lox
```

## Conclusion

All eight test cases produced the expected results. My interpreter now supports variable declarations, variable access, variable assignment, and block scope. It also handles variable-related syntax and runtime errors without crashing.