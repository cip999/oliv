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

class InvalidAttributeException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class Unit: pass

class Block:
    def __init__(self, units: list[Unit]):
        self.units = units
    def is_single_ident(self) -> bool:
        return len(self.units) == 1 and not self.units[0].repeat and self.units[0].block.is_single_ident()

class Attribute:
    def __init__(self, property: str, options: map):
        self.property = property
        self.options = options

class ArithExpr:
    def __init__(self, op: str, lhs, rhs):
        self.op = op
        self.lhs, self.rhs = lhs, rhs
    def evaluate(self) -> int | str:
        x, y = self.lhs.evaluate(), self.rhs.evaluate()
        expr = f'({x}) {self.op} ({y})'
        if isinstance(x, int) and isinstance(y, int):
            return int(eval(expr))
        return expr

class Comparison:
    def __init__(self, op: str, term: ArithExpr):
        self.op = op
        self.term = term

class Interval:
    def __init__(self, a: ArithExpr, b: ArithExpr):
        self.a, self.b = a, b

class Unit:
    def __init__(self, block: Block, attributes: list[Attribute], repeat: Interval | None):
        self.block = block
        self.attributes = attributes
        self.repeat = repeat

class NL(Unit):
    def __init__(self): pass

class Ident(Block):
    def __init__(self, name: str, type: str | None = None):
        self.name = name
        self.type = type or 'int'
    def is_single_ident(self) -> bool:
        return True

class Reference(ArithExpr):
    def __init__(self, ident: Ident, subs: list[ArithExpr]):
        self.ident = ident
        self.subs = subs
    def evaluate(self) -> str:
        result = self.ident.name
        if len(self.subs) > 0:
            result += '[' + ']['.join(str(sub.evaluate()) for sub in self.subs) + ']'
        return result

class Edge:
    def __init__(self, directed: bool, u: Reference, v: Reference):
        self.directed = directed
        self.u, self.v = u, v

class Literal(Unit):
    def __init__(self, val):
        self.val = val

class IntLiteral(Literal, ArithExpr):
    def __init__(self, val: int):
        super().__init__(val)
    def evaluate(self) -> int:
        return self.val

class FloatLiteral(Literal):
    def __init__(self, val: float):
        super().__init__(val)

class StringLiteral(Literal):
    def __init__(self, val: str):
        super().__init__(val.strip('"'))


class Analyzer(IOParserVisitor):
    def __init__(self, special_identifier='i'):
        self.state = {}
        self.sid = special_identifier

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
        for attribute in attributes:
            if attribute.property == 'sorted' or attribute.property == 'distinct':
                okay = repeat and block.is_single_ident()
                if not isinstance(block, Ident):
                    units = [u for u in block.units if not isinstance(u, NL)]
                    if len([u for u in units if isinstance(u, Literal) or not u.block.is_single_ident()]) == 0:
                        okay = True
                if not okay:
                    raise InvalidAttributeException(
                        f'Property "{attribute.property}" is only applicable to a single repeated identifier or to a simple list of identifiers.'
                    )
            if attribute.property == 'graph':
                edge = attribute.options['edges']
                for endpoint in [edge.u, edge.v]:
                    if len(endpoint.subs) == 1 and (endpoint.ident.name not in self.state or self.state[endpoint.ident.name] != 1):
                        raise InvalidReferenceException(f'Invalid edge endpoint: identifier {endpoint.ident.name} not in scope or with depth > 1.')
        return Unit(block, attributes, repeat), variables

    def visitBlock(self, ctx: IOParser.BlockContext) -> tuple[Block, list[str]]:
        if ctx.IDENT() is None:
            units, variables = self.visitSequence(ctx.sequence())
            return Block(units), variables
        ident, type = ctx.IDENT().getText(), None
        if ctx.TYPE():
            type = ctx.TYPE().getText()
        if ident in self.state:
            raise RepeatedIdentifierException(f'Identifier "{ident}" defined multiple times.')
        self.state[ident] = 0
        return Ident(ident, type), [ident]

    def visitAttributes(self, ctx: IOParser.AttributesContext) -> list[Attribute]:
        attributes = [self.visitAttribute(attribute_ctx) for attribute_ctx in ctx.attribute()]
        specified = set()
        for att in attributes:
            if att.property != 'comparison' and att.property in specified:
                raise InvalidAttributeException(f'Property "{att.property}" specified multiple times.')
            specified.add(att.property)
        return attributes

    def visitAttribute(self, ctx: IOParser.AttributeContext) -> Attribute:
        property = None
        options = {}
        if ctx.SORTED():
            property = 'sorted'
            for opt in ['asc', 'desc', 'strict']:
                if len(eval(f'ctx.{opt.upper()}()')) > 1:
                    raise InvalidAttributeException(f'Option "{opt}" of property "sorted" can be declared at most once.')
            if ctx.ASC(0) and ctx.DESC(0):
                raise InvalidAttributeException('Cannot have have both "asc" and "desc" options for attribyte "sorted".')
            if ctx.ASC(0):
                options['asc'] = True
            elif ctx.DESC(0):
                options['desc'] = True
            if ctx.STRICT(0):
                options['strict'] = True
        elif ctx.DISTINCT():
            property = 'distinct'
        elif ctx.GRAPH():
            property = 'graph'
            for opt in ['nodes', 'edges']:
                if len(eval(f'ctx.{opt.upper()}()')) != 1:
                    raise InvalidAttributeException(f'Option "{opt}" of property "{property}" must be declared exactly once.')
            options['nodes'] = self.visitInterval(ctx.interval(0))
            options['edges'] = self.visitEdge(ctx.edge(0))
            for opt in ['connected', 'tree', 'line', 'bipartite', 'dag']:
                occurrences = eval(f'ctx.{opt.upper()}()')
                if len(occurrences) > 1:
                    raise InvalidAttributeException(f'Option "{opt}" of property "{property}" can be declared at most onece.')
                if len(occurrences) == 1:
                    options[opt] = True
            if ctx.DAG(0):
                if not options['edges'].directed:
                    raise InvalidAttributeException('If "dag" is specified, edges must be directed.')
        elif ctx.comparison():
            property = 'comparison'
            if property not in options:
                options[property] = []
            options[property].append(self.visitComparison(ctx.comparison()))
        return Attribute(property, options)

    def visitEdge(self, ctx: IOParser.EdgeContext) -> Edge:
        endpoints = []
        for i in range(2):
            reference_ctx = ctx.reference(i)
            ident = reference_ctx.IDENT().getText()
            if ident == self.sid:
                if self.sid in self.state:
                    raise InvalidReferenceException(f'Referenced special identifier "{self.sid}" when it had already been declared.')
                if reference_ctx.arithExpr(0):
                    raise InvalidReferenceException(f'Special identifier "{self.sid}" cannot have subscripts.')
                reference = Reference(Ident(ident), [])
            else:
                sid_state = -1
                if self.sid in self.state:
                    sid_state = self.state[self.sid]
                    del self.state[self.sid]
                else:
                    self.state[self.sid] = 0
                reference = Reference(Ident(ident), [self.visitArithExpr(sub_ctx) for sub_ctx in reference_ctx.arithExpr()])
                if len(reference.subs) != 1:
                    raise InvalidReferenceException(f'Invalid edge endpoint "{reference_ctx.getText()}": must have exactly one subscript.')
                if sid_state == -1:
                    del self.state[self.sid]
                else:
                    self.state[self.sid] = sid_state
            endpoints.append(reference)
        return Edge(bool(ctx.ARROW()), *endpoints)

    def visitComparison(self, ctx: IOParser.ComparisonContext) -> Comparison:
        return Comparison(ctx.compOp().getText(), self.visitArithExpr(ctx.arithExpr()))

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
            raise InvalidReferenceException(f'Identifier "{ident}" not in scope for reference "{ctx.getText()}".')
        subs = [self.visitArithExpr(sub_ctx) for sub_ctx in ctx.arithExpr()]
        if self.state[ident] != len(subs):
            raise InvalidReferenceException(f'Number of subscripts ({len(subs)}) in reference "{ctx.getText()}" does not match the expected one ({self.state[ident]}).')
        return Reference(Ident(ident), subs)

    def visitLiteral(self, ctx: IOParser.LiteralContext) -> Literal:
        if ctx.INT():
            return IntLiteral(int(ctx.INT().getText()))
        if ctx.FLOAT():
            return FloatLiteral(float(ctx.FLOAT().getText()))
        return StringLiteral(ctx.STR().getText())
