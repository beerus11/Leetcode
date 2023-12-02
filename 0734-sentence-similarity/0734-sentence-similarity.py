class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1)!=len(sentence2):
            return False
        hm = defaultdict(set)
        for a,b in similarPairs:
            hm[a].add(b)
            hm[b].add(a)
        for i in range(len(sentence1)):
            if sentence1[i]==sentence2[i] or sentence2[i] in hm[sentence1[i]] :
                continue
            return False
        return True