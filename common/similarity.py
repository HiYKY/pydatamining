from math import sqrt

def user_jaccard_similarity(set1, set2):
    return len(set1.intersection(set2))/len(set1.union(set2))

def user_cosine_similarity(set1, set2):
    return len(set1.intersection(set2))/sqrt(len(set1)*len(set2))

def user_similarity_improve():
#    hot item and cold item.
#    code item : more percentage.
    pass


def item_similarity_simple(set1, set2):
#    return |set1 and set2|/|set1|
    return user_cosine_similarity(set1,set2)


def test():
    print user_jaccard_similarity(set([1,2,3]), set([3,5,6]))==1/5
    print user_cosine_similarity(set([1,2,3]), set([3,5,6]))==1.0/3.0
    print item_similarity_simple(set([1,2,3]), set([3,5,6]))==1.0/3.0
    

#test()