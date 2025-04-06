import csv

# File paths
txt_file = "joyride.txt"
data_file = "comrades.txt"
output_csv = "output_joyride.csv"

# Step 1: Load comrade numbers from the txt file
with open(txt_file, "r", encoding="utf-8") as f:
    comrades_to_find = {line.strip()[1:].zfill(5) for line in f if line.startswith("#")}

# Optional: print for debug
print("Loaded Comrade Numbers:", sorted(comrades_to_find))

# Step 2: Read the data lines and match
rows = []
with open(data_file, "r", encoding="utf-8") as f:
    for line in f:
        if "Comrade" in line and "Rarest trait" in line:
            parts = line.strip().split(" | ")
            if len(parts) < 2:
                continue

            rank_part = parts[0]
            trait_part = parts[1]

            try:
                rank_num = rank_part.split(" - ")[0].replace("Rank ", "").zfill(5)
                comrade_num = rank_part.split("Comrade #")[1].zfill(5)
                trait = trait_part.split("= ")[1].strip()

                # Debug: check matching
                if comrade_num in comrades_to_find:
                    print(f"✅ Match found: Comrade #{comrade_num}")
                    rows.append({
                        "Rank": rank_num,
                        "Comrade": comrade_num,
                        "Rarest trait": trait
                    })
            except Exception as e:
                print("⚠️ Error parsing line:", line)
                print("   ", e)

# Step 3: Write to CSV
with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Rank", "Comrade", "Rarest trait"])
    writer.writeheader()
    writer.writerows(rows)

print(f"✅ Done! CSV written to {output_csv}")
