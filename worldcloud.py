
inputText = "ich bin ein neuer Text. Mich kann man bearbeiten, wie jeden Text!"
uninteresting_words = ("ich","mich","man", "ein")

def is_relevant(word, word_set):
	for r_word in word_set:
		if word.lower() == r_word:
			return False
	return True

def count_words(inputText, uninteresting_words):
	textList = inputText.split()
	relevant_words = {}
	for text in textList:
		alphaChar = []
		word = ""
		for character in text:
			if character.isalpha():
				alphaChar.append(character)
			word = "".join(alphaChar)
		# jetzt muss verglichen werden ob word nicht unrelevant
		if is_relevant(word,uninteresting_words):
			word = word.lower()
			if word not in relevant_words:
				relevant_words[word] = 0
			relevant_words[word] += 1
	return relevant_words

result = count_words(inputText,uninteresting_words)
print(result)