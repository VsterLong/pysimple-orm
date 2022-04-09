def dict_2_class(dict_obj, class_name=None):
    ret_obj = class_name()
    for key in dict_obj:
        if hasattr(ret_obj, key):
            setattr(ret_obj, key, dict_obj[key])

    return ret_obj


def dict_arr_2_class(dict_arr, class_name=None):
    obj_arr = []
    for o in dict_arr:
        obj = dict_2_class(o, class_name)
        obj_arr.append(obj)
    return obj_arr
