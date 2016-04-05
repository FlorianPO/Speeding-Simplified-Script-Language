# -*- coding: utf-8 -*-

# FUNCTIONS _______________________________
def revDict(dict, value):
    for k, v in dict.items():
        if v == value:
            return k