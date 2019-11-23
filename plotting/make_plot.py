#! /usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

# The simplest of simplest plots.
if True:
    # Here is the simplest call we can make. Things to notice.
    # The axes are black, the line is blue. There are no symbols but
    # a line is drawn connecting the 10 data points. The indeterminate
    # axes is asumed to start at 0 and is the same number of values as
    # deterministic axis. There is a bit of space added to both x and y
    # axis so you can see the ends of the data. It is also making a guess
    # as to how many axis labels to show. Also the size of the plot has
    # a default. Any other things you notice?
    plt.plot(np.arange(100))
    if False:
        plt.plot(np.ones(50))  # What about a second plot of all zeros, but fewer?
    plt.show()


# The simplest of plots.
if False:
    # x axis values
    x = [1, 2, 3]
    # corresponding y axis values
    y = [2, 4, 1]

    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('My first graph!')

    # function to show the plot
    plt.show()

    # What if make a second plot right after making the first?
    if False:
         plt.plot(x, y, linestyle='', marker='*', markersize=10, color='red')
         plt.show()


# Let's get a littl more complicated with plots.
if False:
    # numpy.linspace returns evenly spaced numbers over a specified interval.
    # numpy.linspace(start, stop, num=50, endpoint=True, retstep=False,
    #                dtype=None, axis=0)
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)

    # Transform the data using cosign and exponential functions
    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    # Create the plot figure and set up the space. We are defining two plots
    # with one column and two rows. Set the first plot for all the
    # following calls. Note the use of **kwargs. This means all the rest of
    # the possible keyword arguments that can be passed into the plotting call.
    # You will not see all possible arguments in the function defintion because
    # the the kwargs are passed to sub-routines as well. So you may need to
    # dig a bit to get the argument you need.
    plt.subplot(2, 1, 1)  # subplot(nrows, ncols, index, **kwargs)

    # Plot the data using large plotting symbol and a line connecting
    # the symbols. It will default to use black for axes and blue for
    # line/symbol.
    plt.plot(x1, y1, 'o-')

    # Now we add a title to the plot.
    plt.title('A tale of 2 subplots')

    # And add a y-axis because we are scientists! But no x-lable, yet.
    plt.ylabel('Damped oscillation')

    # Now we switch to the second plot. So all following calls go to
    # second plotting area.
    plt.subplot(2, 1, 2)

    # Make a plot using small symbols and dashed line. Also we choose to
    # use green for plot
    # symbol and line color.
    plt.plot(x2, y2, '.--', color='green')

    # Now we add a x-axis title to the second plot.
    plt.xlabel('time (s)')

    # And of coures a y-axix because we are not heathens.
    plt.ylabel('Undamped')

    # So far everything has happened in plotting space but no plot was
    # actually created. We need to state the plot should be drawn.
    # Up until now we could change any
    # parameter and the plot would be updated. Once we call to make the plot
    # the latest settings will be used. By default a new window will appear.
    plt.show()

if False:
    # Set the seed for random value. This means we get the same result every time.
    np.random.seed(19680801)

    # example data
    mu = 100  # mean of distribution
    sigma = 15  # standard deviation of distribution
    x = mu + sigma * np.random.randn(437)

    num_bins = 50

    # This is setting up the figure and axes variables.
    # Figure is the general white space and axes is the plotting part. We can
    # have one figure but as many axes as we want. Axis is the x and y axis that
    # have tick marks and lables.
    fig, axes = plt.subplots()

    # the histogram of the data
    n, bins, patches = axes.hist(x, num_bins, density=1)

    # add a 'best fit' line
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
         np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
    axes.plot(bins, y, '--')
    axes.set_xlabel('Smarts')
    axes.set_ylabel('Probability density')

    # The 'r' at the start of a string means regular expression. This forces
    # the string to be exactly as it is listed in memory.' The specail
    # characters are used as escape sequences to set Greek letters.'
    axes.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

    # Tweak spacing to prevent clipping of ylabel. Not sure it's needed?
    fig.tight_layout()  # This adjusts the spaceing at ends of plot ranges.
    plt.show()


if False:
    # this is to make some data to plot
    np.random.seed(19680801)
    # Make a 2-D array
    data = np.random.randn(2, 100)

    # this is setting up the figure and set how many plots we are going to make.
    # We are making two rows and two columns for a total of four plots.
    # We are also stating how big the figure size should be. The numbers for
    # figsize are *100 = pixels. So (5, 5) is (500, 500) pixels.
    fig, axes = plt.subplots(2, 2, figsize=(5, 5))

    # When we made the figure and returned axes, that is a list of length two
    # with each element being a list of lenght two. This means we can make
    # each plot or update each plot by referencing the axes. Start at upper
    # left. [row, column] Axes is the plot, axis is the x and y axis.
    print('axes:\n', axes)
    print('type(axes):', type(axes))
    axes[0, 0].hist(data[0])  # Histogram of one slice of the 2-D array.
    axes[1, 0].scatter(data[0], data[1])  # Scatter of 1 slice vs. other slice
    axes[0, 1].plot(data[0], data[1])  # Plot of 1 slice with other as axis
    axes[1, 1].hist2d(data[0], data[1])  # 2 dimentional histogram

    plt.show()

if False:
    # Some constants. Make these smaller to increase the resolution.
    dx, dy = 0.05, 0.05

    # generate two 2-D grids for the x & y bounds. Don't worry much about this
    # it is just to make some data to plot.
    y, x = np.mgrid[slice(1, 5 + dy, dy),
                    slice(1, 5 + dx, dx)]

    z = np.sin(x)**10 + np.cos(10 + y*x) * np.cos(x)

    # x and y are bounds, so z should be the value *inside* those bounds.
    # Therefore, remove the last value from the z array. Again don't worry too
    # much about this just making data for an example plot.
    z = z[:-1, :-1]
    levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())

    # pick the desired colormap, sensible levels, and define a normalization
    # instance which takes data values and translates those into levels.
    # PiYG is the name of the colormap.
    cmap = plt.get_cmap('PiYG')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

    # Notice that the axes are split out using tuple syntax. This
    # means we can reference with name only instead of needing to
    # subset.
    fig, (ax0, ax1) = plt.subplots(nrows=2)
    print(type((ax0, ax1)))
    print(type(ax0))

    # Now we make the plot for first row. We are using the color map
    # defined above. If we didn't it would choose a default.
    # Also notice that we are returning a variable that is used to
    # set the colorbar. This variable is referencing the plotted data
    # specifically not including the x and y axes.
    im = ax0.pcolormesh(x, y, z, cmap=cmap, norm=norm)

    # This is adding a colorbar to the plot.
    # What if we didn't add a colorbar, what would happen?
    fig.colorbar(im, ax=ax0)
    ax0.set_title('pcolormesh with levels')

    # Contours are *point* based plots, so convert our bound into point
    # centers.
    # This is the second plot. Notice how we have called using ax1 from
    # previous plt.subplots call.
    cf = ax1.contourf(x[:-1, :-1] + dx/2.,
                      y[:-1, :-1] + dy/2., z, levels=levels,
                      cmap=cmap)
    fig.colorbar(cf, ax=ax1)  # Add a colorbar to the plot
    ax1.set_title('contourf with levels')

    # adjust spacing between subplots so `ax1` title and `ax0` tick labels
    # don't overlap. Try it without and see what happens. There is another way
    # to finetune the spacing if you don't like this.
    fig.tight_layout()

    plt.show()
