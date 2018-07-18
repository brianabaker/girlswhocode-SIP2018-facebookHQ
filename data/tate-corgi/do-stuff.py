import tate

# total pieces of art: 3332
list_of_art = tate.get_artwork()

female_metal_art = []
art_1950_1955 = []

# how many women work with metal artwork?
# how many pieces were created in the early 50's?

for ele in list_of_art:
    word = "metal"
    dates = [1950, 1951, 1952, 1953, 1954, 1955]
    if (word in ele["data"]["medium"].lower()) and (ele["artist"]["gender"] == "Female"):
        female_metal_art.append(ele)
    if (ele["metadata"]["creation year"]) in dates:
        art_1950_1955.append(ele)

# number of women artists over time
# i'd have to find min year and max year

print("")
print("Number of women making metal art:", len(female_metal_art))
print("")
print("Number of pieces made between 1950 and 1955:", len(art_1950_1955))

# women making metal art in the 1950s
