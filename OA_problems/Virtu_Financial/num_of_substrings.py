# Python3 implementation of the above approach

# Function to return the number of
# substrings of same characters
def findNumbers(s):
    # Size of the string
    n = len(s)

    # Initialize count to 1
    count = 1
    result = 0

    # Initialize left to 0 and right to 1
    # to traverse the string
    left = 0
    right = 1

    while right < n:

        # Checking if consecutive
        # characters are same and
        # increment the count
        if s[left] == s[right]:
            count += 1

        # When we encounter a
        # different characters
        else:

            # Increment the result
            result += count * (count + 1) // 2

            # To repeat the whole
            # process set left equals
            # right and count variable to 1
            left = right
            count = 1

        right += 1

    # Store the final value of result
    result += count * (count + 1) // 2

    print(result)


# Driver code
s = "bbbcbb"

findNumbers(s)

# This code is contributed by Mohit Kumar
