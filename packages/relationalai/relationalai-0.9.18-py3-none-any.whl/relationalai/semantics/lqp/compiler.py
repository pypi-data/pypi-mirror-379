#--------------------------------------------------
# Compiler
#--------------------------------------------------

from relationalai.semantics.lqp import ir as lqp, model2lqp
from relationalai.semantics.lqp.passes import lqp_passes
from relationalai.semantics.metamodel import ir, compiler as c

from typing import Optional

class Compiler(c.Compiler):
    def __init__(self):
        super().__init__(lqp_passes())

    def do_compile(self, model: ir.Model, options:dict={}) -> tuple[Optional[tuple], lqp.Transaction]:
        fragment_id: bytes = options.get("fragment_id", bytes(404))
        return model2lqp.to_lqp(model, fragment_id)
