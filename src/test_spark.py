from pyspark.sql import SparkSession


def main():
    spark = (
        SparkSession.builder
        .appName("AzureDEPipelineTest")
        .master("local[*]")
        .getOrCreate()
    )

    data = [
        (1, "Customer_A", 500.0),
        (2, "Customer_B", 750.0),
        (3, "Customer_C", 900.0),
    ]

    df = spark.createDataFrame(
        data,
        ["customer_id", "customer_name", "amount"]
    )

    print("\n=== Spark DataFrame ===")
    df.show()

    print("\n=== Spark Schema ===")
    df.printSchema()

    spark.stop()


if __name__ == "__main__":
    main()