import numpy as np
def improbable(warehouse):
    cols_max_values = [max(warehouse[:,[i]]) for i in xrange(len(warehouse))]
    rows_max_values = warehouse[np.arange(len(warehouse)), np.argmax(warehouse, axis=1)]
    total_crate = 0

    #step 1: move the crates into suitable positions
    for idx,row in enumerate(warehouse):
        # if max value on a row is on the row i, first col
        # then find the same value on others column, which is not in same row with current

        if max(row) == warehouse[[idx][0]][0]:
            indices = [x for x in zip(*np.where(warehouse == max(row))) if x[0] != idx]
            for i in indices:
                if max(warehouse[i[0]]) > max(row):
                    warehouse[idx,i[1]], warehouse[i[0],i[1]] = warehouse[i[0],i[1]], warehouse[idx,i[1]]

                    #warehouse[[idx],i[1]][0],warehouse[[i[0]],i[1]][0] = warehouse[[i[0]],i[1]][0],warehouse[[idx],i[1]][0]

    for r in xrange(len(warehouse)):
        for c in xrange(len(warehouse[0])):
            if warehouse[r,c] < max(warehouse[r]) and warehouse[r,c] < max(warehouse[:,c]) and warehouse[r,c] > 1:
                total_crate += warehouse[r,c] - 1
                warehouse[r,c] = 1


    print warehouse



    #print warehouse[np.arange(len(warehouse)), np.argmax(warehouse, axis=0)]

if __name__ == '__main__':
     improbable(warehouse=np.array([[1,4,0,5,2],
                                    [2,1,2,0,1],
                                    [0,2,3,4,4],
                                    [0,3,0,3,1],
                                   [1,2,2,1,1]]))

     improbable(warehouse=np.array([[5,]]))
    #print np.arange(35).reshape(5,7)
    #print np.arange(35).reshape(5, 7)[1:,::3]