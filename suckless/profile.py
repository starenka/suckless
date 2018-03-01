#!/usr/bin/env python
# coding=utf-8

from memory_profiler import profile as memory_profiler


def line_profiler(view=None, extra_view=None):
    # https://djangosnippets.org/snippets/10483/
    import line_profiler

    def wrapper(view):
        def wrapped(*args, **kwargs):
            prof = line_profiler.LineProfiler()
            prof.add_function(view)
            if extra_view:
                [prof.add_function(v) for v in extra_view]
            with prof:
                resp = view(*args, **kwargs)
            prof.print_stats()
            return resp
        return wrapped
    if view:
        return wrapper(view)
    return wrapper
