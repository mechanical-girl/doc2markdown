import sys

"""
doc2markdown creates a GitHub-Markdown formatted README.md file in the local
directory, containing neatly formatted docstrings of the input file.

"""

def naUnd(): pass

def trim(docstring):
    if not docstring:
        return ''
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = 2**31-1
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < 2**31-1:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\n'.join(trimmed)

try: fileName = sys.argv[1]
except: naUnd()

while True:
    try:
        with open(fileName, 'r') as f:
            file = f.read()
        break
    except:
        fileName = input("File to read: ")

file = file.replace('class', 'def')
decs = file.split('def')

with open('README.md','w') as readme:
    readme.write('{}\n======\n{}\n\nSyntax\n------\n'.format(fileName.split('.')[0],trim(decs[0].split('"""')[1])))

for dec in decs[1:]:
    if '"""' in dec:
        stack = dec.split('"""')
        with open('README.md','a') as readme:
            functionName = "###{}".format(stack[0].split('(')[0])
            functionSyntax = "`{}`: ".format(stack[0].replace(':',''))
            functionDocs = trim(stack[1])
            readme.write("{}\n{}\n{}\n\n".format(functionName,functionSyntax, functionDocs))
