
class Medium:

    # description: paste the description here
    # enter parameters: paste the enter parameters examples here
    # return: paste the return expected here
    def nameOfFunction(self, value1, value2):
        # script here
        return None

    # description: Create a function to return sorted array using merge sort
    # enter parameter: array = [4, 8, 6, 9, 0, -1, -20, 9, 3, 44, 6]
    # return: [-20, -1, 0, 3, 4, 6, 6, 8, 9, 9, 44]
    def mergeSort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]

        # Recursive call on each half
            self.mergeSort(left)
            self.mergeSort(right)

        # Two iterators for traversing the two halves
            i = 0
            j = 0
        
        # Iterator for the main list
            k = 0
        
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
              # The value from the left half has been used
                    array[k] = left[i]
              # Move the iterator forward
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
            # Move to the next slot
                k += 1

        # For all the remaining values
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k]=right[j]
                j += 1
                k += 1
            
            return(array)

    # description: Create a function to return next permutation of given string. i.e, rearrange string into the lexicographically next greater permutation of given string.
    #              If such arrangement is not possible, return its lowest possible order
    # enter parameter: string = "58523"
    # return: "58532"
    def nextPermutation(self, string):
        # paste your script here
        return None

    # description: Create a function that returns weather given string matchs given pattern
    #              in pattern, * represents it can be replaced by zero or more characters and ? represents it can be replaced by exactly one character
    # enter parameter: string = "abbbbcbbc" | pattern = "ab*?b*c"
    # return: true
    def matchPattern(self, string, pattern):
        # paste your script here
        return None