# Databricks notebook source
spark.conf.set(
    "fs.azure.account.key.weatherforecaststorage.dfs.core.windows.net",
    dbutils.secrets.get(scope="wf_scope", key="ADLS_weather_key"))


# COMMAND ----------

df = spark.read.format('json').load("abfss://weatherforecastcontainer@weatherforecaststorage.dfs.core.windows.net/Visual Crossing API Data")
df.printSchema()

# COMMAND ----------

import pyspark.sql.functions as F

# COMMAND ----------

df_daily_data = df.select("resolvedAddress","address",F.explode("days").alias("days"))
df_daily_data = df_daily_data.select("resolvedAddress","address",F.col("days.datetime").alias("date"),F.explode("days.hours").alias("hours"))
df_daily_data = df_daily_data.select("resolvedAddress","address",F.col("date"), F.col("hours.datetime").alias("hourtime"), F.col("hours.temp").alias("temp"), F.col("hours.conditions").alias("conditions"))
df_daily_data = df_daily_data.withColumn("hourtime", F.substring("hourtime", 0, 2))
df_daily_data.display()
