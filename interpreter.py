from nodes import *
from values import Number

class Interpreter:
  def __init__(self, symbol_table):
    self.symbol_table = symbol_table

  def visit(self, node):
    method_name = f"visit_{type(node).__name__}" # type(node).__name__ is the name of the 'node' attribute
    method = getattr(self, method_name) # getattr(self, method_name) is the same as self.visit_ + type(self.node)
    return method(node)

  def visit_NumberNode(self, node):
    return Number(node.value)

  def visit_AddNode(self, node):
    return Number(self.visit(node.node_1).value + self.visit(node.node_2).value)

  def visit_SubtractNode(self, node):
    return Number(self.visit(node.node_1).value - self.visit(node.node_2).value)

  def visit_MultiplyNode(self, node):
    return Number(self.visit(node.node_1).value * self.visit(node.node_2).value)

  def visit_DivideNode(self, node):
    try:
      return Number(self.visit(node.node_1).value / self.visit(node.node_2).value)
    except:
      raise Exception("ERROR: math error: cannot divide by 0")

  def visit_MinusNode(self, node):
    return Number(-(self.visit(node.node).value))

  def visit_PlusNode(self, node):
    return Number(-(self.visit(node.node).value))

  def visit_VarAssignNode(self, node):
    self.symbol_table.set(node.var_name, node.var_value)
    return Number(self.visit(self.symbol_table.get(node.var_name))) # return the value of the variable

  def visit_VarAccessNode(self, node):
    var_name = node.var_name
    value = self.symbol_table.get(var_name)

    if not value:
      return print(f"'{var_name}' is not defined")

    return self.visit(value)