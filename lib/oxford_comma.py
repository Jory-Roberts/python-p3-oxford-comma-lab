def oxford_comma(items):
    if len(items) == 1 :
        return " ".join(items)
    elif len(items) == 2 :
        return " and ".join(items)
    else :
        string_item = ""
        i = 1
        for item in items :
            if(len(items) == i) :
                string_item = string_item + "and " + item
            else :
                i += 1
                string_item = string_item + item + ", "
    return string_item
