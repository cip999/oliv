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
        4,1,48,176,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,1,1,1,
        1,1,1,1,1,1,3,1,45,8,1,1,1,1,1,1,1,1,1,1,1,3,1,52,8,1,3,1,54,8,1,
        1,2,1,2,1,2,1,2,3,2,60,8,2,1,2,1,2,1,2,1,2,3,2,66,8,2,1,3,1,3,1,
        3,5,3,71,8,3,10,3,12,3,74,9,3,1,4,1,4,1,4,4,4,79,8,4,11,4,12,4,80,
        1,4,3,4,84,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,4,4,100,8,4,11,4,12,4,101,1,4,1,4,3,4,106,8,4,1,5,1,5,1,5,
        1,5,3,5,112,8,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,3,7,122,8,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,136,8,9,10,9,12,
        9,139,9,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,147,8,10,10,10,12,10,
        150,9,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,158,8,11,1,12,1,12,1,
        12,1,12,1,12,5,12,165,8,12,10,12,12,12,168,9,12,1,13,1,13,1,14,1,
        14,1,15,1,15,1,15,0,2,18,20,16,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,0,6,1,0,3,5,1,0,26,27,1,0,28,30,1,0,32,34,1,0,18,19,1,0,
        20,25,186,0,32,1,0,0,0,2,53,1,0,0,0,4,65,1,0,0,0,6,67,1,0,0,0,8,
        105,1,0,0,0,10,107,1,0,0,0,12,115,1,0,0,0,14,118,1,0,0,0,16,125,
        1,0,0,0,18,129,1,0,0,0,20,140,1,0,0,0,22,157,1,0,0,0,24,159,1,0,
        0,0,26,169,1,0,0,0,28,171,1,0,0,0,30,173,1,0,0,0,32,36,3,2,1,0,33,
        35,3,2,1,0,34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,
        0,37,1,1,0,0,0,38,36,1,0,0,0,39,54,5,45,0,0,40,54,3,26,13,0,41,44,
        3,4,2,0,42,43,5,43,0,0,43,45,3,14,7,0,44,42,1,0,0,0,44,45,1,0,0,
        0,45,51,1,0,0,0,46,47,5,42,0,0,47,48,5,39,0,0,48,49,3,6,3,0,49,50,
        5,40,0,0,50,52,1,0,0,0,51,46,1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,
        53,39,1,0,0,0,53,40,1,0,0,0,53,41,1,0,0,0,54,3,1,0,0,0,55,59,5,15,
        0,0,56,57,5,22,0,0,57,58,5,1,0,0,58,60,5,24,0,0,59,56,1,0,0,0,59,
        60,1,0,0,0,60,66,1,0,0,0,61,62,5,39,0,0,62,63,3,0,0,0,63,64,5,40,
        0,0,64,66,1,0,0,0,65,55,1,0,0,0,65,61,1,0,0,0,66,5,1,0,0,0,67,72,
        3,8,4,0,68,69,5,41,0,0,69,71,3,8,4,0,70,68,1,0,0,0,71,74,1,0,0,0,
        72,70,1,0,0,0,72,73,1,0,0,0,73,7,1,0,0,0,74,72,1,0,0,0,75,83,5,2,
        0,0,76,78,5,35,0,0,77,79,7,0,0,0,78,77,1,0,0,0,79,80,1,0,0,0,80,
        78,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,84,5,36,0,0,83,76,1,0,
        0,0,83,84,1,0,0,0,84,106,1,0,0,0,85,106,5,6,0,0,86,87,5,7,0,0,87,
        99,5,35,0,0,88,89,5,9,0,0,89,90,5,31,0,0,90,100,3,16,8,0,91,92,5,
        10,0,0,92,93,5,31,0,0,93,100,3,10,5,0,94,100,5,11,0,0,95,100,5,8,
        0,0,96,100,5,12,0,0,97,100,5,13,0,0,98,100,5,14,0,0,99,88,1,0,0,
        0,99,91,1,0,0,0,99,94,1,0,0,0,99,95,1,0,0,0,99,96,1,0,0,0,99,97,
        1,0,0,0,99,98,1,0,0,0,100,101,1,0,0,0,101,99,1,0,0,0,101,102,1,0,
        0,0,102,103,1,0,0,0,103,106,5,36,0,0,104,106,3,12,6,0,105,75,1,0,
        0,0,105,85,1,0,0,0,105,86,1,0,0,0,105,104,1,0,0,0,106,9,1,0,0,0,
        107,111,3,24,12,0,108,109,5,27,0,0,109,112,5,27,0,0,110,112,5,16,
        0,0,111,108,1,0,0,0,111,110,1,0,0,0,112,113,1,0,0,0,113,114,3,24,
        12,0,114,11,1,0,0,0,115,116,3,30,15,0,116,117,3,18,9,0,117,13,1,
        0,0,0,118,121,5,39,0,0,119,122,3,18,9,0,120,122,3,16,8,0,121,119,
        1,0,0,0,121,120,1,0,0,0,122,123,1,0,0,0,123,124,5,40,0,0,124,15,
        1,0,0,0,125,126,3,18,9,0,126,127,5,44,0,0,127,128,3,18,9,0,128,17,
        1,0,0,0,129,130,6,9,-1,0,130,131,3,20,10,0,131,137,1,0,0,0,132,133,
        10,1,0,0,133,134,7,1,0,0,134,136,3,20,10,0,135,132,1,0,0,0,136,139,
        1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,19,1,0,0,0,139,137,1,
        0,0,0,140,141,6,10,-1,0,141,142,3,22,11,0,142,148,1,0,0,0,143,144,
        10,1,0,0,144,145,7,2,0,0,145,147,3,22,11,0,146,143,1,0,0,0,147,150,
        1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,21,1,0,0,0,150,148,1,
        0,0,0,151,158,3,24,12,0,152,158,5,33,0,0,153,154,5,35,0,0,154,155,
        3,18,9,0,155,156,5,36,0,0,156,158,1,0,0,0,157,151,1,0,0,0,157,152,
        1,0,0,0,157,153,1,0,0,0,158,23,1,0,0,0,159,166,5,15,0,0,160,161,
        5,37,0,0,161,162,3,18,9,0,162,163,5,38,0,0,163,165,1,0,0,0,164,160,
        1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,25,1,
        0,0,0,168,166,1,0,0,0,169,170,7,3,0,0,170,27,1,0,0,0,171,172,7,4,
        0,0,172,29,1,0,0,0,173,174,7,5,0,0,174,31,1,0,0,0,18,36,44,51,53,
        59,65,72,80,83,99,101,105,111,121,137,148,157,166
    ]

class IOParser ( Parser ):

    grammarFileName = "IOParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'sorted'", "'asc'", "'desc'", 
                     "'strict'", "'distinct'", "'graph'", "'tree'", "'nodes'", 
                     "'edges'", "'connected'", "'line'", "'bipartite'", 
                     "'dag'", "<INVALID>", "'->'", "'~'", "'&'", "'|'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'='", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "','", "':'", "'_'", "'..'", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "TYPE", "SORTED", "ASC", "DESC", "STRICT", 
                      "DISTINCT", "GRAPH", "TREE", "NODES", "EDGES", "CONNECTED", 
                      "LINE", "BIPARTITE", "DAG", "IDENT", "ARROW", "NOT", 
                      "AND", "OR", "EQ", "NOT_EQ", "LT", "LTE", "GT", "GTE", 
                      "PLUS", "MINUS", "MULT", "DIV", "MOD", "ASSIGN", "FLOAT", 
                      "INT", "STR", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
                      "LBRACE", "RBRACE", "COMMA", "COLUMN", "UNDERSCORE", 
                      "DOTS", "NL", "WS", "INLINE_COMMENT", "BLOCK_COMMENT" ]

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
    RULE_boolBinOp = 14
    RULE_compOp = 15

    ruleNames =  [ "sequence", "unit", "block", "attributes", "attribute", 
                   "edge", "comparison", "repeat", "interval", "arithExpr", 
                   "addend", "term", "reference", "literal", "boolBinOp", 
                   "compOp" ]

    EOF = Token.EOF
    TYPE=1
    SORTED=2
    ASC=3
    DESC=4
    STRICT=5
    DISTINCT=6
    GRAPH=7
    TREE=8
    NODES=9
    EDGES=10
    CONNECTED=11
    LINE=12
    BIPARTITE=13
    DAG=14
    IDENT=15
    ARROW=16
    NOT=17
    AND=18
    OR=19
    EQ=20
    NOT_EQ=21
    LT=22
    LTE=23
    GT=24
    GTE=25
    PLUS=26
    MINUS=27
    MULT=28
    DIV=29
    MOD=30
    ASSIGN=31
    FLOAT=32
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
            self.state = 32
            self.unit()
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35764192706560) != 0):
                self.state = 33
                self.unit()
                self.state = 38
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
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(IOParser.NL)
                pass
            elif token in [32, 33, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.literal()
                pass
            elif token in [15, 39]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.block()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==43:
                    self.state = 42
                    self.match(IOParser.UNDERSCORE)
                    self.state = 43
                    self.repeat()


                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 46
                    self.match(IOParser.COLUMN)
                    self.state = 47
                    self.match(IOParser.LBRACE)
                    self.state = 48
                    self.attributes()
                    self.state = 49
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

        def LT(self):
            return self.getToken(IOParser.LT, 0)

        def TYPE(self):
            return self.getToken(IOParser.TYPE, 0)

        def GT(self):
            return self.getToken(IOParser.GT, 0)

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
        self._la = 0 # Token type
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(IOParser.IDENT)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 56
                    self.match(IOParser.LT)
                    self.state = 57
                    self.match(IOParser.TYPE)
                    self.state = 58
                    self.match(IOParser.GT)


                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(IOParser.LBRACE)
                self.state = 62
                self.sequence()
                self.state = 63
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
            self.state = 67
            self.attribute()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 68
                self.match(IOParser.COMMA)
                self.state = 69
                self.attribute()
                self.state = 74
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
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(IOParser.SORTED)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 76
                    self.match(IOParser.LPAREN)
                    self.state = 78 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 77
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 80 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                            break

                    self.state = 82
                    self.match(IOParser.RPAREN)


                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(IOParser.DISTINCT)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.match(IOParser.GRAPH)
                self.state = 87
                self.match(IOParser.LPAREN)
                self.state = 99 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 99
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [9]:
                        self.state = 88
                        self.match(IOParser.NODES)
                        self.state = 89
                        self.match(IOParser.ASSIGN)
                        self.state = 90
                        self.interval()
                        pass
                    elif token in [10]:
                        self.state = 91
                        self.match(IOParser.EDGES)
                        self.state = 92
                        self.match(IOParser.ASSIGN)
                        self.state = 93
                        self.edge()
                        pass
                    elif token in [11]:
                        self.state = 94
                        self.match(IOParser.CONNECTED)
                        pass
                    elif token in [8]:
                        self.state = 95
                        self.match(IOParser.TREE)
                        pass
                    elif token in [12]:
                        self.state = 96
                        self.match(IOParser.LINE)
                        pass
                    elif token in [13]:
                        self.state = 97
                        self.match(IOParser.BIPARTITE)
                        pass
                    elif token in [14]:
                        self.state = 98
                        self.match(IOParser.DAG)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 101 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 32512) != 0)):
                        break

                self.state = 103
                self.match(IOParser.RPAREN)
                pass
            elif token in [20, 21, 22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
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
            self.state = 107
            self.reference()
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.state = 108
                self.match(IOParser.MINUS)
                self.state = 109
                self.match(IOParser.MINUS)
                pass
            elif token in [16]:
                self.state = 110
                self.match(IOParser.ARROW)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 113
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

        def compOp(self):
            return self.getTypedRuleContext(IOParser.CompOpContext,0)


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
            self.state = 115
            self.compOp()
            self.state = 116
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
            self.state = 118
            self.match(IOParser.LBRACE)
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 119
                self.arithExpr(0)
                pass

            elif la_ == 2:
                self.state = 120
                self.interval()
                pass


            self.state = 123
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
            self.state = 125
            self.arithExpr(0)
            self.state = 126
            self.match(IOParser.DOTS)
            self.state = 127
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
            self.state = 130
            self.addend(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = IOParser.ArithExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithExpr)
                    self.state = 132
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 133
                    _la = self._input.LA(1)
                    if not(_la==26 or _la==27):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 134
                    self.addend(0) 
                self.state = 139
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
            self.state = 141
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 148
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = IOParser.AddendContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_addend)
                    self.state = 143
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 144
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 145
                    self.term() 
                self.state = 150
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.reference()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(IOParser.INT)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.match(IOParser.LPAREN)
                self.state = 154
                self.arithExpr(0)
                self.state = 155
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
            self.state = 159
            self.match(IOParser.IDENT)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 160
                    self.match(IOParser.LBRACK)
                    self.state = 161
                    self.arithExpr(0)
                    self.state = 162
                    self.match(IOParser.RBRACK) 
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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

        def FLOAT(self):
            return self.getToken(IOParser.FLOAT, 0)

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
            self.state = 169
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30064771072) != 0)):
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


    class BoolBinOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(IOParser.AND, 0)

        def OR(self):
            return self.getToken(IOParser.OR, 0)

        def getRuleIndex(self):
            return IOParser.RULE_boolBinOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolBinOp" ):
                listener.enterBoolBinOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolBinOp" ):
                listener.exitBoolBinOp(self)




    def boolBinOp(self):

        localctx = IOParser.BoolBinOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_boolBinOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            _la = self._input.LA(1)
            if not(_la==18 or _la==19):
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


    class CompOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(IOParser.EQ, 0)

        def NOT_EQ(self):
            return self.getToken(IOParser.NOT_EQ, 0)

        def LT(self):
            return self.getToken(IOParser.LT, 0)

        def LTE(self):
            return self.getToken(IOParser.LTE, 0)

        def GT(self):
            return self.getToken(IOParser.GT, 0)

        def GTE(self):
            return self.getToken(IOParser.GTE, 0)

        def getRuleIndex(self):
            return IOParser.RULE_compOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompOp" ):
                listener.enterCompOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompOp" ):
                listener.exitCompOp(self)




    def compOp(self):

        localctx = IOParser.CompOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_compOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
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
         




