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

**There should be one – and preferably only one – obvious way to do it**

-we get to one of the main differences between Python and Ruby ..

### The Ruby Way

While Python values one main way of solving a problem, Ruby - influenced by Perl - provides the developer more freedom and power:

*Ruby believes in empowering its programmers,giving them flexibility, freedom and power. But most of all, it belives in making programmer fun for its creator.*

—Yukihiro Matsumoto (Matz)

With more freedom and less syntactyical rules, many Rubyists believe that Ruby is a much more elegant language - and it is. But you can also often see messy code (especially from beginners) that can be difficult for other developers to read. For example, you can put multiple statements on one line. This can look good - and be readable - depending on how it's coded or it can be a mess.

Let's compare some code. The following snippets of code are for solving the Fibonnoci sequence:

*Ruby:*

```ruby
fib = Hash.new{ |h,k| h[k] = k < 2 ? k : h[k-1] + h[k-2] }
```

*Python:*

```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```

Although you can write this code in many ways, both of these methods are *true* to the language. In other words, the Ruby example is very Ruby-ish while the Python example is very Python-ish. Can you read the Ruby code? It may be more elegant, since it is on one line, but it's very hard to read. Meanwhile, I can easily follow the Python code. You of course can write code anyway you want. It's adviseable to write Ruby code, when beginning, in a more Pythonic way - which simply means making it more readable:

```ruby
def fib(n)
  if n <= -2
    (-1)**(n+1) * fib(n.abs)
  elsif n <= 1
    n.abs
  else
    fib(n-1) + fib(n-2)
  end
end
```

