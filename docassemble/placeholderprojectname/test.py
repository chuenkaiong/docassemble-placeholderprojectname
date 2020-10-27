output = []
with open("iso3166_alpha2_codes.csv") as f:
    for line in f:
        output.append(line[0:2])

print(output)