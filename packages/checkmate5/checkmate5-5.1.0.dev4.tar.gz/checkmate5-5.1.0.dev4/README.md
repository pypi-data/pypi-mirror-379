
# Welcome to Checkmate!


This is a modified version of original Checkmate.

Original author(s), license(s), acknowelegement(s): https://github.com/quantifiedcode/checkmate


## About
Checkmate is a cross-language (meta-)tool for static code analysis, written in Python. Unlike other tools, it provides a global overview of the code quality in a project and aims to provide clear, actionable insights to the user.


## Licences

* Checkmate is licensed under the MIT license. To view a copy of this license, visit [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT).

* Original Checkmate's parts remain release under MIT License. However modifications are finally released under AGPL-3.0 license (previously LGPL 2.1 with Commons Clause). Please refer to LICENSE for more info. 


# Description

This guide explains how to configure the backend parameter for Checkmate5 (SQLite/Postgres), details the role and usage of the `pk` ("primary key") parameter, and describes how "snapshots" are used to associate findings with file hashes in project history.

---

## 1. Backend Configuration

Checkmate5 supports multiple backend drivers, notably `sqlite` and `sql` (typically PostgreSQL, but could be any SQLAlchemy-supported SQL database).

### How to Specify the Backend

You can specify the backend when initializing a new project or via configuration files:

#### CLI Options
- `--backend`: The backend to use. Choices:
  - `"sql"` (default): Use a SQL database (e.g., PostgreSQL, MySQL)
  - `"sqlite"`: Use SQLite
- `--backend-opts`: Connection string for SQL databases or file path for SQLite
- `--path`: Directory for the project
- `--pk`: Set the project's primary key (see next section)

#### Example CLI Usage
```bash
checkmate init --backend sql --backend-opts "postgresql://user:password@localhost/dbname" --pk myproject123
checkmate init --backend sqlite --backend-opts "sqlite:///path/to/db.sqlite"
```

#### Configuration Structure Example (`.checkmate/config.json`)
```json
{
  "project_id": "myproject123",
  "project_class": "Project",
  "backend": {
    "driver": "sqlite",
    "connection_string": "sqlite:///myproject.db"
  }
}
```

### Backend Parameters

- **driver**: `"sql"` or `"sqlite"`
- **connection_string**: SQLAlchemy-compatible connection string (e.g., `"postgresql://user:pass@host/db"` or `"sqlite:///file.db"`)

### Backend Usage and Methods
- Backend is used to store and retrieve project data and scan results.
- Database connections are tested at initialization.
- Transactions are handled using context managers.
- Database connections can be closed and disposed when finished.

---

## 2. PK-Key (`pk` parameter): Project Primary Key

The `pk` parameter allows you to specify a custom primary key for your project, which is stored as `project_id` in the configuration file.

### Why Use `pk`?
- **Custom Identification**: Set a meaningful or recognizable ID for your project (e.g., `myproject123`).
- **Deterministic Reference**: Ensures you can reference your project by a known key in subsequent commands or queries.
- **Multi-project Management**: Useful for managing multiple projects in the same backend.

### How `pk` is Used

- If you supply `--pk` during initialization, it will be used as your project's primary key.
- If not supplied, a random UUID is generated.
- The `pk`/`project_id` identifies your project for all backend operations and links snapshots, file revisions, and findings to your project.

#### Example Configuration (`.checkmate/config.json`)
```json
{
  "project_id": "myproject123",
  "project_class": "Project",
  "backend": { ... }
}
```

---

## 3. Snapshots: Scanning and Findings by File Hashes in History

### What is a Snapshot?

A **Snapshot** captures the state of your project at a specific commit or point in time. It records:
- The file revisions (with hashes)
- The results of analyzers (issues found)
- The project configuration

### How Snapshots are Created

- When running analysis (e.g., `checkmate analyze`), Checkmate5 creates a Snapshot for the current state.
- Snapshots are linked to specific commits (for Git projects) and store the hashes of all analyzed files.
- The system checks if a file revision with the same hash already exists; if so, it can reuse previous analysis results.

### How Findings Are Associated by File Hash

- **FileRevision** objects are created for each file at each commit; their content is hashed.
- If a file's hash matches a previously analyzed revision, its findings can be reused.
- Issues found by analyzers are hashed with details to ensure uniqueness and allow deduplication.

#### Hash-based File Finding

- Each file revision gets a hash based on its content and path.
- If package databases are involved, a random string may be added to force re-scan.

#### Analysis Workflow

1. **Collect file revisions and their hashes**
2. **Chunk queries to backend to find previously scanned hashes**
3. **Reuse findings for unchanged files**
4. **Only analyze new or changed file revisions**
5. **Save findings and link them to the snapshot**

#### Diffing Snapshots

Checkmate can compare ("diff") snapshots to show what changed between two states:
- Which files were added, deleted, or modified
- Which issues were added or resolved

---

## Summary Table

| Parameter        | Description                                     | Example Value                    |
|------------------|------------------------------------------------|----------------------------------|
| `driver`         | Backend type                                   | "sqlite" or "sql"                |
| `connection_string` | SQLAlchemy DB connection string              | "sqlite:///db.sqlite"            |
|                  |                                                | "postgresql://user:pass@host/db" |
| `pk`             | Primary key for identifying the project         | "myproject123"                   |
| `project_id`     | Alias in config for pk, used in backend         | "myproject123"                   |

| Snapshot Concept | Description                                   |
|------------------|-----------------------------------------------|
| FileRevision     | Represents a file at a specific commit        |
| hash             | SHA-based hash of file contents               |
| Snapshot         | State of project at a commit; list of hashes  |
| Issue            | Findings from analyzers, linked to hashes     |

---

## Further Reading

- Backend Implementation: checkmate/lib/backend.py
- Snapshot & Analysis Logic: checkmate/lib/code/environment.py
- Git Integration & Snapshots: checkmate/contrib/plugins/git/models.py
