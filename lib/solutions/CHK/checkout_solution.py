

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

        def items_one_free_cost(offer_constraint, total_count, item_name):  # return the total cost for bogof type offers
            if total_count // offer_constraint > 0:  # some will be free -
                count_of_full_groups = total_count // offer_constraint  # count of complete sets where one item will be free
                total_count = total_count - count_of_full_groups  # subtract the free item Fs as per deal
                total = shop_item_dictionary.get(item_name) * total_count  # total cost
            else:
                total = shop_item_dictionary.get(item_name) * total_count
            return total

        # shop_item_dictionary.get('A')
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

            a_total_cost = (200 * a_total_discount_five_grouping_count) + (130 * a_total_discount_three_grouping_count) \
                           + (shop_item_dictionary.get('A') * a_count)  # total the cost
        else:
            a_total_cost = 0

        # Total Up cost of occurrences of Item E which has implications on b_count - every two E items gives a free B item

        if e_count > 0:
            if e_count//2 > 0:  # some will be at discount cost
                b_count = b_count - e_count//2
            e_total_cost = shop_item_dictionary.get('E') * e_count  # all at normal cost as less than 2 items
        else:
            e_total_cost = 0

        # Total Up cost of occurrences of Item B

        if b_count > 0:
            if b_count//2 > 0:  # some will be at discount cost
                b_total_discount_grouping_cost = b_count//2
                b_single_normal_cost = b_count % 2
                b_total_cost = (45 * b_total_discount_grouping_cost) + (shop_item_dictionary.get('B') * b_single_normal_cost)
            else:
                b_total_cost = shop_item_dictionary.get('B') * b_count  # all at normal cost as less than 2 items
        else:
            b_total_cost = 0

        # Total Up cost of occurrences of Item C

        if c_count > 0:
            c_total_cost = c_count * shop_item_dictionary.get('C')
        else:
            c_total_cost = 0

        # Total Up cost of occurrences of Item D

        if d_count > 0:
            d_total_cost = d_count * shop_item_dictionary.get('D')
        else:
            d_total_cost = 0

        # Total Up cost of occurrences of Item F

        if f_count > 0:
            f_total_cost = items_one_free_cost(3, f_count, 'F')
        else:
            f_total_cost = 0

        # Total Up cost of occurrences of Item G

        if g_count > 0:
            g_total_cost = g_count * shop_item_dictionary.get('G')
        else:
            g_total_cost = 0

        # Total Up cost of occurrences of Item H

        if h_count > 0:
            h_total_discount_ten_grouping_count = 0
            h_total_discount_five_grouping_count = 0
            if h_count//10 > 0:
                h_total_discount_ten_grouping_count = h_count//10
                h_count = h_count % 10  # h_count will be the remaining amount

            if h_count//5 > 0:  # some will be at discount cost
                h_total_discount_five_grouping_count = h_count//5
                h_count = h_count % 5  # These are charged at normal amount

            h_total_cost = (80 * h_total_discount_ten_grouping_count) + (45 * h_total_discount_five_grouping_count) \
                           + (shop_item_dictionary.get('H') * h_count)  # total the cost
        else:
            h_total_cost = 0

        # Total Up cost of occurrences of Item I

        if i_count > 0:
            i_total_cost = i_count * shop_item_dictionary.get('I')
        else:
            i_total_cost = 0

        # Total Up cost of occurrences of Item J

        if j_count > 0:
            j_total_cost = j_count * shop_item_dictionary.get('J')
        else:
            j_total_cost = 0

        # Total Up cost of occurrences of Item K

        if k_count > 0:
            if k_count//2 > 0:  # some will be at discount cost
                k_total_discount_grouping_cost = k_count//2
                k_single_normal_cost = k_count % 2
                k_total_cost = (150 * k_total_discount_grouping_cost) + (shop_item_dictionary.get('K') * k_single_normal_cost)
            else:
                k_total_cost = shop_item_dictionary.get('K') * k_count  # all at normal cost as less than 2 items
        else:
            k_total_cost = 0

        # Total Up cost of occurrences of Item L

        if l_count > 0:
            l_total_cost = l_count * shop_item_dictionary.get('L')
        else:
            l_total_cost = 0

        # Total Up cost of occurrences of Item N

        if n_count > 0:
            if n_count//3 > 0:  # some will be at discount cost
                m_count = m_count - n_count//3  # reduce m_count as per the offer 3N get one M free
            n_total_cost = shop_item_dictionary.get('N') * n_count  # all at normal cost as less than 2 items
        else:
            n_total_cost = 0

        # Total Up cost of occurrences of Item M

        if m_count > 0:
            m_total_cost = m_count * shop_item_dictionary.get('M')
        else:
            m_total_cost = 0

        # Total Up cost of occurrences of Item O

        if o_count > 0:
            o_total_cost = o_count * shop_item_dictionary.get('O')
        else:
            o_total_cost = 0

        # Total Up cost of occurrences of Item P

        if p_count > 0:
            if p_count//5 > 0:  # some will be at discount cost
                p_total_discount_grouping_cost = p_count//5
                p_single_normal_cost = p_count % 5
                p_total_cost = (200 * p_total_discount_grouping_cost) + (shop_item_dictionary.get('P') * p_single_normal_cost)
            else:
                p_total_cost = shop_item_dictionary.get('P') * p_count  # all at normal cost as less than 2 items
        else:
            p_total_cost = 0

        # Total Up cost of occurrences of Item R

        if r_count > 0:
            if r_count // 3 > 0:  # some will be at discount cost
                q_count = q_count - r_count // 3  # reduce q_count as per the offer 3R get one Q free
            r_total_cost = shop_item_dictionary.get('R') * r_count  # all at normal cost as less than 2 items
        else:
            r_total_cost = 0

        # Total Up cost of occurrences of Item Q

        if q_count > 0:
            if q_count//3 > 0:  # some will be at discount cost
                q_total_discount_grouping_cost = q_count//3
                q_single_normal_cost = q_count % 3
                q_total_cost = (80 * q_total_discount_grouping_cost) + (shop_item_dictionary.get('Q') * q_single_normal_cost)
            else:
                q_total_cost = shop_item_dictionary.get('Q') * q_count  # all at normal cost as less than 2 items
        else:
            q_total_cost = 0



        # Total Up cost of occurrences of Item U

        if u_count > 0:
            u_total_cost = items_one_free_cost(4, u_count, 'U')
        else:
            u_total_cost = 0

        # Total Up cost of occurrences of Item V

        if v_count > 0:
            v_total_discount_three_grouping_count = 0
            v_total_discount_two_grouping_count = 0
            if v_count//3 > 0:
                v_total_discount_three_grouping_count = v_count//3
                v_count = v_count % 3  # v_count will be the remaining amount

            if v_count//2 > 0:  # some will be at discount cost
                v_total_discount_two_grouping_count = v_count//2
                v_count = v_count % 2  # These are charged at normal amount

            v_total_cost = (130 * v_total_discount_three_grouping_count) + (90 * v_total_discount_two_grouping_count) \
                           + (shop_item_dictionary.get('V') * v_count)  # total the cost
        else:
            v_total_cost = 0

        # Total Up number of S,T,X,Y,Z

        s_t_x_y_z_list = [s_count, t_count, x_count, y_count, z_count]
        sum_of_s_t_x_y_z = sum(s_t_x_y_z_list)
        s_t_x_y_z_discount_cost = 0

        if sum_of_s_t_x_y_z // 3 > 0:
            s_t_x_y_z_discount_cost = (sum_of_s_t_x_y_z // 3) * 45
            s_t_x_y_z_remaining = sum_of_s_t_x_y_z % 3
            while z_count > 0 and s_t_x_y_z_remaining > 0:   # order in favor of customer as to leave cheapest item at full price
                z_count = z_count - 1
                s_t_x_y_z_remaining = s_t_x_y_z_remaining - 1
            while s_count > 0 and s_t_x_y_z_remaining > 0:
                s_count = s_count - 1
                s_t_x_y_z_remaining = s_t_x_y_z_remaining - 1
            while t_count > 0 and s_t_x_y_z_remaining > 0:
                t_count = t_count - 1
                s_t_x_y_z_remaining = s_t_x_y_z_remaining - 1
            while y_count > 0 and s_t_x_y_z_remaining > 0:
                y_count = y_count - 1
                s_t_x_y_z_remaining = s_t_x_y_z_remaining - 1
            while x_count > 0 and s_t_x_y_z_remaining > 0:
                x_count = x_count - 1
                s_t_x_y_z_remaining = s_t_x_y_z_remaining - 1

        # Total Up cost of occurrences of Item S

        if s_count > 0:
            s_total_cost = s_count * shop_item_dictionary.get('S')
        else:
            s_total_cost = 0

        # Total Up cost of occurrences of Item T

        if t_count > 0:
            t_total_cost = t_count * shop_item_dictionary.get('T')
        else:
            t_total_cost = 0

        # Total Up cost of occurrences of Item W

        if w_count > 0:
            w_total_cost = w_count * shop_item_dictionary.get('W')
        else:
            w_total_cost = 0

        # Total Up cost of occurrences of Item X

        if x_count > 0:
            x_total_cost = x_count * shop_item_dictionary.get('X')
        else:
            x_total_cost = 0

        # Total Up cost of occurrences of Item Y

        if y_count > 0:
            y_total_cost = y_count * shop_item_dictionary.get('Y')
        else:
            y_total_cost = 0

        # Total Up cost of occurrences of Item Z

        if z_count > 0:
            z_total_cost = z_count * shop_item_dictionary.get('Z')
        else:
            z_total_cost = 0

        total_cost = a_total_cost + b_total_cost + c_total_cost + d_total_cost + e_total_cost + f_total_cost \
                     + g_total_cost + h_total_cost + i_total_cost + j_total_cost + k_total_cost + l_total_cost \
                     + m_total_cost + n_total_cost + o_total_cost + p_total_cost + q_total_cost + r_total_cost \
                     + s_total_cost + t_total_cost + u_total_cost + v_total_cost + w_total_cost + x_total_cost \
                     + y_total_cost + z_total_cost + s_t_x_y_z_discount_cost  # sum costs for all items

        return total_cost


    #raise NotImplementedError()

