from xml.dom.expatbuilder import parseString


## Think SLICING for many of these.

def create_list_from_tuple(t):
    """
    This function takes a tuple of elements and returns a list containing those elements of the tuple.
    """
    # pass  # implement me
    list_of_tuple = [i for i in t]
    return list_of_tuple


#

def drop_last(lst):
    """
    This function takes a list and returns a list with the last item removed.
    """
    # pass  # implement me
    lst.pop()
    return lst


#

def drop_first_two(lst):
    """
    This function takes a list and returns a list with the first two items removed.
    """
    # pass  # implement me
    first_second_removed = [lst.pop(0)] + [lst.pop(0)]
    return lst


#

def drop_mangle(lst):
    """
    This function takes a list and returns a list with the first two items AND last item removed.
    """
    # pass  # implement me
    first_two_last = [lst.pop(0)] + [lst.pop(0)] + [lst.pop(-1)]
    return lst


#

def add_item_front(lst, a):
    """
    This function takes a list and an item,
    returning the list with the item prepended to the list
    """
    # pass  # implement me

    lst.insert(0, a)
    return lst


#

def add_item_end(lst, a):
    """
    This function takes a list and an item,
    returning the list with the item appended to the list
    """
    # pass  # implement me
    lst.append(a)
    return lst


#


def add_list_to_list(lsta, lstb):
    """
    This function takes two lists and appends one to the other,
    returning a list
    """
    # pass  # implement me
    newlist = lsta + lstb
    return newlist


#

def list_and_list_to_tuple(lsta, lstb):
    """
    This function takes two lists and returns a tuple containing the two lists
    """
    # pass  # implement me
    lstc = [lsta] + [lstb]
    tuple_lst = tuple(lstc)
    return tuple_lst
#

def list_and_list_to_list(lsta, lstb):
    """
    This function takes two lists and returns a list containing the two lists
    """
    # pass  # implement me
    lstc = [lsta] + [lstb]
    return lstc



def list_from_range(n):
    """
    This function returns list with 0..n as integers in a list
    """
    # pass  # implement me
    nlst = list(range(n))
    return nlst


def list_from_range2(n, m):
    """
    This function returns list with n..m (without m) as integers in a list
    """
    # pass  # implement me
    nlst = list(range(n,m))
    return nlst


def list_from_range3(n, m):
    """
    This function returns list with n..m (including m(!)) as integers in a list
    """
    # pass  # implement me
    nlst = list(range(n,m+1))
    return nlst


def list_from_range4(n, m):
    """
    This function returns list with n..m (WITHOUT n and including m) as integers in a list
    """
    # pass  # implement me
    nlst = list(range(n+1,m+1))
    return nlst


def list_from_range_by(n, step):
    """
    This function returns list with 0..n as integers by step in a list
    (read the test)
    """
    # pass  # implement me
    nlst = list(range(0,n,step))
    return nlst


def rev_list(lst):
    """
    This function returns list which is a reverse of the argument list
    (read the test)
    """
    # pass  # implement me
    reverselst = lst[::-1]
    return reverselst


def concat_list_indexwise(lst1, lst2):
    """
    Write a program to add two lists index-wise. 
    Create a new list that contains the 0th index item from both the list, 
    then the 1st index item, and so on till the last element. 
    Any leftover items will get added at the end of the new list.
    """
    # parseString  # implement me
    lst3 = [lst1[i] + lst2[i] for i in range(len(lst1))]
    return lst3



def square_each_item(lst):
    """
    This function returns list which each item in argument list has been squared
    (read the test)
    """
    # pass  # implement me
    nlst = [value**2 for value in lst]
    return nlst


def remove_empty_strs(lst):
    """
     Remove empty strings from the list of strings
     """
    # pass
    newlst = [i for i in lst if i != ""]
    return newlst


def remove_item_from(lst, aaa):
    """
    Remove all occurrences of a specific item from a list.
    """
    # pass
    newlst = [i for i in lst if i != aaa]
    return newlst


def leave_item_in(lst, aaa):
    """
    Leave all occurrences of a specific item in a list.
    """
    # pass
    newlst = []
    for i in lst:
        if i == aaa:
            newlst.append(i)
    return newlst




def length_of(lst):
    """
    return the length of the list
    """
    # pass
    return len(lst)

