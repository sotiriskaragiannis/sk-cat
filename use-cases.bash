# Collection of use cases.

# 1. test stdin with no filename provided
python3 sk-cat.py

# 2. test stdin with a '-' provided
python3 sk-cat.py -

# 3. test single filename
python3 sk-cat.py testfiles/test.txt

# 4. test single filename and then stdin
python3 sk-cat.py testfiles/test.txt -

# 5. test stdin and then filenames
python3 sk-cat.py - testfiles/test.txt

# 6. test multiple filenames
python3 sk-cat.py testfiles/test.txt testfiles/test2.txt

# 7. test with a directory
python3 sk-cat.py testfiles

# 8. test with a filename and a directory
python3 sk-cat.py testfiles/test.txt testfiles

# 9. test pipelining
head -n1 testfiles/test.txt | python3 sk-cat.py -

# 10. test pipelining 2
tree | head -n3 | python3 sk-cat.py -

# 11. test with single non existing file
python3 sk-cat.py testfiles/file.txt

# 12. test with one existing and one non existing file
python3 sk-cat.py testfiles/test.txt testfiles/file.txt

# 13. input pipelining
sed G testfiles/test.txt | python3 sk-cat.py

# 14. output pipelining
python3 sk-cat.py testfiles/test.txt | head -n4

# 15. both input and output pipelining
sed G testfiles/test.txt | python3 sk-cat.py | head -n4

# 16. test with -n with one file
python3 sk-cat.py testfiles/test2.txt -n

# 17. test with -n with two files
python3 sk-cat.py testfiles/test.txt testfiles/test2.txt -n

# 18. test with -n and output pipelining
python3 sk-cat.py testfiles/test.txt -n | head -n4

# 19. test with -n and input pipelining
sed G testfiles/test.txt | python3 sk-cat.py -n

# 20. test with -n and stdin
python3 sk-cat.py -n
