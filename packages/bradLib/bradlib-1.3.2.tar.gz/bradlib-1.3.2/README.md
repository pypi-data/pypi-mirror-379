# bradLib

A simple personal library. Currently contains `csv2tab` and `plotter`.
Will update as I create more utilities.

## `bradLib.csv2tab(file, caption = "", alignment = "")`
### Usage

|Parameters  | Type |                                                                |
|------------|------|----------------------------------------------------------------|
|`file`      | `str`| The path to the csv file, either relative or absolute          |
|`caption`   | `str`| Text to go in the table caption                                |
|`alignment` | `str`| The alignment for each column, must match the number of columns. Can be: `l`,`r`, or `c` for left, right or centered|

### `csv` formatting

Data columns should have the intended headers including units e.g.
> "x position"

Error columns must contain "Error" e.g.
> "xError"

## `bradLib.plotter(title = None, figsize=(8,5))`
### Usage

|Parameters  | Type |                |
|------------|------|----------------|
|`title`     | `str`| The plot title |
|`figsize`   | `tuple`| The dimensions for the produced figure|

Initialise a plotter object as 
```
plot = plotter("title", figsize = (8,5))
```

### `plotter.save(name)`

|Parameters  | Type |                |
|------------|------|----------------|
|`name`     | `str`| The filename for the produced image |

### `plotter.plot(data, xyLabels = [None, None], label=None, legendLoc="best")`

|Parameters  | Type |                |
|------------|------|----------------|
|`data`     | `array-like`| The data to be plotted , formatted as `[x, y]` where `x` and `y` are 1-D arrays of same length|
|`xyLabels` | `tuple`     | The axis labels for the plot|
|`label`    | `str`       | The label for the data, used alongside a legend|
|`legendloc`| `str`       | The location to place the legend|

### `plotter.scatter(data, xyLabels = [None, None], label=None, legendLoc="best", colour=None, markerSize=10, markerStyle = "o")`

|Parameters   | Type |                |
|-------------|------|----------------|
|`data`       | `array-like`| The data to be plotted , formatted as `[x, y]` where `x` and `y` are 1-D arrays of same length|
|`xyLabels`   | `tuple`     | The axis labels for the plot|
|`label`      | `str`       | The label for the data, used alongside a legend|
|`legendloc`  | `str`       | The location to place the legend|
|`colour`     | `str`       | The colour for the markers|
|`markerSize` | `int`       | The size for the markers|
|`markerStyle`| `str`       | The style for the markers|

> Note: Check [matplotlib](https://matplotlib.org/stable/) documentation for colour, markersize and markerstyle usage

### `plotter.errorbar(data, errorbars)`

|Parameters   | Type |                |
|-------------|------|----------------|
|`data`       | `array-like`| The data to be plotted , formatted as `[x, y]` where `x` and `y` are 1-D arrays of same length|
|`errorbars`  | `array-like`| The data to be plotted , formatted as `[xError, yError]`|


