import re
import ast
from itertools import product


def verify(expr: str) -> str:
    """Simple SAT-like verification for small arithmetic expressions.

    Returns one of ``"sat"``, ``"unsat"`` or ``"unknown"`` depending on the
    evaluation result.
    """

    # Find variable names (letters and underscores) ignoring Python keywords
    vars_found = sorted({v for v in re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*", expr) if not re.fullmatch(r"True|False|and|or|not", v)})
    domain = [-1, 0, 1]

    def _eval_ast(node, env):
        if isinstance(node, ast.Expression):
            return _eval_ast(node.body, env)
        if isinstance(node, ast.BoolOp):
            vals = [_eval_ast(v, env) for v in node.values]
            if isinstance(node.op, ast.And):
                return all(vals)
            if isinstance(node.op, ast.Or):
                return any(vals)
            raise ValueError("Unsupported boolean operator")
        if isinstance(node, ast.BinOp):
            left = _eval_ast(node.left, env)
            right = _eval_ast(node.right, env)
            op = node.op
            if isinstance(op, ast.Add):
                return left + right
            if isinstance(op, ast.Sub):
                return left - right
            if isinstance(op, ast.Mult):
                return left * right
            if isinstance(op, ast.Div):
                return left / right
            if isinstance(op, ast.FloorDiv):
                return left // right
            if isinstance(op, ast.Mod):
                return left % right
            if isinstance(op, ast.Pow):
                return left ** right
            raise ValueError("Unsupported binary operator")
        if isinstance(node, ast.UnaryOp):
            operand = _eval_ast(node.operand, env)
            if isinstance(node.op, ast.UAdd):
                return +operand
            if isinstance(node.op, ast.USub):
                return -operand
            if isinstance(node.op, ast.Not):
                return not operand
            raise ValueError("Unsupported unary operator")
        if isinstance(node, ast.Compare):
            left = _eval_ast(node.left, env)
            for op, comparator in zip(node.ops, node.comparators):
                right = _eval_ast(comparator, env)
                if isinstance(op, ast.Eq):
                    ok = left == right
                elif isinstance(op, ast.NotEq):
                    ok = left != right
                elif isinstance(op, ast.Lt):
                    ok = left < right
                elif isinstance(op, ast.LtE):
                    ok = left <= right
                elif isinstance(op, ast.Gt):
                    ok = left > right
                elif isinstance(op, ast.GtE):
                    ok = left >= right
                else:
                    raise ValueError("Unsupported comparison operator")
                if not ok:
                    return False
                left = right
            return True
        if isinstance(node, ast.Name):
            if node.id in env:
                return env[node.id]
            raise ValueError(f"Unknown variable: {node.id}")
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float, bool)):
                return node.value
            raise ValueError("Invalid constant")
        raise ValueError("Unsupported expression")

    evaluated = False
    try:
        parsed = ast.parse(expr, mode="eval")
    except SyntaxError:
        return "unknown"

    for values in product(domain, repeat=len(vars_found)):
        env = dict(zip(vars_found, values))
        try:
            result = _eval_ast(parsed, env)
            evaluated = True
            if result:
                return "sat"
        except Exception:
            continue

    if evaluated:
        return "unsat"
    return "unknown"
