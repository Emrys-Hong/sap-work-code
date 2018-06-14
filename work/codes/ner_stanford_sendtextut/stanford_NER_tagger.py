from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import nltk 

nltk.internals.config_java("C:/Program Files/Java/jdk-10.0.1/bin/java.exe")
st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz','stanford-ner.jar',encoding='utf-8')

text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'

tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

print(classified_text)