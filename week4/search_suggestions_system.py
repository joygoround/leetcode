# https://leetcode.com/problems/search-suggestions-system/


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        result = []
        for i in range(1, len(searchWord)+1):
            to_search = searchWord[:i]
            three_products = []
            for product in sorted(products):
                if product.startswith(to_search):
                    three_products.append(product)
                if len(three_products) == 3:
                    break
            result.append(three_products)
        return result


# could not solve with trie :/
