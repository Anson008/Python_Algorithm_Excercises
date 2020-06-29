from stack.my_stack import Stack
from tree.binary_tree import BinaryTree
import operator


def build_parse_tree(fp_exp):
    fp_list = fp_exp.split()
    p_stack = Stack()
    e_tree = BinaryTree()

    e_tree.set_root(0)
    current_node = e_tree.get_root()
    p_stack.push(current_node)

    for i in fp_list:
        if i == '(':
            e_tree.insert_left(current_node, 1)
            p_stack.push(current_node)
            current_node = e_tree.get_left(current_node)
        elif i not in ["+", "-", "*", "/", ")"]:
            e_tree.set_node(current_node, int(i))
            parent = p_stack.pop()
            current_node = parent
        elif i in ["+", "-", "*", "/"]:
            e_tree.set_node(current_node, i)
            e_tree.insert_right(current_node, i)
            p_stack.push(current_node)
            current_node = e_tree.get_right(current_node)
        elif i == ")":
            current_node = p_stack.pop()
        else:
            raise ValueError
    return e_tree


def evaluate(root):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    left = root.left
    right = root.right

    if left and right:
        oper = opers[root.key]
        return oper(evaluate(left), evaluate(right))
    else:
        return root.key


if __name__ == "__main__":
    #expr = "( ( 10 + 5 ) * 3 )"
    expr = "( 3 + ( 4 * 5 ) )"
    pt = build_parse_tree(expr)
    post_order = pt.post_order_traversal(pt.get_root())
    in_order = pt.in_order_traversal(pt.get_root())
    print("Post-order traversal:", post_order)
    print("In-order traversal:", in_order)

    res = evaluate(pt.get_root())
    print("Result:", res)
