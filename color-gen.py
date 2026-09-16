import argparse
import random
import json

def generate_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append({"r": r, "g": g, "b": b})
    return colors

def main():
    parser = argparse.ArgumentParser(description="Generate random RGB colors and save to a JSON file.")
    parser.add_argument("-n", "--num-colors", type=int, default=50, help="Number of colors to generate (default: 50)")
    parser.add_argument("-o", "--output", type=str, default="colors.json", help="Path to save the generated colors file (default: colors.json)")
    
    args = parser.parse_args()
    
    colors = generate_colors(args.num_colors)
    
    with open(args.output, "w") as f:
        json.dump(colors, f, indent=4)
        
    print(f"Generated {args.num_colors} colors and saved to {args.output}")

if __name__ == "__main__":
    main()

