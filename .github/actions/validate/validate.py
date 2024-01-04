import os, re, json
import yaml
from yamllint.config import YamlLintConfig
from yamllint import linter

# Global variables
body = ""
labels = ""
comment = ""

# Function to set output variables
def set_var(key, value):
    print(f"📝 Setting output variable '{key}'...")
    value = value.replace('%', '%25')   # Replace '%' characters with '%25'
    value = value.replace('`', '%60')   # Replace backtick characters with '%60'
    value = value.replace('\n', '%0A')  # Replace newline characters with '%0A'
    value = value.replace('\r', '%0D')  # Replace carriage return characters with '%0D'
    with open(os.getenv('GITHUB_OUTPUT'), 'a') as file:
        file.write(f"{key}={value}\n")

# Function to mark automatic validation as a failure
def fail(fail_label, fail_reason=""):
    global labels, comment
    labels = f"{labels},{fail_label}"
    comment = f"🚫 **Automatic validation failed.**\n\nReason: {fail_reason}"
    complete()

# Function to mark automatic validation as a success
def success(format):
    global labels, comment
    labels = f"{labels},schema-valid"
    comment = f"✅ **Automatic validation of new {format.upper()} schema succeeded.** Issue is ready for manual review."
    complete()

# Function to return the needed output variables and end the workflow
def complete():
    global body, labels, comment
    set_var("issue_body", body)
    set_var("issue_labels", labels)
    set_var("issue_comment", comment)
    print("🏁 Workflow complete.")
    exit(0)

# Main entrypoint
def run():
    print(f"🔍 Beginning validator workflow for issue #{os.environ['INPUT_ISSUE_NUMBER']}...")
    
    # Declare global variables
    global body, labels, comment
    
    # Get the issue text and labels
    issue_body = os.environ['INPUT_ISSUE_BODY']
    body = issue_body
    issue_labels = os.environ['INPUT_ISSUE_LABELS'].replace('"','').split(',')
    labels = ",".join(issue_labels)
    
    # Check if the issue is the correct type
    if "new-schema" not in issue_labels:
        print("🛑 Issue is not a 'new-schema' issue, validation aborted.")
        complete()
    else:
        labels = "new-schema"
        print("✅ Issue is a 'new-schema' issue, extracting parameters...")
            
    # Get the needed parameters from the issue text using regex
    try:
        body_pattern = r"### 📂 Name\s*\n*(.*?)\n*\s*### 📰 Short Description\s*\n*(.*?)\n*\s*### 📜 Format\s*\n*(.*?)\n*\s*### 📋 Schema\s*\n*(.*?)\n*\s*### 🔑 Authentication\s*\n*(.*?)\n*\s*### 📝 Description\s*\n*(.*?)\n*\s*"
        matches = re.findall(body_pattern, issue_body, re.DOTALL)
        title, format, schema, auth = matches[0][0], matches[0][2], matches[0][3], matches[0][4]
    except:
        print("❌ Issue text is invalid, validation failed, running failure procedure...")
        fail("schema-invalid-issue", "Issue text is invalid, meaning that it probably doesn't match the issue template.")
    
    # Check if the title is valid
    if not title or len(title) == 0:
        print("❌ Title is empty, validation failed, running failure procedure...")
        fail("schema-invalid-title", "Title isn't specified.")
    else: print(f"✅ Title is valid: '{title}'.")
    
    # Check if the format is valid
    if not format or len(format) == 0:
        print("❌ Format is empty, validation failed, running failure procedure...")
        fail("schema-invalid-format", "Format isn't specified.")
    else:
        format = format.lower()
        print(f"🟡 Format is specified, validating format...")
        if format not in ["json", "yaml"]:
            print("❌ Format is invalid, validation failed, running failure procedure...")
            fail("schema-invalid-format", "Format is not 'JSON' or 'YAML'.")
        else:
            print(f"✅ Format is valid: '{format}'.")
            body = body.replace('```txt', f'```{format}')
    
    # Lint the schema
    if not schema or len(schema) == 0:
        print("❌ Schema is empty, validation failed, running failure procedure...")
        fail("schema-invalid-schema", "Schema isn't specified.")
    else:
        print(f"🟡 Schema is specified, validating schema...")
        schema = schema.replace('```{format}', '').replace('```txt', '').replace('```', '').strip()
        try:
            if format == "json": json.loads(schema)
            elif format == "yaml": linter.run(schema, YamlLintConfig('extends: default'))
            print(f"✅ Schema is a valid {format.upper()}.")
        except:
            print("❌ Schema is invalid, validation failed, running failure procedure...")
            fail("schema-invalid-schema", f"Schema isn't a valid {format.upper()}.")
            
    # Check if the authentication is valid
    if not auth or len(auth) == 0:
        print("❌ Authentication is empty, validation failed, running failure procedure...")
        fail("schema-invalid-auth", "Authentication isn't specified.")
    else:
        print(f"🟡 Authentication is specified, validating authentication...")
        if auth not in ['No authentication', 'API Key [Basic]', 'API Key [Bearer]', 'API Key [Other]', 'OAuth [Default]', 'OAuth [Basic auth header]']:
            print("❌ Authentication type is invalid, validation failed, running failure procedure...")
            fail("schema-invalid-auth", "Authentication type is invalid.")
        else: print(f"✅ Authentication is valid: '{auth}'.")
    
    # Check if the schema contains the required properties
    if format == "json":
        schema = json.loads(schema)
        print("📜 Checking JSON schema for required properties...")
        
        # Check if the schema contains the required properties
        required_properties = ["info", "servers", "paths"]
        for prop in required_properties:
            if prop not in schema:
                print(f"❌ Schema is missing required property '{prop}', validation failed, running failure procedure...")
                fail("schema-invalid-schema", f"Schema is missing required property `{prop}`.")

        # Check if 'info' contains 'title' and 'version'
        if 'title' not in schema['info'] or 'version' not in schema['info']:
            print("❌ 'info' is missing 'title' or 'version', validation failed, running failure procedure...")
            fail("schema-invalid-schema", "`info` is missing `title` or `version`.")

        # Check if there is at least 1 valid server
        if not schema['servers'] or not isinstance(schema['servers'], list) or not schema['servers'][0].get('url'):
            print("❌ No valid server found, validation failed, running failure procedure...")
            fail("schema-invalid-schema", "No valid server found in `servers`.")

        # Check if there is at least 1 path
        if not schema['paths'] or not isinstance(schema['paths'], dict) or not list(schema['paths'].keys()):
            print("❌ No valid path found, validation failed, running failure procedure...")
            fail("schema-invalid-schema", "No valid path found in `paths`.")
        
        # Successfull validation of JSON schema
        print(f"✅ Schema is a valid JSON and contains all required properties.")
    elif format == "yaml":
        schema = yaml.safe_load(schema)
        print("📜 Checking YAML schema for required properties...")
        required_properties = ["info", "servers", "paths"]
        for prop in required_properties:
            if prop not in schema:
                print(f"❌ Schema is missing required property '{prop}', validation failed, running failure procedure...")
                fail("schema-invalid-schema", f"Schema is missing required property `{prop}`.")

        # Check if 'info' contains 'title' and 'version'
        if 'title' not in schema['info'] or 'version' not in schema['info']:
            print("❌ 'info' is missing 'title' or 'version', validation failed, running failure procedure...")
            fail("schema-invalid-schema", "`info` is missing `title` or `version`.")

        # Check if there is at least 1 valid server
        if not schema['servers'] or not isinstance(schema['servers'], list) or not schema['servers'][0].get('url'):
            print("❌ No valid server found, validation failed, running failure procedure...")
            fail("schema-invalid-schema", "No valid server found in `servers`.")

        # Check if there is at least 1 path
        if not schema['paths'] or not isinstance(schema['paths'], dict) or not list(schema['paths'].keys()):
            print("❌ No valid path found, validation failed, running failure procedure...")
            fail("schema-invalid-schema", "No valid path found in `paths`.")
        
        # Successfull validation of YAML schema
        print(f"✅ Schema is a valid YAML and contains all required properties.")
    
    # Successfull validation of the issue
    success(format)

if __name__ == '__main__': run()