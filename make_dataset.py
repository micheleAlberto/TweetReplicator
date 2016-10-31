from __future__ import absolute_import, division, print_function

import os
from six.moves import urllib

import tflearn
from tflearn.data_utils import *
import h5py
from trainMeta import path,maxlen,batch_size,internal_size,dropout,run_name,redundancy,dataset_name


X, Y, char_idx = \
    textfile_to_semi_redundant_sequences(path, seq_maxlen=maxlen, redun_step=redundancy)
inverted_char_idx={v:k for k,v in char_idx.iteritems()}
char_vector=[inverted_char_idx[i] for i in range(len(inverted_char_idx))]


h5f = h5py.File(dataset_name, 'w')
h5f.create_dataset('X', data=X)
h5f.create_dataset('Y', data=Y)
h5f.create_dataset('charvector',data=char_vector)
h5f.close()
