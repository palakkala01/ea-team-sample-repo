from tecton import FileConfig, BatchSource



ttori_50_personas_strategies_ds = FileConfig(uri="s3://eddie-vanguard-poc/ea_team_data.csv",
                                    file_format="csv"
                                    )

tori_50_personas_strategies_batch = BatchSource(name="tori_50_personas_strategies_batch", batch_config=ttori_50_personas_strategies_ds)   