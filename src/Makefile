
start: parser
	python3 test_SSSL.py > AST
	
parser:
	python3 -m grako -m SSSL -o parser_SSSL.py SSSL.ebnf
	
clean:
	rm *~
	rm parser_SSSL.py
	rm AST
	rm -r __pycache__
	
