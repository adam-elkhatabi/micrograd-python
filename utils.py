from graphviz import Digraph


# visualization of the Value class operations

def trace(root):
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges

def draw_graph(root):
    g = Digraph(name='myGraph', format='svg', graph_attr={'rankdir' : 'LR'})

    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))

        g.node(name=uid, label=f"{{ {n.label} | data : {n.data:.4f} | grad : {n.grad:.4f} }}", shape='record' )

        if n._op:
            g.node(name= uid + n._op, label=n._op)

            g.edge(uid + n._op, uid)

    for n1, n2 in edges:
        g.edge(str(id(n1)), str(id(n2)) + n2._op)

    return g