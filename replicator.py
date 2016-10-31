import tflearn
from trainMeta import path,maxlen,batch_size,internal_size,dropout,run_name,redundancy,dataset_name

def replicator(char_idx):
    g = tflearn.input_data([None, maxlen, len(char_idx)])
    g = tflearn.lstm(g, internal_size, return_seq=True)
    g = tflearn.dropout(g, dropout)
    g = tflearn.lstm(g, internal_size, return_seq=True)
    g = tflearn.dropout(g, dropout)
    g = tflearn.lstm(g, internal_size)
    g = tflearn.dropout(g, dropout)
    g = tflearn.fully_connected(g, len(char_idx), activation='softmax')
    g = tflearn.regression(g, 
        optimizer='adam', 
        loss='categorical_crossentropy',
        learning_rate=0.05)
    rep = tflearn.SequenceGenerator(g, dictionary=char_idx,
                      seq_maxlen=maxlen,
                      clip_gradients=5.0,
			          tensorboard_verbose=3,
			          tensorboard_dir='logs',
                      checkpoint_path='tweeterReplicator')
    return rep
