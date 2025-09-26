import os, pandas as pd
from influxdb_client import InfluxDBClient, WritePrecision

from catrxneng.utils.time import Time


class Influx:

    def __init__(self, url, org, bucket, measurement):
        self.url = url
        self.org = org
        self.bucket = bucket
        self.measurement = measurement

    def upload_dataframe(self, dataframe):
        dataframe = dataframe.copy()
        dataframe.set_index("timestamp", inplace=True)
        # dataframe.index.name = "time"  # InfluxDB requires index to be named "time"
        # Ensure step_name is string if present
        # if "step_name" in dataframe.columns:
        #     dataframe["step_name"] = dataframe["step_name"].astype(str)
        # print(f"DataFrame info before upload:")
        # print(dataframe.info())
        # print(f"DataFrame head:")
        # print(dataframe.head())
        # print(f"Index dtype: {dataframe.index.dtype}")
        # print(f"Index name: {dataframe.index.name}")
        # print(f"URL: {self.url}")
        # print(f"Org: {self.org}")
        # print(f"Bucket: {self.bucket}")
        # print(f"Measurement: {self.measurement}")
        
        with InfluxDBClient(
            url=self.url, token=os.getenv("INFLUXDB_TOKEN"), org=self.org
        ) as client:
            # print(f"Client created successfully")
            # Test connection
            # try:
            #     health = client.health()
            #     print(f"InfluxDB health: {health}")
            # except Exception as e:
            #     print(f"Health check failed: {e}")
            
            with client.write_api() as write_api:
                # print(f"Write API created successfully")
                try:
                    write_api.write(
                        bucket=self.bucket,
                        record=dataframe,
                        data_frame_measurement_name=self.measurement,
                        write_precision=WritePrecision.S,
                    )
                    # print("Write call completed")
                    # write_api.flush()
                    # print("Flush completed")
                    # print("Write operation completed without exception")
                except Exception as e:
                    print(f"Write operation failed with exception: {e}")
                    raise

    def generate_query(self, start: Time, end: Time, dt_sec, tags):
        tag_string = ""
        for tag in list(tags.values()):
            tag_string = tag_string + 'r["_field"] == "' + tag + '" or '
        tag_string = tag_string[:-4]
        tag_string = tag_string + ")"

        query_start = (
            start.UTC.strftime("%Y-%m-%d") + "T" + start.UTC.strftime("%H:%M:%S") + "Z"
        )
        query_end = (
            end.UTC.strftime("%Y-%m-%d") + "T" + end.UTC.strftime("%H:%M:%S") + "Z"
        )

        self.query = """
        from(bucket: "BUCKET")
        |> range(start: START, stop: END)
        |> filter(fn: (r) => r["_measurement"] == "MEASUREMENT")
        |> filter(fn: (r) => TAGS
        |> aggregateWindow(every: SECONDSs, fn: last, createEmpty: false)
        |> map(fn: (r) => ({ r with _time: int(v: r._time) / 1000000000}))
        |> keep(columns: ["_time", "_field", "_value"])
        |> yield(name: "last")
        |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
        """

        self.query = self.query.replace("BUCKET", self.bucket)
        self.query = self.query.replace("MEASUREMENT", self.measurement)
        self.query = self.query.replace("START", query_start)
        self.query = self.query.replace("END", query_end)
        self.query = self.query.replace("TAGS", tag_string)
        self.query = self.query.replace("SECONDS", str(int(dt_sec)))

    def request_data(self):
        timeout_min = 5
        with InfluxDBClient(
            url=self.url,
            token=os.getenv("INFLUXDB_TOKEN"),
            org=self.org,
            timeout=timeout_min * 60 * 1000,
        ) as client:
            try:
                self.raw_dataframes = client.query_api().query_data_frame(
                    query=self.query
                )
            except ValueError:
                self.query = self.query.split("|> pivot")[0]
                self.raw_dataframes = client.query_api().query_data_frame(
                    query=self.query
                )

    def format_data(self):
        self.data = pd.concat(self.raw_dataframes, ignore_index=True)
        self.data = self.data[["_time", "_field", "_value"]]
        self.data.rename(
            columns={"_time": "timestamp", "_value": "value"}, inplace=True
        )
        self.data_dict = {
            key: self.data[self.data["_field"] == value][["timestamp", "value"]]
            for key, value in self.tags.items()
        }
        for key, dataset in self.data_dict.items():
            try:
                dataset.loc[:, "value"] = dataset["value"] * self.conf[key].get(
                    "multiplier", 1
                )
                dataset.loc[:, "value"] = dataset["value"] + self.conf[key].get(
                    "add", 0
                )
            except TypeError:
                pass
