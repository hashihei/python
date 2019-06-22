import  numpy as np
import time

out = 49
outlist = []
start_t = time.time()
for i1 in np.arange(2,out-1,1):
  for i2 in np.arange(2,out-1,1):
    if (i1 * i2 == out):
      outlist.append(np.array(i1,i2))
  
end_t = time.time()
for out in outlist:
  print(out)
print("計算時間：",end_t - start_t," Sec")
