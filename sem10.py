y = [7, 6, 8, 4, 7, 11, 100]

def l1(y):
    best_error = 1000000
    best_y_hat = -1
    for temp_y_hat in range(min(y), max(y)):
        temp_error = 0
        for observation in y:
            temp_error+=abs(observation-temp_y_hat)
        temp_error = temp_error/len(y)
        if best_error > temp_error:
            best_error = temp_error
            best_y_hat = temp_y_hat
    return (best_y_hat, best_error)



def l2(y):
    best_error = 1000000
    best_y_hat = -1
    for temp_y_hat in range(min(y), max(y)):
        temp_error = 0
        for observation in y:
            temp_error+=pow(observation-temp_y_hat,2)
        temp_error = temp_error/len(y)
        if best_error > temp_error:
            best_error = temp_error
            best_y_hat = temp_y_hat
    return (best_y_hat, best_error)


print(f"y_hat fot L1: {l1(y)[0]} with error {l1(y)[1]}")
print(f"y_hat fot L2: {l2(y)[0]} with error {l2(y)[1]}")