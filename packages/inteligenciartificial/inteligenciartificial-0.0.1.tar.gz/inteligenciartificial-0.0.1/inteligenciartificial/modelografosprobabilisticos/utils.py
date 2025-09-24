def accuracy_score(y_true, y_pred):
    y_true=list(y_true); y_pred=list(y_pred)
    return sum(int(a==b) for a,b in zip(y_true,y_pred))/len(y_true) if y_true else 0.0
