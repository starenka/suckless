# Unsorted utils for Python & Django

## line profiling

A decorator for easy line profiling. First import the decorator

`from suckless.debug import line_profile`

and use it:

    @line_profiler
    def foo():
        pass

## pdb & ipdb template filters

Add `suckless` to `INSTALLED_APPS`:

    INSTALLED_APPS += [
        'suckless',
    ]

in template you want to debug load suckless templatetags:

`{% load suckless %}`

using `pdb` or `ipdb` filter `{{ request|ipdb }}` will drop you into shell:

    > /....../suckless/templatetags/suckless.py(23)ipdb()
         22         ipdb.set_trace()
    ---> 23         return x  # <---- this is your filtered variable. Have fun'''
         24     return x

    ipdb> x
    MergeDict(<QueryDict: {}>, <QueryDict: {}>)
