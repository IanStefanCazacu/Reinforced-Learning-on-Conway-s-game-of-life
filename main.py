import torch
import time
import argparse
from environment import Environment

def main(width, height, live_cell_prob, generations, no_interface):
    env = Environment(width, height, live_cell_prob)

    if not no_interface:
        print("Initial grid:")
        env.print_grid()
        time.sleep(0.5)

    for gen in range(1, generations + 1):
        x = torch.randint(-2, env.get_grid().shape[1] + 2, (1,)).item()
        y = torch.randint(-2, env.get_grid().shape[0] + 2, (1,)).item()
        env.change_cell_state(x, y)
        env.next_generation()

        live_cells = env.get_grid().sum().item()

        if no_interface:
            print(f"Generation {gen}: {live_cells} live cells, grid size: {env.get_grid().shape}")
        else:
            print(f"Generation {gen}: grid size: {env.get_grid().shape}")
            env.print_grid()
            time.sleep(0.05)

        if live_cells == 0:
            print(f"All cells are dead. Simulation stopped at generation {gen}.")
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run GPU-enabled Infinite Conway's Game of Life in Console")
    parser.add_argument("--width", type=int, default=10)
    parser.add_argument("--height", type=int, default=10)
    parser.add_argument("--live_cell_prob", type=float, default=0.3)
    parser.add_argument("--generations", type=int, default=50)
    parser.add_argument("--no_interface", action="store_true", help="Disable printing and show only stats")

    args = parser.parse_args()
    main(args.width, args.height, args.live_cell_prob, args.generations, args.no_interface)




    
    #command example: python main.py --width 10 --height 10 --live_cell_prob 0.3 --generations 2000 --no_interface
    #another example: python main.py --width 3 --height 3 --live_cell_prob 0.3 --generations 200 
    #another example: python main.py --width 100 --height 100 --live_cell_prob 0.2 --generations 20000 --no_interface
    #optimal for testing: python main.py --width 250 --height 250 --live_cell_prob 0.3 --generations 20000 --no_interface