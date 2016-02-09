
start: parser
	python3 test_SSSL.py
	
parser:
	python3 -m grako -m SSSL -o parser_SSSL.py SSSL.ebnf
	
clean:
	rm *~
	rm parser_SSSL.py
	rm -r __pycache__
	
