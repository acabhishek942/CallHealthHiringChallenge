import math

N, K, n, m, p = [ int(x) for x in input().split(' ')]
"""
p -> expiry limit
m -> capacity of each van on a day
n -> no. of vans
K -> no. of products expiring each day
N -> total no. of products
"""

max_days = (p / K) + 1
per_day_movement_required = math.ceil((N - p) / max_days)
per_day_extra_movement_required = per_day_movement_required - (n * m)
print(int(per_day_extra_movement_required / m))