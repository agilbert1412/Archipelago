from BaseClasses import Location


class APGOLocation(Location):
    game = "Archipela-Go!"


# [Centimeters in a marathon] * [Centimeters in a half-marathon]
offset = 8902301100000

location_table = {
    "Goal": offset,
}

max_per_category = 1000
for i in range(1, max_per_category+1):
    location_table[f"Short {i}"] = offset + i
    location_table[f"Medium {i}"] = offset + i + max_per_category
    location_table[f"Long {i}"] = offset + i + (max_per_category * 2)
    location_table[f"Fast {i}"] = offset + i + (max_per_category * 3)