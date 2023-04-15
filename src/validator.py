import sys
from contextlib import contextmanager

from analyzer import *


IMPORTS = [
    'iostream',
    'cassert',
    'cmath',
    'string',
    'vector',
    'queue',
    'set',
    'unordered_set',
    'map',
    'unordered_map',
    'algorithm',
    'numeric',
]


class Variable:
    def __init__(self, name: str, type: str, dimensions: list[str]):
        self.name = name
        self.type = type
        self.dimensions = dimensions

class FunctionSignature:
    def __init__(self, ret: str, name: str, *params: str):
        self.ret = ret
        self.name = name
        self.params = params


MAIN = FunctionSignature('int', 'main', 'int argc', 'char **argv')
READ = FunctionSignature('void', 'read')


class Writer:
    def __init__(self, file: str | None = None, input: str | None = None):
        if file is None:
            self.file = sys.stdout
        else:
            self.file = open(file, 'w')
        if input is None:
            self.input = 'std::cin'
        else:
            raise(NotImplementedError('Read from custom file is not suppoerted yet.'))
        self.level = 0

    def type(self, var: Variable) -> str:
        inner_type = var.type if var.type != 'string' else 'std::string'
        return 'std::vector<' * len(var.dimensions) + inner_type + '>' * len(var.dimensions)

    def write(self, *text: str):
        indent = '\t' * self.level
        content = indent + ('\n'+indent).join(text)
        print(content, file=self.file)

    def nl(self):
        print(file=self.file)

    def open_block(self, header: str):
        self.write(header + ' {')
        self.level += 1

    def open_function(self, signature: FunctionSignature):
        params = ', '.join(signature.params)
        self.open_block(f'{signature.ret} {signature.name}({params})')

    def open_for(self, init: str, condition: str, increment: str):
        self.open_block(f'for ({init}; {condition}; {increment})')

    def close_block(self):
        self.level -= 1
        self.write('}')

    def write_imports(self):
        self.write(*[f'#include <{imp}>' for imp in IMPORTS])
        self.nl()

    def write_declaration(self, var: Variable):
        self.write(f'{self.type(var)} {var.name};')

    def write_read(self, var: str, *subs: str):
        to_read = var
        if len(subs) > 0:
            to_read += '[' + ']['.join(subs) + ']'
        self.write(self.input + ' >> ' + to_read + ';')


class ValidatorFactory:
    def __init__(self, file: str | None = None):
        self.writer = Writer(file)

    @contextmanager
    def iter_var(self):
        try:
            i = 0
            while True:
                var = ['i', 'j', 'k'][i % 3]
                if i >= 3:
                    var = var + str(i // 3)
                if self.idents is None or var not in self.idents:
                    self.idents.add(var)
                    yield var
                    break
                i += 1
        finally:
            self.idents.remove(var)

    def generate(self, units: list[Unit]):
        self.writer.write_imports()
        self.writer.nl()

        variables = self.variables_from_units(units)
        self.idents = {var.name for var in variables}
        for var in variables:
            self.writer.write_declaration(var)
        self.writer.nl()

        self.writer.open_function(READ)
        self.read_units(units)
        self.writer.close_block()
        self.writer.nl()

        self.writer.open_function(MAIN)
        self.writer.close_block()

    def variables_from_units(self, units: list[Unit]) -> list[Variable]:
        variables = []
        for unit in units:
            variables.extend(self.variables_from_unit(unit))
        return variables

    def variables_from_unit(self, unit: Unit) -> list[Variable]:
        if isinstance(unit, NL) or isinstance(unit, Literal):
            return []
        variables = self.variables_from_block(unit.block)
        if unit.repeat:
            a, b = unit.repeat.a, unit.repeat.b
            dim = str(ArithExpr('-', b, a).evaluate())
            for var in variables:
                var.dimensions.append(dim)
        return variables

    def variables_from_block(self, block: Block) -> list[Variable]:
        if isinstance(block, Ident):
            return [Variable(block.name, block.type, [])]
        return self.variables_from_units(block.units)

    def read_units(self, units: list[Unit], *subs: str):
        for unit in units:
            self.read_unit(unit, *subs)

    def read_unit(self, unit: Unit, *subs: str):
        if isinstance(unit, NL) or isinstance(unit, Literal):
            return
        if unit.repeat is None:
            self.read_block(unit.block, *subs)
        else:
            a, b = unit.repeat.a.evaluate(), unit.repeat.b.evaluate()
            with self.iter_var() as var:
                self.writer.open_for(f'int {var} = {a}', f'{var} < {b}', f'++{var}')
                self.idents
                self.read_block(unit.block, *subs, var)
                self.writer.close_block()

    def read_block(self, block: Block, *subs: str):
        if isinstance(block, Ident):
            self.writer.write_read(block.name, *subs)
        else:
            self.read_units(block.units, *subs)


input = open('../grammar/sample.ip', 'r')
lexer = IOLexer(InputStream(input.read()))
parser = IOParser(CommonTokenStream(lexer))

ctx = parser.sequence()

analyzer = Analyzer()
sequence, vars = analyzer.visitSequence(ctx)
print(*vars)

factory = ValidatorFactory('validator.cpp')
factory.generate(sequence)