import inspect
import dis

import sklearn
from sklearn import decomposition
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Pre-Processing
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
x = {ppname: {i:j for i,j in preproces().__dict__.items()} for ppname,preproces in [(i,j) for i,j in getmembers(sklearn.preprocessing.data,isclass) if j.__module__== 'sklearn.preprocessing.data']}

print(x)

# Example: Update individual pre-processors with selected parameters. If not specified, default parameter settings will apply
uparams = {
           'Normalizer':{
                         'norm': ['l1', 'l2', 'max'],
                         'include_bias': [False]
                        },
           'Anormalizer':{
                         'norm': ['l1', 'l2', 'max'],
                         'include_bias': [False]
                         }          
          }

for key in uparams.keys():

    if key not in x.keys():
        print(key,'\t',repr(key),'is not a valid class ')
    if key in x.keys():
        for par in uparams[key]:
            if par in x[key]:
                if x[key][par]==uparams[key][par]:
                    print(key,'\t',repr(par),'is already equal to ',repr(x[key][par]))
                else:
                    print(key,'\t',repr(par),'updated to',uparams[key][par],'from',repr(x[key][par]))
                    x[key][par]=uparams[key][par]
            elif par not in x[key]:
                print(key,'\t',repr(par),'is not in',x[key].keys())
