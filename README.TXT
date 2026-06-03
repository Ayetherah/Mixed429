- Mixed429
How it came to be:
	I was wondering if I could make a system to better support hand writing binary than HEX.
	I do not know if I was successfull, I only know that the final release works better than
	the initial version. And I think that counts for something :3

Encode:
	python3 paper.py encode in-file-1.rawr | python3 abbreviate.py - > in-file-1.rawr.txt
	python3 pack.py in-file-1.rawr.txt > in-file-1.rawr-packed.txt

Decode:
	python3 unpack.py in-file-1.rawr-packed.txt > in-file-1.rawr-unpacked.txt
	python3 expand.py in-file-1.rawr-unpacked.txt | python3 decode-paper.py decode - out-file-1.rawr

Documentation:
	This thing does not work with high entropy files well, it does not work with big files well,
	it does not work with small files well. But once in a blue moon it can match or get a smaller
	size than the binary file being encoded, and that counts for something :3

Question:
	What does it do though?
Answer:
	He's doing his best :3
