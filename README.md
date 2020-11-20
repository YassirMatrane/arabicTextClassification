# arabicTextClassification
After collecting 40 thousand tweets and preprocessing it, I used word embeddings with arabert and tf-idf along with two neural network architectures and 5 machine learning algorithms. Due to the huge size of the dataset, I chose Amazon SageMaker to train the models.


How do we run the project?

in the fold src we have the most important files that are used for:
1) preprocessing.py is used for applying preprocessing the the data such as cleaning, stop words and tokenization etc.
2) tfIdfWithModel.ipynb consists in applying word embeddings using tf-idf and storing the vectorizers in the fold vectorizers in order to use it for any further machine learning algorithms such as decision tree, naive bayes etc.
3) araBertPredMod.ipynb is used as a pretrained model and word embeddings 
4) run.py is the file from which we run our application 
