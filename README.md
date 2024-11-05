# Sudoku Solver: My Introduction to Test Driven Development

I made this project as my first foray into test-first TDD.

## The Short Story

I deliberately made the project small, in a language I knew well (Python), and on an idea (solving sudoku) I could succeed at. This meant I could focus on practising TDD.

I learned:
- to test behaviours, not implementation
- starting with a high concept naturally lead to testing the underlying concepts
- the green stage was highly successful even when I wrote stupid solutions like `return True` because it encouraged me to make more (usually negative) tests to improve the solution
- the refactor stage encouraged me to simplify large functions
- TDD relies on you knowing your tools - it was hard for me to test a Django project because I wasn't familiar enough with Django

## The Long Story

Previously I had attempted a web project which was of substantial size (for me) and was implemented in Django, which I was still learning. I struggled to understand *what* to test and *in what way*. Introductions to the topic repeated the "Red, Green, Refactor" mantra and repeatedly underlined the need to test all code. When I wanted to add a new function, was I to test the function's existance? The types of its arguments and return value? Its internal logic?

Frustrated with a few useless attempts on the Django project, I allowed myself to use testing but not commit to test-first. Then, having written some tests, they quickly broke and became redundant. I would need to write entirely new tests and the benefit of TDD was entirely lost on me.

Misery loves company and as I perused the subject on YouTube, I was delighted to find that these drawbacks had not gone unnoticed. With a couple of provocatively titled talks (), I soon heard that "The TDD naysayers are just doing it wrong!" Scowling, I heard the presenters out in their hypocrisy, and eventually heard their plea to test *behaviour*, not classes or functions.

So, I ruminated this cud again. I would make a very small project just to see if I could learn the TDD manner and realise its benefits.

I halted at first as to what to test in the beginning. But with a prod from an LLM, I realised it didn't matter too much where I started: pull on a string and you will eventually unravel the whole yarn.

I religiously kept to test-first and to the Red-Green-Refactor. Because the programme is simple Python, I was confident in it and understood it well.

That said, TDD did confront me with something I thought I knew but didn't. I thought I understood how lists were changed and required, but when it came to implementing my `solve(puzzle)` function, it took me to break our some manual tests to realise the `invert(puzzle)` function had a side effect of changing the puzzle in question.

## The Code

There are two high-level behaviours which begat all other subroutines:
1. checking a puzzle is valid
2. solving a puzzle

There may be implementation troubles if I change the definition of what a `puzzle` is. Currently it is a 2d list of digits. (Some, not all, the functions accept a puzzle that is not the standard 9x9 size.) But would making it a class decouple the tests from this particular implementation? I hope to develop this little project more to see how TDD changes over time.

Oh, and this project has a wee recursion in `solve(puzzle)`. Despite that, the solution for solve stinks and it takes a long time to run. (More improvements to make!)