import h5py
import numpy as np
import datetime as dt

def printname(name):
        print name

with h5py.File('file.hdf5','w') as hf:
    
    #cretea new dataset and store numpy array
    dset = hf.create_dataset('my_data',(100,), dtype='i')
    dset[...] = np.arange(100)

    grp = hf.create_group('group1')
    #add some metadata to group
    grp.attrs['name'] = 'main group'
    grp.attrs['author'] = 'ksopyla'
    #create dataset in group1
    train = np.random.random([100,100])
    seg_ds = grp.create_dataset('train',data=train)
    
    
    #we can easily create nested groups
    sub_grp = grp.create_group('subgroup1/subgroup11')
    ones_arr = np.ones((250,5000))
    sub_ds = sub_grp.create_dataset('sensors', data=ones_arr)
    sub_ds.attrs['sensor type'] = 'sensor IO'
    sub_ds.attrs['date_taken'] = dt.datetime.now().isoformat()
    


with  h5py.File('file.hdf5','r') as hf:

    # show all objects in file
    hf.visit(printname)
    
    #get data set
    dset = hf.get('my_data')
    print(dset[0:10])
    
    #get data set, another way
    dset2 = hf['my_data']
    print(dset2[30:50])
    
    
    #get gruoup
    grp = hf['group1']
    grp.items()
    
    #iterate over attributes
    for item in grp.attrs.keys():
        print item + ":", grp.attrs[item]
    
    
    print(hf.keys())



hf = h5py.File('file.hdf5','r')

hf.close()
