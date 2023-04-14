# Generated from IOParser.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,48,163,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,5,0,31,8,0,10,0,12,0,34,9,0,1,1,1,1,1,1,1,1,1,1,3,1,41,8,
        1,1,1,1,1,1,1,1,1,1,1,3,1,48,8,1,3,1,50,8,1,1,2,1,2,1,2,1,2,1,2,
        3,2,57,8,2,1,3,1,3,1,3,5,3,62,8,3,10,3,12,3,65,9,3,1,4,1,4,1,4,4,
        4,70,8,4,11,4,12,4,71,1,4,3,4,75,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,91,8,4,11,4,12,4,92,1,4,1,4,3,4,
        97,8,4,1,5,1,5,1,5,1,5,3,5,103,8,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,
        7,3,7,113,8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,
        9,127,8,9,10,9,12,9,130,9,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,138,
        8,10,10,10,12,10,141,9,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,149,
        8,11,1,12,1,12,1,12,1,12,1,12,5,12,156,8,12,10,12,12,12,159,9,12,
        1,13,1,13,1,13,0,2,18,20,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        0,4,1,0,2,4,1,0,27,28,1,0,29,31,1,0,33,34,174,0,28,1,0,0,0,2,49,
        1,0,0,0,4,56,1,0,0,0,6,58,1,0,0,0,8,96,1,0,0,0,10,98,1,0,0,0,12,
        106,1,0,0,0,14,109,1,0,0,0,16,116,1,0,0,0,18,120,1,0,0,0,20,131,
        1,0,0,0,22,148,1,0,0,0,24,150,1,0,0,0,26,160,1,0,0,0,28,32,3,2,1,
        0,29,31,3,2,1,0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,
        1,0,0,0,33,1,1,0,0,0,34,32,1,0,0,0,35,50,5,45,0,0,36,50,3,26,13,
        0,37,40,3,4,2,0,38,39,5,43,0,0,39,41,3,14,7,0,40,38,1,0,0,0,40,41,
        1,0,0,0,41,47,1,0,0,0,42,43,5,42,0,0,43,44,5,39,0,0,44,45,3,6,3,
        0,45,46,5,40,0,0,46,48,1,0,0,0,47,42,1,0,0,0,47,48,1,0,0,0,48,50,
        1,0,0,0,49,35,1,0,0,0,49,36,1,0,0,0,49,37,1,0,0,0,50,3,1,0,0,0,51,
        57,5,14,0,0,52,53,5,39,0,0,53,54,3,0,0,0,54,55,5,40,0,0,55,57,1,
        0,0,0,56,51,1,0,0,0,56,52,1,0,0,0,57,5,1,0,0,0,58,63,3,8,4,0,59,
        60,5,41,0,0,60,62,3,8,4,0,61,59,1,0,0,0,62,65,1,0,0,0,63,61,1,0,
        0,0,63,64,1,0,0,0,64,7,1,0,0,0,65,63,1,0,0,0,66,74,5,1,0,0,67,69,
        5,35,0,0,68,70,7,0,0,0,69,68,1,0,0,0,70,71,1,0,0,0,71,69,1,0,0,0,
        71,72,1,0,0,0,72,73,1,0,0,0,73,75,5,36,0,0,74,67,1,0,0,0,74,75,1,
        0,0,0,75,97,1,0,0,0,76,97,5,5,0,0,77,78,5,6,0,0,78,90,5,35,0,0,79,
        80,5,8,0,0,80,81,5,32,0,0,81,91,3,16,8,0,82,83,5,9,0,0,83,84,5,32,
        0,0,84,91,3,10,5,0,85,91,5,10,0,0,86,91,5,7,0,0,87,91,5,11,0,0,88,
        91,5,12,0,0,89,91,5,13,0,0,90,79,1,0,0,0,90,82,1,0,0,0,90,85,1,0,
        0,0,90,86,1,0,0,0,90,87,1,0,0,0,90,88,1,0,0,0,90,89,1,0,0,0,91,92,
        1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,94,1,0,0,0,94,97,5,36,0,0,
        95,97,3,12,6,0,96,66,1,0,0,0,96,76,1,0,0,0,96,77,1,0,0,0,96,95,1,
        0,0,0,97,9,1,0,0,0,98,102,3,24,12,0,99,100,5,28,0,0,100,103,5,28,
        0,0,101,103,5,15,0,0,102,99,1,0,0,0,102,101,1,0,0,0,103,104,1,0,
        0,0,104,105,3,24,12,0,105,11,1,0,0,0,106,107,5,20,0,0,107,108,3,
        18,9,0,108,13,1,0,0,0,109,112,5,39,0,0,110,113,3,18,9,0,111,113,
        3,16,8,0,112,110,1,0,0,0,112,111,1,0,0,0,113,114,1,0,0,0,114,115,
        5,40,0,0,115,15,1,0,0,0,116,117,3,18,9,0,117,118,5,44,0,0,118,119,
        3,18,9,0,119,17,1,0,0,0,120,121,6,9,-1,0,121,122,3,20,10,0,122,128,
        1,0,0,0,123,124,10,1,0,0,124,125,7,1,0,0,125,127,3,20,10,0,126,123,
        1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,19,1,
        0,0,0,130,128,1,0,0,0,131,132,6,10,-1,0,132,133,3,22,11,0,133,139,
        1,0,0,0,134,135,10,1,0,0,135,136,7,2,0,0,136,138,3,22,11,0,137,134,
        1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,21,1,
        0,0,0,141,139,1,0,0,0,142,149,3,24,12,0,143,149,5,33,0,0,144,145,
        5,35,0,0,145,146,3,18,9,0,146,147,5,36,0,0,147,149,1,0,0,0,148,142,
        1,0,0,0,148,143,1,0,0,0,148,144,1,0,0,0,149,23,1,0,0,0,150,157,5,
        14,0,0,151,152,5,37,0,0,152,153,3,18,9,0,153,154,5,38,0,0,154,156,
        1,0,0,0,155,151,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,158,
        1,0,0,0,158,25,1,0,0,0,159,157,1,0,0,0,160,161,7,3,0,0,161,27,1,
        0,0,0,17,32,40,47,49,56,63,71,74,90,92,96,102,112,128,139,148,157
    ]

class IOParser ( Parser ):

    grammarFileName = "IOParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sorted'", "'asc'", "'desc'", "'strict'", 
                     "'distinct'", "'graph'", "'tree'", "'nodes'", "'edges'", 
                     "'connected'", "'line'", "'bipartite'", "'dag'", "<INVALID>", 
                     "'->'", "<INVALID>", "'~'", "'&'", "'|'", "<INVALID>", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'='", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "':'", 
                     "'_'", "'..'", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "SORTED", "ASC", "DESC", "STRICT", "DISTINCT", 
                      "GRAPH", "TREE", "NODES", "EDGES", "CONNECTED", "LINE", 
                      "BIPARTITE", "DAG", "IDENT", "ARROW", "BOOL_BIN_OP", 
                      "NOT", "AND", "OR", "COMP_OP", "EQ", "NOT_EQ", "LT", 
                      "LTE", "GT", "GTE", "PLUS", "MINUS", "MULT", "DIV", 
                      "MOD", "ASSIGN", "INT", "STR", "LPAREN", "RPAREN", 
                      "LBRACK", "RBRACK", "LBRACE", "RBRACE", "COMMA", "COLUMN", 
                      "UNDERSCORE", "DOTS", "NL", "WS", "INLINE_COMMENT", 
                      "BLOCK_COMMENT" ]

    RULE_sequence = 0
    RULE_unit = 1
    RULE_block = 2
    RULE_attributes = 3
    RULE_attribute = 4
    RULE_edge = 5
    RULE_comparison = 6
    RULE_repeat = 7
    RULE_interval = 8
    RULE_arithExpr = 9
    RULE_addend = 10
    RULE_term = 11
    RULE_reference = 12
    RULE_literal = 13

    ruleNames =  [ "sequence", "unit", "block", "attributes", "attribute", 
                   "edge", "comparison", "repeat", "interval", "arithExpr", 
                   "addend", "term", "reference", "literal" ]

    EOF = Token.EOF
    SORTED=1
    ASC=2
    DESC=3
    STRICT=4
    DISTINCT=5
    GRAPH=6
    TREE=7
    NODES=8
    EDGES=9
    CONNECTED=10
    LINE=11
    BIPARTITE=12
    DAG=13
    IDENT=14
    ARROW=15
    BOOL_BIN_OP=16
    NOT=17
    AND=18
    OR=19
    COMP_OP=20
    EQ=21
    NOT_EQ=22
    LT=23
    LTE=24
    GT=25
    GTE=26
    PLUS=27
    MINUS=28
    MULT=29
    DIV=30
    MOD=31
    ASSIGN=32
    INT=33
    STR=34
    LPAREN=35
    RPAREN=36
    LBRACK=37
    RBRACK=38
    LBRACE=39
    RBRACE=40
    COMMA=41
    COLUMN=42
    UNDERSCORE=43
    DOTS=44
    NL=45
    WS=46
    INLINE_COMMENT=47
    BLOCK_COMMENT=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IOParser.UnitContext)
            else:
                return self.getTypedRuleContext(IOParser.UnitContext,i)


        def getRuleIndex(self):
            return IOParser.RULE_sequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequence" ):
                listener.enterSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequence" ):
                listener.exitSequence(self)




    def sequence(self):

        localctx = IOParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sequence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.unit()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35759897722880) != 0):
                self.state = 29
                self.unit()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(IOParser.NL, 0)

        def literal(self):
            return self.getTypedRuleContext(IOParser.LiteralContext,0)


        def block(self):
            return self.getTypedRuleContext(IOParser.BlockContext,0)


        def UNDERSCORE(self):
            return self.getToken(IOParser.UNDERSCORE, 0)

        def repeat(self):
            return self.getTypedRuleContext(IOParser.RepeatContext,0)


        def COLUMN(self):
            return self.getToken(IOParser.COLUMN, 0)

        def LBRACE(self):
            return self.getToken(IOParser.LBRACE, 0)

        def attributes(self):
            return self.getTypedRuleContext(IOParser.AttributesContext,0)


        def RBRACE(self):
            return self.getToken(IOParser.RBRACE, 0)

        def getRuleIndex(self):
            return IOParser.RULE_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnit" ):
                listener.enterUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnit" ):
                listener.exitUnit(self)




    def unit(self):

        localctx = IOParser.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_unit)
        self._la = 0 # Token type
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(IOParser.NL)
                pass
            elif token in [33, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.literal()
                pass
            elif token in [14, 39]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.block()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==43:
                    self.state = 38
                    self.match(IOParser.UNDERSCORE)
                    self.state = 39
                    self.repeat()


                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 42
                    self.match(IOParser.COLUMN)
                    self.state = 43
                    self.match(IOParser.LBRACE)
                    self.state = 44
                    self.attributes()
                    self.state = 45
                    self.match(IOParser.RBRACE)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(IOParser.IDENT, 0)

        def LBRACE(self):
            return self.getToken(IOParser.LBRACE, 0)

        def sequence(self):
            return self.getTypedRuleContext(IOParser.SequenceContext,0)


        def RBRACE(self):
            return self.getToken(IOParser.RBRACE, 0)

        def getRuleIndex(self):
            return IOParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = IOParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(IOParser.IDENT)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(IOParser.LBRACE)
                self.state = 53
                self.sequence()
                self.state = 54
                self.match(IOParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IOParser.AttributeContext)
            else:
                return self.getTypedRuleContext(IOParser.AttributeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.COMMA)
            else:
                return self.getToken(IOParser.COMMA, i)

        def getRuleIndex(self):
            return IOParser.RULE_attributes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributes" ):
                listener.enterAttributes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributes" ):
                listener.exitAttributes(self)




    def attributes(self):

        localctx = IOParser.AttributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attributes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.attribute()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 59
                self.match(IOParser.COMMA)
                self.state = 60
                self.attribute()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SORTED(self):
            return self.getToken(IOParser.SORTED, 0)

        def LPAREN(self):
            return self.getToken(IOParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(IOParser.RPAREN, 0)

        def ASC(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.ASC)
            else:
                return self.getToken(IOParser.ASC, i)

        def DESC(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.DESC)
            else:
                return self.getToken(IOParser.DESC, i)

        def STRICT(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.STRICT)
            else:
                return self.getToken(IOParser.STRICT, i)

        def DISTINCT(self):
            return self.getToken(IOParser.DISTINCT, 0)

        def GRAPH(self):
            return self.getToken(IOParser.GRAPH, 0)

        def NODES(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.NODES)
            else:
                return self.getToken(IOParser.NODES, i)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.ASSIGN)
            else:
                return self.getToken(IOParser.ASSIGN, i)

        def interval(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IOParser.IntervalContext)
            else:
                return self.getTypedRuleContext(IOParser.IntervalContext,i)


        def EDGES(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.EDGES)
            else:
                return self.getToken(IOParser.EDGES, i)

        def edge(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IOParser.EdgeContext)
            else:
                return self.getTypedRuleContext(IOParser.EdgeContext,i)


        def CONNECTED(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.CONNECTED)
            else:
                return self.getToken(IOParser.CONNECTED, i)

        def TREE(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.TREE)
            else:
                return self.getToken(IOParser.TREE, i)

        def LINE(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.LINE)
            else:
                return self.getToken(IOParser.LINE, i)

        def BIPARTITE(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.BIPARTITE)
            else:
                return self.getToken(IOParser.BIPARTITE, i)

        def DAG(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.DAG)
            else:
                return self.getToken(IOParser.DAG, i)

        def comparison(self):
            return self.getTypedRuleContext(IOParser.ComparisonContext,0)


        def getRuleIndex(self):
            return IOParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)




    def attribute(self):

        localctx = IOParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(IOParser.SORTED)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 67
                    self.match(IOParser.LPAREN)
                    self.state = 69 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 68
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 71 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
                            break

                    self.state = 73
                    self.match(IOParser.RPAREN)


                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(IOParser.DISTINCT)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.match(IOParser.GRAPH)
                self.state = 78
                self.match(IOParser.LPAREN)
                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 90
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 79
                        self.match(IOParser.NODES)
                        self.state = 80
                        self.match(IOParser.ASSIGN)
                        self.state = 81
                        self.interval()
                        pass
                    elif token in [9]:
                        self.state = 82
                        self.match(IOParser.EDGES)
                        self.state = 83
                        self.match(IOParser.ASSIGN)
                        self.state = 84
                        self.edge()
                        pass
                    elif token in [10]:
                        self.state = 85
                        self.match(IOParser.CONNECTED)
                        pass
                    elif token in [7]:
                        self.state = 86
                        self.match(IOParser.TREE)
                        pass
                    elif token in [11]:
                        self.state = 87
                        self.match(IOParser.LINE)
                        pass
                    elif token in [12]:
                        self.state = 88
                        self.match(IOParser.BIPARTITE)
                        pass
                    elif token in [13]:
                        self.state = 89
                        self.match(IOParser.DAG)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 92 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 16256) != 0)):
                        break

                self.state = 94
                self.match(IOParser.RPAREN)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 95
                self.comparison()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdgeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IOParser.ReferenceContext)
            else:
                return self.getTypedRuleContext(IOParser.ReferenceContext,i)


        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.MINUS)
            else:
                return self.getToken(IOParser.MINUS, i)

        def ARROW(self):
            return self.getToken(IOParser.ARROW, 0)

        def getRuleIndex(self):
            return IOParser.RULE_edge

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdge" ):
                listener.enterEdge(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdge" ):
                listener.exitEdge(self)




    def edge(self):

        localctx = IOParser.EdgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_edge)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.reference()
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.state = 99
                self.match(IOParser.MINUS)
                self.state = 100
                self.match(IOParser.MINUS)
                pass
            elif token in [15]:
                self.state = 101
                self.match(IOParser.ARROW)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 104
            self.reference()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMP_OP(self):
            return self.getToken(IOParser.COMP_OP, 0)

        def arithExpr(self):
            return self.getTypedRuleContext(IOParser.ArithExprContext,0)


        def getRuleIndex(self):
            return IOParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = IOParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(IOParser.COMP_OP)
            self.state = 107
            self.arithExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(IOParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(IOParser.RBRACE, 0)

        def arithExpr(self):
            return self.getTypedRuleContext(IOParser.ArithExprContext,0)


        def interval(self):
            return self.getTypedRuleContext(IOParser.IntervalContext,0)


        def getRuleIndex(self):
            return IOParser.RULE_repeat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeat" ):
                listener.enterRepeat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeat" ):
                listener.exitRepeat(self)




    def repeat(self):

        localctx = IOParser.RepeatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_repeat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(IOParser.LBRACE)
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 110
                self.arithExpr(0)
                pass

            elif la_ == 2:
                self.state = 111
                self.interval()
                pass


            self.state = 114
            self.match(IOParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntervalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IOParser.ArithExprContext)
            else:
                return self.getTypedRuleContext(IOParser.ArithExprContext,i)


        def DOTS(self):
            return self.getToken(IOParser.DOTS, 0)

        def getRuleIndex(self):
            return IOParser.RULE_interval

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterval" ):
                listener.enterInterval(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterval" ):
                listener.exitInterval(self)




    def interval(self):

        localctx = IOParser.IntervalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_interval)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.arithExpr(0)
            self.state = 117
            self.match(IOParser.DOTS)
            self.state = 118
            self.arithExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addend(self):
            return self.getTypedRuleContext(IOParser.AddendContext,0)


        def arithExpr(self):
            return self.getTypedRuleContext(IOParser.ArithExprContext,0)


        def PLUS(self):
            return self.getToken(IOParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(IOParser.MINUS, 0)

        def getRuleIndex(self):
            return IOParser.RULE_arithExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithExpr" ):
                listener.enterArithExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithExpr" ):
                listener.exitArithExpr(self)



    def arithExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = IOParser.ArithExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_arithExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.addend(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = IOParser.ArithExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithExpr)
                    self.state = 123
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 124
                    _la = self._input.LA(1)
                    if not(_la==27 or _la==28):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 125
                    self.addend(0) 
                self.state = 130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AddendContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(IOParser.TermContext,0)


        def addend(self):
            return self.getTypedRuleContext(IOParser.AddendContext,0)


        def MULT(self):
            return self.getToken(IOParser.MULT, 0)

        def DIV(self):
            return self.getToken(IOParser.DIV, 0)

        def MOD(self):
            return self.getToken(IOParser.MOD, 0)

        def getRuleIndex(self):
            return IOParser.RULE_addend

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddend" ):
                listener.enterAddend(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddend" ):
                listener.exitAddend(self)



    def addend(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = IOParser.AddendContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_addend, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = IOParser.AddendContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_addend)
                    self.state = 134
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 135
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 136
                    self.term() 
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reference(self):
            return self.getTypedRuleContext(IOParser.ReferenceContext,0)


        def INT(self):
            return self.getToken(IOParser.INT, 0)

        def LPAREN(self):
            return self.getToken(IOParser.LPAREN, 0)

        def arithExpr(self):
            return self.getTypedRuleContext(IOParser.ArithExprContext,0)


        def RPAREN(self):
            return self.getToken(IOParser.RPAREN, 0)

        def getRuleIndex(self):
            return IOParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = IOParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_term)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.reference()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.match(IOParser.INT)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.match(IOParser.LPAREN)
                self.state = 145
                self.arithExpr(0)
                self.state = 146
                self.match(IOParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(IOParser.IDENT, 0)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.LBRACK)
            else:
                return self.getToken(IOParser.LBRACK, i)

        def arithExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IOParser.ArithExprContext)
            else:
                return self.getTypedRuleContext(IOParser.ArithExprContext,i)


        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.RBRACK)
            else:
                return self.getToken(IOParser.RBRACK, i)

        def getRuleIndex(self):
            return IOParser.RULE_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference" ):
                listener.enterReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference" ):
                listener.exitReference(self)




    def reference(self):

        localctx = IOParser.ReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(IOParser.IDENT)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 151
                    self.match(IOParser.LBRACK)
                    self.state = 152
                    self.arithExpr(0)
                    self.state = 153
                    self.match(IOParser.RBRACK) 
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(IOParser.INT, 0)

        def STR(self):
            return self.getToken(IOParser.STR, 0)

        def getRuleIndex(self):
            return IOParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = IOParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            _la = self._input.LA(1)
            if not(_la==33 or _la==34):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.arithExpr_sempred
        self._predicates[10] = self.addend_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithExpr_sempred(self, localctx:ArithExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def addend_sempred(self, localctx:AddendContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




