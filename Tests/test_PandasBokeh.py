import json
import pandas as pd
import numpy as np
import pandas_bokeh
import os

directory = os.path.dirname(__file__)
os.makedirs(os.path.join(directory, "Plots"), exist_ok=True)

def test_basic_lineplot():
    """Test for basic lineplot"""

    # Create basic lineplot:
    np.random.seed(42)
    df = pd.DataFrame(
        {"Google": np.random.randn(1000) + 0.2, "Apple": np.random.randn(1000) + 0.17},
        index=pd.date_range("1/1/2000", periods=1000),
    )
    df.index.name = "Date"
    df = df.cumsum()
    df = df + 50
    p_basic_lineplot = df.plot_bokeh(kind="line", show_figure=False)
    p_basic_lineplot_accessor = df.plot_bokeh.line(show_figure=False)

    # Output plot as HTML:
    output = pandas_bokeh.row([p_basic_lineplot, p_basic_lineplot_accessor])
    with open(os.path.join(directory, "Plots", "Basic_lineplot.html"), "w") as f:
        f.write(pandas_bokeh.embedded_html(output))

    assert True


def test_complex_lineplot():
    """Test for complexd lineplot"""

    # Create complex lineplot:
    np.random.seed(42)
    df = pd.DataFrame(
        {"Google": np.random.randn(1000) + 0.2, "Apple": np.random.randn(1000) + 0.17},
        index=pd.date_range("1/1/2000", periods=1000),
    )
    df.index.name = "Date"
    df = df.cumsum()
    df = df + 50
    arguments = dict(
        figsize=(600, 450),
        y="Apple",
        title="Apple vs Google",
        xlabel="Date",
        ylabel="Stock price [$]",
        yticks=[0, 100, 200, 300, 400],
        ylim=(0, 400),
        toolbar_location=None,
        colormap=["red", "blue"],
        hovertool_string="""<img
                        src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/170px-Apple_logo_black.svg.png" 
                        height="42" alt="@imgs" width="42"
                        style="float: left; margin: 0px 15px 15px 0px;"
                        border="2"></img> Apple 
                        
                        <h4> Stock Price: </h4> @{Apple}""",
        panning=False,
        zooming=False,
        show_figure=False,
    )
    p_complex_lineplot = df.plot_bokeh(kind="line", **arguments)
    p_complex_lineplot_accessor = df.plot_bokeh.line(**arguments)

    # Output plot as HTML:
    output = pandas_bokeh.row([p_complex_lineplot, p_complex_lineplot_accessor])
    with open(os.path.join(directory, "Plots", "Complex_lineplot.html"), "w") as f:
        f.write(pandas_bokeh.embedded_html(output))

    assert True


def test_lineplot_with_points():
    "Test for lineplot with data points:"

    # Create complex lineplot:
    np.random.seed(42)
    df = pd.DataFrame(
        {"Google": np.random.randn(1000) + 0.2, "Apple": np.random.randn(1000) + 0.17},
        index=pd.date_range("1/1/2000", periods=1000),
    )
    df.index.name = "Date"
    df = df.cumsum()
    df = df + 50
    arguments = dict(
        figsize=(600, 450),
        title="Apple vs Google",
        xlabel="Date",
        ylabel="Stock price [$]",
        yticks=[0, 100, 200, 300, 400],
        ylim=(100, 200),
        xlim=("2001-01-01", "2001-02-01"),
        colormap=["red", "blue"],
        plot_data_points=True,
        plot_data_points_size=10,
        marker="asterisk",
        show_figure=False,
    )
    p_lineplot_with_points = df.plot_bokeh(kind="line", **arguments)
    p_lineplot_with_points_accessor = df.plot_bokeh.line(**arguments)

    # Output plot as HTML:
    output = pandas_bokeh.row([p_lineplot_with_points, p_lineplot_with_points_accessor])
    with open(os.path.join(directory, "Plots", "Lineplot_with_points.html"), "w") as f:
        f.write(pandas_bokeh.embedded_html(output))

    assert True


def test_lineplot_with_points():
    "Test for lineplot with data points:"

    # Create complex lineplot:
    np.random.seed(42)
    df = pd.DataFrame(
        {"Google": np.random.randn(1000) + 0.2, "Apple": np.random.randn(1000) + 0.17},
        index=pd.date_range("1/1/2000", periods=1000),
    )
    df.index.name = "Date"
    df = df.cumsum()
    df = df + 50
    arguments = dict(
        figsize=(600, 450),
        title="Apple vs Google",
        xlabel="Date",
        ylabel="Stock price [$]",
        yticks=[0, 100, 200, 300, 400],
        ylim=(100, 200),
        xlim=("2001-01-01", "2001-02-01"),
        colormap=["red", "blue"],
        plot_data_points=True,
        plot_data_points_size=10,
        marker="asterisk",
        show_figure=False,
    )
    p_lineplot_with_points = df.plot_bokeh(kind="line", **arguments)
    p_lineplot_with_points_accessor = df.plot_bokeh.line(**arguments)

    # Output plot as HTML:
    output = pandas_bokeh.row([p_lineplot_with_points, p_lineplot_with_points_accessor])
    with open(os.path.join(directory, "Plots", "Lineplot_with_points.html"), "w") as f:
        f.write(pandas_bokeh.embedded_html(output))

    assert True


def test_pointplot():
    "Test for pointplot"

    x = np.arange(-3, 3, 0.1)
    y2 = x ** 2
    y3 = x ** 3
    df = pd.DataFrame({"x": x, "Parabula": y2, "Cube": y3})

    arguments = dict(
        x="x",
        xticks=range(-3, 4),
        size=5,
        colormap=["#009933", "#ff3399"],
        title="Pointplot (Parabula vs. Cube)",
        marker="x",
        show_figure=False,
    )

    p_pointplot = df.plot_bokeh(kind="point", **arguments)
    p_pointplot_accessor = df.plot_bokeh.point(**arguments)

    # Output plot as HTML:
    output = pandas_bokeh.row([p_pointplot, p_pointplot_accessor])
    with open(os.path.join(directory, "Plots", "Pointplot.html"), "w") as f:
        f.write(pandas_bokeh.embedded_html(output))

    assert True


def test_scatterplot():
    "Test for scatterplot"

    # Load Iris Dataset:
    df = pd.read_csv(
        r"https://raw.githubusercontent.com/PatrikHlobil/Pandas-Bokeh/master/Documentation/Testdata/iris/iris.csv"
    )

    # Create Div with DataFrame:
    from bokeh.models import Div

    div_df = Div(text=df.head(10).to_html(index=False), width=550)
    div_df_accessor = Div(text=df.head(10).to_html(index=False), width=550)

    # Create Scatterplot:
    arguments = dict(
        x="petal length (cm)",
        y="sepal width (cm)",
        category="species",
        title="Iris DataSet Visualization",
        show_figure=False,
    )

    p_scatter = df.plot_bokeh(kind="scatter", **arguments)
    p_scatter_accessor = df.plot_bokeh.scatter(**arguments)

    # Combine Div and Scatterplot via grid layout:
    output = pandas_bokeh.plot_grid(
        [[div_df, p_scatter], [div_df_accessor, p_scatter_accessor]],
        show_plot=False,
        return_html=True,
    )

    with open(os.path.join(directory, "Plots", "Scatterplot.html"), "w") as f:
        f.write(output)

    assert True


def test_scatterplot_2():
    "Test 2 for scatterplot"

    # Load Iris Dataset:
    df = pd.read_csv(
        r"https://raw.githubusercontent.com/PatrikHlobil/Pandas-Bokeh/master/Documentation/Testdata/iris/iris.csv"
    )

    # Change one value to clearly see the effect of the size keyword
    df.loc[13, "sepal length (cm)"] = 15

    # Make scatterplot:
    # Create Scatterplot:
    arguments = dict(
        x="petal length (cm)",
        y="sepal width (cm)",
        category="species",
        title="Iris DataSet Visualization",
        size="sepal length (cm)",
        show_figure=False,
    )

    p_scatter = df.plot_bokeh(kind="scatter", **arguments)
    p_scatter_accessor = df.plot_bokeh.scatter(**arguments)

    # Output plot as HTML:
    output = pandas_bokeh.row([p_scatter, p_scatter_accessor])
    with open(os.path.join(directory, "Plots", "Scatterplot_2.html"), "w") as f:
        f.write(pandas_bokeh.embedded_html(output))

    assert True


def test_barplot_basic():
    "Basic Test for Barplot"

    data = {
        "fruits": ["Apples", "Pears", "Nectarines", "Plums", "Grapes", "Strawberries"],
        "2015": [2, 1, 4, 3, 2, 4],
        "2016": [5, 3, 3, 2, 4, 6],
        "2017": [3, 2, 4, 4, 5, 3],
    }
    df = pd.DataFrame(data).set_index("fruits")

    # Make scatterplot:
    # Create Scatterplot:
    arguments = dict(
        ylabel="Price per Unit [€]",
        title="Fruit prices per Year",
        alpha=0.6,
        show_figure=False,
    )

    p_bar = df.plot_bokeh(kind="bar", **arguments)
    p_bar_accessor = df.plot_bokeh.bar(**arguments)

    # Output plot as HTML:
    output = pandas_bokeh.row([p_bar, p_bar_accessor])
    with open(os.path.join(directory, "Plots", "Barplot_basic.html"), "w") as f:
        f.write(pandas_bokeh.embedded_html(output))

    assert True


def test_barplot_stacked():
    "Test for stacked Barplot"

    data = {
        "fruits": ["Apples", "Pears", "Nectarines", "Plums", "Grapes", "Strawberries"],
        "2015": [2, 1, 4, 3, 2, 4],
        "2016": [5, 3, 3, 2, 4, 6],
        "2017": [3, 2, 4, 4, 5, 3],
    }
    df = pd.DataFrame(data).set_index("fruits")

    # Make scatterplot:
    # Create Scatterplot:
    arguments = dict(
        ylabel="Price per Unit [€]",
        title="Fruit prices per Year",
        stacked=True,
        alpha=0.6,
        show_figure=False,
    )

    p_bar = df.plot_bokeh(kind="bar", **arguments)
    p_bar_accessor = df.plot_bokeh.bar(**arguments)

    # Output plot as HTML:
    output = pandas_bokeh.row([p_bar, p_bar_accessor])
    with open(os.path.join(directory, "Plots", "Barplot_stacked.html"), "w") as f:
        f.write(pandas_bokeh.embedded_html(output))

    assert True


def test_barplot_layout():
    "Test for Barplot layout"

    data = {
        "fruits": ["Apples", "Pears", "Nectarines", "Plums", "Grapes", "Strawberries"],
        "2015": [2, 1, 4, 3, 2, 4],
        "2016": [5, 3, 3, 2, 4, 6],
        "2017": [3, 2, 4, 4, 5, 3],
        show_figure=False,
    }
    df = pd.DataFrame(data).set_index("fruits")

    p_bar = df.plot_bokeh.bar(
        ylabel="Price per Unit [€]", title="Fruit prices per Year", alpha=0.6
    )

    p_stacked_bar = df.plot_bokeh.bar(
        ylabel="Price per Unit [€]",
        title="Fruit prices per Year",
        stacked=True,
        alpha=0.6,
        show_figure=False,
    )

    # Reset index, such that "fruits" is now a column of the DataFrame:
    df.reset_index(inplace=True)

    # Create horizontal bar (via kind keyword):
    p_hbar = df.plot_bokeh(
        kind="barh",
        x="fruits",
        xlabel="Price per Unit [€]",
        title="Fruit prices per Year",
        alpha=0.6,
        legend="bottom_right",
        show_figure=False,
    )

    # Create stacked horizontal bar (via barh accessor):
    p_stacked_hbar = df.plot_bokeh.barh(
        x="fruits",
        stacked=True,
        xlabel="Price per Unit [€]",
        title="Fruit prices per Year",
        alpha=0.6,
        legend="bottom_right",
        show_figure=False,
    )

    # Plot all barplot examples in a grid:
    output = pandas_bokeh.plot_grid(
        [[p_bar, p_stacked_bar], [p_hbar, p_stacked_hbar]],
        plot_width=450,
        show_plot=False,
    )

    # Output plot as HTML:
    with open(os.path.join(directory, "Plots", "Barplot_layout.html"), "w") as f:
        f.write(output)

    assert True
