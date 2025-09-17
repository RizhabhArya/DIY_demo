import random
import csv

# Define categories and their materials/tools
categories = {
    "Organizer & Storage": {
        "core_materials": ["Cardboard Box", "Shoebox", "Plastic Container"],
        "supporting_materials": ["Bubble Wrap", "Newspaper", "Soda Tabs"],
        "tools": ["Scissors", "Glue Gun", "Tape", "Marker"]
    },
    "Lighting & Lantern": {
        "core_materials": ["Glass Jar", "Candle Jar", "Wire Piece"],
        "supporting_materials": ["Rope Piece", "Beads", "Ribbon Scrap", "Glitter"],
        "tools": ["Drill", "Pliers", "Tape", "Glue Gun", "Paintbrush"]
    },
    "Wearable & Accessories": {
        "core_materials": ["Cloth Scrap", "Old Button", "Ribbon Scrap"],
        "supporting_materials": ["Thread", "Safety Pin", "Sequins"],
        "tools": ["Needle", "Thread", "Scissors", "Sewing Machine"]
    },
    "Art/Decor & Sculpture": {
        "core_materials": ["CD", "Puzzle Piece", "Wooden Frame Scrap"],
        "supporting_materials": ["Glitter", "Stickers", "Popsicle Stick"],
        "tools": ["Glue Gun", "Paintbrush", "Scissors"]
    },
    "Toys & Play": {
        "core_materials": ["Lego Piece", "Plastic Bottle", "Old Battery"],
        "supporting_materials": ["String Piece", "Bottle Cap", "Small Bell"],
        "tools": ["Scissors", "Glue Gun", "Tape", "Marker"]
    },
    "Upcycled Furniture/Utility": {
        "core_materials": ["Wooden Frame Scrap", "Drawer Handle", "Rope Piece"],
        "supporting_materials": ["Twine", "Curtain Ring", "Carpet Scrap"],
        "tools": ["Screwdriver", "Drill", "Hammer", "Measuring Tape"]
    }
}

# Adjectives and product types
adjectives = ["Eco", "Upcycled", "DIY", "Creative", "Handmade"]
product_types = ["Lantern", "Planter", "Organizer", "Coaster", "Sculpture", "Bracelet", "Pouch", "Frame", "Wall Art"]

# Instruction pools
prep_pool = ["Clean and prepare all waste materials.", "Wash items thoroughly.", "Ensure materials are dry."]
cut_shape_pool = ["Cut bottles into halves.", "Trim cardboard edges.", "Shape fabric pieces as needed."]
assemble_pool = ["Glue or tape pieces together.", "Secure parts with string or screws.", "Attach components carefully."]
decorate_pool = ["Paint or decorate as desired.", "Add stickers, glitter, or fabric patches."]
finish_pool = ["Let dry completely.", "Place in the chosen location.", "Test functionality if applicable."]

def generate_instruction_steps():
    steps = []
    steps.append(random.choice(prep_pool))
    if random.random() > 0.5:
        steps.append(random.choice(cut_shape_pool))
    steps.append(random.choice(assemble_pool))
    if random.random() > 0.3:
        steps.append(random.choice(decorate_pool))
    steps.append(random.choice(finish_pool))
    return " | ".join(steps)

def generate_dataset(num_rows=100000, output_file="diy_waste_projects.csv"):
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Project", "Waste Items", "Tools", "Instructions"])
        writer.writeheader()

        for _ in range(num_rows):
            category = random.choice(list(categories.keys()))
            cat_data = categories[category]
            
            core_materials = random.sample(cat_data["core_materials"], k=random.randint(1, len(cat_data["core_materials"])))
            supporting_materials = random.sample(cat_data["supporting_materials"], k=random.randint(0, len(cat_data["supporting_materials"])))
            waste_items_pool = core_materials + supporting_materials

            # Ensure at least 2 items
            if len(waste_items_pool) <= 2:
                waste_items = waste_items_pool
            else:
                waste_items_count = random.randint(2, min(20, len(waste_items_pool)))
                waste_items = random.sample(waste_items_pool, k=waste_items_count)
            
            tools = random.sample(cat_data["tools"], k=random.randint(1, min(5, len(cat_data["tools"]))))
            
            project_name = f"{random.choice(adjectives)} {random.choice(product_types)}"
            instructions = generate_instruction_steps()
            
            row = {
                "Project": project_name,
                "Waste Items": ", ".join(waste_items),
                "Tools": ", ".join(tools),
                "Instructions": instructions
            }
            writer.writerow(row)

    print(f"Dataset generation complete: {output_file}")

# Run generator
if __name__ == "__main__":
    generate_dataset(num_rows=100000, output_file="diy_waste_projects.csv")
