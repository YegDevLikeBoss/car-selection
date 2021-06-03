import pandas as pd
import random
from tqdm import tqdm
from gensim.models import Word2Vec

import warnings;
warnings.filterwarnings('ignore')

df = pd.read_excel('static/dataset.xlsx')
print("Dataset")
print(df.head())
print()

print(f"Dataset shape {df.shape} \n")

# check for missing values
print("Check for missing values")
print(df.isnull().sum())
print()

# remove missing values
df.dropna(inplace=True)

# again check missing values
print("Check for missing values")
print(df.isnull().sum())
print()

df['id']= df['id'].astype(str)

customers = df["customer_id"].unique().tolist()

print(f"{len(customers)} customers in dataset")

# shuffle customer ID's
random.shuffle(customers)

# extract 90% of customer ID's
customers_train = [customers[i] for i in range(round(0.9*len(customers)))]

# split data into train and validation set
train_df = df[df['customer_id'].isin(customers_train)]
validation_df = df[~df['customer_id'].isin(customers_train)]

# list to capture purchase history of the customers
purchases_train = []

# populate the list with the product codes
for i in tqdm(customers_train):
    temp = train_df[train_df["customer_id"] == i]["id"].tolist()
    purchases_train.append(temp)

# list to capture purchase history of the customers
purchases_val = []

# populate the list with the product codes
for i in tqdm(validation_df['customer_id'].unique()):
    temp = validation_df[validation_df["customer_id"] == i]["id"].tolist()
    purchases_val.append(temp)

# train word2vec model
model = Word2Vec(window = 10, sg = 1, hs = 0,
                 negative = 10, # for negative sampling
                 alpha=0.03, min_alpha=0.0007,
                 seed = 14, min_count=2) # TODO change mincount when updated dataset

model.build_vocab(purchases_train, progress_per=20)

model.train(purchases_train, total_examples = model.corpus_count,
            epochs=15, report_delay=1)

# save word2vec model
model.save("static/car_recommender.model")

model.init_sims(replace=True)

print("Model")
print(model)
print()

products = train_df[["id", "name"]]