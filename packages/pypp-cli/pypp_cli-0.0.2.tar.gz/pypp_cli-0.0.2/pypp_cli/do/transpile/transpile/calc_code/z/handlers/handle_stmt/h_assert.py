import ast
from dataclasses import dataclass

from pypp_cli.do.transpile.transpile.y.d_types import QInc
from pypp_cli.do.transpile.transpile.calc_code.z.deps import Deps


@dataclass(frozen=True, slots=True)
class AssertHandler:
    _d: Deps

    def handle(self, node: ast.Assert) -> str:
        self._d.add_inc(QInc("pypp_assert.h"))
        test_str = self._d.handle_expr(node.test)
        if node.msg is not None:
            msg_str = self._d.handle_expr(node.msg)
        else:
            msg_str = 'pypp::PyStr("")'
        return f"pypp::assert({test_str}, {msg_str});"
