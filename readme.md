#Tweet Replicator
Tweet Replicator is an LSTM based recurrent neural network that learn from the tweets (and linked articles) of a tweeter user to emulate the user tweets

##How to 
1. edit tweetMeta.py
2. ```python tweet_dumper.py```
3. tweak trainMeta.py
4. ```python make_dataset.py```
5. ```python train.py ```

To compare different parametrization : ``` tensorboard --logdir='logs/' ```

To generate some random tweet:

```python run_model.py```

##Dependencies
*   [Tensorflow](https://www.tensorflow.org/)
*   [tflearn](http://tflearn.org/)
*   h5py
*   [tweepy](https://github.com/tweepy/tweepy)
*   glob
*   [Goose](https://github.com/grangier/python-goose)

