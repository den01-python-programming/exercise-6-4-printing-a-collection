# Exercise 6.4 Printing a Collection

The exercise template has a predefined `SimpleCollection` class, which is used to represent a group of values. The class is missing the `__str__` method used for printing.

Implement a `__str__` method for the class that will perform as demonstrated in the following examples.

```java
s = SimpleCollection("alphabet")
print(s)

print()

s.add("a")
print(s)

print()

s.add("b")
print(s)

print()

s.add("c")
print(s)
```

```plaintext
The collection alphabet is empty.

The collection alphabet has 1 element:
a

The collection alphabet has 2 elements:
a
b

The collection alphabet has 3 elements:
a
b
c
```

```java
s = SimpleCollection("characters")
print(s)

print()

s.add("magneto")
print(s)

print()

s.add("mystique")
print(s)

print()

s.add("phoenix")
print(s)
```

```plaintext
The collection characters is empty.

The collection characters has 1 element:
magneto

The collection characters has 2 elements:
magneto
mystique

The collection characters has 3 elements:
magneto
mystique
phoenix
```

**NB:** You can add newlines in a `print` or `__str__` `return` statement with a `\n` character.
