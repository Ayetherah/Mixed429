#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("Usage: python3 expand.py <final.txt>", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    lines = f.read().strip().splitlines()

if len(lines) < 2:
    raise ValueError("File must contain key line and data line")

key_line = lines[0]
data_line = lines[1]

# Parse key line: "A=4294967295 B=4278124286 ... ZA=12345678 ..."
code_to_num = {}
for pair in key_line.split():
    code, num = pair.split('=')
    code_to_num[code] = num

# Expand the data line
tokens = data_line.split('.')
expanded = [code_to_num.get(t, t) for t in tokens]

print('.'.join(expanded))
