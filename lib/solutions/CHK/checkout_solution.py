

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = str(skus).upper()  # Convert string to Upper Case
    allowed_chs = "ABCD"
    if not all(ch in allowed_chs for ch in allowed_chs): # make sure all string values are right otherwise return -1

        return -1
    else:
        a_count = skus.count("A")  # count occurrences of each item
        b_count = skus.count("B")
        c_count = skus.count("C")
        d_count = skus.count("D")

        #Total Up cost of occurrences of Item A

        if a_count > 0:
            


    #raise NotImplementedError()

