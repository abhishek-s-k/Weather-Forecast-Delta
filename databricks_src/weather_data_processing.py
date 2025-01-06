# Databricks notebook source
spark.conf.set(
    "fs.azure.account.key.weatherforecaststorage.dfs.core.windows.net",
    dbutils.secrets.get(scope="wf_scope", key="ADLS_weather_key"))


# COMMAND ----------

df = spark.read.format('json').load("abfss://weatherforecastcontainer@weatherforecaststorage.dfs.core.windows.net/Visual Crossing API Data")


# COMMAND ----------

df.display()
