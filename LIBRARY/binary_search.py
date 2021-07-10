def binary_search(array, item):
   head = 0
   tail = len(array) - 1

   while head <= tail:
       center = (head + tail) // 2
       if array[center] == item:
           return center
       elif array[center] < item:
           head = center + 1
       else:
           tail = center - 1

   return None