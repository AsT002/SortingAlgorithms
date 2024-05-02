def swap(lst, i, j):
  """
    This method swaps the values of indexes specified in the parameter.
    Args:
      lst -> list
      i -> valid index of list 
      j -> valid index of list

    Returns: None
  """
  lst[i], lst[j] = lst[j], lst[i];

def bubbleSort(lst):
  """
    This method sorts the values of a list through the bubble sort algorithm.
    Args:
      lst -> list

    Returns: the original list or None if parameter is invalid
  """
  if (type(lst) == list):
    for i in range(len(lst) - 1):
      hasSwapped = False;
      for j in range(len(lst) - i - 1):
        if (lst[j] > lst[j + 1]):
          swap(lst, j, j + 1);
          hasSwapped = True;
      if (not hasSwapped):
        return lst;
        
  return None;

def selectionSort(lst):
  """
    This method sorts the values of a list through the selection sort algorithm.
    Args:
      lst -> list

    Returns: the original list or None if parameter is invalid
  """
  if (type(lst) == list):
    for i in range(len(lst)):
      smallest = i;
      for j in range(i + 1, len(lst)):
        if (lst[j] < lst[smallest]):
          smallest = j
      swap(lst, i, smallest);
    return lst;
    
  return None;

def insertionSort(lst):
  """
    This method sorts the values of a list through the insertion sort algorithm.
    Args:
      lst -> list

    Returns: the original list or None if parameter is invalid
  """
  if (type(lst) == list):
    for i in range(1, len(lst)):
      key = lst[i];
      j = i - 1;
      while ( j >= 0 and lst[j] > key):
        lst[j + 1] = lst[j];
        j -= 1;
      lst[j + 1] = key; 
    return lst;

  return None; 
