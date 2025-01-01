# Generated from stellaris.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .stellarisParser import stellarisParser
else:
    from stellarisParser import stellarisParser

# This class defines a complete generic visitor for a parse tree produced by stellarisParser.

class stellarisVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by stellarisParser#content.
    def visitContent(self, ctx:stellarisParser.ContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellarisParser#expr.
    def visitExpr(self, ctx:stellarisParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellarisParser#keyval.
    def visitKeyval(self, ctx:stellarisParser.KeyvalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellarisParser#key.
    def visitKey(self, ctx:stellarisParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellarisParser#val.
    def visitVal(self, ctx:stellarisParser.ValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellarisParser#attrib.
    def visitAttrib(self, ctx:stellarisParser.AttribContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellarisParser#accessor.
    def visitAccessor(self, ctx:stellarisParser.AccessorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellarisParser#array.
    def visitArray(self, ctx:stellarisParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellarisParser#array_elements.
    def visitArray_elements(self, ctx:stellarisParser.Array_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellarisParser#group.
    def visitGroup(self, ctx:stellarisParser.GroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellarisParser#id_.
    def visitId_(self, ctx:stellarisParser.Id_Context):
        return self.visitChildren(ctx)



del stellarisParser