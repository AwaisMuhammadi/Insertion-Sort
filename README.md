# Insertion Sort

Selection sort is simple in-place sorting algorithm. Take a list of numbers as input and sort them.

# Working

Maintain two subarrays in given array: 
    <ol><li>Subarray which is already sorted</li>
    <li>Remaining subarray which is unsorted</li></ol>

    <ol><li>Iterate from arr[1] to arr[n] over the array. </li>
    <li>Compare the current element with its predecessor</li>
    <li>If the key is smaller than its predecessor, compare it to the element before. Move the current element to its sorted position and move all the greater elements to one place ahead</li></ol>
    
# Complexcity

Complexcity of Insertion sort algorithm is O(n^2).
