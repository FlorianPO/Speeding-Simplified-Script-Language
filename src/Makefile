
start: parser
	python3 test_SSSL.py > AST
	
parser:
	python3 -m grako -m SSSL -o parser_SSSL.py SSSL.ebnf

clean:
	rm -f *~
	rm -f -r __pycache__

mrproper: clean
	rm -f parser_SSSL.py
	rm -f AST

	
