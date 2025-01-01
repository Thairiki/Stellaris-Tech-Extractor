# Generated from stellaris.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .stellarisParser import stellarisParser
else:
    from stellarisParser import stellarisParser

# This class defines a complete listener for a parse tree produced by stellarisParser.
class stellarisListener(ParseTreeListener):

    # Enter a parse tree produced by stellarisParser#content.
    def enterContent(self, ctx:stellarisParser.ContentContext):
        pass

    # Exit a parse tree produced by stellarisParser#content.
    def exitContent(self, ctx:stellarisParser.ContentContext):
        pass


    # Enter a parse tree produced by stellarisParser#expr.
    def enterExpr(self, ctx:stellarisParser.ExprContext):
        pass

    # Exit a parse tree produced by stellarisParser#expr.
    def exitExpr(self, ctx:stellarisParser.ExprContext):
        pass


    # Enter a parse tree produced by stellarisParser#keyval.
    def enterKeyval(self, ctx:stellarisParser.KeyvalContext):
        pass

    # Exit a parse tree produced by stellarisParser#keyval.
    def exitKeyval(self, ctx:stellarisParser.KeyvalContext):
        pass


    # Enter a parse tree produced by stellarisParser#key.
    def enterKey(self, ctx:stellarisParser.KeyContext):
        pass

    # Exit a parse tree produced by stellarisParser#key.
    def exitKey(self, ctx:stellarisParser.KeyContext):
        pass


    # Enter a parse tree produced by stellarisParser#val.
    def enterVal(self, ctx:stellarisParser.ValContext):
        pass

    # Exit a parse tree produced by stellarisParser#val.
    def exitVal(self, ctx:stellarisParser.ValContext):
        pass


    # Enter a parse tree produced by stellarisParser#attrib.
    def enterAttrib(self, ctx:stellarisParser.AttribContext):
        pass

    # Exit a parse tree produced by stellarisParser#attrib.
    def exitAttrib(self, ctx:stellarisParser.AttribContext):
        pass


    # Enter a parse tree produced by stellarisParser#accessor.
    def enterAccessor(self, ctx:stellarisParser.AccessorContext):
        pass

    # Exit a parse tree produced by stellarisParser#accessor.
    def exitAccessor(self, ctx:stellarisParser.AccessorContext):
        pass


    # Enter a parse tree produced by stellarisParser#array.
    def enterArray(self, ctx:stellarisParser.ArrayContext):
        pass

    # Exit a parse tree produced by stellarisParser#array.
    def exitArray(self, ctx:stellarisParser.ArrayContext):
        pass


    # Enter a parse tree produced by stellarisParser#array_elements.
    def enterArray_elements(self, ctx:stellarisParser.Array_elementsContext):
        pass

    # Exit a parse tree produced by stellarisParser#array_elements.
    def exitArray_elements(self, ctx:stellarisParser.Array_elementsContext):
        pass


    # Enter a parse tree produced by stellarisParser#group.
    def enterGroup(self, ctx:stellarisParser.GroupContext):
        pass

    # Exit a parse tree produced by stellarisParser#group.
    def exitGroup(self, ctx:stellarisParser.GroupContext):
        pass


    # Enter a parse tree produced by stellarisParser#id_.
    def enterId_(self, ctx:stellarisParser.Id_Context):
        pass

    # Exit a parse tree produced by stellarisParser#id_.
    def exitId_(self, ctx:stellarisParser.Id_Context):
        pass



del stellarisParser