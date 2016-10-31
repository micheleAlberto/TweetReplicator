
from replicator import replicator
import h5py
from trainMeta import
from glob import glob
from tflearn.data_utils import random_sequence_from_textfile path,maxlen,batch_size,internal_size,dropout,run_name,redundancy,dataset_name

def select_most_trained_model():
    candidates=glob(run_name+'_epoch')
    return max(
        candidates,
        key=lambda filename:filename.split('_epoch')[1][:-4])

dataset = h5py.File(dataset_name, 'r')
char_idx={k:v for k,v in enumerate(dataset['charvector'])}
dataset.close()

m=replicator(char_idx)
m.load(select_most_trained_model())

l = 140

seed = random_sequence_from_textfile(path, maxlen)
print 'seed: \n\t',seed
for temperature in [0.4,0.6,0.8]:
    sentence=m.generate(l,
		    temperature=0.7, 
		    seq_seed=seed)
    print 't= ',temperature,' sentence: \n\t',sentence
	
