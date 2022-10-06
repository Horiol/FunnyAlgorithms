
def stalin_sort(to_be_sorted):
    results = [to_be_sorted[0]] 

    for value in to_be_sorted[1:]:
        if value >= results[-1]:
            results.append(value)

    return results
