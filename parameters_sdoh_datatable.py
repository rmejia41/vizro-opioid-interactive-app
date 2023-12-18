import pandas as pd
import vizro.models as vm
import vizro.plotly.express as px
from vizro import Vizro
from vizro.tables import dash_data_table

#df = pd.read_csv('C:/Users/Biu9/OneDrive - CDC/Python files/Python Vizro/SDOH_county_2020.csv')
df = pd.read_csv('C:/Users/Biu9/OneDrive - CDC/Python files/Python Vizro/SDOH_county_2020.csv', encoding='ISO-8859-1') #fixes utf-8 codec can’t decode bytes in position 0-1
df.info()
#print(df.head())

#group by and get aggregated data to display average total dentists
df_agg_dent = df.groupby(['STATE', 'fips', 'REGION', 'COUNTY', 'CDCW_TOT_POPULATION'])[['CDCW_DRUG_DTH_RATE']].mean()
df_agg_dent.reset_index(inplace=True)
print(df_agg_dent[:5])

page = vm.Page(
    title="CDC PLACES Dash DataTable",
    components=[
        vm.Table(id="table", title="Dash DataTable", figure=dash_data_table(data_frame=df_agg_dent, editable=True)),
    ],
    controls=[
        vm.Parameter(selector=vm.Dropdown(options=[{"label":"True", "value":True},
                                                   {"label":"False", "value":False}],
                                          multi=False,
                                          value=True,
                                          title="Editable Cells"),
                     targets=["table.editable"]),
              ],
)
dashboard = vm.Dashboard(pages=[page])

Vizro().build(dashboard).run()