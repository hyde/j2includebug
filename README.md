This demonstrates how mitsuhiko/jinja2#84 breaks certain includes.

Working
=======

```
mkvirtualenv j26
pip install jinja2==2.6
python gen.py
```

Output:

```
<h2>A</h2>
A, A, A
<h2>B</h2>
B, B, B
<h2>C</h2>
C, C, C
```

Breaking
========

```
mkvirtualenv j27
pip install jinja2==2.7
python gen.py
```

Error:

```
...
RuntimeError: maximum recursion depth exceeded while calling a Python object
```
