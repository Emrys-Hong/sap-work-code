import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
districts = pd.read_excel('districts_in_thailand.xls')
corpus = list(districts.loc[:,districts.columns[0]])

# corpus = ['บ.เอสแอนด์เจ อินเตอร์เนชั่นแนล อินเดอร์ไพร 600/4 ม.11 ตำบลหน']
vectorizer = CountVectorizer()
features = vectorizer.fit_transform(corpus).todense()
for f in features:
    print(euclidean_distances('บ.เอสแอนด์เจ อินเตอร์เนชั่นแนล อินเดอร์ไพร 600/4 ม.11 ตำบลหน',f))