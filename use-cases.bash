# Collection of use cases.

# test stdin with no filename provided
python3 sk-cat.py

# test stdin with a '-' provided
python3 sk-cat.py -

# test single filename
python3 sk-cat.py testfiles/test.txt

# test single filename and then stdin
python3 sk-cat.py testfiles/test.txt -

# test stdin and then filenames
python3 sk-cat.py - testfiles/test.txt

# test multiple filenames
python3 sk-cat.py testfiles/test.txt testfiles/test2.txt

# test with a directory
python3 sk-cat.py testfiles

# test with a filename and a directory
python3 sk-cat.py testfiles/test.txt testfiles

# test pipelining
head -n1 testfiles/test.txt | python3 sk-cat.py -

# test pipelining 2
tree | head -n3 | python3 sk-cat.py -

# test with single non existing file
python3 sk-cat.py testfiles/file.txt

# test with one existing and one non existing file
python3 sk-cat.py testfiles/test.txt testfiles/file.txt

# TODO: Add functionality for -n
