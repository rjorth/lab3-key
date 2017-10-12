def quicksort(a):
        less = []
        equal = []
        greater = []

        if len(a) > 1:
            pivot = a[0]
            for x in a:
                if x < pivot:
                    less.append(x)
                if x == pivot:
                    equal.append(x)
                if x > pivot:
                    greater.append(x)
            return quicksort(less) + equal + quicksort(greater)
        else:
            return a
