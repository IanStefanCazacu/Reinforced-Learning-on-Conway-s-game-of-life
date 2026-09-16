# PyTorch Game of Life

A PyTorch-accelerated implementation of Conway's Game of Life featuring dynamic grid auto-expansion and auto-cropping.

## Overview

This project implements Conway's Game of Life with grid expansion capabilities that automatically resize the grid bounds when live cells reach the edge. It features both a pure Python set-based implementation and a GPU/CPU accelerated PyTorch implementation using 2D convolutions.

## Features

- PyTorch convolution-based step updates (`F.conv2d`).
- Automatic grid expansion when active cells touch the border.
- Automatic edge cropping to eliminate empty surrounding rows and columns.
- Command-line interface with customizable grid parameters.
- Option to toggle visual console output or run in stats-only mode for benchmarking.

## Project Structure

- `environment.py`: Defines the PyTorch `Environment` class, grid operations, dynamic padding, and convolution logic.
- `main.py`: Main entry point for running PyTorch simulations with command-line arguments.
- `game_of_life_v1.py`: Set and Counter based standard Python implementation of Conway's Game of Life.
- `reinforced_learning_agents.py`: Place-holder for future reinforcement learning agent implementations.

## Installation

Ensure you have PyTorch installed:

```bash
pip install torch
