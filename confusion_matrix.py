import numpy as np
def confusion_matrix(prediction, annotation, class_labels=None):
    """ Computes the confusion matrix.
    
    Parameters
    ----------
    prediction : np.array
        an N dimensional numpy array containing the predicted
        class labels
    annotation : np.array
        an N dimensional numpy array containing the ground truth
        class labels
    class_labels : np.array
        a C dimensional numpy array containing the ordered set of class
        labels. If not provided, defaults to all unique values in
        annotation.
    
    Returns
    -------
    np.array
        a C by C matrix, where C is the number of classes.
        Classes should be ordered by class_labels.
        Rows are ground truth per class, columns are predictions.
    """

    #######################################################################
    #                 ** TASK 3.1: COMPLETE THIS METHOD **
    #######################################################################

    assert len(prediction) == len(annotation)

    if not class_labels:
        class_labels = np.unique(annotation)

    confusion = np.zeros((len(class_labels), len(class_labels)), dtype=np.int)

    for index in range(len(prediction)):
        prediction_class = list(class_labels).index(prediction[index])
        annotation_class = list(class_labels).index(annotation[index])
        confusion[annotation_class][prediction_class] += 1

    return confusion

def accuracy(confusion):
    """ Computes the accuracy given a confusion matrix.
    
    Parameters
    ----------
    confusion : np.array
        The confusion matrix (C by C, where C is the number of classes).
        Rows are ground truth per class, columns are predictions
    
    Returns
    -------
    float
        The accuracy (between 0.0 to 1.0 inclusive)
    """

    #######################################################################
    #                 ** TASK 3.2: COMPLETE THIS METHOD **
    #######################################################################

    accuracy = confusion.trace() / confusion.sum()
    print()
    print("accuracy = trace / sum")
    print("= %d / %d" % (confusion.trace(), confusion.sum()))
    print ("= %.4f" %(accuracy))
    return accuracy

def precision(confusion):
    """ Computes the precision score per class given a confusion matrix.
    
    Also returns the macro-averaged precision across classes.
    
    Parameters
    ----------
    confusion : np.array
        The confusion matrix (C by C, where C is the number of classes).
        Rows are ground truth per class, columns are predictions.
    
    Returns
    -------
    np.array
        A C-dimensional numpy array, with the precision score for each
        class in the same order as given in the confusion matrix.
    float
        The macro-averaged precision score across C classes.   
    """

    #######################################################################
    #                 ** TASK 3.3: COMPLETE THIS METHOD **
    #######################################################################

    # Initialise array to store precision for C classes
    p = []
    for index in range(len(confusion)):
        true_positive = confusion[index][index]
        rest = confusion.sum(axis=0)[index]
        print()
        print("precision_%s= TP / col_sum" %(index+1))
        print("= %d / %d" % (true_positive, rest))
        print("= %.4f" %(true_positive/rest))
        p.append(true_positive / rest)

    # You will also need to change this        
    macro_p = np.average(p)
    p = np.array(p)
    return (p, macro_p)

def recall(confusion):
    """ Computes the recall score per class given a confusion matrix.
    
    Also returns the macro-averaged recall across classes.
    
    Parameters
    ----------
    confusion : np.array
        The confusion matrix (C by C, where C is the number of classes).
        Rows are ground truth per class, columns are predictions.
    
    Returns
    -------
    np.array
        A C-dimensional numpy array, with the recall score for each
        class in the same order as given in the confusion matrix.
    
    float
        The macro-averaged recall score across C classes.   
    """

    #######################################################################
    #                 ** TASK 3.4: COMPLETE THIS METHOD **
    #######################################################################

    # Initialise array to store recall for C classes
    r = []
    for index in range(len(confusion)):
        true_positive = confusion[index][index]
        rest = confusion.sum(axis=1)[index]
        print()
        print("recall_%s= TP / row_sum" %(index+1))
        print("= %d / %d" % (true_positive, rest))
        print("= %.4f" %(true_positive/rest))
        r.append(true_positive / rest)

    # You will also need to change this        
    macro_r = np.average(r)
    r = np.array(r)
    return (r, macro_r)

def f1_score(confusion):
    """ Computes the f1 score per class given a confusion matrix.
    
    Also returns the macro-averaged f1-score across classes.
    
    Parameters
    ----------
    confusion : np.array
        The confusion matrix (C by C, where C is the number of classes).
        Rows are ground truth per class, columns are predictions.
    
    Returns
    -------
    np.array
        A C-dimensional numpy array, with the f1 score for each
        class in the same order as given in the confusion matrix.
    
    float
        The macro-averaged f1 score across C classes.   
    """

    #######################################################################
    #                 ** YOUR TASK: COMPLETE THIS METHOD **
    #######################################################################

    # Initialise array to store recall for C classes
    f = []
    prec, p = precision(confusion)
    rec, r= recall(confusion)
    for i in range(len(confusion)):
        f1= (2 * prec[i] * rec[i]) / (prec[i] + rec[i])
        print()
        print("f1_%s= 2*precision*recall / precision + recall" %(i+1))
        print("= 2 * %.4f * %.4f  / %.4f +%.4f" % (prec[i], rec[i], prec[i], rec[i]))
        print("= %.4f" %(f1))

        f.append(f1)

    # You will also need to change this
    macro_f = np.average(f)
    f = np.array(f)
    return (f, macro_f)


print("----------plotting own cm ----------")
preds = ['neutral', 'negative', 'negative', 'neutral', 'negative', 
        'negative', 'neutral', 'neutral', 'neutral','positive', 
        'positive', 'neutral']
trues = ['neutral', 'neutral', 'negative', 'positive', 'neutral', 
        'neutral', 'neutral', 'negative', 'neutral','positive', 
        'positive', 'neutral']
classes = ['negative', 'neutral', 'positive']
        
confusion = confusion_matrix(preds,trues,classes)
acc = accuracy(confusion)

(p, macro_p) = precision(confusion)
(r, macro_r) = recall(confusion)
(f, macro_f) = f1_score(confusion)

print()
print(confusion)
print("\nAccuracy: {}".format(acc))
print("Class: Precision, Recall, F1")
for (i, (p1, r1, f1)) in enumerate(zip(p, r, f)):
    print("{}: {:.2f}, {:.2f}, {:.2f}".format(classes[i], p1, r1, f1))

print()
print("Macro-averaged Precision: {:.2f}".format(macro_p))
print("Macro-averaged Recall: {:.2f}".format(macro_r))
print("Macro-averaged F1: {:.2f}".format(macro_f))

print("------------------------------------")
print("----------evaluating existing cm ----------")

confusion = np.array([[1000,100,50],[20,0,10],[10,10,0]])
classes = ['class_1', 'class_2','class_3']
acc = accuracy(confusion)

(p, macro_p) = precision(confusion)
(r, macro_r) = recall(confusion)
(f, macro_f) = f1_score(confusion)

print()
print(confusion)
print("\nAccuracy: {}".format(acc))
print("Class: Precision, Recall, F1")
for (i, (p1, r1, f1)) in enumerate(zip(p, r, f)):
    print("{}: {:.2f}, {:.2f}, {:.2f}".format(classes[i], p1, r1, f1))

print()
print("Macro-averaged Precision: {:.2f}".format(macro_p))
print("Macro-averaged Recall: {:.2f}".format(macro_r))
print("Macro-averaged F1: {:.2f}".format(macro_f))
print("------------------------------------")


