class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        pr_1 = 0
        pb_1 = 0
        pg_1 = 0
        for cost in costs:
            pr = min(pb_1, pg_1) + cost[0]
            pb = min(pr_1, pg_1) + cost[1]
            pg = min(pr_1, pb_1) + cost[2]
            pr_1 = pr
            pb_1 = pb
            pg_1 = pg
        return min(pr_1, pb_1, pg_1)