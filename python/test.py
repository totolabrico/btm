import copy

from settings import*

seq=[]
i=0 
while i<2:
	seq.append(copy.deepcopy(sequencer_setting))
	i+=1
seq[0][0][1]=False
print(seq[1][0][1])
