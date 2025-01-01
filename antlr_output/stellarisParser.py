# Generated from stellaris.g4 by ANTLR 4.13.2
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
        4,1,14,94,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,5,0,26,8,0,10,0,
        12,0,29,9,0,1,0,1,0,1,1,4,1,34,8,1,11,1,12,1,35,1,2,1,2,5,2,40,8,
        2,10,2,12,2,43,9,2,1,2,1,2,1,3,1,3,3,3,49,8,3,1,4,1,4,1,4,1,4,3,
        4,55,8,4,1,5,1,5,1,5,1,5,3,5,61,8,5,1,6,1,6,1,7,1,7,3,7,67,8,7,1,
        7,1,7,1,8,1,8,1,8,1,8,5,8,75,8,8,10,8,12,8,78,9,8,1,9,1,9,5,9,82,
        8,9,10,9,12,9,85,9,9,1,9,3,9,88,8,9,1,9,1,9,1,10,1,10,1,10,0,0,11,
        0,2,4,6,8,10,12,14,16,18,20,0,3,1,0,1,3,1,0,4,6,1,0,9,11,98,0,27,
        1,0,0,0,2,33,1,0,0,0,4,37,1,0,0,0,6,48,1,0,0,0,8,54,1,0,0,0,10,56,
        1,0,0,0,12,62,1,0,0,0,14,64,1,0,0,0,16,70,1,0,0,0,18,79,1,0,0,0,
        20,91,1,0,0,0,22,26,3,2,1,0,23,26,5,13,0,0,24,26,5,14,0,0,25,22,
        1,0,0,0,25,23,1,0,0,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,
        27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,31,5,0,0,1,31,1,1,0,
        0,0,32,34,3,4,2,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,
        1,0,0,0,36,3,1,0,0,0,37,41,3,6,3,0,38,40,7,0,0,0,39,38,1,0,0,0,40,
        43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,
        0,44,45,3,8,4,0,45,5,1,0,0,0,46,49,3,20,10,0,47,49,3,10,5,0,48,46,
        1,0,0,0,48,47,1,0,0,0,49,7,1,0,0,0,50,55,3,20,10,0,51,55,3,10,5,
        0,52,55,3,14,7,0,53,55,3,18,9,0,54,50,1,0,0,0,54,51,1,0,0,0,54,52,
        1,0,0,0,54,53,1,0,0,0,55,9,1,0,0,0,56,57,3,20,10,0,57,60,3,12,6,
        0,58,61,3,10,5,0,59,61,3,20,10,0,60,58,1,0,0,0,60,59,1,0,0,0,61,
        11,1,0,0,0,62,63,7,1,0,0,63,13,1,0,0,0,64,66,5,7,0,0,65,67,3,16,
        8,0,66,65,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,68,69,5,8,0,0,69,15,
        1,0,0,0,70,76,3,20,10,0,71,75,3,20,10,0,72,75,5,14,0,0,73,75,5,13,
        0,0,74,71,1,0,0,0,74,72,1,0,0,0,74,73,1,0,0,0,75,78,1,0,0,0,76,74,
        1,0,0,0,76,77,1,0,0,0,77,17,1,0,0,0,78,76,1,0,0,0,79,87,5,7,0,0,
        80,82,3,2,1,0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,
        0,0,0,84,88,1,0,0,0,85,83,1,0,0,0,86,88,3,20,10,0,87,83,1,0,0,0,
        87,86,1,0,0,0,88,89,1,0,0,0,89,90,5,8,0,0,90,19,1,0,0,0,91,92,7,
        2,0,0,92,21,1,0,0,0,12,25,27,35,41,48,54,60,66,74,76,83,87
    ]

class stellarisParser ( Parser ):

    grammarFileName = "stellaris.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'>'", "'<'", "'.'", "'@'", "':'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDENTIFIER", "INTEGER", "STRING", "COMMENT", 
                      "SPACE", "NL" ]

    RULE_content = 0
    RULE_expr = 1
    RULE_keyval = 2
    RULE_key = 3
    RULE_val = 4
    RULE_attrib = 5
    RULE_accessor = 6
    RULE_array = 7
    RULE_array_elements = 8
    RULE_group = 9
    RULE_id_ = 10

    ruleNames =  [ "content", "expr", "keyval", "key", "val", "attrib", 
                   "accessor", "array", "array_elements", "group", "id_" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    IDENTIFIER=9
    INTEGER=10
    STRING=11
    COMMENT=12
    SPACE=13
    NL=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(stellarisParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellarisParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellarisParser.ExprContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(stellarisParser.SPACE)
            else:
                return self.getToken(stellarisParser.SPACE, i)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(stellarisParser.NL)
            else:
                return self.getToken(stellarisParser.NL, i)

        def getRuleIndex(self):
            return stellarisParser.RULE_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent" ):
                listener.enterContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent" ):
                listener.exitContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContent" ):
                return visitor.visitContent(self)
            else:
                return visitor.visitChildren(self)




    def content(self):

        localctx = stellarisParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 28160) != 0):
                self.state = 25
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [9, 10, 11]:
                    self.state = 22
                    self.expr()
                    pass
                elif token in [13]:
                    self.state = 23
                    self.match(stellarisParser.SPACE)
                    pass
                elif token in [14]:
                    self.state = 24
                    self.match(stellarisParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(stellarisParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyval(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellarisParser.KeyvalContext)
            else:
                return self.getTypedRuleContext(stellarisParser.KeyvalContext,i)


        def getRuleIndex(self):
            return stellarisParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = stellarisParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 32
                    self.keyval()

                else:
                    raise NoViableAltException(self)
                self.state = 35 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyvalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(stellarisParser.KeyContext,0)


        def val(self):
            return self.getTypedRuleContext(stellarisParser.ValContext,0)


        def getRuleIndex(self):
            return stellarisParser.RULE_keyval

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyval" ):
                listener.enterKeyval(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyval" ):
                listener.exitKeyval(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyval" ):
                return visitor.visitKeyval(self)
            else:
                return visitor.visitChildren(self)




    def keyval(self):

        localctx = stellarisParser.KeyvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_keyval)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.key()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 38
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(stellarisParser.Id_Context,0)


        def attrib(self):
            return self.getTypedRuleContext(stellarisParser.AttribContext,0)


        def getRuleIndex(self):
            return stellarisParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey" ):
                return visitor.visitKey(self)
            else:
                return visitor.visitChildren(self)




    def key(self):

        localctx = stellarisParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_key)
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.id_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.attrib()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(stellarisParser.Id_Context,0)


        def attrib(self):
            return self.getTypedRuleContext(stellarisParser.AttribContext,0)


        def array(self):
            return self.getTypedRuleContext(stellarisParser.ArrayContext,0)


        def group(self):
            return self.getTypedRuleContext(stellarisParser.GroupContext,0)


        def getRuleIndex(self):
            return stellarisParser.RULE_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVal" ):
                listener.enterVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVal" ):
                listener.exitVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal" ):
                return visitor.visitVal(self)
            else:
                return visitor.visitChildren(self)




    def val(self):

        localctx = stellarisParser.ValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_val)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.id_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.attrib()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.array()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.group()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttribContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellarisParser.Id_Context)
            else:
                return self.getTypedRuleContext(stellarisParser.Id_Context,i)


        def accessor(self):
            return self.getTypedRuleContext(stellarisParser.AccessorContext,0)


        def attrib(self):
            return self.getTypedRuleContext(stellarisParser.AttribContext,0)


        def getRuleIndex(self):
            return stellarisParser.RULE_attrib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttrib" ):
                listener.enterAttrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttrib" ):
                listener.exitAttrib(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrib" ):
                return visitor.visitAttrib(self)
            else:
                return visitor.visitChildren(self)




    def attrib(self):

        localctx = stellarisParser.AttribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.id_()
            self.state = 57
            self.accessor()
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 58
                self.attrib()
                pass

            elif la_ == 2:
                self.state = 59
                self.id_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccessorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellarisParser.RULE_accessor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessor" ):
                listener.enterAccessor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessor" ):
                listener.exitAccessor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccessor" ):
                return visitor.visitAccessor(self)
            else:
                return visitor.visitChildren(self)




    def accessor(self):

        localctx = stellarisParser.AccessorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_accessor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
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


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_elements(self):
            return self.getTypedRuleContext(stellarisParser.Array_elementsContext,0)


        def getRuleIndex(self):
            return stellarisParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = stellarisParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(stellarisParser.T__6)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0):
                self.state = 65
                self.array_elements()


            self.state = 68
            self.match(stellarisParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellarisParser.Id_Context)
            else:
                return self.getTypedRuleContext(stellarisParser.Id_Context,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(stellarisParser.NL)
            else:
                return self.getToken(stellarisParser.NL, i)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(stellarisParser.SPACE)
            else:
                return self.getToken(stellarisParser.SPACE, i)

        def getRuleIndex(self):
            return stellarisParser.RULE_array_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_elements" ):
                listener.enterArray_elements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_elements" ):
                listener.exitArray_elements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_elements" ):
                return visitor.visitArray_elements(self)
            else:
                return visitor.visitChildren(self)




    def array_elements(self):

        localctx = stellarisParser.Array_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.id_()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 28160) != 0):
                self.state = 74
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [9, 10, 11]:
                    self.state = 71
                    self.id_()
                    pass
                elif token in [14]:
                    self.state = 72
                    self.match(stellarisParser.NL)
                    pass
                elif token in [13]:
                    self.state = 73
                    self.match(stellarisParser.SPACE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(stellarisParser.Id_Context,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellarisParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellarisParser.ExprContext,i)


        def getRuleIndex(self):
            return stellarisParser.RULE_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup" ):
                listener.enterGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup" ):
                listener.exitGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroup" ):
                return visitor.visitGroup(self)
            else:
                return visitor.visitChildren(self)




    def group(self):

        localctx = stellarisParser.GroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(stellarisParser.T__6)
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0):
                    self.state = 80
                    self.expr()
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.state = 86
                self.id_()
                pass


            self.state = 89
            self.match(stellarisParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(stellarisParser.IDENTIFIER, 0)

        def STRING(self):
            return self.getToken(stellarisParser.STRING, 0)

        def INTEGER(self):
            return self.getToken(stellarisParser.INTEGER, 0)

        def getRuleIndex(self):
            return stellarisParser.RULE_id_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_" ):
                listener.enterId_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_" ):
                listener.exitId_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_" ):
                return visitor.visitId_(self)
            else:
                return visitor.visitChildren(self)




    def id_(self):

        localctx = stellarisParser.Id_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_id_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
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





