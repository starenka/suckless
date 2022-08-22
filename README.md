# Unsorted utils for Python & Django dev

## line profiling

A decorator for easy line profiling. First import the decorator.

`from suckless.profile import line_profiler`

Use it like this:

    ```
    @line_profiler
    def foo():
        _ = [one for one in xrange(20000)]
        time.sleep(10)
        _ = 100**400
    ```

and check the spitted output:

    ```
    Timer unit: 1e-06 s

    Total time: 10.0388 s
    File: foo.py
    Function: foo at line 8

    Line #      Hits         Time  Per Hit   % Time  Line Contents
    ==============================================================
         8                                           @line_profiler
         9                                           def foo():
        10     20001        33403      1.7      0.3      _ = [one for one in xrange(20000)]
        11         1     10004643 10004643.0     99.7      time.sleep(10)
        12         1          783    783.0      0.0      _ = 100**400
    ```


## memory profiling

A decorator for easy memory profiling. First import the decorator.

`from suckless.profile import memory_profiler`

Use it like this:

    ```
    @memory_profiler
    def foo():
        _ = [one for one in xrange(20000)]
        time.sleep(10)
        _ = 100**400
    ```

and check the spitted output:

```
   python foo.py 
   Timer unit: 1e-06 s

   Total time: 10.0153 s
   File: foo.py
   Function: foo at line 8

   Line #      Hits         Time  Per Hit   % Time  Line Contents
   ==============================================================
     8                                           @line_profiler
     9                                           def foo():
    10     20001       8148.0      0.4      0.1      _ = [one for one in xrange(20000)]
    11         1   10006747.0 10006747.0     99.9      time.sleep(10)
    12         1        392.0    392.0      0.0      _ = 100**400

```

  

## pdb & ipdb template filters

Add `suckless` to `INSTALLED_APPS`:

    INSTALLED_APPS += [
        'suckless',
    ]

in template you want to debug load suckless templatetags:

`{% load suckless %}`

using `pdb` or `ipdb` filter `{{ request|ipdb }}` will drop you into shell:

    22         ipdb.set_trace()
    ---> 23         return x  # <---- this is your filtered variable. Have fun!
         24     return x

    ipdb> x
    MergeDict(<QueryDict: {}>, <QueryDict: {}>)
