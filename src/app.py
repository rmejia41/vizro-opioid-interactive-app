import pandas as pd
import dash
import vizro.plotly.express as px
from vizro import Vizro
import vizro.models as vm
import statsmodels.api as sm

#df = pd.read_csv('https://github.com/rmejia41/open_datasets/raw/main/SDOH_county_2020.csv')
df = pd.read_csv('https://github.com/rmejia41/open_datasets/raw/main/SDOH_county_2020.csv', encoding='ISO-8859-1') #fixes utf-8 codec can’t decode bytes in position 0-1
df.info()
#print(df.head())

#group by and get aggregated data to display average total dentists
# df_agg_dent = df.groupby(['STATE', 'fips', 'REGION'])[['AHRF_TOT_DENTISTS']].mean()
# df_agg_dent.reset_index(inplace=True)
# print(df_agg_dent[:5])

app = dash.Dash(__name__)
server = app.server

page = vm.Page(
    title="Dashboard: Correlation of US Assault Death Rate, GINI Index, and Opioid Death Rate by US Regions, PLACES, 2020",
    components=[
        vm.Graph(id="scatter_chart", figure=px.scatter(df, x="ACS_GINI_INDEX", y="CDCW_ASSAULT_DTH_RATE", color="REGION", trendline="ols",
                labels={'ACS_GINI_INDEX': "GINI Index", 'CDCW_ASSAULT_DTH_RATE': "Assault Death Rate", 'CDCW_OPIOID_DTH_RATE': "Opioid Death Rate "})),
                           ],
        controls=[
        # use the dropdown to update (target) the x attribute of the scatter chart
        # scatter chart attributes: https://plotly.com/python-api-reference/generated/plotly.express.scatter.html#plotly.express.scatter
        vm.Parameter(selector=vm.Dropdown(options=["ACS_GINI_INDEX", "CDCW_OPIOID_DTH_RATE"], #dropdown options affect heat index of scatter plot
                                          multi=False,
                                          value="ACS_GINI_INDEX",
                                          title="X axis"),
                     targets=["scatter_chart.x"]),
           ],
)

dashboard = vm.Dashboard(pages=[page])

Vizro().build(dashboard).run()

if __name__ == '__main__':
    app.run_server(debug=False)
