class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        list[list]
        for l in range(len(score)):
            for i in range(len(score)-1):
                if score[i][k]<score[i+1][k]:
                    score[i], score[i + 1] = score[i + 1], score[i]
        return score