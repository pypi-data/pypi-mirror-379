import matplotlib.pyplot    as     plt
import plotly.graph_objects as     go

def append_plots(plot_list, labels=None, line_styles=None, colors=None, 
                 swap_axes=False, show=True, grid=False,
                 xlim=None, ylim=None, title=None, xlabel=None, ylabel=None):
    """
    Combines multiple individual matplotlib Axes or plotly Figures into a single figure.
    
    Parameters same as before.
    
    Returns:
    - matplotlib Axes object OR plotly Figure object depending on input.
    """

    if not plot_list:
        raise ValueError("plot_list cannot be empty")

    first_plot = plot_list[0]

    # Check if matplotlib plot (Axes)
    if hasattr(first_plot, 'lines'):
        fig, ax = plt.subplots()
        for i, plot_ax in enumerate(plot_list):
            first_line = True
            for line in plot_ax.lines:
                x, y = line.get_data()

                linestyle = line.get_linestyle()
                if line_styles and i < len(line_styles):
                    linestyle = line_styles[i]

                color = line.get_color()
                if colors and i < len(colors):
                    color = colors[i]

                if swap_axes:
                    ax.plot(y, x, color=color, linestyle=linestyle,
                            label=labels[i] if first_line and labels and i < len(labels) else None)
                else:
                    ax.plot(x, y, color=color, linestyle=linestyle,
                            label=labels[i] if first_line and labels and i < len(labels) else None)

                first_line = False

        if xlim:
            ax.set_xlim(xlim)
        if ylim:
            ax.set_ylim(ylim)
        if title:
            ax.set_title(title)
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)
        if grid:
            ax.grid()
        if labels:
            ax.legend()
        if show:
            plt.show()
        else:
            plt.close()

        return ax

    # Check if plotly figure
    elif hasattr(first_plot, 'data'):
        combined_fig = go.Figure()
        for i, fig in enumerate(plot_list):
            for trace in fig.data:
                # Clone the trace to avoid mutating original
                new_trace = trace

                # Apply colors if provided and trace supports it
                if colors and i < len(colors):
                    if hasattr(new_trace, 'line'):
                        new_trace.line.color = colors[i]
                    elif hasattr(new_trace, 'marker'):
                        new_trace.marker.color = colors[i]

                # Apply line styles if provided and trace supports it (only for scatter lines)
                if line_styles and i < len(line_styles):
                    if isinstance(new_trace, go.Scatter) and hasattr(new_trace, 'line'):
                        new_trace.line.dash = line_styles[i]

                # Apply labels if available and applicable
                if labels and i < len(labels):
                    new_trace.name = labels[i]

                combined_fig.add_trace(new_trace)

        if title:
            combined_fig.update_layout(title=title)
        if xlabel or ylabel:
            combined_fig.update_layout(xaxis_title=xlabel if xlabel else None,
                                      yaxis_title=ylabel if ylabel else None)
        if xlim:
            combined_fig.update_xaxes(range=xlim)
        if ylim:
            combined_fig.update_yaxes(range=ylim)
        if grid:
            combined_fig.update_layout(xaxis_showgrid=True, yaxis_showgrid=True)

        if show:
            combined_fig.show()

        return combined_fig

    else:
        raise TypeError("Unknown plot object type passed to append_plots.")