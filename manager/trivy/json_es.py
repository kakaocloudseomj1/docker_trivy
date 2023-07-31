import json
import requests

# Elasticsearch endpoint and index name
ELASTICSEARCH_URL = "http://211.183.3.100:9200"
INDEX_NAME = input("INDEX_NAME: ")  # Replace with your desired index name

# JSON data file
json_file = "/trivy_results/w2/extracted_data.json"  # Replace with the path to your extracted JSON file

# Read the extracted JSON data from the file
with open(json_file, "r") as file:
    extracted_data = json.load(file)

# Prepare the Elasticsearch bulk request data
bulk_data = ""
for entry in extracted_data:
    action = {
        "index": {
            "_index": INDEX_NAME,
            "_type": "_doc"
        }
    }
    data = json.dumps(entry)
    bulk_data += f"{json.dumps(action)}\n{data}\n"

print(bulk_data)

# Send the data to Elasticsearch using the bulk API
headers = {"Content-Type": "application/json"}
response = requests.post(f"{ELASTICSEARCH_URL}/_bulk", data=bulk_data, headers=headers)

# curl -X POST 'localhost:9200/test/_bulk?pretty' -H 'Content-Type: application/x-ndjson' --data-binary @extracted_data.json
