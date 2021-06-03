from gensim.models import Word2Vec

model = Word2Vec.load("static/car_recommender.model")

def recommend(car_id: str):
    return model.wv.most_similar(car_id, topn=5)