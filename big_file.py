import h5py
import numpy as np
import time
import datetime as dt

def printname(name):
        print name

CHUNK = 100
MAX_CHUNKS=5000
ARR_SIZE = 1000

row_count = CHUNK


kbytes_write = CHUNK*ARR_SIZE*4*(MAX_CHUNKS/1024.0)
print('Write {} KB, {} MB'.format(kbytes_write, kbytes_write/1024))

start = dt.datetime.now()
with h5py.File('large.hdf5','w') as hf:
    dset = hf.create_dataset('data',
                        (CHUNK,ARR_SIZE),
                        maxshape=(None,ARR_SIZE), chunks=True)
    
    #write first chunk
    arr = np.ones((CHUNK, ARR_SIZE))
    dset[:]=arr
    
    #expand dataset and write next chunks in to the file
    for i in range(MAX_CHUNKS):
        
        arr = (i+2)*np.ones((CHUNK, ARR_SIZE))
        rows = arr.shape[0]    
            
        dset.resize(row_count+rows, axis=0)
        
        dset[row_count:]=arr
        
        row_count+= rows
 
duration = dt.datetime.now() - start
throughput = kbytes_write/(1024*duration.total_seconds())
print('Writing takes {} {}MB/s'.format(duration, throughput))
    
    
with h5py.File('large.hdf5','r') as hf
    hf.visit(printname)
    dset = hf.get('data')
    
    
    a = np.zeros((100,100))
    dset.read_direct(a, np.s_[0:10,0:10],np.s_[0:10,0:10])
    print(dset[80:110])
    print(hf.keys())
    print(dset.shape)
