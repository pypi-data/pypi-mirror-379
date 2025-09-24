import matplotlib.pyplot    as     plt
import plotly.graph_objects as     go

def extend_plots(plot_list, dx=0, colors=None, show=True):
    if not plot_list:
        raise ValueError("Plot list cannot be empty")
    
    # Detect if first plot is matplotlib or plotly
    first_plot = plot_list[0]

    # Check for matplotlib plot: look for .lines or .get_lines()
    if hasattr(first_plot, 'lines') or hasattr(first_plot, 'get_lines'):
        # Matplotlib branch
        # Assume plot_list are matplotlib Axes or Figures with lines
        fig, ax = plt.subplots()
        for p in plot_list:
            # Support Axes or Figure input:
            if hasattr(p, 'lines'):
                lines = p.lines
            elif hasattr(p, 'get_lines'):
                lines = p.get_lines()
            else:
                lines = []
            for line in lines:
                x, y = line.get_data()
                ax.plot(x + dx, y, color=colors)
        if show:
            plt.show()
        else:
            plt.close()
        return ax
    
    # Check for Plotly plot: look for .data attribute (list of traces)
    elif hasattr(first_plot, 'data'):
        # Plotly branch
        # Combine traces from all figures into one figure
        combined_fig = go.Figure()
        for fig in plot_list:
            for trace in fig.data:
                # Optionally shift trace x by dx if it has x data
                # This requires modifying trace.x which may be tuple/list/np.array
                if hasattr(trace, 'x') and trace.x is not None:
                    shifted_x = [xi + dx for xi in trace.x] if isinstance(trace.x, (list, tuple)) else trace.x
                    trace = trace.update(x=shifted_x)
                combined_fig.add_trace(trace)
        if show:
            combined_fig.show()
    
        return combined_fig

    else:
        raise TypeError("Unknown plot object type passed to extend_plots.")
