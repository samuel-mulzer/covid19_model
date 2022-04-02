import numpy as np
import matplotlib.pyplot as plt
from covid19_model.models import sir_vs
from covid19_model.solver import solve
from covid19_model.visualizer import visualize


def simulate(model, x0, n, t, d, h, args, labels, save=False):
    model = sir_vs
    x0 = np.array(x0, dtype=float)
    tspan = np.arange(t, t+d, h)
    
    solution = solve(model, x0, tspan, h, args)
    save_loc = visualize(solution.copy(), n, tspan, args, labels, save)

    i_max = solution[1].max()
    print(f"i_max: {i_max:.2g} | {i_max*n:.2g}")

    if save:
        print(f"saved to {save_loc}")
    plt.show()