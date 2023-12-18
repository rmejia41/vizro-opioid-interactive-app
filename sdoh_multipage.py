import pandas as pd
import vizro.plotly.express as px
from vizro import Vizro
import vizro.models as vm
import statsmodels.api as sm


df = pd.read_csv('C:/Users/Biu9/OneDrive - CDC/Python files/Python Vizro/SDOH_county_2020.csv', encoding='ISO-8859-1')
# sdoh_data = (
#         df.groupby(by=["STATE", "COUNTY", "REGION"]).
#             agg({"ACS_GINI_INDEX": "mean", "CDCW_ASSAULT_DTH_RATE": "mean"}).reset_index()
#     )

Home = vm.Page(
    title="Home",
    components=[
        vm.Card(text="""PLACES is a collaboration between CDC, the Robert Wood Johnson Foundation, and the CDC Foundation. 
        PLACES provides health data for small areas across the country. This allows local health departments and jurisdictions, 
        regardless of population size and rurality, to better understand the burden and geographic distribution of health measures in 
        their areas and assist them in planning public health interventions. PLACES provides model-based, population-level analysis and
        community estimates of health measures to all counties, places (incorporated and census designated places), census tracts, and ZIP Code
        Tabulation Areas (ZCTAs) across the United States. Learn more about PLACES.
""",
        href="https://www.cdc.gov/places/"),

        vm.Graph(id="scatter_chart", figure=px.scatter(df, x="ACS_GINI_INDEX", y="CDCW_ASSAULT_DTH_RATE", color="REGION", trendline="ols", labels={'ACS_GINI_INDEX': "GINI Index", 'CDCW_ASSAULT_DTH_RATE': "Assault Death Rate "})),
    ],
    controls=[
        vm.Filter(column="STATE", selector=vm.Dropdown(value=["ALL"])),
    ],
)

Sunburst = vm.Page(
    title="Sunburst Graph",
    path="State-Death Injury Rate Distribution, PLACES, 2020",
    components=[
        vm.Graph(
            id="sunburst", figure=px.sunburst(df, path=["REGION", "STATE"], values="CDCW_ASSAULT_DTH_RATE", color="REGION")
        )
    ],
    controls=[
        vm.Filter(column="REGION", targets=["sunburst"]),
        vm.Parameter(targets=["sunburst.color"], selector=vm.RadioItems(options=["STATE", "REGION"], title="Color")),
    ],
)

dashboard = vm.Dashboard(pages=[Home, Sunburst]) #theme="vizro_dark"

Vizro().build(dashboard).run(port=8064)