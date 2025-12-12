import re
from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        paragraph = re.sub(r"[!?',;.]", " ", paragraph)
        words = paragraph.split()
        banned_set = set(banned)
        valid_words = [word for word in words if word not in banned_set]
        return Counter(valid_words).most_common(1)[0][0]