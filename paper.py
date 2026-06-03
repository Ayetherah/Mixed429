
#!/usr/bin/env python3
import sys

def file_to_paper(input_path):
    with open(input_path, 'rb') as f:
        data = f.read()

    size_chunk = len(data).to_bytes(4, 'big')
    data = size_chunk + data

    rem = len(data) % 4
    if rem:
        data += b'\x00' * (4 - rem)

    nums = []
    for i in range(0, len(data), 4):
        n = int.from_bytes(data[i:i+4], 'big')
        nums.append(str(n))

    return '.'.join(nums)


def paper_to_file(text, output_path):
    num_strings = text.strip().split('.')
    chunks = b''
    for s in num_strings:
        n = int(s)
        if n < 0 or n > 0xFFFFFFFF:
            raise ValueError(f"Number out of range: {n}")
        chunks += n.to_bytes(4, 'big')

    if len(chunks) < 4:
        raise ValueError("Missing size header")
    orig_len = int.from_bytes(chunks[:4], 'big')
    file_data = chunks[4:4 + orig_len]

    with open(output_path, 'wb') as f:
        f.write(file_data)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 paper.py encode file > paper.txt")
        print("  python3 paper.py decode paper.txt outputfile")
        sys.exit(1)

    command = sys.argv[1]

    if command == "encode":
        if len(sys.argv) != 3:
            print("Encode: python3 paper.py encode <file>")
            sys.exit(1)
        output = file_to_paper(sys.argv[2])
        print(output)

    elif command == "decode":
        if len(sys.argv) != 4:
            print("Decode: python3 paper.py decode <textfile> <outfile>")
            sys.exit(1)
        with open(sys.argv[2], 'r') as f:
            text = f.read()
        paper_to_file(text, sys.argv[3])
        print(f"File restored to {sys.argv[3]}")

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
