---
name: node-builder
description: 'Generate Python code that creates docutils nodes to match a reStructuredText file.'
---

# node-builder

## Workflow

The workflow for creating the Python code to generate the docutils nodes is broken up
into three parts:

- **Set up environment**: Set up a Python environment with the necessary packages and create
  the interim files necessary to generate the Python code.
- **Generate Python code**: Write Python code that concatenates a list of docutils nodes that
  matches the contents of the `/tmp/nodes.txt` file.
- **Test the generated code**: Run the generated code and verify that the output matches the
  contents of the `/tmp/nodes.txt` file.

### Set up environment

All commands should be run in the project's `.github/workflows/skills/node-builder`
directory.

All file paths are relative to the `.github/workflows/skills/node-builder` directory.

Follow these steps:

1. Create a new Python virtual environment with `python3 -m venv .venv`
2. Activate the virtual environment with `source .venv/bin/activate`
3. Install docutils with `pip install docutils`
4. With the provided file name, run `cat <filename> | python rst_to_nodes.py > /tmp/nodes.txt`
  to convert the reStructuredText input to docutils nodes and capture the output in the
  `/tmp/nodes.txt` file.

### Generate Python code

Write Python code that creates a list of docutils nodes matching the content of the
`/tmp/nodes.txt` file. Use the example at the end of this file as a reference.

Also follow these guidelines:

- Nodes should be declared before their child nodes.
- If possible, nodes should be declared and added to their parent in one line.
- Nodes should have classes and content assigned before child nodes are added.
- Nodes should only be added to a parent node once all child nodes have been assigned.
- If a string is used more than three times, it should be assigned to a variable.
- Structures like tables should be added to a container node.

Write the generated code to the `/tmp/nodegen.py` file so it can be called during
testing.

### Test the generated code

Before you write the code to a file or the chat, you must ensure that the output
of the generated Python code matches the parsed reStructuredText.

1. Run the generated code with `python3 /tmp/nodegen.py`
2. Verify that this output matches the contents of the `/tmp/nodes.txt` file
3. If the output does not match, adjust `/tmp/nodegen.py` and repeat

Once the output matches, share the code by either writing it to the requested file
or displaying it in chat.

## Example

Given the following reStructuredText input:

```
Heading
=======

.. important

    Admonition text

*Emphasis*

**Strong emphasis**

``Monospaced``

.. list-table::
    :header-rows: 1

    * - 1.1
      - 1.2
    * - 2.1
      - 2.2

.. code-block::

    literal block

```

The contents of the `/tmp/nodes.txt` file would be:

```
lorem ipsum
```

The generated Python code would be:

```python
title_node = nodes.title(text="Heading")

admonition_node = nodes.important()
admonition_content = nodes.paragraph()
admonition_content += nodes.Text("Admonition text")
admonition_node += admonition_content

italic_paragraph = nodes.paragraph()
italic_paragraph += nodes.emphasis(text="Emphasis")

bold_paragraph = nodes.paragraph()
bold_paragraph += nodes.strong(text="Strong emphasis")

monospaced_paragraph = nodes.paragraph()
monospaced_paragraph += nodes.literal(text="Monospaced")

div_node = nodes.container()
table_node = nodes.table()
div_node += table_node()

table_group = nodes.tgroup(cols=2)
table_group += nodes.colspec(width=50)
table_group += nodes.colspec(width=50)
table_node += table_group

table_head = nodes.thead()
header_row = nodes.row()

entry_1_1 = nodes.entry()
entry_1_1 += nodes.paragraph(text="1.1")
header_row = entry_1_1

entry_1_2 = nodes.entry()
entry_1_2 += nodes.paragraph(text="1.2")
header_row += entry_1_2

table_head += header_row
table_node += table_head

table_body = nodes.tbody()
body_row = nodes.row()

entry_2_1 = nodes.entry()
entry_2_1 += nodes.paragraph(text="2.1")
body_row += entry_2_1

entry_2_2 = nodes.entry()
entry_2_2 += nodes.paragraph(text="2.2")
body_row += entry_2_2

table_body += body_row
table_node += table_body

code_block_node = nodes.literal_block(text="literal block")
```
