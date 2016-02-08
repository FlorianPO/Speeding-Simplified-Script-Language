# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from parser_SSSL import SSSLParser

import sys

import grako
from grako.codegen import codegen

def main():
	parser = SSSLParser()
	ast = parser.parse('int a = c', rule_name='START')
	print(ast)

if __name__ == '__main__':
    main()
