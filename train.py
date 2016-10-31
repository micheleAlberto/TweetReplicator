import tflearn
from replicator import replicator
import h5py
from tflearn.data_utils import random_sequence_from_textfile
from trainMeta import path,maxlen,batch_size,internal_size,dropout,run_name,redundancy,dataset_name

dataset = h5py.File(dataset_name, 'r')
X = dataset['X']
Y = dataset['Y']
char_idx={k:v for k,v in enumerate(dataset['charvector'])}

m=replicator(char_idx)

for i in range(100):
    seed = random_sequence_from_textfile(path, maxlen)
    run_identifier=run_name+'_epoch'+str(i)
    m.fit(X, Y, 
	    validation_set=0.2, 
	    batch_size=batch_size,
        n_epoch=1, 
	    run_id=run_identifier) 
    m.save(run_identifier+'.sqg')
    print "-- TESTING..."
    print "-- Test with temperature of 1.0 --"
    print m.generate(140, temperature=1.0, seq_seed=seed)
    print "-- Test with temperature of 0.5 --"
    print m.generate(140, temperature=0.5, seq_seed=seed)
