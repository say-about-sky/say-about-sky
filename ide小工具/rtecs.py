import time
def run_time(func,*v,**k):
    st=time.time()
    val=func(*v,**k)
    end=(time.time()-st)
    return val,end
