ax.annotate(f'({i}, {j})',  # Text to display
                xy=(i, j),  # Point to annotate
                xytext=(i, j + 0.5),  # Position of the text
                textcoords='offset points',  # Coordinate system for text position
                ha='center',  # Horizontal alignment
                color='red',  # Set color to red
                fontsize=12,  # Set font size to 12
                arrowprops=dict(facecolor='black', shrink=0.05))