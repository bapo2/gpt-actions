<!-- Header -->
<h1 align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="./header-dark.svg">
        <source media="(prefers-color-scheme: light)" srcset="./header-light.svg">
        <img alt="Repository header" src="./header-dark.svg" height="55">
    </picture>
</h1>
<p align="center">
    <i align="center">Ready-to-use action-schemas for "custom GPTs" via the ChatGPT webapp.</i>
</p>

<!-- Badges -->
<h4 align="center">
    <a href="https://github.com/bapo2/gpt-actions/issues/new?assignees=&labels=new-schema&projects=&template=new_action_template.yml&title=%5BNew+GPT+Action%5D%3A+">
        <img alt="Actions contributed" src="https://img.shields.io/badge/8%20actions%20contributed-ef571d?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48c3ZnIHdpZHRoPSIzNnB4IiBoZWlnaHQ9IjM2cHgiIHN0cm9rZS13aWR0aD0iMiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNvbG9yPSIjZmZmZmZmIj48cGF0aCBkPSJNNiAxMkgxMk0xOCAxMkgxMk0xMiAxMlY2TTEyIDEyVjE4IiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg%2BPC9zdmc%2B">
    </a>
    <a href="https://github.com/bapo2/gpt-actions/issues?q=is%3Aissue+is%3Aopen+label%3Aschema-valid+">
        <img alt="Schemas awaiting approval" src="https://img.shields.io/github/issues/bapo2/gpt-actions/schema-valid?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48c3ZnIHdpZHRoPSIzNnB4IiBoZWlnaHQ9IjM2cHgiIHN0cm9rZS13aWR0aD0iMiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNvbG9yPSIjZmZmZmZmIj48cGF0aCBkPSJNMTMuNSA2TDEwIDE4LjUiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD48cGF0aCBkPSJNNi41IDguNUwzIDEyTDYuNSAxNS41IiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg%2BPHBhdGggZD0iTTE3LjUgOC41TDIxIDEyTDE3LjUgMTUuNSIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI%2BPC9wYXRoPjwvc3ZnPg%3D%3D&label=schemas%20awaiting%20approval&color=21bf1b">
    </a>
    <a href="https://github.com/bapo2/gpt-actions/stargazers">
        <img alt="GitHub stars" src="https://img.shields.io/github/stars/bapo2/gpt-actions?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48c3ZnIHdpZHRoPSIzNnB4IiBoZWlnaHQ9IjM2cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNvbG9yPSIjZmZmZmZmIj48ZyBjbGlwLXBhdGg9InVybCgjY2xpcDBfMzA1N18xNDYyOCkiPjxwYXRoIGQ9Ik05Ljk1MjQyIDkuNjIyNzJMMTEuNTEwOSA2LjMxODE2QzExLjcxMSA1Ljg5Mzk1IDEyLjI4OSA1Ljg5Mzk1IDEyLjQ4OTEgNi4zMTgxNkwxNC4wNDc2IDkuNjIyNzJMMTcuNTMyOSAxMC4xNTU5QzE3Ljk4MDEgMTAuMjI0MyAxOC4xNTgzIDEwLjc5OTYgMTcuODM0NiAxMS4xMjk2TDE1LjMxMyAxMy43MDAxTDE1LjkwODEgMTcuMzMxNEMxNS45ODQ1IDE3Ljc5NzggMTUuNTE2OCAxOC4xNTM0IDE1LjExNjcgMTcuOTMzMUwxMiAxNi4yMTc3TDguODgzMjggMTcuOTMzMUM4LjQ4MzE2IDE4LjE1MzQgOC4wMTU0NSAxNy43OTc4IDguMDkxODcgMTcuMzMxNEw4LjY4Njk1IDEzLjcwMDFMNi4xNjU0NSAxMS4xMjk2QzUuODQxNyAxMC43OTk2IDYuMDE5OTMgMTAuMjI0MyA2LjQ2NzExIDEwLjE1NTlMOS45NTI0MiA5LjYyMjcyWiIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI%2BPC9wYXRoPjxwYXRoIGQ9Ik0yMiAxMkwyMyAxMiIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI%2BPC9wYXRoPjxwYXRoIGQ9Ik0xMiAyVjEiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD48cGF0aCBkPSJNMTIgMjNWMjIiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD48cGF0aCBkPSJNMjAgMjBMMTkgMTkiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD48cGF0aCBkPSJNMjAgNEwxOSA1IiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg%2BPHBhdGggZD0iTTQgMjBMNSAxOSIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI%2BPC9wYXRoPjxwYXRoIGQ9Ik00IDRMNSA1IiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg%2BPHBhdGggZD0iTTEgMTJMMiAxMiIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI%2BPC9wYXRoPjwvZz48ZGVmcz48Y2xpcFBhdGggaWQ9ImNsaXAwXzMwNTdfMTQ2MjgiPjxyZWN0IHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0id2hpdGUiPjwvcmVjdD48L2NsaXBQYXRoPjwvZGVmcz48L3N2Zz4%3D&color=eeaf00">
    </a>
    <a href="https://github.com/bapo2">
        <img alt="GitHub followers" src="https://img.shields.io/github/followers/bapo2?label=follow%20bapo2&style=flat-square&logo=github">
    </a>
<h4>

<!-- Banner -->
<h4 align="center">
    <img alt="Pretty banner thing" src="./banner.png">
</h4>

<!-- Section Links -->
<p align="center">
    <b>
        <a href="#-action-directory">Action Directory</a>
        &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
        <a href="#-what-is-this">What is This?</a>
        &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
        <a href="#-how-to-use">How to Use</a>
        &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
        <a href="#-contributing">Contributing</a>
        &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
        <a href="#-todo">TODO</a>
    </b>
</p>
<br>

<!-- Action Directory -->
<table>
<thead><tr><th width="9999px"><h2 align="center">📁 Action Directory</h2></th></tr></thead>
<tbody><tr></tr>
<!-- START_SCHEMA_DIRECTORY -->
<!-- START_SCHEMA: "APIs.guru Search" -->
<tr></tr><tr><td><details><summary><b>APIs.guru Search</b> - <i>Uses the APIs.guru web service to gather information on publicly-accessible APIs.</i></summary><p><ul>
<li><b>Author:</b> <a href="https://github.com/bapo2">bapo2</a></li>
<li><b>Schema format:</b> JSON</li>
<li><b>Authentication type:</b> No authentication</li></ul></p>
<p><b>Description:</b><br>

Because [@elmstedt](https://github.com/elmstedt) mentioned on the forums that those looking to create API actions should use [apis.guru](https://apis.guru/) (among other resources) for reference in creating schemas, I've decided to write an action that should make this easier by allowing GPT to look for information from this web service all on its own.

This isn't perfect, as some API specs can be quite long and will thus give the `ResponseTooLargeError`, however I have tried to compensate for this by instructing the model to return a link to the appropriate API docs in the event that it cannot parse the spec directly from the site.</p>
<p><b>Import URL:</b><br>

```
https://raw.githubusercontent.com/bapo2/gpt-actions/main/schemas/apisguru-search/schema.json
```
</p><details><summary><b>Schema</b></summary>

```json
{
    "info": {
      "title": "APIs.guru Search",
      "description": "Allows various queries to the apis.guru web service, which enables searching through information on various publically accessible APIs for a wide variety of different use-cases.",
      "version": "v1.0.0"
    },
    "servers": [
      {
        "url": "https://api.apis.guru/v2"
      }
    ],
    "paths": {
      "/providers.json": {
        "get": {
          "description": "Lists all the providers that are available in the apis.guru database.",
          "operationId": "listProviders",
          "deprecated": false
        }
      },
      "/{provider}.json": {
        "get": {
          "description": "Lists all the APIs for a given provider (typically based on the results of the 'listProviders' operation).",
          "operationId": "listProviderAPIs",
          "parameters": [
            {
              "name": "provider",
              "in": "path",
              "description": "The provider string to list the APIs for.",
              "required": true,
              "schema": {
                "type": "string"
              }
            }
          ],
          "deprecated": false
        }
      },
      "/specs/{provider}/{api}/{version}/openapi.json": {
        "get": {
          "description": "Returns the OpenAPI specification for a given API from a given provider (look in the 'swaggerUrl' field of the 'listProviderAPIs' operation for the parameters to use here, which are the last 3 respectively before 'openapi.json').",
          "operationId": "getAPI",
          "parameters": [
            {
              "name": "provider",
              "in": "path",
              "description": "The provider string to list the APIs for (e.g. 'github.com').",
              "required": true,
              "schema": {
                "type": "string"
              }
            },
            {
              "name": "api",
              "in": "path",
              "description": "The API string to get the specification for (e.g. 'api.github.com').",
              "required": true,
              "schema": {
                "type": "string"
              }
            },
            {
                "name": "version",
                "in": "path",
                "description": "The version string to get the specification for (e.g. '1.1.4').",
                "required": true,
                "schema": {
                  "type": "string"
                }
            }
          ],
          "deprecated": false
        }
      }
    },
    "responses": {
        "200": {
            "description": "Successful, continue as normal."
        },
        "ResponseTooLargeError": {
            "description": "If the output is too long to retrieve, inform the user that this is a technical limitation of your system, then attempt to instead give the user a link to the API docs, which can likely be found in previously retrieved data."
        }
    },
    "components": {
      "schemas": {}
    }
}
```
</details></details></td></tr>
<!-- END_SCHEMA: "APIs.guru Search" -->

<!-- START_SCHEMA: "ArXiv Search" -->
<tr></tr><tr><td><details><summary><b>ArXiv Search</b> - <i>A GET-request based search operation for searching through arXiv.</i></summary><p><ul>
<li><b>Author:</b> <a href="https://github.com/bapo2">bapo2</a></li>
<li><b>Schema format:</b> JSON</li>
<li><b>Authentication type:</b> No authentication</li></ul></p>
<p><b>Description:</b><br>

This allows GPT to make requests for entries from [arXiv,](https://arxiv.org/) a free distribution service and an open-access archive for millions of scholarly articles via the `https://export.arxiv.org` endpoint. The specification for said endpoint can be found [here.](https://info.arxiv.org/help/api/index.html)</p>
<p><b>Import URL:</b><br>

```
https://raw.githubusercontent.com/bapo2/gpt-actions/main/schemas/arxiv-search/schema.json
```
</p><details><summary><b>Schema</b></summary>

```json
{
    "info": {
        "title": "ArXiv Search",
        "description": "A GET-request based search operation for searching through arXiv.",
        "version": "v1.0.0"
    },
    "servers": [
        {
            "url": "https://export.arxiv.org"
        }
    ],
    "paths": {
        "/api/query": {
            "get": {
                "description": "Searches through arXiv for the given query.",
                "operationId": "searchArxiv",
                "parameters": [
                    {
                        "name": "search_query",
                        "in": "query",
                        "description": "The query to search for.",
                        "required": true,
                        "schema": {
                            "type": "string"
                        }
                    },
                    {
                        "name": "start",
                        "in": "query",
                        "description": "The index of the first result to return.",
                        "required": false,
                        "schema": {
                            "type": "integer"
                        }
                    },
                    {
                        "name": "max_results",
                        "in": "query",
                        "description": "The maximum number of results to return. Defaults to 10.",
                        "required": false,
                        "schema": {
                            "type": "integer"
                        }
                    },
                    {
                        "name": "sortBy",
                        "in": "query",
                        "description": "The field to sort by.",
                        "required": false,
                        "schema": {
                            "type": "string",
                            "enum": [
                                "relevance",
                                "lastUpdatedDate",
                                "submittedDate"
                            ]
                        }
                    },
                    {
                        "name": "sortOrder",
                        "in": "query",
                        "description": "The order to sort by.",
                        "required": false,
                        "schema": {
                            "type": "string",
                            "enum": [
                                "ascending",
                                "descending"
                            ]
                        }
                    }
                ],
                "deprecated": false
            }
        }
    },
    "components": {
        "schemas": {}
    }
}
```
</details></details></td></tr>
<!-- END_SCHEMA: "ArXiv Search" -->

<!-- START_SCHEMA: "DevDocs Reader" -->
<tr></tr><tr><td><details><summary><b>DevDocs Reader</b> - <i>Allows GPT to read pages from the devdocs.io documentation hub.</i></summary><p><ul>
<li><b>Author:</b> <a href="https://github.com/bapo2">bapo2</a></li>
<li><b>Schema format:</b> YAML</li>
<li><b>Authentication type:</b> No authentication</li></ul></p>
<p><b>Description:</b><br>

This action allows GPT to read entries on DevDocs via `devdocs.io`. Simply provide it with the URL of the entry (e.g. "https://devdocs.io/javascript/global_objects/array/fill") and it will attempt to use a GET request to read the raw HTML of said entry. This is a makeshift implementation because DevDocs provides no official API for reading from its website.

Occasionally, this may return a `ResponseTooLargeError`, which is caused by the response having >100k characters. **This is a limitation of ChatGPT, not of DevDocs, and there's not much I can do about it sadly.**</p>
<p><b>Import URL:</b><br>

```
https://raw.githubusercontent.com/bapo2/gpt-actions/main/schemas/devdocs-reader/schema.yaml
```
</p><details><summary><b>Schema</b></summary>

```yaml
openapi: 3.0.0
info:
  title: DevDocs Reader
  description: >-
    A GET-request based search operation for DevDocs. This is useful, as DevDocs contains a myriad of various documentations for different things. If using this, ask the user about the parameters beforehand. If doing as an intermediary research step, ask the user to go find the URL.
  version: v1.0.0
servers:
  - url: https://documents.devdocs.io
    description: DevDocs Documentation Hub
paths:
  /{doc}/{topic}.html:
    get:
      operationId: readDevDocs
      summary: Fetch Documentation from DevDocs
      description: >-
        Searches for a specific topic and path in DevDocs based on the provided documentation name and topic. This endpoint simulates user navigation on the DevDocs website to retrieve documentation content.
      parameters:
        - name: doc
          in: path
          description: The name of the documentation, such as "vuex~4" or "css". The exact value should be identified by the user.
          required: true
          schema:
            type: string
          example: javascript
        - name: topic
          in: path
          description: The path of the section/topic, such as "guide/actions" for Vuex or "display-box" for CSS.
          required: true
          schema:
            type: string
          example: strings
      responses:
        '200':
          description: Successfully retrieved the documentation content.
        '400':
          description: Bad request, often due to missing or invalid parameters.
        '404':
          description: The specified documentation or topic was not found.
        '429':
          description: Too many requests - rate limiting applied.
components:
  schemas: {}
```
</details></details></td></tr>
<!-- END_SCHEMA: "DevDocs Reader" -->

<!-- START_SCHEMA: "Github File Lister" -->
<tr></tr><tr><td><details><summary><b>Github File Lister</b> - <i>Allows for the traversal of Github repos similar to using the 'ls' command.</i></summary><p><ul>
<li><b>Author:</b> <a href="https://github.com/bapo2">bapo2</a></li>
<li><b>Schema format:</b> JSON</li>
<li><b>Authentication type:</b> API Key [Bearer]</li></ul></p>
<p><b>Description:</b><br>

This allows GPT to use the `api.github.com` endpoint to traverse directories in a repository similar to how one would use the `ls` command. It also allows fetching of a given file's `download_url` to pass to the file reader if both actions are present on the same GPT.

Providing an API key is optional when reading from public repos, but is required when reading from private ones. To create one for GPT to use, simply go to [the "developer settings" page](https://github.com/settings/tokens) and create a PAT with read-access to whatever you want GPT to be able to view.</p>
<p><b>Import URL:</b><br>

```
https://raw.githubusercontent.com/bapo2/gpt-actions/main/schemas/github-file-lister/schema.json
```
</p><details><summary><b>Schema</b></summary>

```json
{
    "info": {
        "title": "Github File Lister",
        "description": "Acts like the 'ls' command and can list the contents of directories on Github repos. Can not be used to read file contents directly, as it will return base64.",
        "version": "v1.0.0"
    },
    "servers": [
        {
            "url": "https://api.github.com"
        }
    ],
    "paths": {
        "/repos/{owner}/{repo}/contents/{path}": {
            "get": {
                "description": "Gets the contents (files) of a specific repo/directory. The 'download_url' property can be used to get the path for the file reader. Make sure to use the 'Github File Reader' action when trying to read contents (if its available).",
                "operationId": "listGithubFiles",
                "parameters": [
                    {
                        "name": "owner",
                        "in": "path",
                        "description": "The owner of the repository (username).",
                        "required": true,
                        "schema": {
                            "type": "string"
                        }
                    },
                    {
                        "name": "repo",
                        "in": "path",
                        "description": "The name of the repository itself.",
                        "required": true,
                        "schema": {
                            "type": "string"
                        }
                    },
                    {
                        "name": "path",
                        "in": "path",
                        "description": "The path to the file or folder (leave this blank to just get the root of the repo). This is case-sensetive.",
                        "required": true,
                        "schema": {
                            "type": "string"
                        }
                    }
                ],
                "deprecated": false
            }
        }
    },
    "components": {
        "schemas": {}
    }
}
```
</details></details></td></tr>
<!-- END_SCHEMA: "Github File Lister" -->

<!-- START_SCHEMA: "Github File Reader" -->
<tr></tr><tr><td><details><summary><b>Github File Reader</b> - <i>Can read files on Github via their "raw" URLs.</i></summary><p><ul>
<li><b>Author:</b> <a href="https://github.com/bapo2">bapo2</a></li>
<li><b>Schema format:</b> JSON</li>
<li><b>Authentication type:</b> API Key [Bearer]</li></ul></p>
<p><b>Description:</b><br>

This allows GPT to read a file from Github via its `raw.githubusercontent.com` URL. When paired with the "Github File Lister" action, this is capable of allowing GPT to look through and read any repository accessible to it.

Providing an API key is optional when reading from public repos, but is required when reading from private ones. To create one for GPT to use, simply go to [the "developer settings" page](https://github.com/settings/tokens) and create a PAT with read-access to whatever you want GPT to be able to view.</p>
<p><b>Import URL:</b><br>

```
https://raw.githubusercontent.com/bapo2/gpt-actions/main/schemas/github-file-reader/schema.json
```
</p><details><summary><b>Schema</b></summary>

```json
{
    "info": {
        "title": "Github File Reader",
        "description": "Request the raw contents of a file from a Github repository given its path.",
        "version": "v1.0.0"
    },
    "servers": [
        {
            "url": "https://raw.githubusercontent.com"
        }
    ],
    "paths": {
        "/{owner}/{repo}/{branch}/{filepath}": {
            "get": {
                "description": "Returns the raw contents of a file from a Github repository given its path. The relevant details can be queried from the 'Github File Lister' action if it is available.",
                "operationId": "readGithubFile",
                "parameters": [
                    {
                        "name": "owner",
                        "in": "path",
                        "description": "The owner of the repository (username).",
                        "required": true,
                        "schema": {
                            "type": "string"
                        }
                    },
                    {
                        "name": "repo",
                        "in": "path",
                        "description": "The name of the repository.",
                        "required": true,
                        "schema": {
                            "type": "string"
                        }
                    },
                    {
                        "name": "branch",
                        "in": "path",
                        "description": "The branch of the repository (this is 'main' by default).",
                        "required": true,
                        "schema": {
                            "type": "string"
                        }
                    },
                    {
                        "name": "filepath",
                        "in": "path",
                        "description": "The path to the file.",
                        "required": true,
                        "schema": {
                            "type": "string"
                        }
                    }
                ],
                "deprecated": false
            }
        }
    },
    "components": {
        "schemas": {}
    }
}
```
</details></details></td></tr>
<!-- END_SCHEMA: "Github File Reader" -->

<!-- START_SCHEMA: "Klarna Product Search" -->
<tr></tr><tr><td><details><summary><b>Klarna Product Search</b> - <i>Find products that match your query</i></summary><p><ul>
<li><b>Author:</b> <a href="https://github.com/sanzgiri">sanzgiri</a></li>
<li><b>Schema format:</b> YAML</li>
<li><b>Authentication type:</b> No authentication</li></ul></p>
<p><b>Description:</b><br>

This is an action for Klarna Product Search. Its primary function is to assist users in finding products that match their queries. It can search for a wide range of products based on specific user requests, including details like product type, brand, price range, and more. Additionally, it has the capability to generate images of these products using DALL-E, providing a visual representation of the items you're interested in. </p>
<p><b>Import URL:</b><br>

```
https://raw.githubusercontent.com/bapo2/gpt-actions/main/schemas/klarna-product-search/schema.yaml
```
</p><details><summary><b>Schema</b></summary>

```yaml
openapi: 3.0.1
servers:
  - url: https://www.klarna.com/us/shopping
info:
  title: Open AI Klarna product Api
  version: v0
  x-apisguru-categories:
    - ecommerce
  x-logo:
    url: https://www.klarna.com/static/img/social-prod-imagery-blinds-beauty-default.jpg
  x-origin:
    - format: openapi
      url: https://www.klarna.com/us/shopping/public/openai/v0/api-docs/
      version: "3.0"
  x-providerName: klarna.com
  x-serviceName: openai
tags:
  - description: Open AI Product Endpoint. Query for products.
    name: open-ai-product-endpoint
paths:
  /public/openai/v0/products:
    get:
      deprecated: false
      operationId: productsUsingGET
      parameters:
        - description: A precise query that matches one very small category or product that needs to be searched for to find the products the user is looking for. If the user explicitly stated what they want, use that as a query. The query is as specific as possible to the product name or category mentioned by the user in its singular form, and don't contain any clarifiers like latest, newest, cheapest, budget, premium, expensive or similar. The query is always taken from the latest topic, if there is a new topic a new query is started.
          in: query
          name: q
          required: true
          schema:
            type: string
        - description: number of products returned
          in: query
          name: size
          required: false
          schema:
            type: integer
        - description: maximum price of the matching product in local currency, filters results
          in: query
          name: budget
          required: false
          schema:
            type: integer
      responses:
        "200":
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ProductResponse"
          description: Products found
        "503":
          description: one or more services are unavailable
      summary: API for fetching Klarna product information
      tags:
        - open-ai-product-endpoint
components:
  schemas:
    Product:
      properties:
        attributes:
          items:
            type: string
          type: array
        name:
          type: string
        price:
          type: string
        url:
          type: string
      title: Product
      type: object
    ProductResponse:
      properties:
        products:
          items:
            $ref: "#/components/schemas/Product"
          type: array
      title: ProductResponse
      type: object
```
</details></details></td></tr>
<!-- END_SCHEMA: "Klarna Product Search" -->

<!-- START_SCHEMA: "Semantic Scholar Search" -->
<tr></tr><tr><td><details><summary><b>Semantic Scholar Search</b> - <i>A GET-request based search operation for papers on Semantic Scholar.</i></summary><p><ul>
<li><b>Author:</b> <a href="https://github.com/bapo2">bapo2</a></li>
<li><b>Schema format:</b> JSON</li>
<li><b>Authentication type:</b> No authentication</li></ul></p>
<p><b>Description:</b><br>

This allows GPT to request entries from Semantic Scholar, which uses a vector space model to find relevant papers based on a query (which can be very helpful for natural language searches). The API specification for Semantic Scholar can be found [here.](https://api.semanticscholar.org/api-docs/)</p>
<p><b>Import URL:</b><br>

```
https://raw.githubusercontent.com/bapo2/gpt-actions/main/schemas/semantic-scholar-search/schema.json
```
</p><details><summary><b>Schema</b></summary>

```json
{
    "info": {
        "title": "Semantic Scholar Search",
        "description": "A GET-request based search operation for papers on Semantic Scholar, which uses a vector space model to find relevant papers based on a query (it can be very helpful for natural language searches).",
        "version": "v1.0.0"
    },
    "servers": [
        {
            "url": "https://api.semanticscholar.org"
        }
    ],
    "paths": {
        "/graph/v1/paper/search": {
            "get": {
                "description": "Relevancy-based search for papers on Semantic Scholar.",
                "operationId": "searchSemanticScholar",
                "parameters": [
                    {
                        "name": "query",
                        "in": "query",
                        "description": "The search query itself, this can be any natural language query.",
                        "required": true,
                        "schema": {
                            "type": "string"
                        }
                    },
                    {
                        "name": "limit",
                        "in": "query",
                        "description": "The maximum number of papers to return. Defaults to 10, maximum is 100.",
                        "required": false,
                        "schema": {
                            "type": "integer"
                        }
                    },
                    {
                        "name": "fields",
                        "in": "query",
                        "description": "The fields to return in the response. Use the pre-specified value for this (don't change it).",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "enum": ["url,abstract,publicationTypes,tldr,openAccessPdf"]
                        }
                    },
                    {
                        "name": "fieldsOfStudy",
                        "in": "query",
                        "description": "The fields of study to filter the results by. These are comma-separated values, e.g. \"Computer Science,Medicine\".",
                        "required": false,
                        "schema": {
                            "type": "string",
                            "enum": [
                                "Computer Science",
                                "Medicine",
                                "Chemistry",
                                "Biology",
                                "Materials Science",
                                "Physics",
                                "Geology",
                                "Psychology",
                                "Art",
                                "History",
                                "Geography",
                                "Sociology",
                                "Business",
                                "Political Science",
                                "Economics",
                                "Philosophy",
                                "Mathematics",
                                "Engineering",
                                "Environmental Science",
                                "Agricultural and Food Sciences",
                                "Education",
                                "Law",
                                "Linguistics"
                            ]
                        }
                    },
                    {
                        "name": "publicationDateOrYear",
                        "in": "query",
                        "description": "The publication date or year to filter the results by (inclusive). Accepts the format <startDate>:<endDate> (YYYY-MM-DD), e.g. 2016-03:2020-06 (as early as March, 2016 or as late as June, 2020).",
                        "required": false,
                        "schema": {
                            "type": "string"
                        }
                    },
                    {
                        "name": "publicationTypes",
                        "in": "query",
                        "description": "The publication types to filter the results by. These are comma-separated values, e.g. \"JournalArticle,CaseReport\".",
                        "required": false,
                        "schema": {
                            "type": "string",
                            "enum": [
                                "Review",
                                "JournalArticle",
                                "CaseReport",
                                "ClinicalTrial",
                                "Dataset",
                                "Editorial",
                                "LettersAndComments",
                                "MetaAnalysis",
                                "News",
                                "Study",
                                "Book",
                                "BookSection"
                            ]
                        }
                    }
                ],
                "deprecated": false
            }
        }
    },
    "components": {
        "schemas": {}
    }
}
```
</details></details></td></tr>
<!-- END_SCHEMA: "Semantic Scholar Search" -->

<!-- START_SCHEMA: "StackExchange Search" -->
<tr></tr><tr><td><details><summary><b>StackExchange Search</b> - <i>A GET-request based search operation for any of several StackExchange boards.</i></summary><p><ul>
<li><b>Author:</b> <a href="https://github.com/bapo2">bapo2</a></li>
<li><b>Schema format:</b> JSON</li>
<li><b>Authentication type:</b> No authentication</li></ul></p>
<p><b>Description:</b><br>

This allows GPT to make several types of queries to any of several StackExchange boards. The documentation for StackExchange's API can be found [here.](https://api.stackexchange.com/) This is useful if GPT happens to run into a development problem that it has difficulty solving, and is a good source of some information in general.</p>
<p><b>Import URL:</b><br>

```
https://raw.githubusercontent.com/bapo2/gpt-actions/main/schemas/stackexchange-search/schema.json
```
</p><details><summary><b>Schema</b></summary>

```json
{
    "info": {
        "title": "StackExchange Search",
        "description": "A GET-request based search operation for any of several StackExchange boards. This is useful as these boards contain vast amounts of useful information to both common and uncommon queries.",
        "version": "v1.0.0"
    },
    "servers": [
        {
            "url": "https://api.stackexchange.com"
        }
    ],
    "paths": {
        "/2.3/search": {
            "get": {
                "description": "Search one of several StackExchange boards based on the provided parameters.",
                "operationId": "searchStack",
                "parameters": [
                    {
                        "name": "intitle",
                        "in": "query",
                        "description": "The query to use for searching.",
                        "required": true,
                        "schema": {
                            "type": "string"
                        }
                    },
                    {
                        "name": "sort",
                        "in": "query",
                        "description": "How to sort the results returned for the query.",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "enum": [
                                "activity",
                                "votes",
                                "creation",
                                "relevance"
                            ]
                        }
                    },
                    {
                        "name": "order",
                        "in": "query",
                        "description": "The order in which to sort the results.",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "enum": [
                                "asc",
                                "desc"
                            ]
                        }
                    },
                    {
                        "name": "site",
                        "in": "query",
                        "description": "The StackExchange site to search.",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "enum": [
                                "stackoverflow",
                                "serverfault",
                                "superuser",
                                "askubuntu",
                                "unix",
                                "cs",
                                "softwareengineering",
                                "codegolf",
                                "codereview",
                                "cstheory",
                                "security",
                                "cryptography",
                                "reverseengineering",
                                "datascience",
                                "devops",
                                "ux",
                                "dba",
                                "gis",
                                "webmasters",
                                "arduino",
                                "raspberrypi",
                                "networkengineering",
                                "iot",
                                "tor",
                                "sqa",
                                "mathoverflow",
                                "math",
                                "mathematica",
                                "dsp",
                                "gamedev",
                                "robotics",
                                "genai",
                                "computergraphics"
                            ]
                        }
                    },
                    {
                        "name": "tagged",
                        "in": "query",
                        "description": "A semicolon-separated list of tags to search for.",
                        "required": false,
                        "schema": {
                            "type": "string"
                        }
                    },
                    {
                        "name": "nottagged",
                        "in": "query",
                        "description": "A semicolon-separated list of tags to exclude from the search.",
                        "required": false,
                        "schema": {
                            "type": "string"
                        }
                    },
                    {
                        "name": "accepted",
                        "in": "query",
                        "description": "Whether or not to search for only accepted answers.",
                        "required": false,
                        "schema": {
                            "type": "boolean"
                        }
                    },
                    {
                        "name": "pagesize",
                        "in": "query",
                        "description": "The number of results to return per page.",
                        "required": false,
                        "schema": {
                            "type": "integer"
                        }
                    }
                ],
                "deprecated": false
            }
        },
        "/2.3/questions/{id}/answers": {
            "get": {
                "description": "Bring up all answers for a given question ID.",
                "operationId": "searchStackAnswers",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "description": "The ID of the question to query.",
                        "required": true,
                        "schema": {
                            "type": "integer"
                        }
                    },
                    {
                        "name": "site",
                        "in": "query",
                        "description": "The StackExchange site to query from.",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "enum": [
                                "stackoverflow",
                                "serverfault",
                                "superuser",
                                "askubuntu",
                                "unix",
                                "cs",
                                "softwareengineering",
                                "codegolf",
                                "codereview",
                                "cstheory",
                                "security",
                                "cryptography",
                                "reverseengineering",
                                "datascience",
                                "devops",
                                "ux",
                                "dba",
                                "gis",
                                "webmasters",
                                "arduino",
                                "raspberrypi",
                                "networkengineering",
                                "iot",
                                "tor",
                                "sqa",
                                "mathoverflow",
                                "math",
                                "mathematica",
                                "dsp",
                                "gamedev",
                                "robotics",
                                "genai",
                                "computergraphics"
                            ]
                        }
                    },
                    {
                        "name": "filter",
                        "in": "query",
                        "description": "This is required in order to actually get the body of the answer.",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "enum": [
                                "!nNPvSNdWme"
                            ]
                        }
                    },
                    {
                        "name": "order",
                        "in": "query",
                        "description": "The order in which to sort the results.",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "enum": [
                                "asc",
                                "desc"
                            ]
                        }
                    },
                    {
                        "name": "sort",
                        "in": "query",
                        "description": "How to sort the results returned for the query.",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "enum": [
                                "activity",
                                "votes",
                                "creation"
                            ]
                        }
                    },
                    {
                        "name": "pagesize",
                        "in": "query",
                        "description": "The number of results to return per page.",
                        "required": false,
                        "schema": {
                            "type": "integer"
                        }
                    },
                    {
                        "name": "page",
                        "in": "query",
                        "description": "The page number to return given the page size.",
                        "required": false,
                        "schema": {
                            "type": "integer"
                        }
                    }
                ],
                "deprecated": false
            }
        },
        "/2.3/answers/{ids}": {
            "get": {
                "description": "Bring up relevant data for one of more answers based on the provided IDs.",
                "operationId": "getStackAnswers",
                "parameters": [
                    {
                        "name": "ids",
                        "in": "path",
                        "description": "A semicolon-separated list of answer IDs to query.",
                        "required": true,
                        "schema": {
                            "type": "string"
                        }
                    },
                    {
                        "name": "order",
                        "in": "query",
                        "description": "The order in which to sort the results.",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "enum": [
                                "asc",
                                "desc"
                            ]
                        }
                    },
                    {
                        "name": "sort",
                        "in": "query",
                        "description": "How to sort the results returned for the query.",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "enum": [
                                "activity",
                                "votes",
                                "creation"
                            ]
                        }
                    },
                    {
                        "name": "site",
                        "in": "query",
                        "description": "The StackExchange site to query from.",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "enum": [
                                "stackoverflow",
                                "serverfault",
                                "superuser",
                                "askubuntu",
                                "unix",
                                "cs",
                                "softwareengineering",
                                "codegolf",
                                "codereview",
                                "cstheory",
                                "security",
                                "cryptography",
                                "reverseengineering",
                                "datascience",
                                "devops",
                                "ux",
                                "dba",
                                "gis",
                                "webmasters",
                                "arduino",
                                "raspberrypi",
                                "networkengineering",
                                "iot",
                                "tor",
                                "sqa",
                                "mathoverflow",
                                "math",
                                "mathematica",
                                "dsp",
                                "gamedev",
                                "robotics",
                                "genai",
                                "computergraphics"
                            ]
                        }
                    },
                    {
                        "name": "filter",
                        "in": "query",
                        "description": "This is required in order to actually get the body of the answer.",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "enum": [
                                "!nNPvSNdWme"
                            ]
                        }
                    }
                ],
                "deprecated": false
            }
        }
    },
    "components": {
        "schemas": {}
    }
}
```
</details></details></td></tr>
<!-- END_SCHEMA: "StackExchange Search" -->
<!-- END_SCHEMA_DIRECTORY -->
</tbody>
</table>

<!-- Description -->
## 🤔 What is This?

This repository is meant as a compendium of action-schemas for [ChatGPT's](https://chat.openai.com/) "custom GPT" feature, which allows users to implement highly customizable API function-calls into their prompt-tuned instances of GPT, letting it perform a wide variety of tasks using request to said APIs. This is accomplished by providing the model with an OpenAPI-spec compliant schema (in either JSON or YAML format) that describes the API call(s) to be made in detail, including the request body, headers, and query parameters, as well as the expected response body and status code (if need be). The model then uses this schema to generate a request to the API, and returns the response body as its output, which it can then use in completions as context for the task being performed.

This feature is extremely powerful, and can be used to perform a wide variety of tasks, from simple things like getting the weather or searching for a video on YouTube, to more complex tasks like creating and managing a GitHub repository programmatically. See the [official ChatGPT docs](https://platform.openai.com/docs/actions) for more information on how this feature works. **In essence, anything accessible via an API can be interacted with by the model using this feature, with virtually no limitations on what can be done.**

In the interest of building a community around this incredibly versatile feature, and to allow for the development of more capable and powerful actions to equip GPT with, I created this repository as a place for users to share their action-schemas publicly, so that others can use them in their own "custom GPTs", and so that they can be improved upon iteratively by the community as a whole. **If you have an action-schema you'd like to share, please consider contributing it to this repository!** See the [contributing](#-contributing) section for more information on how to do so.

<!-- How to Use -->
## 📖 How to Use

<h4 align="center">
    <img alt="How to import actions" width="100%" src="./importing-actions.gif">
</h4>

To use an action from this repository, simply copy the import URL of the action you'd like to use, and **paste it into the "Import from URL" field** in the "Add actions" section of the ChatGPT webapp's "Create a GPT" panel. After this, you can test the action by either prompting the model to use it or by clicking "Test" next to the `path` you wish to test. If the action is working properly, you should see a status indicator that the model is querying the appropriate endpoint, after which it will show if the action was successful or not.

> [!NOTE]
> If you are using an action that requires authentication, you will need to provide the appropriate credentials in the "Authentication" section of the "Add actions" panel. If applicable, the instructions for this will be included in the action's description (if not, please open an issue on this repository requesting that the author add them).

<!-- Contributing -->
## 🤝 Contributing

*If you'd like to contribute an action-schema to this repository, please follow the steps below:*

1. **[Submit a new schema for approval](https://github.com/bapo2/gpt-actions/issues/new?assignees=&labels=new-schema&projects=&template=new_action_template.yml&title=%5BNew+GPT+Action%5D%3A+) by filling out the template provided.** This will aid you in creating a new issue for the schema you wish to contribute, and will ensure that all the necessary information is provided for the schema to be approved and added to the repository.
2. **The schema will be automatically validated by a GitHub workflow,** ensuring that all required information is provided and that the schema is syntactically valid according to what is required by the respective format accepted by the ChatGPT webapp.
3. **If the schema is valid and all required information is provided, it will be marked for manual review.** This is to ensure that the schema is not malicious, otherwise harmful, or breaks any of the rules outlined in the repo's [code of conduct.](./CODE_OF_CONDUCT.md)
4. **Once the schema has manually been reviewed and approved by a repository maintainer, it will be marked for inclusion.** This means that, at the next PR triggered by workflow dispatch, the schema will be added to the repository among the other existing entries. PRs for this repository are structured as batches of all schemas that have been marked for inclusion since the last PR. This is so that the repository is updated in bulk rather than one schema at a time and so that we can keep track of the number of schemas that have been contributed to the repository. **This is done fairly often, so you shouldn't have to wait long for your schema to be added to the repository.**

> [!TIP]
> If the schema is not valid, the workflow will attempt to provide a sufficiently descriptive error message to help you fix the issue, at which point you can simply edit the issue to fix the problem and the workflow will re-run automatically.

*If you'd like to [contribute to the repository](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project) in other ways, such as by improving the documentation, adding new features, or fixing bugs in the workflows, please feel free to submit a PR:*

1. **[Fork the repository.](https://github.com/bapo2/gpt-actions/fork)** This will create a copy of the repository under your own account, which you can then make changes to. You only need to copy the default branch, `main`.
2. **Make the changes you'd like to contribute.** This can be done either directly on GitHub or by cloning the repository to your local machine and making the changes there.
3. **[Submit a pull request.](https://github.com/bapo2/gpt-actions/compare)** This will open a new PR, which will be reviewed by a repository maintainer. If the changes are approved, they will be merged into the repository at an appropriate time as not to conflict with automated workflows.

<!-- TODO -->
## 📝 TODO

This will be updated as new features are added to the repository.

- [ ] Add issue templates for feature requests, reports of invalid schemas, and other presumably common issues.
- [ ] Add a workflow to allow authors to update existing schemas similar to submitting a new ones.
- [ ] Have the PR workflow run on a schedule rather than on workflow dispatch.
- [ ] Add a more elegant means of removing obsolete schemas from the repository.
