def merge(left, right):
    temp = []
    pointer_r = pointer_l = 0
    while pointer_l < len(left) and pointer_r < len(right):
        if left[pointer_l] < right[pointer_r]:
            temp.append(left[pointer_l])
            pointer_l += 1
        else:
            temp.append(right[pointer_r])
            pointer_r += 1
    return temp.extend(right[pointer_r:] if pointer_l == len(left) else left[pointer_l:])


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)/2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print merge_sort(a)
