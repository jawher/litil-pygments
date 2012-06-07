# -*- coding: utf-8 -*-

import re

from pygments.lexer import Lexer, RegexLexer, bygroups, include, do_insertions
from pygments.token import Text, Comment, Operator, Keyword, Name, \
     String, Number, Punctuation, Literal, Generic, Error

class LitilLexer(RegexLexer):
    name = 'Litil'
    aliases = ['litil']
    filenames = ['*.ltl']

    keywords = [
      'let', 'if', 'then', 'else', 'match', 'data', 'try',
      'catch', 'exception', 'throw', 'true', 'false'
    ]
    keyopts = [
      '=','\(','\)','\*','\+',',','-','/', '=>'
      '->','\.',':','<','::',
      '>','\[','\\\\',
      '\]','{','\|','}'
    ]

    word_operators = ['and', 'or', 'not']
    primitives = ['Number', 'Boolean', 'String', 'Char']

    tokens = {
        'escape-sequence': [
            (r'\\[\\\"\'ntbr]', String.Escape),
            (r'\\[0-9]{3}', String.Escape),
            (r'\\x[0-9a-fA-F]{2}', String.Escape),
        ],
        'root': [
            (r'\s+', Text),
            (r'false|true|\(\)|\[\]', Name.Builtin.Pseudo),
            (r'\b([A-Z][A-Za-z0-9_\']*)', Name.Class),
            (r'\-\-.*$', Comment),
            (r'\b(%s)\b' % '|'.join(keywords), Keyword),
            (r'(%s)' % '|'.join(keyopts[::-1]), Operator),
            (r'\b(%s)\b' % '|'.join(word_operators), Operator.Word),
            (r'\b(%s)\b' % '|'.join(primitives), Keyword.Type),
            (r"[^\W\d][\w']*", Name),
            (r'\d[\d_]*', Number.Integer),
            (r"'(?:(\\[\\\"'ntbr ])|(\\[0-9]{3})|(\\x[0-9a-fA-F]{2}))'",
             String.Char),
            (r"'.'", String.Char),
            (r'"', String.Double, 'string'),
            (r'[~?][a-z][\w\']*:', Name.Variable),
        ],
        'string': [
            (r'[^\\"]+', String.Double),
            include('escape-sequence'),
            (r'\\\n', String.Double),
            (r'"', String.Double, '#pop'),
        ],
    }