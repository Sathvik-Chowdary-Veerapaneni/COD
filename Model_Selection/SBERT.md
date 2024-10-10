# SBERT

## BERT
- BERT were popular for constructing **word embeddings**, vectors of numbers representing semantic meanings of words.

1. Words in the form of embeddings, has huge advantage for ML algorithms.
2. Were, ML algo not able to operate with raw texts
3. Converting the raw words into vectors, algorithms can easily operatable.
4. Which opens the door to comapre different words, by their similarity score using different standard metric distances such as, Ecludidean, and Cosine following more.

## Problem with BERT
- The basic BERT version builds embeddings only on word level, nothing but individual word had their respective vector values.
- Core problem of BERT, every time two sentences are passaed and procesed simultaneously making it difficult to get embeddings, that would independently represent only a single sentence.
- Deriving independet sentence embeddings is one of the main problems of BERT
  


### Cross-Encoder architecture
- Ineffieciency of cross-encoder architecture
- It is possible to use BERT for calculating the similarity between a pair of documents.
- But, it leads to a quadratic complexity
  - ``` n*(n-1)/2 ```
  - with n=10,000 requires, 49 Million inference BERT computaions. which not optimized.

## Approches
1. So, after analyzing the above, cross encoder architecture.
2. It looks logical to pre-compute embeddings independently for each  setence and storing those embeddginds.
3. And, We can directly compute a choosen distance metric standards, on pairs of documents which is much faster.
4. 


## SBERT Model
To overcome this with upgraded models, we had **SBERT**.
1. It works with siamese(twin) network concept, which means, each time two setences are passed independently through same BERT model. 
2. The model accepts both inputs in parllel, so the outputs are not dependent on each other.
3. sentence -> BERT Model -> Polling Layer
   1. A pooling layer is applied to BERT embeddings to get thir lower dimensionality representation.
      1. Intial 512, 768 dimensional vectors are transformed to a choosing mean pooling layer as **default one**
      2. when botj sentences are passed through pooling layers, we have two 768 dimensional vectors **u and v**.
      3. using these two vectos, authors proposed three approches
         1. Classification Objective - 