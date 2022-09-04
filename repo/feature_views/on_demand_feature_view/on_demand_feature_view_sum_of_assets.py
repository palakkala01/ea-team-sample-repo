from tecton import RequestSource, on_demand_feature_view
from tecton.types import String, Timestamp, Float64, Field, Bool, Array, Int64

request_schema = [Field('assets', String)]
transaction_request = RequestSource(schema=request_schema)
output_schema = [Field('sum_assets', Float64)]

@on_demand_feature_view(
    sources=[transaction_request],
    mode='python',
    schema=output_schema,
    description='on_demand_feature_view_sum_of_assets'
)
def on_demand_feature_view_sum_of_assets(transaction_request):
    from datetime import date 
    import datetime as dt
    import math


    assets = transaction_request['assets']
    assets = assets.replace("[", "")
    assets = assets.replace("]", "")
    assets = assets.replace("\"", "")
    asset_array = assets.split(',')

    sum = 0
    for asset in asset_array:
       asset = int(asset)
       sum = sum + int(asset)

    return {'sum_assets' : float(sum)}
