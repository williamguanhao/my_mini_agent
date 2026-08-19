import ast
import operator

from ..tool import Tool


class CalculatorTool(Tool):

    @property
    def name(self):
        return "calculator"

    @property
    def description(self):
        return "Calculate a basic arithmetic expression."

    @property
    def parameters(self):
        return {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": (
                        "Arithmetic expression such as "
                        "2 + 3 * 4"
                    ),
                }
            },
            "required": ["expression"],
        }

    def execute(self, arguments):

        expression = arguments["expression"]

        tree = ast.parse(
            expression,
            mode="eval",
        )

        return str(
            self._evaluate(tree.body)
        )

    def _evaluate(self, node):

        operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.FloorDiv: operator.floordiv,
            ast.Mod: operator.mod,
            ast.Pow: operator.pow,
        }

        if isinstance(node, ast.Constant):

            if isinstance(
                node.value,
                (int, float),
            ):
                return node.value

            raise ValueError(
                "Only numbers are allowed."
            )

        if isinstance(node, ast.UnaryOp):

            value = self._evaluate(node.operand)

            if isinstance(node.op, ast.USub):
                return -value

            if isinstance(node.op, ast.UAdd):
                return value

            raise ValueError(
                "Unsupported unary operator."
            )

        if isinstance(node, ast.BinOp):

            left = self._evaluate(node.left)
            right = self._evaluate(node.right)

            operation = operators.get(
                type(node.op)
            )

            if operation is None:
                raise ValueError(
                    "Unsupported operator."
                )

            return operation(left, right)

        raise ValueError(
            "Invalid arithmetic expression."
        )