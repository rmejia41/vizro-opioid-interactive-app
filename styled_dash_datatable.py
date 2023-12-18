import vizro.models as vm
import vizro.plotly.express as px
from vizro import Vizro
from vizro.tables import dash_data_table

df = px.data.gapminder().query("year == 2007")

column_definitions = [
    {"name": "country", "id": "country", "type": "text", "editable": False},
    {"name": "continent", "id": "continent", "type": "text"},
    {"name": "year", "id": "year", "type": "datetime"},
    {"name": "lifeExp", "id": "lifeExp", "type": "numeric"},
    {"name": "pop", "id": "pop", "type": "numeric"},
    {"name": "gdpPercap", "id": "gdpPercap", "type": "numeric"},
]

style_data_conditional = [
    {
        "if": {
            "column_id": "year",
        },
        "backgroundColor": "dodgerblue",
        "color": "white",
    },
    {"if": {"filter_query": "{lifeExp} < 55", "column_id": "lifeExp"}, "backgroundColor": "#85144b", "color": "white"},
    {
        "if": {"filter_query": "{gdpPercap} > 10000", "column_id": "gdpPercap"},
        "backgroundColor": "green",
        "color": "white",
    },
    {"if": {"column_type": "text"}, "textAlign": "left"},
    {
        "if": {"state": "active"},
        "backgroundColor": "rgba(0, 116, 217, 0.3)",
        "border": "1px solid rgb(0, 116, 217)",
    },
]

style_header_conditional = [{"if": {"column_type": "text"}, "textAlign": "left"}]

page = vm.Page(
    title="Example of a styled Dash DataTable",
    components=[
        vm.Table(
            id="table",
            title="Styled table",
            figure=dash_data_table(
                data_frame=df,
                columns=column_definitions,
                sort_action="native",
                editable=True,
                style_data_conditional=style_data_conditional,
                style_header_conditional=style_header_conditional,
            ),
        ),
    ],
    controls=[vm.Filter(column="continent")],
)
dashboard = vm.Dashboard(pages=[page])

Vizro().build(dashboard).run()