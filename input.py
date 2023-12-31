from os import path

import dlt
from pyspark.sql import DataFrame
from pyspark.sql.functions import regexp_replace


@dlt.view
def input():
    csv_path = "dbfs:/data-asset-bundles-dais2023/fe_medium_posts_raw.csv"
    return spark.read.csv(csv_path, header=True)


@dlt.table
def input_clean():
    df: DataFrame = dlt.read("input")
    df = df.filter(df.link != 'null')
    df = df.withColumn("author", regexp_replace("author", "\\([^()]*\\)", ""))
    return df
