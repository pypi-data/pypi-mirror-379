# lovelang.py
# LoveLang Interpreter
# Features:
#  - multi-arg bolo(...)
#  - lovetrue / lovefalse
#  - agartum / nehito (if/else)
#  - jabtak (while) with proper variable persistence
#  - dilse / lautjao (functions)
#  - detailed syntax + runtime error messages with line/column & snippet

import sys
import re

#####################
# Lexer
#####################

TOKEN_SPEC = [
    ('NUMBER',   r'\d+(\.\d+)?'),
    ('STRING',   r'"([^"\\]|\\.)*"|\'([^\'\\]|\\.)*\''),
    ('ID',       r'[A-Za-z_]\w*'),
    ('NEWLINE',  r'\n'),
    ('SKIP',     r'[ \t]+'),
    ('COMMENT',  r'\#.*'),
    ('OP',       r'==|!=|<=|>=|&&|\|\||[+\-*/%<>=!()]'),
    ('LBRACE',   r'\{'),
    ('RBRACE',   r'\}'),
    ('COMMA',    r','),
    ('SEMICOLON',r';'),
]

MASTER_RE = re.compile('|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPEC))

KEYWORDS = {
    'suno', 'bolo',
    'agartum', 'nehito',
    'jabtak',
    'thodaroko', 'miltehe', 'trust',
    'dilse', 'lautjao',
    'lovetrue', 'lovefalse'
}

class Token:
    def __init__(self, kind, value, index, line=None, col=None):
        self.kind = kind
        self.value = value
        self.index = index
        self.line = line
        self.col = col
    def __repr__(self):
        return f'Token({self.kind}, {self.value!r}, line={self.line}, col={self.col})'

def lex(code):
    pos = 0
    line = 1
    col = 1
    tokens = []
    L = len(code)
    while pos < L:
        m = MASTER_RE.match(code, pos)
        if not m:
            # compute line/col from pos (fallback)
            before = code[:pos]
            line = before.count('\n') + 1
            last_n = before.rfind('\n')
            if last_n == -1:
                col = pos + 1
            else:
                col = pos - last_n
            # show line snippet
            lines = code.splitlines()
            snippet = lines[line-1] if 0 <= line-1 < len(lines) else ''
            caret = ' ' * (col-1) + '^'
            raise SyntaxError(f'Lex error: Unexpected char {code[pos]!r} at line {line} column {col}\n{snippet}\n{caret}')
        kind = m.lastgroup
        value = m.group(kind)
        token = None

        # create token object if needed
        if kind == 'NUMBER':
            num = float(value) if '.' in value else int(value)
            token = Token('NUMBER', num, pos)
        elif kind == 'STRING':
            s = value[1:-1]
            s = bytes(s, "utf-8").decode("unicode_escape")
            token = Token('STRING', s, pos)
        elif kind == 'ID':
            if value in KEYWORDS:
                token = Token(value.upper(), value, pos)
            else:
                token = Token('ID', value, pos)
        elif kind in ('NEWLINE', 'SKIP', 'COMMENT'):
            token = None
        else:
            token = Token(kind, value, pos)

        # attach line & col to token and append if token exists
        if token is not None:
            token.line = line
            token.col = col
            tokens.append(token)

        # update line & col based on matched text
        nl = value.count('\n')
        if nl:
            # after last newline, column becomes len(after) + 1
            parts = value.split('\n')
            line += nl
            col = len(parts[-1]) + 1
        else:
            col += len(value)
        pos = m.end()

    tokens.append(Token('EOF', '', pos, line, col))
    return tokens

#####################
# Parser
#####################

class ParseError(SyntaxError):
    pass

class Parser:
    def __init__(self, tokens, source):
        self.tokens = tokens
        self.pos = 0
        self.source = source

    def current(self):
        return self.tokens[self.pos]

    def eat(self, kind=None, value=None):
        tok = self.current()
        if kind and tok.kind != kind:
            self.error(f'Expected {kind} but got {tok.kind}', tok)
        if value is not None and getattr(tok, 'value', None) != value:
            self.error(f'Expected token value {value!r} but got {tok.value!r}', tok)
        self.pos += 1
        return tok

    def error(self, msg, tok):
        ln = getattr(tok, 'line', None)
        col = getattr(tok, 'col', None)
        snippet = ''
        caret = ''
        if ln is not None:
            lines = self.source.splitlines()
            if 0 <= ln-1 < len(lines):
                snippet = lines[ln-1]
                caret = ' ' * (col-1) + '^' if col is not None else ''
        raise ParseError(f'SyntaxError: {msg} at line {ln} column {col}\n{snippet}\n{caret}')

    def parse(self):
        stmts = []
        while self.current().kind != 'EOF':
            stmts.append(self.parse_statement())
        return ('block', stmts)

    def parse_statement(self):
        start_tok = self.current()
        start_line = getattr(start_tok, 'line', None)
        start_col = getattr(start_tok, 'col', None)

        tok = self.current()
        if tok.kind == 'ID':
            next_tok = self.tokens[self.pos+1]
            if next_tok.kind == 'OP' and next_tok.value == '=':
                node = self.parse_assign()
                return node + (('@pos', start_line, start_col),)
            else:
                expr = self.parse_expression()
                if self.current().kind == 'SEMICOLON': self.eat('SEMICOLON')
                return ('expr_stmt', expr) + (('@pos', start_line, start_col),)
        elif tok.kind == 'BOLO':
            node = self.parse_print()
            return node + (('@pos', start_line, start_col),)
        elif tok.kind == 'SUNO':
            expr = self.parse_expression()
            if self.current().kind == 'SEMICOLON': self.eat('SEMICOLON')
            return ('expr_stmt', expr) + (('@pos', start_line, start_col),)
        elif tok.kind == 'AGARTUM':
            node = self.parse_if()
            return node + (('@pos', start_line, start_col),)
        elif tok.kind == 'JABTAK':
            node = self.parse_while()
            return node + (('@pos', start_line, start_col),)
        elif tok.kind == 'DILSE':
            node = self.parse_func()
            return node + (('@pos', start_line, start_col),)
        elif tok.kind == 'LAUTJAO':
            self.eat('LAUTJAO')
            expr = self.parse_expression()
            if self.current().kind == 'SEMICOLON': self.eat('SEMICOLON')
            return ('return', expr) + (('@pos', start_line, start_col),)
        elif tok.kind == 'TRUST':
            self.eat('TRUST')
            if self.current().kind == 'SEMICOLON': self.eat('SEMICOLON')
            return ('pass',) + (('@pos', start_line, start_col),)
        elif tok.kind == 'THODAROKO':
            self.eat('THODAROKO')
            if self.current().kind == 'SEMICOLON': self.eat('SEMICOLON')
            return ('continue',) + (('@pos', start_line, start_col),)
        elif tok.kind == 'MILTEHE':
            self.eat('MILTEHE')
            if self.current().kind == 'SEMICOLON': self.eat('SEMICOLON')
            return ('break',) + (('@pos', start_line, start_col),)
        else:
            expr = self.parse_expression()
            if self.current().kind == 'SEMICOLON': self.eat('SEMICOLON')
            return ('expr_stmt', expr) + (('@pos', start_line, start_col),)

    def parse_assign(self):
        name_tok = self.eat('ID')
        self.eat('OP', '=')
        expr = self.parse_expression()
        if self.current().kind == 'SEMICOLON': self.eat('SEMICOLON')
        return ('assign', name_tok.value, expr)

    def parse_print(self):
        self.eat('BOLO')
        self.eat('OP', '(')
        exprs = []
        if not (self.current().kind == 'OP' and self.current().value == ')'):
            while True:
                exprs.append(self.parse_expression())
                if self.current().kind == 'COMMA':
                    self.eat('COMMA')
                    continue
                break
        self.eat('OP', ')')
        if self.current().kind == 'SEMICOLON': self.eat('SEMICOLON')
        return ('print', exprs)

    def parse_if(self):
        self.eat('AGARTUM')
        self.eat('OP', '(')
        cond = self.parse_expression()
        self.eat('OP', ')')
        self.eat('LBRACE')
        then_block = []
        while self.current().kind != 'RBRACE':
            then_block.append(self.parse_statement())
        self.eat('RBRACE')
        else_block = None
        if self.current().kind == 'NEHITO':
            self.eat('NEHITO')
            self.eat('LBRACE')
            else_block = []
            while self.current().kind != 'RBRACE':
                else_block.append(self.parse_statement())
            self.eat('RBRACE')
        return ('if', cond, ('block', then_block), ('block', else_block) if else_block else None)

    def parse_while(self):
        self.eat('JABTAK')
        self.eat('OP', '(')
        cond = self.parse_expression()
        self.eat('OP', ')')
        self.eat('LBRACE')
        body = []
        while self.current().kind != 'RBRACE':
            body.append(self.parse_statement())
        self.eat('RBRACE')
        return ('while', cond, ('block', body))

    def parse_func(self):
        self.eat('DILSE')
        name_tok = self.eat('ID')
        self.eat('OP', '(')
        params = []
        if not (self.current().kind == 'OP' and self.current().value == ')'):
            # first param
            p = self.eat('ID')
            params.append(p.value)
            while self.current().kind == 'COMMA':
                self.eat('COMMA')
                p = self.eat('ID')
                params.append(p.value)
        self.eat('OP', ')')
        self.eat('LBRACE')
        body = []
        while self.current().kind != 'RBRACE':
            body.append(self.parse_statement())
        self.eat('RBRACE')
        return ('func', name_tok.value, params, ('block', body))

    def parse_expression(self, min_prec=0):
        tok = self.current()
        if tok.kind == 'NUMBER':
            self.eat('NUMBER')
            left = ('num', tok.value)
        elif tok.kind == 'STRING':
            self.eat('STRING')
            left = ('str', tok.value)
        elif tok.kind == 'LOVETRUE':
            self.eat('LOVETRUE')
            left = ('bool', True)
        elif tok.kind == 'LOVEFALSE':
            self.eat('LOVEFALSE')
            left = ('bool', False)
        elif tok.kind == 'ID':
            name_tok = self.eat('ID')
            if self.current().kind == 'OP' and self.current().value == '(':
                self.eat('OP', '(')
                args = []
                if not (self.current().kind == 'OP' and self.current().value == ')'):
                    while True:
                        args.append(self.parse_expression())
                        if self.current().kind == 'COMMA':
                            self.eat('COMMA'); continue
                        break
                self.eat('OP', ')')
                left = ('call', name_tok.value, args)
            else:
                left = ('var', name_tok.value)
        elif tok.kind == 'OP' and tok.value == '(':
            self.eat('OP', '(')
            left = self.parse_expression()
            self.eat('OP', ')')
        elif tok.kind == 'OP' and tok.value in ('-', '!'):
            op = self.eat('OP').value
            right = self.parse_expression(100)
            left = ('unary', op, right)
        elif tok.kind == 'SUNO':
            self.eat('SUNO')
            self.eat('OP', '(')
            expr = self.parse_expression()
            self.eat('OP', ')')
            left = ('suno', expr)
        else:
            self.error(f'Unexpected token {tok.kind} {getattr(tok,"value", "")!r}', tok)

        # precedence climbing
        prec = {
            '||': 1, '&&': 2,
            '==': 3, '!=': 3,
            '<': 4, '>': 4, '<=': 4, '>=': 4,
            '+': 5, '-': 5,
            '*': 6, '/': 6, '%': 6,
        }

        while True:
            tok = self.current()
            if tok.kind == 'OP' and tok.value in prec and prec[tok.value] >= min_prec:
                op = tok.value
                op_prec = prec[op]
                self.eat('OP', op)
                right = self.parse_expression(op_prec + 1)
                left = ('binop', op, left, right)
            else:
                break
        return left

#####################
# Interpreter
#####################

class RuntimeErrorWithPos(RuntimeError):
    pass

class ReturnException(Exception):
    def __init__(self, value): self.value = value
class BreakException(Exception): pass
class ContinueException(Exception): pass

class Environment:
    def __init__(self, parent=None):
        self.parent = parent
        self.vars = {}
    def get(self, name):
        if name in self.vars: return self.vars[name]
        if self.parent: return self.parent.get(name)
        raise NameError(f'Undefined variable: {name}')
    def set(self, name, value): self.vars[name] = value

class Interpreter:
    def __init__(self, tree, source):
        self.tree = tree
        self.source = source
        self.global_env = Environment()
        self.setup_builtins()

    def setup_builtins(self):
        env = self.global_env
        env.set('bolo', ('builtin_print',))
        env.set('suno', ('builtin_input',))

    # pretty error printer
    def format_pos(self, pos):
        if not pos or pos[0] != '@pos': return None
        _, line, col = pos
        lines = self.source.splitlines()
        if 1 <= line <= len(lines):
            snippet = lines[line-1]
            caret = ' ' * (col-1) + '^'
            return f'line {line} col {col}\n{snippet}\n{caret}'
        return f'line {line} col {col}'

    def runtime_error(self, msg, pos=None):
        pos_msg = self.format_pos(pos)
        if pos_msg:
            raise RuntimeErrorWithPos(f'RuntimeError: {msg} at {pos_msg}')
        else:
            raise RuntimeError(f'RuntimeError: {msg}')

    def eval(self):
        return self.eval_block(self.tree, self.global_env)

    def eval_block(self, node, env):
        # node is ('block', [stmts...])
        res = None
        for stmt in node[1]:
            res = self.exec_statement(stmt, env)
        return res

    def exec_statement(self, stmt, env):
        # stmt may have trailing pos: last element could be ('@pos',line,col)
        t = stmt[0]
        pos = stmt[-1] if isinstance(stmt[-1], tuple) and stmt[-1][0] == '@pos' else None

        if t == 'assign':
            name = stmt[1]
            expr = stmt[2]
            val = self.eval_expr(expr, env)
            env.set(name, val)
            return val

        elif t == 'print':
            exprs = stmt[1]
            values = [self.eval_expr(e, env) for e in exprs]
            print(*values)
            return None

        elif t == 'expr_stmt':
            return self.eval_expr(stmt[1], env)

        elif t == 'if':
            cond = stmt[1]
            then_block = stmt[2]
            else_block = stmt[3]
            if self.eval_expr(cond, env):
                return self.eval_block(then_block, env)
            elif else_block:
                return self.eval_block(else_block, env)
            return None

        elif t == 'while':
            cond = stmt[1]
            block = stmt[2]
            while True:
                cond_val = self.eval_expr(cond, env)
                if not cond_val:
                    break
                try:
                    # execute body statements in same env so loop vars persist
                    for inner_stmt in block[1]:
                        self.exec_statement(inner_stmt, env)
                except BreakException:
                    break
                except ContinueException:
                    continue
            return None

        elif t == 'func':
            name = stmt[1]
            params = stmt[2]
            body = stmt[3]
            env.set(name, ('userfunc', params, body))
            return None

        elif t == 'return':
            val = self.eval_expr(stmt[1], env)
            raise ReturnException(val)

        elif t == 'pass':
            return None

        elif t == 'break':
            raise BreakException()

        elif t == 'continue':
            raise ContinueException()

        else:
            self.runtime_error(f'Unknown statement type: {t}', pos)

    def exec_block_with_control(self, block, env):
        # Execute block in given env; propagate control exceptions
        for stmt in block[1]:
            try:
                self.exec_statement(stmt, env)
            except (ReturnException, BreakException, ContinueException):
                raise

    def eval_expr(self, expr, env):
        kind = expr[0]
        # extract pos if present for expressions
        pos = expr[-1] if isinstance(expr[-1], tuple) and expr[-1][0] == '@pos' else None

        if kind == 'num':
            return expr[1]
        if kind == 'str':
            return expr[1]
        if kind == 'bool':
            return expr[1]
        if kind == 'var':
            name = expr[1]
            try:
                return env.get(name)
            except NameError as ne:
                self.runtime_error(str(ne), pos)
        if kind == 'binop':
            op = expr[1]
            a = self.eval_expr(expr[2], env)
            b = self.eval_expr(expr[3], env)
            try:
                return self.apply_op(op, a, b)
            except ZeroDivisionError:
                self.runtime_error('Division by zero', pos)
            except Exception as e:
                self.runtime_error(f'Operator error: {e}', pos)
        if kind == 'unary':
            op = expr[1]
            v = self.eval_expr(expr[2], env)
            if op == '-':
                try: return -v
                except Exception as e:
                    self.runtime_error(f'Unary - error: {e}', pos)
            if op == '!':
                return not v
        if kind == 'call':
            name = expr[1]
            args = [self.eval_expr(a, env) for a in expr[2]]
            return self.call_func(name, args, env, pos)
        if kind == 'suno':
            prompt = self.eval_expr(expr[1], env)
            try:
                return input(str(prompt))
            except Exception as e:
                self.runtime_error(f'Input error: {e}', pos)

        self.runtime_error(f'Unknown expression kind: {kind}', pos)

    def apply_op(self, op, a, b):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/':
            if b == 0:
                raise ZeroDivisionError()
            return a / b
        if op == '%': return a % b
        if op == '==': return a == b
        if op == '!=': return a != b
        if op == '<': return a < b
        if op == '<=': return a <= b
        if op == '>': return a > b
        if op == '>=': return a >= b
        if op == '&&': return bool(a) and bool(b)
        if op == '||': return bool(a) or bool(b)
        raise Exception(f'Unknown operator {op}')

    def call_func(self, name, args, env, pos=None):
        # look up function or builtin
        try:
            val = env.get(name)
        except NameError:
            try:
                val = self.global_env.get(name)
            except NameError:
                self.runtime_error(f'Function not found: {name}', pos)

        if isinstance(val, tuple) and val[0] == 'builtin_print':
            # builtin print - print args directly
            print(*args)
            return None
        if isinstance(val, tuple) and val[0] == 'builtin_input':
            prompt = args[0] if args else ''
            try:
                return input(str(prompt))
            except Exception as e:
                self.runtime_error(f'Input error: {e}', pos)

        if isinstance(val, tuple) and val[0] == 'userfunc':
            _, params, body = val
            if len(args) != len(params):
                self.runtime_error(f'Argument count mismatch for {name}: expected {len(params)}, got {len(args)}', pos)
            # function local env with parent = caller env
            local = Environment(env)
            for p, a in zip(params, args):
                local.set(p, a)
            try:
                # execute function body; catch return
                for inner in body[1]:
                    self.exec_statement(inner, local)
            except ReturnException as re:
                return re.value
            return None

        self.runtime_error(f'Call target not callable: {name}', pos)

####################
# Runner
####################

def run_code(code, filename='<string>'):
    try:
        tokens = lex(code)
        p = Parser(tokens, code)
        tree = p.parse()
        interp = Interpreter(tree, code)
        interp.eval()
    except ParseError as pe:
        print(str(pe), file=sys.stderr)
    except RuntimeErrorWithPos as re_pos:
        print(str(re_pos), file=sys.stderr)
    except RuntimeError as re:
        print(str(re), file=sys.stderr)
    except Exception as e:
        # Fallback
        print('Unhandled error:', e, file=sys.stderr)

def main():
    if len(sys.argv) < 2:
        print("Usage: python lovelang.py file.pyr")
        sys.exit(1)
    path = sys.argv[1]
    try:
        with open(path, 'r', encoding='utf-8') as f:
            code = f.read()
    except FileNotFoundError:
        print(f'File not found: {path}')
        sys.exit(1)
    run_code(code, path)

if __name__ == '__main__':
    main()
