def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """
    # pass  # implement me
    return dict(zip(keys, values))


def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """
    # pass  # implement me
    return({**d1,**d2})


###must be string


def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    """

    # pass  # implement me
    new_dict = {i: d1 for i in lst}
    return new_dict


def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    #
    # pass  # implement me
    new_dict = {k:v for k,v in datadict.items() if k in keylist}
    return new_dict


def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    # pass

    final_dict = {key: datadict[key] for key in datadict if key not in keylist}
    return final_dict


def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    if key in datadict.values():
        return True
    else:
        return False
    # pass


def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    # pass
    min_value = min(ddd.values())
    key = [k for k, v in ddd.items() if v == min_value]
    return key[0]


def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    # pass
    max_value = max(ddd.values())
    key = [k for k, v in ddd.items() if v == max_value]
    return key[0]
