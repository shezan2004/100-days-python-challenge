class Solution(object):
    def findNthDigit(self, n):
        digit_length = 1
        count = 9
        start = 1

        # Find the digit-length block where n belongs
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10

        # Find the actual number that contains the nth digit
        number = start + (n - 1) // digit_length

        # Find the digit inside that number
        digit_index = (n - 1) % digit_length
        return int(str(number)[digit_index])
