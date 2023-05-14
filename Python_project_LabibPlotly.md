![](https://dit.sn/wp-content/uploads/2019/03/Logo.png)

# Plotly Open Source Graphing Library for Python
# Content

- [Introduction to plotly](#introduction-to-plotly)
- [Installation](#installation)
- [Package Structure of Plotly](#package-structure-of-plotly)
- [Simple plot](#simple-plot) 
- [Creating Different Types of Charts related to data visualization :](#creating-different-types-of-charts-related-to-data-visualization)  
     1 [Line Chart](#line-chart)  
     2 [Bar Chart](#bar-chart)  
     3 [Histograms](#histograms)  
     4 [Scatter Plot and Bubble charts](#scatter-plot-and-bubble-charts)  
     5 [Pie Charts](#pie-charts)  
     6 [Box Plots](#box-plots)    
     7 [Gantt Charts](#gantt-charts)  
     8 [Contour Plots](#contour-plots)  
     9 [Heatmaps](#heatmaps)     
     10 [3D Scatter Plot Plotly](#3d-scatter-plot-plotly)  
     11 [3D Surface Plots](#3d-surface-plots)       
- [More Plots using Plotly](#more-plots-using-plotly)  
- [Conclusion](#conclusion)

## _Introduction to plotly_

**Python Plotly** Library is an open-source library that can be used for **data visualization and understanding data simply and easily**. Plotly supports various types of plots like line charts, scatter plots, histograms, cox plots, etc  
- Plotly has hover tool capabilities that allow us to detect any **outliers** or anomalies in a large number of data points.  
- It is visually attractive that can be accepted by a wide range of audiences.  
- It allows us for the endless customization of our graphs that makes our plot more meaningful and understandable for others.  
## _Installation_
Plotly does not come built-in with Python. To install it type the below command in the terminal.  
```sh
pip install plotly
```
## _Package Structure of Plotly_  

There are three main modules in Plotly. They are:
- plotly.plotly
- plotly.graph.objects
- plotly.tools
- plotly.express  

**plotly.plotly** sert d'interface entre la machine locale et Plotly. Il contient des fonctions qui nécessitent une réponse du serveur de Plotly.  
**plotly.graph_objects** module contains the objects (Figure, layout, data, and the definition of the plots like scatter plot, line chart) that are responsible for creating the plots.  The Figure can be represented either as dict or instances of **plotly.graph_objects.Figure** and these are serialized as JSON before it gets passed to plotly.js. Consider the below example for better understanding.  
**plotly.tools** provides various additional tools. For example, it allows you to create subplots, i.e. a set of sub-graphs.  
**plotly.express** allows us to display our graphs immediately. 

## _Simple plot_ 
After learning the installation and basic structure of the Plotly, let’s create a simple plot using the pre-defined data sets defined by the plotly.  
Example:
```sh
import plotly.express as px


# Creating the Figure instance
fig = px.line(x=[1, 2, 3], y=[1, 2, 3])

# showing the plot
fig.show()
```
Output:
![](SimplePlot.png)  

In the above example, the plotly.express module is imported which returns the Figure instance. We have created a simple line chart by passing the x, y coordinates of the points to be plotted.

## _Creating Different Types of Charts related to data visualization_  
With plotly we can create more than 40 charts and every plot can be created using the **plotly.express and plotly.graph_objects class**. Let’s see some commonly used charts with the help of Plotly.  

### _Line Chart_
[Line plot](https://www.geeksforgeeks.org/line-chart-using-plotly-in-python/) in Plotly is much accessible and illustrious annexation to plotly which manage a variety of types of data and assemble easy-to-style statistic. With **px.line** each data position is represented as a vertex  (which location is given by the x and y columns) of a polyline mark in 2D space.  
Example:  
```sh
import plotly.express as px

# using the iris dataset
df = px.data.iris()

# plotting the line chart
fig = px.line(df, x="species", y="petal_width")

# showing the plot
fig.show()
```  
Output :
![](line_chart.png)  
Refer to the below articles to get detailed information about the line charts.
- [plotly.express.line() function in Python](https://www.geeksforgeeks.org/plotly-express-line-function-in-python/)
- [Line Chart using Plotly in Python](https://www.geeksforgeeks.org/line-chart-using-plotly-in-python/)

### _Bar Chart_  
A [bar chart](https://www.geeksforgeeks.org/bar-chart-using-plotly-in-python/) is a pictorial representation of data that presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent. In other words, it is the pictorial representation of dataset. These data sets contain the numerical values of variables that represent the length or height.  
Example:  
```sh
import plotly.express as px

# using the iris dataset
df = px.data.iris()

# plotting the bar chart
fig = px.bar(df, x="sepal_width", y="sepal_length")

# showing the plot
fig.show()
```  
Output :  
![](bar_chart.png)  
Refer to the below articles to get detailed information about the bar chart.
- [Bar chart using Plotly in Python](https://www.geeksforgeeks.org/bar-chart-using-plotly-in-python/)
- [How to create Stacked bar chart in Python-Plotly?](https://www.geeksforgeeks.org/how-to-create-stacked-bar-chart-in-python-plotly/)
- [How to group Bar Charts in Python-Plotly?](https://www.geeksforgeeks.org/how-to-group-bar-charts-in-python-plotly/)

### _Histograms_  
A [histogram](https://www.geeksforgeeks.org/histogram-using-plotly-in-python/) contains a rectangular area to display the statistical information which is proportional to the frequency of a variable and its width in successive numerical intervals. A graphical representation that manages a group of data points into different specified ranges. It has a special feature that shows no gaps between the bars and similar to a vertical bar graph.  
Example: 
```sh
import plotly.express as px

# using the iris dataset
df = px.data.iris()

# plotting the histogram
fig = px.histogram(df, x="sepal_length", y="petal_width")

# showing the plot
fig.show()
```  
Output :  
![](histogram.png)  
Refer to the below articles to get detailed information about the histograms.

- [Histogram using Plotly in Python](https://www.geeksforgeeks.org/histogram-using-plotly-in-python/)  
- [Histograms in Plotly using graph_objects class](https://www.geeksforgeeks.org/histograms-in-plotly-using-graph_objects-class/)  
- [How to create a Cumulative Histogram in Plotly?](https://www.geeksforgeeks.org/how-to-create-a-cumulative-histogram-in-plotly/)

### _Scatter Plot and Bubble charts_  
A [scatter plot](https://www.geeksforgeeks.org/scatter-plot-using-plotly-in-python/) is a set of dotted points to represent individual pieces of data in the horizontal and vertical axis. A graph in which the values of two variables are plotted along X-axis and Y-axis, the pattern of the resulting points reveals a correlation between them.  
A [bubble plot](https://www.geeksforgeeks.org/bubble-chart-using-plotly-in-python/) is a scatter plot with bubbles (color-filled circles). Bubbles have various sizes dependent on another variable in the data. It can be created using the scatter() method of plotly.express.
Example 1: Scatter Plot  

```sh
import plotly.express as px

# using the iris dataset
df = px.data.iris()

# plotting the scatter chart
fig = px.scatter(df, x="species", y="petal_width")

# showing the plot
fig.show()
```  
Output : 
![](Scatter_Plot.png)  

Example 2: Bubble Plot  

```sh
import plotly.express as px

# using the iris dataset
df = px.data.iris()

# plotting the bubble chart
fig = px.scatter(df, x="species", y="petal_width",
				size="petal_length", color="species")

# showing the plot
fig.show()
```  
Output :  

![](Bubble_Plot.png)  

Refer to the below articles to get detailed information about the scatter plots and bubble plots.
- [plotly.express.scatter() function in Python](https://www.geeksforgeeks.org/plotly-express-scatter-function-in-python/)
- [Scatter plot in Plotly using graph_objects class](https://www.geeksforgeeks.org/scatter-plot-in-plotly-using-graph_objects-class/)
- [Scatter plot using Plotly in Python](https://www.geeksforgeeks.org/scatter-plot-using-plotly-in-python/)
- [Bubble chart using Plotly in Python](https://www.geeksforgeeks.org/bubble-chart-using-plotly-in-python/)  

### _Pie Charts_  

A [pie chart](https://www.geeksforgeeks.org/pie-plot-using-plotly-in-python/) is a circular statistical graphic, which is divided into slices to illustrate numerical proportions. It depicts a special chart that uses “pie slices”, where each sector shows the relative sizes of data. A circular chart cuts in a form of radii into segments describing relative frequencies or magnitude also known as circle graph.  
Example:  
  
```sh
import plotly.express as px

# using the tips dataset
df = px.data.tips()

# plotting the pie chart
fig = px.pie(df, values="total_bill", names="day")

# showing the plot
fig.show()
```  
Output :  

![](pie_chart.png)  

Refer to the below articles to get detailed information about the pie charts.
- [Pie plot using Plotly in Python](https://www.geeksforgeeks.org/pie-plot-using-plotly-in-python/)  

### _Box Plots_  

A [Box Plot](https://www.geeksforgeeks.org/understanding-different-box-plot-with-visualization/) is also known as Whisker plot is created to display the summary of the set of data values having properties like minimum, first quartile, median, third quartile and maximum. In the box plot, a box is created from the first quartile to the third quartile, a vertical line is also there which goes through the box at the median. Here x-axis denotes the data to be plotted while the y-axis shows the frequency distribution.  
Example:  
```sh
import plotly.express as px

# using the tips dataset
df = px.data.tips()

# plotting the box chart
fig = px.box(df, x="day", y="total_bill")

# showing the plot
fig.show()
```  
Output :  
![](box_plot.png)  

Refer to the below articles to get detailed information about box plots.
- [Box Plot using Plotly in Python](https://www.geeksforgeeks.org/box-plot-using-plotly-in-python/)
- [Box plot in Plotly using graph_objects class](https://www.geeksforgeeks.org/box-plot-in-plotly-using-graph_objects-class/)
- [How to create Grouped box plot in Plotly?](https://www.geeksforgeeks.org/how-to-create-grouped-box-plot-in-plotly/)  

### _Gantt Charts_  

[Generalized Activity Normalization Time Table (GANTT) chart](https://www.geeksforgeeks.org/short-note-on-gantt-chart/) is type of chart in which series of horizontal lines are present that show the amount of work done or production completed in given period of time in relation to amount planned for those projects. 
Example:  
```sh
import plotly.figure_factory as ff

# Data to be plotted
df = [dict(Task="A", Start='2020-01-01', Finish='2009-02-02'),
	dict(Task="Job B", Start='2020-03-01', Finish='2020-11-11'),
	dict(Task="Job C", Start='2020-08-06', Finish='2020-09-21')]

# Creating the plot
fig = ff.create_gantt(df)
fig.show()
```  
Output :  
![](gantt_chart.png)  

### Contour Plots  

[Contour plots](https://www.geeksforgeeks.org/contour-plots/) also called level plots are a tool for doing multivariate analysis and visualizing 3-D plots in 2-D space. If we consider X and Y as our variables we want to plot then the response Z will be plotted as slices on the X-Y plane due to which contours are sometimes referred as Z-slices or iso-response.  
A contour plots is used in the case where you want to see the changes in some value (Z) as a function with respect to the two values (X, Y). Consider the below example.  
Example:  
```sh
import plotly.graph_objects as go


# Creating the X, Y value that will
# change the values of Z as a function
feature_x = np.arange(0, 50, 2)
feature_y = np.arange(0, 50, 3)

# Creating 2-D grid of features
[X, Y] = np.meshgrid(feature_x, feature_y)

Z = np.cos(X / 2) + np.sin(Y / 4)  

# plotting the figure
fig = go.Figure(data =
	go.Contour(x = feature_x, y = feature_y, z = Z))

fig.show()
```  
Output :  

![](contour_plot.png)  

Refer to the below articles to get detailed information about contour plots.
- [Contour Plots using Plotly in Python](https://www.geeksforgeeks.org/contour-plots-using-plotly-in-python/)  

### _Heatmaps_  

[Heatmap](https://www.geeksforgeeks.org/create-heatmaps-using-graph_objects-class-in-plotly/) is defined as a graphical representation of data using colors to visualize the value of the matrix. In this, to represent more common values or higher activities brighter colors basically reddish colors are used and to represent less common or activity values, darker colors are preferred. Heatmap is also defined by the name of the shading matrix.  
Example:  
```sh
import plotly.graph_objects as go


feature_x = np.arange(0, 50, 2)
feature_y = np.arange(0, 50, 3)

# Creating 2-D grid of features
[X, Y] = np.meshgrid(feature_x, feature_y)

Z = np.cos(X / 2) + np.sin(Y / 4)

# plotting the figure  
fig = go.Figure(data =
	go.Heatmap(x = feature_x, y = feature_y, z = Z,))

fig.show()
```  
Output :  

![](Heatmap.png)  

Refer to the below articles to get detailed information about the heatmaps.
- [Create Heatmaps using graph_objects class in Plotly](https://www.geeksforgeeks.org/create-heatmaps-using-graph_objects-class-in-plotly/)
- [Annotated Heatmaps using Plotly in Python](https://www.geeksforgeeks.org/annotated-heatmaps-using-plotly-in-python/)  

### _3D Scatter Plot Plotly_  

[3D Scatter Plot](https://www.geeksforgeeks.org/3d-surface-plots-using-plotly-in-python/) can plot two-dimensional graphics that can be enhanced by mapping up to three additional variables while using the semantics of hue, size, and style parameters. All the parameter control visual semantic which are used to identify the different subsets. Using redundant semantics can be helpful for making graphics more accessible. It can be created using the scatter_3d function of plotly.express class.  
Example:  
```sh
import plotly.express as px

# Data to be plotted
df = px.data.iris()

# Plotting the figure
fig = px.scatter_3d(df, x = 'sepal_width',
					y = 'sepal_length',
					z = 'petal_width',
					color = 'species')

fig.show()
```  
Output :  
![](3d_scatter_plot.png)  

Refer to the below articles to get detailed information about the 3D scatter plot.
- [3D scatter plot using Plotly in Python](https://www.geeksforgeeks.org/3d-surface-plots-using-plotly-in-python/)
- [3D Scatter Plot using graph_objects Class in Plotly-Python](https://www.geeksforgeeks.org/3d-scatter-plot-using-graph_objects-class-in-plotly-python/)
- [3D Bubble chart using Plotly in Python](https://www.geeksforgeeks.org/3d-bubble-chart-using-plotly-in-python/)  

### _3D Surface Plots_

[Surface plot](https://www.geeksforgeeks.org/3d-surface-plots-using-plotly-in-python/) is those plot which has three-dimensions data which is X, Y, and Z. Rather than showing individual data points, the surface plot has a functional relationship between dependent variable Y and have two independent variables X and Z. This plot is used to distinguish between dependent and independent variables.  
Example:  
```sh
import plotly.graph_objects as go
import numpy as np

# Data to be plotted
x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
y = x.copy().T
z = np.cos(x ** 2 + y ** 2)

# plotting the figure
fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])

fig.show()
```  
Output :  
![](3d_surface_plot.png)  

## _More Plots using Plotly_  

- [plotly.express.scatter_geo() function in Python](https://www.geeksforgeeks.org/plotly-express-scatter_geo-function-in-python/)

- [plotly.express.scatter_polar() function in Python](https://www.geeksforgeeks.org/plotly-express-scatter_polar-function-in-python/)  
- [plotly.express.scatter_ternary() function in Python](https://www.geeksforgeeks.org/plotly-express-scatter_ternary-function-in-python/)  

- [plotly.express.line_ternary() function in Python](https://www.geeksforgeeks.org/plotly-express-line_ternary-function-in-python/)  

- [Filled area chart using plotly in Python](https://www.geeksforgeeks.org/filled-area-chart-using-plotly-in-python/)  

- [How to Create Stacked area plot using Plotly in
Python?](https://www.geeksforgeeks.org/how-to-create-stacked-area-plot-using-plotly-in-python/)  

- [Sunburst Plot using Plotly in Python](https://www.geeksforgeeks.org/sunburst-plot-using-plotly-in-python/)  

- [Sunburst Plot using graph_objects class in plotly](https://www.geeksforgeeks.org/sunburst-plot-using-graph_objects-class-in-plotly/)  

- [plotly.figure_factory.create_annotated_heatmap() function in Python](https://www.geeksforgeeks.org/plotly-figure_factory-create_annotated_heatmap-function-in-python/)  

- [plotly.figure_factory.create_2d_density() function in Python](https://www.geeksforgeeks.org/plotly-figure_factory-create_2d_density-function-in-python/)  

- [Ternary contours Plot using Plotly in Python](https://www.geeksforgeeks.org/ternary-contours-plot-using-plotly-in-python/)  

- [How to make Log Plots in Plotly – Python?](https://www.geeksforgeeks.org/how-to-make-log-plots-in-plotly-python/)  

- [Polar Charts using Plotly in Python](https://www.geeksforgeeks.org/polar-charts-using-plotly-in-python/)  

- [Carpet Contour Plot using Plotly in Python](https://www.geeksforgeeks.org/carpet-contour-plot-using-plotly-in-python/)  

- [Ternary Plots in Plotly](https://www.geeksforgeeks.org/ternary-plots-in-plotly/)  

- [How to create a Ternary Overlay using Plotly?](https://www.geeksforgeeks.org/how-to-create-a-ternary-overlay-using-plotly/)  

- [Parallel Coordinates Plot using Plotly in Python](https://www.geeksforgeeks.org/parallel-coordinates-plot-using-plotly-in-python/)  
- [Carpet Plots using Plotly in Python](https://www.geeksforgeeks.org/carpet-plots-using-plotly-in-python/)  

- [3D Cone Plots using Plotly in Python](https://www.geeksforgeeks.org/3d-cone-plots-using-plotly-in-python/)  

- [3D Volume Plots using Plotly in Python](https://www.geeksforgeeks.org/3d-volume-plots-using-plotly-in-python/)  

- [3D Streamtube Plots using Plotly in Python](https://www.geeksforgeeks.org/3d-streamtube-plots-using-plotly-in-python/)  

- [3D Mesh Plots using Plotly in Python](https://www.geeksforgeeks.org/3d-mesh-plots-using-plotly-in-python/)  

- [How to create Tables using Plotly in Python?](https://www.geeksforgeeks.org/how-to-create-tables-using-plotly-in-python/)  

- [plotly.figure_factory.create_dendrogram() function in Python](https://www.geeksforgeeks.org/plotly-figure_factory-create_dendrogram-function-in-python/)  

- [Define Node position in Sankey Diagram in plotly](https://www.geeksforgeeks.org/define-node-position-in-sankey-diagram-in-plotly/)  
- [Sankey Diagram using Plotly in Python](https://www.geeksforgeeks.org/sankey-diagram-using-plotly-in-python/)  

- [Quiver Plots using Plotly in Python](https://www.geeksforgeeks.org/quiver-plots-using-plotly-in-python/)  

- [Treemap using Plotly in Python](https://www.geeksforgeeks.org/treemap-using-plotly-in-python/)
- [Treemap using graph_objects class in plotly](https://www.geeksforgeeks.org/treemap-using-graph_objects-class-in-plotly/)  

- [plotly.figure_factory.create_candlestick() function in Python](https://www.geeksforgeeks.org/plotly-figure_factory-create_candlestick-function-in-python/)  

- [plotly.figure_factory.create_choropleth() function in Python](https://www.geeksforgeeks.org/plotly-figure_factory-create_choropleth-function-in-python/)  

- [plotly.figure_factory.create_bullet() in Python](https://www.geeksforgeeks.org/plotly-figure_factory-create_bullet-in-python/)
- [Streamline Plots in Plotly using Python](https://www.geeksforgeeks.org/streamline-plots-in-plotly-using-python/)  

- [How to make Wind Rose and Polar Bar Charts in Plotly – Python?](https://www.geeksforgeeks.org/how-to-make-wind-rose-and-polar-bar-charts-in-plotly-python/)  

## _Conclusion_  

Plotly is a **crucial tool in the field of** [data visualization](https://www.techtarget.com/searchbusinessanalytics/definition/data-visualization#:~:text=Data%20visualization%20is%20the%20practice,outliers%20in%20large%20data%20sets.). Rather easy to learn, it allows you to create complex and elaborate graphics with the aim of representing the data well and making it understandable.  

## __some resources consulted__  

- [Python Plotly](https://www.geeksforgeeks.org/python-plotly-tutorial/)  
- [With Data Visualization, give meaning to your data](https://datascientest.com/avec-la-data-visualisation-donnez-du-sens-a-vos-donnees)  
- [Getting Started with Plot.ly](https://towardsdatascience.com/getting-started-with-plot-ly-3c73706a837c#:~:text=We%20can%20access%20this%20API,online%20to%20store%20your%20plots.)  

-----

__Thank You For Your Kind Attention__




