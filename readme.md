## Should I Learn Python or Ruby?

At first glance, Python and Ruby appear to be very similar languages. Both are high-level, [dynamic](http://en.wikipedia.org/wiki/Dynamic_programming_language) languages used for rapid development. What do I mean by dynamic?

Well, with a dynamically typed language you can do this:

```sh
>>> variable = 1
>>> type(variable)
<type 'int'>
>>> variable = "Foo"
>>> type(variable)
<type 'str'>
>>> variable = ["bar",10]
>>> type(variable)
<type 'list'>
```

Essentially, I can change the datatype (from an integer to a string to a list, in the above example) at any point in a program. In a statically typed language, this would result in an error when compiled.

Both support multiple programming paradigms as well - e.g, procedural, functional, object oriented, and so forth.

However, there are a number of differences ..

### The Python Way

Open your terminal and open the Python shell then type `import this`:

```sh
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

This is what is known as the [Zen of Python](http://www.python.org/dev/peps/pep-0020/), which are the guiding principles of Python. These 19 guidelines can be trimmed to five points:
1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
5. Readability counts.

Essentially, Pythonists value code readability and productivity over all else. 

> Check out [this](http://stackoverflow.com/questions/228181/the-zen-of-python) StackOverflow question to see examples of all the guidelines in use.

Finally, if shortened to one major point-

*There should be one – and preferably only one – obvious way to do it*

-we get to one of the main differences between Python and Ruby ..

### The Python Way
