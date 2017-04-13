import sys, os

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

filename = ''
filepath = ''
try: fileName = sys.argv[1]
except: naUnd()

while True:
    try:
        try:
            if '/' in fileName:
                filepath = fileName[::-1].split('/',1)[1][::-1]
                filename = fileName[::-1].split('/',1)[0][::-1]
                os.chdir('{}//'.format(filepath))
            else: filename = fileName
        except: naUnd()
        with open(filename, 'r') as f:
            file = f.read()
        break
    except:
        fileName = input("File to read: ")
        if '/' in fileName:
            filepath = fileName[::-1].split('/',1)[1][::-1]
            filename = fileName[::-1].split('/',1)[0][::-1]
            os.chdir('{}//'.format(filepath))
        else: filename = fileName
        with open(filename, 'r') as f:
            file = f.read()

lines = file.splitlines()
file = ""
for i, line in enumerate(lines):
    if line.lstrip()[0:4] == "def " or line.lstrip()[0:6] == "class ":
        indent = (len(line) - len(line.lstrip()))
        line = line[indent:]
    file += "{}\n".format(line)

classes = file.split('\nclass ')
items = []
for item in classes: items.append("*{}".format(item))
decs = []
for item in items: decs += item.split('\ndef ')

for dec in decs:
    if not '"""' in dec: decs.remove(dec)

with open('README.md','w') as readme:
    readme.write('{}\n======\n{}\n\nSyntax\n======\n'.format(filename.split('.')[0],trim(decs[0].split('"""')[1])))

for i, dec in enumerate(decs[1:]):
    if '"""' in dec:
        stack = dec.split('"""')
        with open('README.md','a') as readme:
            if stack[0][0] == "*":
                stack[0] = stack[0][1:]
                name = "{}\n------".format(stack[0].split('(')[0])
                syntax = ''
            else:
                name = "### {}".format(stack[0].split('(')[0].replace('_','\\_'))
                syntax = "`{}`: ".format(stack[0].split(':')[0].replace('\n','\n\n'))
            docs = trim(stack[1])
            readme.write("{}\n{}\n{}\n\n".format(name,syntax, docs))
