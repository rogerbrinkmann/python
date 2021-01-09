import ast
import os

class CustomNodeVisitor(ast.NodeVisitor):
    def __init__(self):
        super().__init__()

    def generic_visit(self, node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Assign(self, node):
        print(node)



class CustomNodeTransformer(ast.NodeTransformer):
    def visit_Assign(self, node):
        return 


current_dir = os.path.split(os.path.abspath(__file__))[0]
input_path = os.path.join(current_dir, "sample_script.py")
output_path = os.path.join(current_dir, "modified_script.py")

with open(input_path, "r") as file_reader:
    module_code = file_reader.read()

tree = ast.parse(module_code)

nv = CustomNodeVisitor()
nv.visit(tree)

# nt = CustomNodeTransformer()
# nt.visit(tree)

output = ast.unparse(tree)

with open(output_path, "w") as file_writer:
    file_writer.write(output)