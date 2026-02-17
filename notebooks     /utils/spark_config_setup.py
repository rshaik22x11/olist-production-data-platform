def initialize_spark(spark):
    spark.conf.set("spark.sql.shuffle.partitions", "200")
    print("Spark base configuration initialized.")

