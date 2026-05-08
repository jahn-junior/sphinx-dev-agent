from inspect import cleandoc

from docutils import nodes
from docutils.core import publish_doctree


def parse_rst(rst: str) -> list[nodes.Node]:
    doctree = publish_doctree(cleandoc(rst))

    return list(doctree.children)


if __name__ == "__main__":
    import sys

    rst = sys.stdin.read()
    for node in parse_rst(rst):
        print(node.pformat())
