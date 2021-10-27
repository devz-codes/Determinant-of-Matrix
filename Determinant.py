def determinant(matrix):
    size = len(matrix)
    det =1

    count = size-1
    k=1
    no = 0

    for i in range(0,size):
        if i!=size-1:
            for j in range(count,k-1,-1):
                if matrix[i][i]==0:
                    for l in range(0,size):
                        c = matrix[i][l]
                        matrix[i][l] = matrix[i+1][l]
                        matrix[i+1][l] = c
                    
                    no += 1
                
                factor = matrix[j][i]/matrix[i][i]
                for l in range(0,size):
                    matrix[j][l] -= factor*matrix[i][l]
        else:
            break
        k += 1
    
    for i in range(0,size):
        det *= matrix[i][i]
    
    det *=pow(-1,no)
    return det
