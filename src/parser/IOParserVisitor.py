# Generated from /home/ciprietti/Documents/olimpiadi-informatica/oliv/grammar/IOParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IOParser import IOParser
else:
    from IOParser import IOParser

# This class defines a complete generic visitor for a parse tree produced by IOParser.

class IOParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IOParser#sequence.
    def visitSequence(self, ctx:IOParser.SequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#unit.
    def visitUnit(self, ctx:IOParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#block.
    def visitBlock(self, ctx:IOParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#attributes.
    def visitAttributes(self, ctx:IOParser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#attribute.
    def visitAttribute(self, ctx:IOParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#edge.
    def visitEdge(self, ctx:IOParser.EdgeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#comparison.
    def visitComparison(self, ctx:IOParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#repeat.
    def visitRepeat(self, ctx:IOParser.RepeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#interval.
    def visitInterval(self, ctx:IOParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#arithExpr.
    def visitArithExpr(self, ctx:IOParser.ArithExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#addend.
    def visitAddend(self, ctx:IOParser.AddendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#term.
    def visitTerm(self, ctx:IOParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#reference.
    def visitReference(self, ctx:IOParser.ReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#literal.
    def visitLiteral(self, ctx:IOParser.LiteralContext):
        return self.visitChildren(ctx)



del IOParser