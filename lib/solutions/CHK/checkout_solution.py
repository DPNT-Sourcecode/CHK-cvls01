

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = str(skus)
    allowed_chs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not all(ch in allowed_chs for ch in skus):  # make sure all string values are right otherwise return -1

        return -1
    else:
        a_count = skus.count("A")  # count occurrences of each item
        b_count = skus.count("B")
        c_count = skus.count("C")
        d_count = skus.count("D")
        e_count = skus.count("E")
        f_count = skus.count("F")
        g_count = skus.count("G")
        h_count = skus.count("H")
        i_count = skus.count("I")
        j_count = skus.count("J")
        k_count = skus.count("K")
        l_count = skus.count("L")
        m_count = skus.count("M")
        n_count = skus.count("N")
        o_count = skus.count("O")
        p_count = skus.count("P")
        q_count = skus.count("Q")
        r_count = skus.count("R")
        s_count = skus.count("S")
        t_count = skus.count("T")
        u_count = skus.count("U")
        v_count = skus.count("V")
        w_count = skus.count("W")
        x_count = skus.count("X")
        y_count = skus.count("Y")
        z_count = skus.count("Z")

        # Create a lookup dictionary

        shop_item_dictionary = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20,
                            'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90, 'M': 15, 'N': 40,
                            'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 30, 'T': 20, 'U': 40,
                            'V': 50, 'W': 20, 'X': 90, 'Y': 10, 'Z': 50}


        #shop_item_dictionary.get('A')
        # Total Up cost of occurrences of Item A

        if a_count > 0:
            a_total_discount_five_grouping_count = 0
            a_total_discount_three_grouping_count = 0
            if a_count//5 > 0:
                a_total_discount_five_grouping_count = a_count//5
                a_count = a_count % 5  # a_count will be the remaining amount

            if a_count//3 > 0:  # some will be at discount cost
                a_total_discount_three_grouping_count = a_count//3
                a_count = a_count % 3  # These are charged at normal amount

            a_total_cost = (200 * a_total_discount_five_grouping_count) + (130 * a_total_discount_three_grouping_count) + (50 * a_count)  # total the cost
        else:
            a_total_cost = 0

        # Total Up cost of occurrences of Item E which has implications on b_count - every two E items gives a free B item

        if e_count > 0:
            if e_count//2 > 0:  # some will be at discount cost
                b_count = b_count - e_count//2
            e_total_cost = 40 * e_count  # all at normal cost as less than 2 items
        else:
            e_total_cost = 0

        # Total Up cost of occurrences of Item B

        if b_count > 0:
            if b_count//2 > 0:  # some will be at discount cost
                b_total_discount_grouping_cost = b_count//2
                b_single_normal_cost = b_count % 2
                b_total_cost = (45 * b_total_discount_grouping_cost) + (30 * b_single_normal_cost)
            else:
                b_total_cost = 30 * b_count  # all at normal cost as less than 2 items
        else:
            b_total_cost = 0

        # Total Up cost of occurrences of Item C

        if c_count > 0:
            c_total_cost = c_count * shop_item_dictionary.get('C')
        else:
            c_total_cost = 0

        # Total Up cost of occurrences of Item D

        if d_count > 0:
            d_total_cost = d_count * 15
        else:
            d_total_cost = 0

        # Total Up cost of occurrences of Item F

        if f_count > 0:
            if f_count // 3 > 0:  # some will be free - buy 2 get one free as long as 3 in basket
                f_groups_of_three_count = f_count // 3
                f_count = f_count - f_groups_of_three_count  # subtract the free item Fs as per deal

            f_total_cost = 10 * f_count  # all at normal cost as per new offer
        else:
            f_total_cost = 0

        total_cost = a_total_cost + b_total_cost + c_total_cost + d_total_cost + e_total_cost + f_total_cost    # sum costs for all items

        return total_cost


    #raise NotImplementedError()
