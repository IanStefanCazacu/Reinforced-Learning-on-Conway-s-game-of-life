import torch
import torch.nn.functional as F

class Environment:
    def __init__(self, width=10, height=10, live_cell_prob=0.3, device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.grid = (torch.rand((height, width), device=self.device) < live_cell_prob).to(torch.int8)
        self.kernel = torch.tensor([[1, 1, 1],
                                    [1, 0, 1],
                                    [1, 1, 1]], dtype=torch.float32, device=self.device).unsqueeze(0).unsqueeze(0)

    def print_grid(self):
        cpu_grid = self.grid.cpu().numpy()
        for row in cpu_grid:
            print(" ".join("O" if cell else "." for cell in row))
        print()

    def _expand_if_needed(self):
        top = self.grid[0, :].any()
        bottom = self.grid[-1, :].any()
        left = self.grid[:, 0].any()
        right = self.grid[:, -1].any()
        pad = (1 if left else 0, 1 if right else 0, 1 if top else 0, 1 if bottom else 0)
        if any(pad):
            self.grid = F.pad(self.grid, pad, value=0)

    def _crop_if_empty_edges(self):
        rows = torch.any(self.grid, dim=1)
        cols = torch.any(self.grid, dim=0)
        self.grid = self.grid[rows][:, cols]

    def next_generation(self):
        self._expand_if_needed()
        g = self.grid.float().unsqueeze(0).unsqueeze(0)
        n = F.conv2d(g, self.kernel, padding=1).squeeze()
        self.grid = ((n == 3) | ((self.grid == 1) & (n == 2))).to(torch.int8)
        self._crop_if_empty_edges()
        return self.grid

    def change_cell_state(self, x, y):
        while y < 0:
            self.grid = F.pad(self.grid, (0, 0, 1, 0), value=0)
            y += 1
        while y >= self.grid.shape[0]:
            self.grid = F.pad(self.grid, (0, 0, 0, 1), value=0)
        while x < 0:
            self.grid = F.pad(self.grid, (1, 0, 0, 0), value=0)
            x += 1
        while x >= self.grid.shape[1]:
            self.grid = F.pad(self.grid, (0, 1, 0, 0), value=0)
        self.grid[y, x] = 1 - self.grid[y, x]


    def get_grid(self):
        return self.grid
