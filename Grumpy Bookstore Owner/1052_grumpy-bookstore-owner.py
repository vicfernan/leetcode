class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        total_cients_satisfied = 0
        index_use_sec = 0
        size = 0
        max_size = 0
        i = 0
        x = 0
        max_min = 0

        for customer in customers:
            x = i
            if (minutes + x > len(customers)):
                max_min = len(customers)
            else: 
                max_min = minutes + x
            while x < max_min:
                if (grumpy[x]):
                    size += customers[x]
                x += 1
            if (size >= max_size):
                max_size = size
                index_use_sec = i
            size = 0
            i += 1

        i = 0
        print(index_use_sec)
        for custom in customers:
            if i >= index_use_sec and i < index_use_sec + minutes:
                total_cients_satisfied += custom
            else:
                if (not grumpy[i]):
                    total_cients_satisfied += custom
            i += 1

        return total_cients_satisfied