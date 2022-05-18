

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = str(skus)
    allowed_chs = "ABCDE"
    if not all(ch in allowed_chs for ch in skus):  # make sure all string values are right otherwise return -1

        return -1
    else:
        global a_count
        a_count = skus.count("A")  # count occurrences of each item
        b_count = skus.count("B")
        c_count = skus.count("C")
        d_count = skus.count("D")
        e_count = skus.count("E")

        # Total Up cost of occurrences of Item A
        global a_total_discount_five_grouping_count
        global a_total_discount_three_grouping_count
        #global a_count
        global a_total_cost

        if a_count > 0:

            if a_count//5 > 0:
                a_total_discount_five_grouping_count = a_count//5
                a_count = a_count % 5  # a_count will be the remaining amount

            if a_count//3 > 0:  # some will be at discount cost
                a_total_discount_three_grouping_count = a_count//3
                a_count = a_count % 3

            a_total_cost = (200 * a_total_discount_five_grouping_count) + (130 * a_total_discount_three_grouping_count) + (50 * a_count)  # all at normal cost as less than 3 items
        else:
            a_total_cost = 0

        if b_count > 0:
            if b_count//2 > 0:  # some will be at discount cost
                b_total_discount_grouping_cost = b_count//2
                b_single_normal_cost = b_count % 2
                b_total_cost = (45 * b_total_discount_grouping_cost) + (30 * b_single_normal_cost)
            else:
                b_total_cost = 30 * b_count  # all at normal cost as less than 2 items
        else:
            b_total_cost = 0

        if c_count > 0:
            c_total_cost = c_count * 20
        else:
            c_total_cost = 0

        if d_count > 0:
            d_total_cost = d_count * 15
        else:
            d_total_cost = 0

        total_cost = a_total_cost + b_total_cost + c_total_cost + d_total_cost    # sum costs for all items

        return total_cost
    #raise NotImplementedError()


