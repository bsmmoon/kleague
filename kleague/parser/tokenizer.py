from kleague.parser.token import Token

class Tokenizer():


	def __init__(self):
		print('Tokenizer init')

	def tokenize(self, inputString):
		stringlist = inputString.split(';')

		tokenlist = []
		for string in stringlist:
			token = Token()
			token.setValue(string)
			tokenlist.append(token)

		return tokenlist