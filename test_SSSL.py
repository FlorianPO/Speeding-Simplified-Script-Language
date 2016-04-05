# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from parser_SSSL import SSSLParser

import sys
import json

import grako
from grako.codegen import codegen

def main():
	parser = SSSLParser(trace=True, nameguard=False)
	
	f = open('programme.sssl', 'r')
	
	ast = parser.parse(f.read(), rule_name='START')
	print(json.dumps(ast, indent=2))

if __name__ == '__main__':
    main()
