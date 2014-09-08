#!/usr/bin/env python3
from glob import glob

SIZE = 2

print(r'''
\documentclass[border=2in]{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
''')


for file in glob('data/nodes-*.txt'):
    mark = 'O' if 'metro' in file else 'X'
    for node in open(file):
        if not node.strip():
            continue
        identity, position = node.strip().split('\t')
        x, y = [SIZE * float(n) for n in position[1:-1].split(',')]
        print(r'  \node ({}) at ({},{}) {{{}}};'.format(identity, x, y, mark))

for file in glob('data/paths-*.txt'):
    for path in open(file):
        if not path.strip():
            continue
        color, nodes = path.strip().split('\t')
        nodes = nodes.split()
        for n1, n2 in zip(nodes, nodes[1:]):
            print(r'  \draw[ultra thick,color={}] ({}) to ({});'.format(color, n1, n2))


print(r'''
\end{tikzpicture}
\end{document}
''')
