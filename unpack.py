#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("Usage: python3 unpack.py <packed.txt>", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    lines = f.read().strip().splitlines()
if len(lines) < 2:
    raise ValueError("Input must have key line and data line")

key_line = lines[0]
data_line = lines[1]

# Separate uppercase‑code mappings from pair mappings
upper_map = {}   # A=..., ZA=... etc.
pair_map = {}    # a=..., b=... etc.

for item in key_line.split():
    if '=' in item:
        code, val = item.split('=', 1)
        if len(code) == 1 and code.islower():
            # lowercase → pair mapping
            pair_map[code] = val
        else:
            # uppercase code (A, B, ..., ZA, ZZ) → keep for expand.py
            upper_map[code] = val

# Reconstruct the original uppercase key line (without pair mappings)
upper_key_line = " ".join(f"{code}={num}" for code, num in upper_map.items())

# Expand packed tokens
tokens = data_line.split('.')
expanded = []
for tok in tokens:
    if any(ch.islower() for ch in tok):
        # This token contains packed pairs; expand them
        new_tok = tok
        for letter, pair in pair_map.items():
            new_tok = new_tok.replace(letter, pair)
        expanded.append(new_tok)
    else:
        # Already a plain number or an uppercase code — keep unchanged
        expanded.append(tok)

# Output: uppercase key line + expanded data line
print(upper_key_line)
print('.'.join(expanded))
