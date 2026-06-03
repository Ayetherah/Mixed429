#!/usr/bin/env python3
import sys
from collections import Counter

# --- Settings ---
MIN_LENGTH = 6          # only numbers with at least this many digits
MAX_CODES = 52          # max codes to use (A-Z, then ZA-ZZ)
# -----------------

def generate_codes(n):
    """Generate up to n codes: A, B, ..., Z, ZA, ZB, ..., ZZ"""
    codes = []
    # Single letters A-Z
    for i in range(26):
        if len(codes) >= n:
            break
        codes.append(chr(65 + i))
    # Z + letter combinations ZA-ZZ
    for i in range(26):
        if len(codes) >= n:
            break
        codes.append('Z' + chr(65 + i))
    return codes

# Read input
if len(sys.argv) < 2:
    print("Usage: python3 abbreviate.py <encoded.txt>", file=sys.stderr)
    sys.exit(1)

if sys.argv[1] == '-':
    text = sys.stdin.read().strip()
else:
    with open(sys.argv[1], 'r') as f:
        text = f.read().strip()

nums = text.split('.')
freq = Counter(nums)

# Filter long numbers, sort by frequency then length
candidates = [(num, cnt) for num, cnt in freq.items() if len(num) >= MIN_LENGTH]
candidates.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

# Take top N candidates
chosen = [num for num, _ in candidates[:MAX_CODES]]
codes = generate_codes(len(chosen))

# Build mapping
mapping = {num: code for num, code in zip(chosen, codes)}

# Replace in sequence
abbreviated = [mapping.get(n, n) for n in nums]

# Output key line and data line
key_parts = [f"{code}={num}" for num, code in zip(chosen, codes)]
print(" ".join(key_parts))
print('.'.join(abbreviated))
