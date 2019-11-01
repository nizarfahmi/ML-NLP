from nltk.tokenize import sent_tokenize, word_tokenize

#example_text = "Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is pinkish-blue. You should not eat cardboard."
example_text = "Hai mas Nizar, apa kabarmu hari ini? Cuacanya cerah dan Python itu keren. Langitnya warna biru-pink. Kamu seharusnya gak makan kardus."

#print(sent_tokenize(example_text))
#
#print(word_tokenize(example_text))

for i in word_tokenize(example_text):
	print(i)