# Roman numerals kata in Python

## Overview

This repository contains two exercises designed to improve your skills in
test-driven development.

## Instructions

Roman numerals are a numeral system that was used by ancient Rome. Numbers in 
this system use letters from the Latin alphabet. Currently, it uses seven symbols:

| Symbol | Value |
|:-------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Instead of writing the same letter four times, a rule for subtraction is used:
the letter is written once, then the next largest Roman numeral is written.
For example, 4 is not written as IIII, but instead as IV, because IV is V (5)
minus I (1).

In general, the values for 5, 50, and 500 are not subtracted.

### Exercise 1

The task at hand entails crafting a function `to_roman(number: int) -> str` to
convert regular Arabic numbers into Roman numerals, such as:

* 4 → IV
* 7 → VII
* 9 → IX

The lowest number you can write in Roman Numerals is number I (1). And the
largest numeral is MMMCMXCIX (3999).

### Exercise 2

In this phase, the objective is to develop a function `from_roman(number: str)
-> int` that performs the reverse conversion, transforming Roman numerals into
their corresponding Arabic digits.

## Guiding Principles

* If you don't know an existing algorithm, follow the principles of strict
  Test-Driven Development (TDD) to derive one.
* Reflect on whether the sequence in which you write tests influences the final
  design of your algorithm.
* Consider whether it's more beneficial to devise an algorithm before embarking
  on TDD, especially if you don't already know one.
* If you do know an algorithm, evaluate if it can be implemented using strict
  TDD principles.

### Prerequisites

* [Python 3.8+](https://www.python.org/)
* [pytest](https://pytest.org)

### Run main

```console
make run
```

### Run tests

```console
make test
```
