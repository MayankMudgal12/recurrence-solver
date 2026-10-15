
import os
import matplotlib.pyplot as plt

def main():
    try:
        a, b, p, n = map(float, input("Enter a, b, p, n: ").split())
    except ValueError:
        print("Enter four valid numbers.")
        return

    if a <= 0 or b <= 1 or n < 1 or p < 0:
        print("Invalid input values.")
        return

    levels = []
    total = 0
    i = 0

    while i < 1000 and n / (b ** i) >= 1:
        nodes = a ** i
        size = n / (b ** i)
        cost = size ** p
        level_cost = nodes * cost

        levels.append((i, nodes, size, cost, level_cost))
        total += level_cost
        i += 1

    print("\nLevel\tNodes\tSize\tCost/Node\tLevel Cost")

    for level, nodes, size, cost, level_cost in levels:
        print(f"{level}\t{nodes:.2f}\t{size:.2f}\t{cost:.2f}\t\t{level_cost:.2f}")

    print(f"\nTotal cost = {total:.2f}")

    folder = "recursion_levels"
    os.makedirs(folder, exist_ok=True)

    level_numbers = [item[0] for item in levels]
    costs = [item[4] for item in levels]
    max_cost = max(costs) if costs else 1

    for current in range(len(levels)):
        fig, ax = plt.subplots(figsize=(10, 6))

        shown_levels = level_numbers[:current + 1]
        shown_costs = costs[:current + 1]

        bars = ax.bar(shown_levels, shown_costs)

        ax.set_title(f"Recursion Tree Costs - Up to Level {current}")
        ax.set_xlabel("Recursion Level")
        ax.set_ylabel("Level Cost")
        ax.set_xticks(level_numbers)
        ax.set_xlim(-0.5, max(len(levels) - 0.5, 0.5))
        ax.set_ylim(0, max_cost * 1.2 if max_cost > 0 else 1)

        for bar, cost in zip(bars, shown_costs):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height(),
                f"{cost:.2f}",
                ha="center",
                va="bottom"
            )

        fig.tight_layout()
        filename = os.path.join(folder, f"level_{current}.png")
        fig.savefig(filename, dpi=300, bbox_inches="tight")
        plt.close(fig)

        print(f"Saved: {filename}")

    print(f"\nAll {len(levels)} images saved in '{folder}'.")

if __name__ == "__main__":
    main()
