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

1. lorem ipsum

### Test the generated code

1. lorem ipsum

## Example

Given the following reStructuredText input:

```
lorem ipsum
```

The output of step 4 will be:

```
lorem ipsum
```

The Python code generated in step 5 would be:

```python
lorem ipsum
```
