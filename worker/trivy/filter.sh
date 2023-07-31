sudo apt install -y python3 python3-pip

python3 - << 'EOF'

import json

file_path = "/tmp/result.json"

with open(file_path, 'r') as file:
    data = json.load(file)

extracted_data = []
vulners = data[0]["Vulnerabilities"]  # Correctly access the "Vulnerabilities" list

for vulner in vulners:
    vulnerability_id = vulner["VulnerabilityID"]
    severity = vulner["Severity"]
    extracted_data.append({"VulnerabilityID": vulnerability_id, "Severity": severity})

# Save the extracted data to a new JSON file
output_file = "/trivy_data/extracted_data.json"  # Replace with the desired output file name
with open(output_file, "w") as outfile:
    json.dump(extracted_data, outfile, indent=2)

EOF

