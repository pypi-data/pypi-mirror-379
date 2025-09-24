import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy import latex

def plot_2d(exprs, var, labels=None, line_styles=None, colors=None,
            title="2D Plot", xlabel="x", ylabel="y",
            xlim=None, ylim=None, resolution=400, show=True):
    """
    Plots 2D curves from symbolic expressions or (x, y) datasets using Matplotlib.
    Automatically detects whether labels and axis titles should be symbolic (LaTeX)
    or plain text.

    Rules:
        - Strings containing '\' are treated as LaTeX symbols.
        - Strings without '\' are treated as plain text.
        - SymPy symbols or expressions are automatically converted to LaTeX.
    """

    def smart_label(lbl):
        """Return string for Matplotlib: LaTeX if symbolic, plain text otherwise"""
        if isinstance(lbl, str):
            if "\\" in lbl:
                return f"${lbl}$"   # LaTeX
            else:
                return lbl           # plain text
        else:
            return f"${latex(lbl)}$"  # SymPy expression → LaTeX

    if not isinstance(exprs, list):
        exprs = [exprs]

    # Determine symbol and range
    if isinstance(var, tuple):
        x_sym = var[0]
        x_range = var[1]
    else:
        x_sym = var
        x_range = (-1, 1)

    x_vals = np.linspace(float(x_range[0]), float(x_range[1]), resolution)

    fig, ax = plt.subplots()

    for i, expr in enumerate(exprs):
        style = line_styles[i] if line_styles and i < len(line_styles) else 'solid'
        color = colors[i] if colors and i < len(colors) else None

        label = smart_label(labels[i]) if labels and i < len(labels) else None

        # If expr is (x_data, y_data)
        if isinstance(expr, (tuple, list)) and len(expr) == 2:
            x_data, y_data = expr
            ax.plot(x_data, y_data, label=label, linestyle=style, color=color)
        else:
            expr = sp.sympify(expr)
            if not expr.has(x_sym):
                y_vals = np.full_like(x_vals, float(expr))
            else:
                f = sp.lambdify(x_sym, expr, modules='numpy')
                y_vals = np.array(f(x_vals)).flatten()
            ax.plot(x_vals, y_vals, label=label, linestyle=style, color=color)

    ax.set_title(smart_label(title))
    ax.set_xlabel(smart_label(xlabel))
    ax.set_ylabel(smart_label(ylabel))

    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)
    if labels:
        ax.legend()
    ax.grid(True)

    if show:
        plt.show()
    else:
        plt.close()

    return ax