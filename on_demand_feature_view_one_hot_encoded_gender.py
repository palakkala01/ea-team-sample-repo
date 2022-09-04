from tecton import RequestSource, on_demand_feature_view
from tecton.types import String, Array, Field, Int64

request_schema = [Field('gender', String)]
transaction_request = RequestSource(schema=request_schema)
output_schema = [Field('OneHotEncodingGender', Array(Int64))]

@on_demand_feature_view(
    sources=[transaction_request],
    mode='python',
    schema=output_schema,
    description='One Hot Encoding for a persons gender'
)
def on_demand_feature_view_one_hot_encoded_gender(transaction_request):
    gender = transaction_request['gender']
    if gender == 'M':
       return {'OneHotEncodingGender': [1,0]}
    else:
       return {'OneHotEncodingGender': [0,1]}
