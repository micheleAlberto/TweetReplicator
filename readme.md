#Tweet Replicator
TW is an LSTM based recurrent neural network that learn from the tweets (and linked articles) of a tweeter user to emulate the user tweets

##How to 
1. configure tweetMeta.py
2. ```python tweet_dumper.py```
3. configure trainMeta.py
4. ```python make_dataset.py```
5. ```
python train.py

tensorboard --logdir='logs/' ```
6. ```python run_model.py```

##Dependencies
*   [Tensorflow](https://www.tensorflow.org/)
*   [tflearn](http://tflearn.org/)
*   h5py
*   [tweepy](https://github.com/tweepy/tweepy)
*   glob
*   [Goose](https://github.com/grangier/python-goose)

