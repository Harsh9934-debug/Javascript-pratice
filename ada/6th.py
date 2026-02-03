def merge_sort(a):
    if len(a) < 2: return a
    m = len(a) // 2
    l, r, i, j, res = merge_sort(a[:m]), merge_sort(a[m:]), 0, 0, []
    while i < len(l) and j < len(r):
        if l[i] < r[j]: res.append(l[i]); i += 1
        else: res.append(r[j]); j += 1
    return res + l[i:] + r[j:]

print("Sorted:", *merge_sort(list(map(int, input("Enter numbers space-separated: ").split()))))