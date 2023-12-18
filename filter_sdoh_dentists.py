import pandas as pd
import vizro.plotly.express as px
from vizro import Vizro
import vizro.models as vm

#df = pd.read_csv('C:/Users/Biu9/OneDrive - CDC/Python files/Python Vizro/SDOH_county_2020.csv')
df = pd.read_csv('C:/Users/Biu9/OneDrive - CDC/Python files/Python Vizro/SDOH_county_2020.csv', encoding='ISO-8859-1') #fixes utf-8 codec can’t decode bytes in position 0-1
#df.info()
#print(df.head())

#group by and get aggregated data to display average total dentists
# df_agg_dent = df.groupby(['STATE', 'fips', 'REGION'])[['AHRF_TOT_DENTISTS']].mean()
# df_agg_dent.reset_index(inplace=True)
# print(df_agg_dent[:5])

#vizro app
page = vm.Page(
    title="Dashboard: Total Dentists, US 2020 PLACES",
    components=[
        # components consist of vm.Graph or  vm.Table
        vm.Graph(id="bar_chart", figure=px.bar(df, x="STATE", y="AHRF_TOT_DENTISTS", barmode='overlay')), #points="all", notched=True
        vm.Graph(id="hist_chart", figure=px.histogram(df, x="AHRF_TOT_DENTISTS", color="REGION", marginal = 'box')),
    ],
    controls=[
        # controls consist of vm.Filter or vm.Parameter
        # filter the dataframe (df) of the target graph (histogram), by column sepal_width, using the dropdown
        vm.Filter(column="STATE", selector=vm.Dropdown(), targets=["hist_chart"]),
    ],
)

dashboard = vm.Dashboard(pages=[page])

Vizro().build(dashboard).run(port='8055')