#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by Grako.
#
#    https://pypi.python.org/pypi/grako/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals

from grako.parsing import graken, Parser
from grako.util import re, RE_FLAGS  # noqa


__version__ = (2016, 3, 20, 11, 56, 3, 6)

__all__ = [
    'SSSLParser',
    'SSSLSemantics',
    'main'
]


class SSSLParser(Parser):
    def __init__(self,
                 whitespace=None,
                 nameguard=None,
                 comments_re=None,
                 eol_comments_re=None,
                 ignorecase=None,
                 left_recursion=True,
                 **kwargs):
        super(SSSLParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            **kwargs
        )

    @graken()
    def _START_(self):

        def block0():
            self._INSTR_()
        self._closure(block0)
        self._check_eof()

    @graken()
    def _INSTR_(self):
        with self._choice():
            with self._option():
                self._DECL_()
                self._cut()
            with self._option():
                self._AFFECT_()
            self._error('no available options')

    @graken()
    def _DECL_(self):
        pass
        self.ast['DECL'] = self.last_node
        self._type_()
        self.ast['TYPE'] = self.last_node
        self._nom_()
        self.ast['NAME'] = self.last_node
        self._token('=')
        self._expr_()
        self.ast['EXPR'] = self.last_node

        self.ast._define(
            ['DECL', 'TYPE', 'NAME', 'EXPR'],
            []
        )

    @graken()
    def _AFFECT_(self):
        pass
        self.ast['AFFECT'] = self.last_node
        self._nom_()
        self.ast['NAME'] = self.last_node
        self._token('=')
        self._expr_()
        self.ast['EXPR'] = self.last_node

        self.ast._define(
            ['AFFECT', 'NAME', 'EXPR'],
            []
        )

    @graken()
    def _expr_(self):
        with self._choice():
            with self._option():
                self._t_expr_()
                self._token('+')
                self._expr_()
            with self._option():
                self._t_expr_()
            self._error('no available options')

    @graken()
    def _t_expr_(self):
        with self._choice():
            with self._option():
                self._object_()
                self._cut()
            with self._option():
                self._f_nom_()
                self._cut()
            with self._option():
                self._f_val_()
            self._error('no available options')

    @graken()
    def _object_(self):
        self._nom_()
        self.ast['CLASS_N'] = self.last_node
        self._token('(')
        self._args_()
        self.ast['ARGS'] = self.last_node
        self._token(')')

        self.ast._define(
            ['CLASS_N', 'ARGS'],
            []
        )

    @graken()
    def _args_(self):
        with self._choice():
            with self._option():
                self._expr_()
                self.ast['EXPR'] = self.last_node
                self._token(',')
                self._expr_()
                self.ast['EXPR'] = self.last_node
                self._cut()
            with self._option():
                self._expr_()
                self.ast['EXPR'] = self.last_node
            self._error('no available options')

        self.ast._define(
            ['EXPR'],
            []
        )

    @graken()
    def _type_(self):
        with self._group():
            with self._choice():
                with self._option():
                    self._token('int')
                    self._cut()
                with self._option():
                    self._token('float')
                self._error('expecting one of: float int')

    @graken()
    def _nom_(self):
        self._pattern(r'[a-z]+')

    @graken()
    def _val_(self):
        self._pattern(r'[0-9]+')

    @graken()
    def _f_type_(self):
        self._type_()
        self.ast['TYPE'] = self.last_node

        self.ast._define(
            ['TYPE'],
            []
        )

    @graken()
    def _f_nom_(self):
        self._nom_()
        self.ast['NAME'] = self.last_node

        self.ast._define(
            ['NAME'],
            []
        )

    @graken()
    def _f_val_(self):
        self._val_()
        self.ast['VAL'] = self.last_node

        self.ast._define(
            ['VAL'],
            []
        )


class SSSLSemantics(object):
    def START(self, ast):
        return ast

    def INSTR(self, ast):
        return ast

    def DECL(self, ast):
        return ast

    def AFFECT(self, ast):
        return ast

    def expr(self, ast):
        return ast

    def t_expr(self, ast):
        return ast

    def object(self, ast):
        return ast

    def args(self, ast):
        return ast

    def type(self, ast):
        return ast

    def nom(self, ast):
        return ast

    def val(self, ast):
        return ast

    def f_type(self, ast):
        return ast

    def f_nom(self, ast):
        return ast

    def f_val(self, ast):
        return ast


def main(filename, startrule, trace=False, whitespace=None, nameguard=None):
    import json
    with open(filename) as f:
        text = f.read()
    parser = SSSLParser(parseinfo=False)
    ast = parser.parse(
        text,
        startrule,
        filename=filename,
        trace=trace,
        whitespace=whitespace,
        nameguard=nameguard)
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()

if __name__ == '__main__':
    import argparse
    import string
    import sys

    class ListRules(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            print('Rules:')
            for r in SSSLParser.rule_list():
                print(r)
            print()
            sys.exit(0)

    parser = argparse.ArgumentParser(description="Simple parser for SSSL.")
    parser.add_argument('-l', '--list', action=ListRules, nargs=0,
                        help="list all rules and exit")
    parser.add_argument('-n', '--no-nameguard', action='store_true',
                        dest='no_nameguard',
                        help="disable the 'nameguard' feature")
    parser.add_argument('-t', '--trace', action='store_true',
                        help="output trace information")
    parser.add_argument('-w', '--whitespace', type=str, default=string.whitespace,
                        help="whitespace specification")
    parser.add_argument('file', metavar="FILE", help="the input file to parse")
    parser.add_argument('startrule', metavar="STARTRULE",
                        help="the start rule for parsing")
    args = parser.parse_args()

    main(
        args.file,
        args.startrule,
        trace=args.trace,
        whitespace=args.whitespace,
        nameguard=not args.no_nameguard
    )