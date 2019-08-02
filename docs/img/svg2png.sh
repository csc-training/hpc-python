#!/bin/bash
# convert SVGs to PNGs with a correct size
inkscape communication-patterns.svg -e communication-patterns.png -w 1240
inkscape communication-schematic.svg -e communication-schematic.png -w 443
inkscape communicators.svg -e communicators.png -w 1418
inkscape mpi-bcast.svg -e mpi-bcast.png -w 708
inkscape mpi-data-model.svg -e mpi-data-model.png -w 537
inkscape mpi-gather.svg -e mpi-gather.png -w 708
inkscape mpi-reduce.svg -e mpi-reduce.png -w 708
inkscape mpi-scatter.svg -e mpi-scatter.png -w 708
inkscape ndarray-in-memory.svg -e ndarray-in-memory.png -w 755
inkscape ndarray-in-memory-offset.svg -e ndarray-in-memory-offset.png -w 755
inkscape non-blocking-pattern.svg -e non-blocking-pattern.png -w 708
inkscape processes-threads.svg -e processes-threads.png -w 1594
inkscape vectorised-difference.svg -e vectorised-difference.png -w 454
