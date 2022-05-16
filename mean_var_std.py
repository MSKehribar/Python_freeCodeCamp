# This function named calculate() uses Numpy. It takes 9 value gives us the 
# mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

class calculate():
    def __init__(self,dizi):
        self.dizi=dizi
        

    def __repr__ (self):
        import numpy as np
        if len(self.dizi)!=9:
            x=f'ValueError : List must contain nine numbers.' 
        else:
            x=f''
            matris = np.array(self.dizi).reshape(3,3).copy()
            calc=dict()
            calc["mean"]=               [np.mean(matris,axis=0).tolist(),   np.mean(matris,axis=1).tolist(),np.mean(matris)]
            calc["variance"]=           [np.var(matris,axis=0).tolist(),    np.var(matris,axis=1).tolist(), np.var(matris)]
            calc["standard deviation"]= [np.std(matris,axis=0).tolist(),    np.std(matris,axis=1).tolist(), np.std(matris)]
            calc["max"]=                [np.max(matris,axis=0).tolist(),    np.max(matris,axis=1).tolist(), np.max(matris)]
            calc["min"]=                [np.min(matris,axis=0).tolist(),    np.min(matris,axis=1).tolist(), np.min(matris)]
            calc["sum"]=                [np.sum(matris,axis=0).tolist(),    np.sum(matris,axis=1).tolist(), np.sum(matris)]
            
            print("\n{ \n")
            for i,k in calc.items():
                print("    '",i,"': ",k,"\n")
            print("} \n")
        return x



# Test Part

calculate([0,1,2,3,4,5,6,7,8])

