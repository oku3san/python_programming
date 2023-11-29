ranking = {
    'A': 100,
    'B': 85,
    'C': 92
}

for key in ranking:
    print(key)

print(sorted(ranking))
print(sorted(ranking, key=ranking.get))
print(ranking.get('A'))
print(sorted(ranking, key=ranking.get, reverse=True))
