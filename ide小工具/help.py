import pickle
lod=r'.\help'
with open(lod,'wb') as f:
    pickle.dump(help,f)
