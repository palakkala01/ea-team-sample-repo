from tecton import RequestSource, on_demand_feature_view
from tecton.types import String, Timestamp, Float64, Field, Bool, Array, Int64
from feature_view_global_age_avg import feature_view_global_age_avg

request_schema = [Field('dob', String)]
transaction_request = RequestSource(schema=request_schema)
output_schema = [Field('age', Float64), Field('normalized_age', Float64)]

@on_demand_feature_view(
    sources=[transaction_request, feature_view_global_age_avg],
    mode='python',
    schema=output_schema,
    description='One Hot Encoding for a persons gender'
)
def on_demand_feature_view_normalized_age(transaction_request, feature_view_global_age_avg):
    from datetime import date 
    import datetime as dt
    import math


    dob = transaction_request['dob']

    d = dt.datetime.strptime(dob, "%m-%d-%Y")
    d = d.date()

    dob_year = d.year 
    dob_month = d.month 
    dob_day = d.day 

    today = date.today()
    age = today.year - dob_year - ((today.month, today.day) < (dob_month, dob_day))

    avg_investor_age = feature_view_global_age_avg['avg_investor_age']
    
    sqrt_of_avg = math.sqrt(avg_investor_age)

    normalized_age = age - (avg_investor_age / sqrt_of_avg)

    return {'age' : float(age), 'normalized_age': float(normalized_age)}

