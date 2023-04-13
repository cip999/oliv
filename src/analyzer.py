from antlr4 import InputStream, CommonTokenStream
from parser.IOLexer import IOLexer
from parser.IOParser import IOParser
from parser.IOParserVisitor import IOParserVisitor


class RepeatedIdentifierException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)

class InvalidReferenceException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class Unit:
    def __init__(self, block, attributes, repeat):
        self.block = block
        self.attributes = attributes
        self.repeat = repeat

class NL(Unit):
    def __init__(self): pass

class Block:
    def __init__(self, units: list[Unit]):
        self.units = units

class Attribute:
    def __init__(self, property: str, options):
        self.property = property
        self.options = options

class Edge:
    def __init__(self, directed: bool, a, b):
        self.directed = directed
        self.a, self.b = a, b

class Comparison:
    def __init__(self, op: str, term):
        self.op = op
        self.term = term

class Interval:
    def __init__(self, a, b):
        self.a, self.b = a, b

class ArithExpr:
    def __init__(self, op: str, lhs, rhs):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs

class Reference(ArithExpr):
    def __init__(self, ident, subs: list[ArithExpr]):
        self.ident = ident
        self.subs = subs

class Edge:
    def __init__(self, directed: bool, a: Reference, b: Reference):
        self.directed = directed
        self.a = a
        self.b = b

class Ident(Block):
    def __init__(self, name: str):
        self.name = name

class Literal(Unit): pass

class IntLiteral(Literal, ArithExpr):
    def __init__(self, val: int):
        self.val = val

class StringLiteral(Literal):
    def __init__(self, val: str):
        self.val = val


class Analyzer(IOParserVisitor):
    def __init__(self):
        self.state = {}

    def visitSequence(self, ctx: IOParser.SequenceContext) -> tuple[list[Unit], list[str]]:
        units = []
        variables = []
        for unit_ctx in ctx.unit():
            unit, vars = self.visitUnit(unit_ctx)
            units.append(unit)
            variables.extend(vars)
        return units, variables

    def visitUnit(self, ctx: IOParser.UnitContext) -> tuple[Unit, list[str]]:
        if ctx.NL():
            return NL(), []
        if ctx.literal():
            return self.visitLiteral(ctx.literal()), []
        attributes = self.visitAttributes(ctx.attributes()) if ctx.attributes() else []
        repeat = self.visitRepeat(ctx.repeat()) if ctx.repeat() else None
        block, variables = self.visitBlock(ctx.block())
        if repeat:
            for v in variables:
                self.state[v] += 1
        return Unit(block, attributes, repeat), variables

    def visitBlock(self, ctx: IOParser.BlockContext) -> tuple[Block, list[str]]:
        if ctx.IDENT() is None:
            return self.visitSequence(ctx.sequence())
        ident = ctx.IDENT().getText()
        if ident in self.state:
            raise RepeatedIdentifierException(f'Identifier "{ident}" defined multiple times.')
        self.state[ident] = 0
        return Ident(ident), [ident]

    def visitAttributes(self, ctx: IOParser.AttributesContext) -> list[Attribute]:
        return [self.visitAttribute(attribute_ctx) for attribute_ctx in ctx.attribute()]

    def visitAttribute(self, ctx: IOParser.AttributeContext) -> Attribute:
        options = {}
        name = None
        if ctx.SORTED():
            name = 'sorted'
            if ctx.ASC(0):
                options['asc'] = True
            elif ctx.DESC(0):
                options['desc'] = True
            if ctx.STRICT(0):
                options['strict'] = True
        elif ctx.DISTINCT():
            name = 'distinct'
        elif ctx.GRAPH() or ctx.TREE():
            name = 'graph' if ctx.GRAPH() else 'tree'
            if ctx.NODES(0) or ctx.EDGES(0):
                exit(1)
            options['nodes'] = self.visitInterval(ctx.interval(0))
            options['edges'] = self.visitEdges(ctx.edge(0))
            if ctx.CONNECTED(0):
                options['connected'] = True
            if ctx.LINE(0):
                options['line'] = True
            if ctx.BIPARTITE(0):
                options['bipartite'] = True
            if ctx.DAG(0):
                options['dag'] = True
        elif ctx.comparison():
            name = 'comparison'
            options['constraint'] = self.visitComparison(ctx.comparison())
        return name, options

    def visitEdge(self, ctx: IOParser.EdgeContext) -> Edge:
        directed = (ctx.ARROW() is not None)
        return Edge(
            directed,
            self.visitArithExpr(ctx.reference(0)),
            self.visitArithExpr(ctx.reference(1))
        )

    def visitComparison(self, ctx: IOParser.ComparisonContext) -> Comparison:
        return Comparison(ctx.COMP_OP().getText(), self.visitArithExpr(ctx.arithExpr()))

    def visitRepeat(self, ctx: IOParser.RepeatContext) -> Interval:
        if ctx.interval():
            return self.visitInterval(ctx.interval())
        return Interval(IntLiteral(0), self.visitArithExpr(ctx.arithExpr()))

    def visitInterval(self, ctx: IOParser.IntervalContext) -> Interval:
        return Interval(
            self.visitArithExpr(ctx.arithExpr(0)),
            self.visitArithExpr(ctx.arithExpr(1))
        )

    def visitArithExpr(self, ctx: IOParser.ArithExprContext) -> ArithExpr:
        if not ctx.arithExpr():
            return self.visitAddend(ctx.addend())
        op = ctx.PLUS() or ctx.MINUS()
        return ArithExpr(
            op.getText(),
            self.visitArithExpr(ctx.arithExpr()),
            self.visitAddend(ctx.addend())
        )

    def visitAddend(self, ctx: IOParser.AddendContext) -> ArithExpr:
        if not ctx.addend():
            return self.visitTerm(ctx.term())
        op = ctx.MULT() or ctx.DIV() or ctx.MOD()
        return ArithExpr(
            op.getText(),
            self.visitAddend(ctx.addend()),
            self.visitTerm(ctx.term())
        )

    def visitTerm(self, ctx: IOParser.TermContext) -> ArithExpr:
        if ctx.reference():
            return self.visitReference(ctx.reference())
        if ctx.INT():
            return IntLiteral(int(ctx.INT().getText()))
        return self.visitArithExpr(ctx.arithExpr())

    def visitReference(self, ctx: IOParser.ReferenceContext) -> Reference:
        ident = ctx.IDENT().getText()
        if ident not in self.state:
            raise InvalidReferenceException(f'Identifier "{ident}" not in scope.')
        subs = [self.visitArithExpr(subCtx) for subCtx in ctx.arithExpr()]
        if self.state[ident] != len(subs):
            raise InvalidReferenceException(f'Number of subscripts ({len(subs)}) of identifier "{ident}" does not match the expected one ({self.state[ident]}).')
        return Reference(Ident(ident), subs)

    def visitLiteral(self, ctx: IOParser.LiteralContext) -> Literal:
        if ctx.INT():
            return IntLiteral(int(ctx.INT().getText()))
        return StringLiteral(ctx.STR().getText())


input = open('../grammar/sample.ip', 'r')
lexer = IOLexer(InputStream(input.read()))
parser = IOParser(CommonTokenStream(lexer))

ctx = parser.sequence()

analyzer = Analyzer()
sequence, variables = analyzer.visitSequence(ctx)
print(variables)