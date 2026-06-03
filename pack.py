#!/usr/bin/env python3
import sys
from collections import Counter

# --- Settings ---
MAX_PAIRS = 10          # use a-j lowercase letters
# -----------------

LETTERS = [chr(97 + i) for i in range(MAX_PAIRS)]  # a, b, c, ...

if len(sys.argv) != 2:
    print("Usage: python3 pack.py <final.txt>", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    lines = f.read().strip().splitlines()
if len(lines) < 2:
    raise ValueError("Input must have key line and data line")

key_line = lines[0]
data_line = lines[1]

# Split the data line into number tokens
tokens = data_line.split('.')

# Count all overlapping digit pairs across all tokens
pair_counter = Counter()
for tok in tokens:
    # Only consider tokens that are purely digits (not already replaced with a letter code)
    if tok.isdigit():
        for i in range(len(tok) - 1):
            pair_counter[tok[i:i+2]] += 1

# Choose the top MAX_PAIRS pairs
top_pairs = [pair for pair, _ in pair_counter.most_common(MAX_PAIRS)]

# Create mapping pair -> lowercase letter
pair_to_letter = {pair: LETTERS[i] for i, pair in enumerate(top_pairs)}
# For reverse mapping (we'll store it in the key line)
letter_to_pair = {v: k for k, v in pair_to_letter.items()}

# Apply replacement to each token
packed_tokens = []
for tok in tokens:
    if tok.isdigit():
        new_tok = tok
        for pair, letter in pair_to_letter.items():
            new_tok = new_tok.replace(pair, letter)
        packed_tokens.append(new_tok)
    else:
        # Already a code (uppercase letters, etc.), leave unchanged
        packed_tokens.append(tok)

# Build the new key line
pair_key_parts = [f"{letter}={pair}" for pair, letter in pair_to_letter.items()]
new_key_line = key_line + " " + " ".join(pair_key_parts) if key_line else " ".join(pair_key_parts)

# Output
print(new_key_line)
print('.'.join(packed_tokens))
