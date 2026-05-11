from inspect import cleandoc

from docutils.core import publish_doctree


if __name__ == "__main__":
    import sys

    rst = sys.stdin.read()
    doctree = publish_doctree(cleandoc(rst))
    for node in doctree:
        print(node.pformat())
