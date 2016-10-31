#   DATASET
#path of the txt dataset
path = "allText.txt"
#sequence lenght to be learnt
maxlen = 16
#redundancy step (1 => full dataset)
redundancy=1
#dataset name
dataset_name='dataset{}_{}.h5'.format(maxlen,redundancy)

#   MODEL

#width of lstm layers
internal_size = 64

dropout = 0.8

#   TRAINING
#minibatch
batch_size = 2048
#name to be shown in the tensorboard
run_name="max{}_batch{}_int{}".format(maxlen,batch_size,internal_size)


