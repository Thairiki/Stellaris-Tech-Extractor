from antlr4 import *
from antlr_output.stellarisLexer import stellarisLexer
from antlr_output.stellarisParser import stellarisParser
from CustomStellarisVisitor import CustomStellarisVisitor

def execute(stellaris_script: str):
	input_stream = InputStream(stellaris_script)
	lexer = stellarisLexer(input_stream)
	token_stream = CommonTokenStream(lexer)
	parser = stellarisParser(token_stream)
	tree = parser.content()
	# print(tree.toStringTree(recog=None))
	visitor = CustomStellarisVisitor()
	parsed_data = visitor.visit(tree)

	return parsed_data
