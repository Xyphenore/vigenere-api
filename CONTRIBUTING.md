# Rules to work on the project:

## Commits:

All commits must respect the convention of conventional commit.

A commit needs to have a title.
The title must respect the pattern: 'type: summary' or 'type(scope): summary'.

**All the following is taken from https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13**

### Rules:

- [RULES](conventional_commit_messages.md)
- [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/#summary)

If a type contains **'!'**, the commit introduces a BREAKING CHANGE.<br>
__Example__: feat!(automat): The hub takes a HubProcessing.

### All available scopes :

Directories 'docs' and 'tests' are implicit when use the type 'docs' and 'test'.

#### api:

- api/subscope
    - config
    - vX
    - utils

Example: refactor(api/config): Change signature of Configuration

#### domain:

- domain/subscope
    - models
    - use_cases

Example: refactor(domain/models): Change the model CaesarInput
