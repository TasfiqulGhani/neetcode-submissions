class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            map = {}
            for c in s:
                map[c] = 1 + map.get(c, 0) 
            key = tuple(sorted(map.items()))
            print(key)
            group[key] = group.get(key,[])
            group[key].append(s)
        return list(group.values())
