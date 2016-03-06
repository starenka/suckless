#!/usr/bin/env python
# coding=utf-8
from django import template
from django.conf import settings

register = template.Library()


@register.filter
def pdb(x):
    if settings.DEBUG:
        import pdb
        pdb.set_trace()
        return x  # <---- this is your filtered variable. Have fun'''
    return x


@register.filter
def ipdb(x):
    if settings.DEBUG:
        import ipdb
        ipdb.set_trace()
        return x  # <---- this is your filtered variable. Have fun'''
    return x
