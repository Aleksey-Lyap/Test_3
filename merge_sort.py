def merge_sort(arr, p, r):
    """Функция выполняет сортировку слиянием."""
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = arr[p:p + n1]
    R = arr[q + 1:q + 1 + n2]

    i, j, k = 0, 0, p

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

A = [5, 2, 4, 6, 1, 3, 2, 6]

merge_sort(A, 0, len(A) - 1)
print(A)
