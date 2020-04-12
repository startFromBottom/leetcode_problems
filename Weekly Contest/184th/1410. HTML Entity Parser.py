"""

problem link : https://leetcode.com/problems/html-entity-parser/
submission detail : https://leetcode.com/problems/html-entity-parser/submissions

"""


class Solution:
    """
    Time Complexity : O(n)
    where n : the number of Entity
    """
    def entityParser(self, text: str) -> str:
        html_dict = {
            "&quot;": "\"",
            "&apos;": "\'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/",
        }
        for key, val in html_dict.items():
            text = text.replace(key, val)
        return text

