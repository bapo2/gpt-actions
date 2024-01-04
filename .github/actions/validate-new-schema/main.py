# Imports
import os, re, json, yaml, base64
from yamllint.config import YamlLintConfig
from yamllint import linter

# Sets an output variable
def set_var(key, value, file_path):
    encoded_value = base64.b64encode(value.encode()).decode()
    with open(file_path, 'a') as file: file.write(f"{key}={encoded_value}\n")

# The main function
def validate(issue_labels, issue_body):
    # Check if the issue is a new schema
    if "new-schema" not in issue_labels: return issue_body, issue_labels, ""
        
    # Get the title, format, schema, and auth from the issue body
    try:
        body_pattern = r"### 📂 Name\s*\n*(.*?)\n*?\s*### 📰 Short Description\s*\n*(.*?)\n*?\s*### 📜 Format\s*\n*(.*?)\n*?\s*### 📋 Schema\s*\n*```(?:json|yaml|txt)\n([\s\S]*?)\n```(?:\n*?)\s*### 🔑 Authentication\s*\n*(.*?)\n*?\s*### 📝 Description\s*\n*([\s\S]*?)(?=\n*###|$)"
        title, _, format, schema, auth, _ = re.findall(body_pattern, issue_body, re.DOTALL)[0]
        issue_body = issue_body.replace("```txt", f"```{format.lower()}")
    except IndexError: return issue_body, "schema-invalid-issue", "❌ **Automatic validation of new schema failed.** Issue is not formatted correctly."
    
    # Check if the title, format, schema, and auth are valid
    checks = [
        (not title, "schema-invalid-title"),
        (not format or format.lower() not in ["json", "yaml"], "schema-invalid-format"),
        (not schema, "schema-invalid-schema"),
        (not auth or auth not in ['No authentication', 'API Key [Basic]', 'API Key [Bearer]', 'API Key [Other]', 'OAuth [Default]', 'OAuth [Basic auth header]'], "schema-invalid-auth")
    ]
    
    # Return if any of the checks failed
    for check, label in checks:
        if check: return issue_body, label, f"❌ **Automatic validation of new {format.upper()} schema failed.** Check of field {label.replace('schema-invalid-', '').upper()} failed."

    # Check if the schema is valid with a linter
    format = format.lower()
    try:
        if format == "json":
            schema_obj = json.loads(schema)
        elif format == "yaml":
            schema_obj = yaml.safe_load(schema)
            linter.run(schema, YamlLintConfig('extends: default'))
    except: return issue_body, "schema-invalid-schema", f"❌ **Automatic validation of new schema failed.** Schema is not a valid {format.upper()}."
    
    # Check for required properties
    required_properties = ["info", "servers", "paths"]
    if format == "json" or format == "yaml":
        for prop in required_properties:
            if prop not in schema_obj:
                return issue_body, "schema-invalid-schema", f"❌ **Automatic validation of new schema failed.** Schema is missing required property `{prop}`."
        if 'title' not in schema_obj['info'] or 'version' not in schema_obj['info']:
            return issue_body, "schema-invalid-schema", "❌ **Automatic validation of new schema failed.** `info` is missing `title` or `version`."
        if not schema_obj['servers'] or not isinstance(schema_obj['servers'], list) or not schema_obj['servers'][0].get('url'):
            return issue_body, "schema-invalid-schema", "❌ **Automatic validation of new schema failed.** No valid server found in `servers`."
        if not schema_obj['paths'] or not isinstance(schema_obj['paths'], dict) or not list(schema_obj['paths'].keys()):
            return issue_body, "schema-invalid-schema", "❌ **Automatic validation of new schema failed.** No valid path found in `paths`."
    
    # Return if the schema is valid
    return issue_body, "schema-valid", f"✅ **Automatic validation of new {format.upper()} schema succeeded.** Issue is ready for manual review."

# Initialize the main function with the environment variables and run it
def run():
    # Get the environment variables
    env = os.environ
    issue_body, issue_labels = str(env['INPUT_ISSUE_BODY']).replace('\r\n', '\n'), str(env['INPUT_ISSUE_LABELS'].replace('"','').split(','))
        
    # Run the validation routine against the issue body
    new_body, label, comment = validate(issue_labels, issue_body)
    label = f"new-schema,{str(label)}" if label else ",".join(issue_labels)
    
    # Set the output variables
    set_var("issue_body", new_body, env['GITHUB_OUTPUT'])
    set_var("issue_labels", label, env['GITHUB_OUTPUT'])
    set_var("issue_comment", comment, env['GITHUB_OUTPUT'])

# Run the script
if __name__ == '__main__': run()