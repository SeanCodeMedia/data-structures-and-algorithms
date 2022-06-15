
# recursion
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) == len(t):
            if s == "" and t == "":
                return True

            find_index = t.find(s[0])

            if find_index == -1:
                return False

            else:
                if s[0] == t[find_index]:
                    s = s[1:]
                    t = self.remove(t, find_index)
                    return self.isAnagram(s, t)
        else:
            return False

    def remove(self, string, index):
        return string.replace(string[index], "", 1)


class Solution(object):
    def isAnagram(self, s, t):
        """
        O(N) Look at adding count
        :type s: str
        :type t: str
        :rtype: bool
        """
        # O(S+T)
        hash_table_one = {}
        hash_table_two = {}

        if len(s) != len(t):
            return False

        for x in range(len(s)):
            hash_table_one[s[x]] = 1 + hash_table_one.get(s[x], 0)
            hash_table_two[t[x]] = 1 + hash_table_two.get(t[x], 0)

        for x in hash_table_one:
            if hash_table_one[x] != hash_table_two.get(x, 0):
                return False

        return True


def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        p1 = 0
        p2 = 0

        while p1 < len(s):
            if p2 >= len(t):
                return False
            while p2 < len(t):
                if s[p1] == t[p2]:
                    s = s.replace(s[p1], "", 1)
                    t = t.replace(t[p2], "", 1)
                    p2 = 0
                else:
                    p2 += 1
        return True
