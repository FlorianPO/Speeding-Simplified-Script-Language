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
from grako.util import re, RE_FLAGS, generic_main  # noqa


__version__ = (2016, 3, 29, 11, 38, 47, 1)

__all__ = [
    'SSSLParser',
    'SSSLSemantics',
    'main'
]

KEYWORDS = set([])


class SSSLParser(Parser):
    def __init__(self,
                 whitespace=None,
                 nameguard=None,
                 comments_re=None,
                 eol_comments_re=None,
                 ignorecase=None,
                 left_recursion=True,
                 keywords=KEYWORDS,
                 **kwargs):
        super(SSSLParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            keywords=keywords,
            **kwargs
        )

    @graken()
    def _START_(self):

        def block0():
            self._DEFS_()
            self.add_last_node_to_name('DEFS')
        self._closure(block0)
        self._check_eof()

        self.ast._define(
            [],
            ['DEFS']
        )

    @graken()
    def _DEFS_(self):
        with self._choice():
            with self._option():
                self._DOBJT_()
                self.name_last_node('DOBJT')
            with self._option():
                self._DMAIN_()
                self.name_last_node('DFUNC')
            with self._option():
                self._DFUNC_()
                self.name_last_node('DFUNC')
            self._error('no available options')

        self.ast._define(
            ['DOBJT', 'DFUNC'],
            []
        )

    @graken()
    def _BLOCK_(self):
        self._token('{')
        with self._group():
            with self._choice():
                with self._option():

                    def block0():
                        self._INSTR_()
                        self.add_last_node_to_name('@')
                    self._positive_closure(block0)
                with self._option():
                    self._NULL_()
                    self.name_last_node('@')
                self._error('no available options')
        self._token('}')

    @graken()
    def _INSTR_(self):
        with self._choice():
            with self._option():
                self._DECLAFF_()
                self.name_last_node('DECLAFF')
            with self._option():
                self._DECL_()
                self.name_last_node('DECL')
            with self._option():
                self._AFF_()
                self.name_last_node('AFF')
            with self._option():
                self._CFUNC_()
                self.name_last_node('CFUNC')
            self._error('no available options')

        self.ast._define(
            ['DECLAFF', 'DECL', 'AFF', 'CFUNC'],
            []
        )

    @graken()
    def _DECL_(self):
        self._TYPE_()
        self.name_last_node('TYPE')
        self._nom_()
        self.name_last_node('NAME')

        self.ast._define(
            ['TYPE', 'NAME'],
            []
        )

    @graken()
    def _DECLAFF_(self):
        self._TYPE_()
        self.name_last_node('TYPE')
        self._nom_()
        self.name_last_node('NAME')
        self._token('=')
        self._EXPR_()
        self.name_last_node('EXPR')

        self.ast._define(
            ['TYPE', 'NAME', 'EXPR'],
            []
        )

    @graken()
    def _AFF_(self):
        self._nom_()
        self.name_last_node('NAME')
        self._token('=')
        self._EXPR_()
        self.name_last_node('EXPR')

        self.ast._define(
            ['NAME', 'EXPR'],
            []
        )

    @graken()
    def _CFUNC_(self):
        self._nom_()
        self.name_last_node('NAME')
        self._ARGS_()
        self.name_last_node('ARGS')

        self.ast._define(
            ['NAME', 'ARGS'],
            []
        )

    @graken()
    def _PARAM_(self):
        with self._choice():
            with self._option():
                self._token('(')
                self._EMPTY_()
                self.name_last_node('@')
                self._token(')')
            with self._option():
                self._token('(')
                with self._optional():
                    self.__TYPE_()
                    self.name_last_node('@')
                    self.__nom_()
                    self.name_last_node('@')

                    def block3():
                        self._token(',')
                        self.__TYPE_()
                        self.name_last_node('@')
                        self.__nom_()
                        self.name_last_node('@')
                    self._closure(block3)
                self._token(')')
            self._error('expecting one of: (')

    @graken()
    def _ARGS_(self):
        with self._choice():
            with self._option():
                self._token('(')
                self._EMPTY_()
                self.name_last_node('@')
                self._token(')')
            with self._option():
                self._token('(')
                with self._optional():
                    self.__EXPR_()
                    self.add_last_node_to_name('@')

                    def block2():
                        self._token(',')
                        self.__EXPR_()
                        self.add_last_node_to_name('@')
                    self._closure(block2)
                self._token(')')
            self._error('expecting one of: (')

    @graken()
    def _EMPTY_(self):
        self._empty_closure()

    @graken()
    def _DOBJT_(self):
        self._token('class')
        self._nom_()
        self.name_last_node('Name')
        self._token('{')

        def block1():
            self._DMEMB_()
            self.name_last_node('@')
        self._closure(block1)
        self._token('}')

        self.ast._define(
            ['Name'],
            []
        )

    @graken()
    def _DMEMB_(self):
        with self._choice():
            with self._option():
                self.__DFUNC_()
                self.name_last_node('@')
            with self._option():
                self.__DECLAFF_()
                self.name_last_node('@')
            with self._option():
                self.__DECL_()
                self.name_last_node('@')
            with self._option():
                self.__CSTR_()
                self.name_last_node('@')
            self._error('no available options')

    @graken()
    def _DFUNC_(self):
        self._token('func')
        self._TYPE_()
        self.name_last_node('TYPE')
        self._nom_()
        self.name_last_node('NAME')
        self._PARAM_()
        self.name_last_node('PARAM')
        self._BLOCK_()
        self.name_last_node('BLOCK')

        self.ast._define(
            ['TYPE', 'NAME', 'PARAM', 'BLOCK'],
            []
        )

    @graken()
    def _DMAIN_(self):
        self._TYPE_()
        self.name_last_node('TYPE')
        self._token('Main')
        self.name_last_node('NAME')
        self._PARAM_()
        self.name_last_node('PARAM')
        self._BLOCK_()
        self.name_last_node('BLOCK')

        self.ast._define(
            ['TYPE', 'NAME', 'PARAM', 'BLOCK'],
            []
        )

    @graken()
    def _CSTR_(self):
        self._nom_()
        self.name_last_node('NAME')
        self._PARAM_()
        self.name_last_node('PARAM')
        self._BLOCK_()
        self.name_last_node('BLOCK')

        self.ast._define(
            ['NAME', 'PARAM', 'BLOCK'],
            []
        )

    @graken()
    def _TYPE_(self):
        with self._choice():
            with self._option():
                self._token('int')
            with self._option():
                self._token('float')
            with self._option():
                self._token('string')
            with self._option():
                self._token('void')
            self._error('expecting one of: float int string void')

    @graken()
    def _OPER_(self):
        with self._choice():
            with self._option():
                self._token('+')
            with self._option():
                self._token('-')
            with self._option():
                self._token('*')
            with self._option():
                self._token('*')
            self._error('expecting one of: * + -')

    @graken()
    def __EXPR_(self):
        self._EXPR_()
        self.name_last_node('EXPR')

        self.ast._define(
            ['EXPR'],
            []
        )

    @graken()
    def _EXPR_(self):
        with self._choice():
            with self._option():
                self._t_EXPR_()
                self.name_last_node('@')
                self._OPER_()
                self.name_last_node('@')
                self._EXPR_()
                self.name_last_node('@')
            with self._option():
                self._t_EXPR_()
                self.name_last_node('@')
            self._error('no available options')

    @graken()
    def _t_EXPR_(self):
        with self._choice():
            with self._option():
                self._CFUNC_()
                self.name_last_node('CFUNC')
            with self._option():
                self._nom_()
                self.name_last_node('NAME')
            with self._option():
                self._val_()
                self.name_last_node('VAL')
            self._error('no available options')

        self.ast._define(
            ['CFUNC', 'NAME', 'VAL'],
            []
        )

    @graken()
    def _nom_(self):
        self._pattern(r'[a-zA-Z_]+')

    @graken()
    def _tout_(self):
        self._pattern(r'[0-9a-zA-Z_]+')

    @graken()
    def _val_(self):
        self._pattern(r'[0-9]+')

    @graken()
    def _NULL_(self):
        pass
        self.name_last_node('@')

    @graken()
    def __DFUNC_(self):
        self._DFUNC_()
        self.name_last_node('DFUNC')

        self.ast._define(
            ['DFUNC'],
            []
        )

    @graken()
    def __DECLAFF_(self):
        self._DECLAFF_()
        self.name_last_node('DECLAFF')

        self.ast._define(
            ['DECLAFF'],
            []
        )

    @graken()
    def __DECL_(self):
        self._DECL_()
        self.name_last_node('DECL')

        self.ast._define(
            ['DECL'],
            []
        )

    @graken()
    def __TYPE_(self):
        self._TYPE_()
        self.name_last_node('TYPE')

        self.ast._define(
            ['TYPE'],
            []
        )

    @graken()
    def __nom_(self):
        self._nom_()
        self.name_last_node('NAME')

        self.ast._define(
            ['NAME'],
            []
        )

    @graken()
    def __CSTR_(self):
        self._CSTR_()
        self.name_last_node('CSTR')

        self.ast._define(
            ['CSTR'],
            []
        )


class SSSLSemantics(object):
    def START(self, ast):
        return ast

    def DEFS(self, ast):
        return ast

    def BLOCK(self, ast):
        return ast

    def INSTR(self, ast):
        return ast

    def DECL(self, ast):
        return ast

    def DECLAFF(self, ast):
        return ast

    def AFF(self, ast):
        return ast

    def CFUNC(self, ast):
        return ast

    def PARAM(self, ast):
        return ast

    def ARGS(self, ast):
        return ast

    def EMPTY(self, ast):
        return ast

    def DOBJT(self, ast):
        return ast

    def DMEMB(self, ast):
        return ast

    def DFUNC(self, ast):
        return ast

    def DMAIN(self, ast):
        return ast

    def CSTR(self, ast):
        return ast

    def TYPE(self, ast):
        return ast

    def OPER(self, ast):
        return ast

    def _EXPR(self, ast):
        return ast

    def EXPR(self, ast):
        return ast

    def t_EXPR(self, ast):
        return ast

    def nom(self, ast):
        return ast

    def tout(self, ast):
        return ast

    def val(self, ast):
        return ast

    def NULL(self, ast):
        return ast

    def _DFUNC(self, ast):
        return ast

    def _DECLAFF(self, ast):
        return ast

    def _DECL(self, ast):
        return ast

    def _TYPE(self, ast):
        return ast

    def _nom(self, ast):
        return ast

    def _CSTR(self, ast):
        return ast


def main(
        filename,
        startrule,
        trace=False,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        left_recursion=True,
        **kwargs):

    with open(filename) as f:
        text = f.read()
    parser = SSSLParser(parseinfo=False)
    ast = parser.parse(
        text,
        startrule,
        filename=filename,
        trace=trace,
        whitespace=whitespace,
        nameguard=nameguard,
        ignorecase=ignorecase,
        **kwargs)
    return ast

if __name__ == '__main__':
    import json
    ast = generic_main(main, SSSLParser, name='SSSL')
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()
