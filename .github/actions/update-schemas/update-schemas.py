import os, requests, re, unicodedata, json
from git import Repo, Git
from github import Github

def new_readme_entry(title, author, format, auth, shortdesc, desc, url, schema):
    return f"""
\n<!-- START_SCHEMA: "{title}" -->
<tr><td><details><summary><b>{title}</b> - {shortdesc}</summary><p><ul>
<li><b>Author:</b> <a href="https://github.com/{author}">{author}</a></li>
<li><b>Schema format:</b> {format.upper()}</li>
<li><b>Authentication type:</b> {auth}</li></ul></p>
<p><b>Description:</b><br>
<i>{desc}</i></p>
<p><b>Import URL:</b><br>

```
{url}
```
</p><p><b>Schema:</b>

```{format.lower()}
{schema}
```
</p></details></td></tr>
<!-- END_SCHEMA: "{title}" -->
"""

def run():
    # Set the appropriate environment variables
    token = os.environ['GITHUB_TOKEN']
    repo_path = os.environ['INPUT_REPO_URL']
    repo_url = f"https://{token}@github.com/{repo_path}.git"
    
    # Clone the repo
    repo = Repo.clone_from(repo_url, 'repo')

    # Create a Git command object
    git = Git('repo')

    # Set the GITHUB_TOKEN as the password
    git.config('credential.helper', f'!echo password={token};')
             
    # Get the list of issues to be included
    issue_numbers = os.environ['INPUT_ISSUE_LIST'].replace('"','').replace('#','').split(',')
    
    # From each issue, create a dictionary of the relevant information
    g = Github(os.environ['GITHUB_TOKEN'])
    g_repo = g.get_repo(repo_path)
    issues = []
    for issue in issue_numbers:
        issue = g_repo.get_issue(number=int(issue))
        issues.append({'author': issue.user.login, 'body': issue.body})
    
    # Generate a list of the appropriate information for each issue
    entries = []
    for issue in issues:
        pattern = r"### 📂 Name\s*\n*(.*?)\n*?\s*### 📰 Short Description\s*\n*(.*?)\n*?\s*### 📜 Format\s*\n*(.*?)\n*?\s*### 📋 Schema\s*\n*```json\n([\s\S]*?)\n```(?:\n*?)\s*### 🔑 Authentication\s*\n*(.*?)\n*?\s*### 📝 Description\s*\n*([\s\S]*?)(?=\n*###|$)"
        matches = re.search(pattern, issue['body'], re.DOTALL)
        title, shortdesc, format, schema, auth, desc = matches[0][0], matches[0][1], matches[0][2], matches[0][3], matches[0][4], matches[0][5]
        entries.append({'title': title, 'shortdesc': shortdesc, 'format': format, 'schema': schema, 'auth': auth, 'desc': desc, 'author': issue['author']})
    
    # Create the appropriate folder entries for each issue
    for entry in entries:
        # Slugify the title
        folder_title = unicodedata.normalize('NFKD', entry['title']).encode('ascii', 'ignore').decode('ascii')
        folder_title = re.sub(r'[^\w\s-]', '', folder_title.lower())
        folder_title = re.sub(r'[-\s]+', '-', folder_title).strip('-_')
        
        # Create the folder
        folder_path = os.path.join('repo', 'schemas', folder_title)
        os.mkdir(folder_path)
        
        # Create the schema file
        schema_path = os.path.join(folder_path, f'schema.{entry["format"].lower()}')
        with open(schema_path, 'w') as f:
            f.write(entry['schema'])
        
        # Create the info.json file
        info_path = os.path.join(folder_path, 'info.json')
        with open(info_path, 'w') as f:
            json.dump({'title': entry['title'], 'shortdesc': entry['shortdesc'], 'format': entry['format'], 'auth': entry['auth'], 'desc': entry['desc'], 'author': entry['author']}, f)
        
    # Update the README according to all files in the schemas folder
    readme = os.path.join('repo', '.github', 'README.md')
    readme_text = open(readme, 'r').read()
    readme_text = re.sub(r"(?<=<!-- START_SCHEMA_DIRECTORY -->)(.*?)(?=<!-- END_SCHEMA_DIRECTORY -->)", "", readme_text, flags=re.DOTALL)
    readme_first_half = readme_text.split('<!-- START_SCHEMA_DIRECTORY -->')[0]
    readme_second_half = readme_text.split('<!-- END_SCHEMA_DIRECTORY -->')[1]
    directory = ""
    for folder in os.listdir(os.path.join('repo', 'schemas')):
        if os.path.isdir(os.path.join('repo', 'schemas', folder)):
            info_path = os.path.join('repo', 'schemas', folder, 'info.json')
            with open(info_path, 'r') as f:
                info = json.load(f)
            schema = open(os.path.join('repo', 'schemas', folder, f'schema.{info["format"].lower()}'), 'r').read()
            directory += new_readme_entry(info['title'], info['author'], info['format'], info['auth'], info['shortdesc'], info['desc'], f'https://raw.githubusercontent.com/bapo2/gpt-actions/main/schemas/{folder}/schema.{info["format"].lower()}', schema)
    readme_text = readme_first_half + "<!-- START_SCHEMA_DIRECTORY -->" + directory + "\n<!-- END_SCHEMA_DIRECTORY -->" + readme_second_half
    
    # Update the README
    with open(readme, 'w') as f:
        f.write(readme_text)
    
    # Commit all the changes
    repo.git.add(A=True)
    repo.index.commit('ci(schemas): Add new approved schemas')

    # Check if the update-schemas branch exists
    try:
        update_schemas_branch = repo.create_head('update-schemas')
    except:
        # If it doesn't exist, create it
        update_schemas_branch = repo.create_head('update-schemas', 'main')

    # Switch to the update-schemas branch
    update_schemas_branch.checkout()

    # Push the changes to the update-schemas branch
    repo.git.push('origin', 'update-schemas')

    # Create a pull request using PyGithub
    base = g_repo.get_branch("main")
    head = update_schemas_branch
    g_repo.create_pull(title='ci(schemas): Add new approved schemas', body='This pull request was automatically generated by the update-schemas action.', base=base.name, head=head.name)
    
if __name__ == '__main__':
    run()