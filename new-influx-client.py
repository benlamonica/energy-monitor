import influxdb_client
from influxdb_client import InfluxDBClient

bucket = "python-client-sandbox"
org = "Energy Monitor"
token = "miQdAvNXHiNDVVzPzV5FpkCaR_8qdQ-L1FlPCOXQPI325Kbrh1fgfhkcDUZ4FepaebDdpZ-A1gmtnnjU0_hViA=="
url = "http://localhost:9999"

client = InfluxDBClient(url=url, token=token, org=org)
writeApi = client.write_api()
write_api.write("my-bucket", "my-org", [{"measurement": "h2o_feet", "tags": {"location": "coyote_creek"}, "fields": {"water_level": 1}, "time": 1}])
