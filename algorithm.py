def summary(arr, i1, i2):
        if arr == None or i1 == None or i2 == None:
            return 0
        if i1 > i2:
            return 0
        if len(arr) == 0 or len(arr) == 1:
            return 0
        if i1 < 0 or i2 < 0 or i1 >= len(arr) or i2 >= len(arr):
            return 0
        totalsum = 0
        for i, val in enumerate(arr):
            if i < i1:
                continue
            if i > i2:
                break
            totalsum += val;
        return totalsum

