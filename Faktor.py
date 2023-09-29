article_count, desired_impact_factor = map(int, input().split())
print(((desired_impact_factor-1)*article_count) + 1)