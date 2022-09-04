from tecton import FeatureService
from on_demand_feature_view_normalized_age import on_demand_feature_view_normalized_age
from on_demand_feature_view_one_hot_encoded_gender import on_demand_feature_view_one_hot_encoded_gender
from on_demand_feature_view_sum_of_assets import on_demand_feature_view_sum_of_assets
from feature_view_global_age_avg import feature_view_global_age_avg

ea_team_feature_service = FeatureService(
    name='ea_team_feature_service',
    features=[
        on_demand_feature_view_normalized_age,
        on_demand_feature_view_one_hot_encoded_gender,
        on_demand_feature_view_sum_of_assets,
        feature_view_global_age_avg
    ]
)


