class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        countSoldierList = [(sum(row),i) for i,row in enumerate(mat)]
        countSoldierList.sort(key=lambda x: x[0])
        kWeakestRows = []
        for i in range(k):
            kWeakestRows.append(countSoldierList[i][1])
        return kWeakestRows