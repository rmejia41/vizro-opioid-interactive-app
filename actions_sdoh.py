import pandas as pd
import vizro.models as vm
import vizro.plotly.express as px
from vizro import Vizro
from vizro.actions import filter_interaction

df = pd.read_csv('C:/Users/Biu9/OneDrive - CDC/Python files/Python Vizro/SDOH_county_2020.csv', encoding='ISO-8859-1')
sdoh_data = (
        df.groupby(by=["STATE", "COUNTY", "REGION"]).
            agg({"CDCW_OPIOID_DTH_RATE": "mean", "CDCW_TOT_POPULATION": "sum", "CDCW_SELFHARM_DTH_RATE": "mean"}).reset_index()
    )
#print(sdoh_data.head())
#print(sdoh_data.shape)
#print(sdoh_data.describe())
#print (sdoh_data.index)

dashboard = vm.Dashboard(
    pages=[
        vm.Page(
            title="Data Filter Interaction: Opioid and Self Harm Death Rates, CDC PLACES, 2020 ",
            components=[
                vm.Graph(
                    id="bar_relation_2020",
                    figure=px.box(
                        sdoh_data,
                        x="REGION",
                        y="CDCW_OPIOID_DTH_RATE",
                        color="REGION",
                        points="all",
                        custom_data=["REGION"],
                        labels={'CDCW_OPIOID_DTH_RATE': "Opioid Death Rate "},
                    ),
                    # clicking the custom_data (state) of box plot will filter (target)
                    # the dataframe (continent column) of gapminder_scatter graph
                    actions=[vm.Action(function=filter_interaction(targets=["sdoh_scatter"]))],
                ),
                vm.Graph(
                    id="sdoh_scatter",
                    figure=px.scatter(
                        sdoh_data,
                        x="CDCW_OPIOID_DTH_RATE",
                        y="CDCW_SELFHARM_DTH_RATE",
                        size="CDCW_TOT_POPULATION",
                        color="STATE",
                        labels={'ACS_GINI_INDEX': "GINI Index", 'CDCW_SELFHARM_DTH_RATE': "Self Harm Death Rate", 'CDCW_OPIOID_DTH_RATE': "Opioid Death Rate "},
                    ),
                ),
            ],
        ),
    ]
)

Vizro().build(dashboard).run(port=8058)