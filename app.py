import dash
import dash_cytoscape as cyto
import dash_html_components as html

app = dash.Dash(__name__)

default_stylesheet = [
    {
        "selector": "node",
        "style": {
            "background-color": "#BFD7B5",
            "label": "data(label)",
            "width": "30%",
            "height": "50%",
        },
    }
]

app.layout = html.Div(
    [
        cyto.Cytoscape(
            id="cytospace",
            elements=[
                {
                    "data": {"id": "one", "label": "Node 1"},
                    "position": {"x": 50, "y": 50},
                    "size": 20,
                },
                {
                    "data": {"id": "two", "label": "Node 2"},
                    "position": {"x": 200, "y": 200},
                    "size": 70,
                },
                {"data": {"source": "one", "target": "two", "label": "Node 1 to 2"}},
            ],
            layout={"name": "preset"},
            stylesheet=default_stylesheet,
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
