def qsort(l):

  # Basisfälle: Leere oder einelementige Listen sind sortiert.
  if (len(l) <= 1):
    return l
  
  pivot, *tail = l

  links = [el for el in tail if el < pivot]
  rechts = [el for el in tail if el >= pivot]

  return qsort(links) + [pivot] + qsort(rechts)


l1 = [10, 25, 3, 50, 15, 5, 1, 77, 95, -2, 75]
print(qsort(l1))