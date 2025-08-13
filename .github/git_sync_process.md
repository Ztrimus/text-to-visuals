---
title: Atomic Commit Workflow Prompt
description: Guides the user to write atomic, focused commit messages.
tags: [git, workflow, commit, best-practices]
---

#### Input
- Receives file change information and open issues from CLI commands (e.g., `git status`, `git diff`, `gh issue list`).


#### Expected Output
- Executes the workflow to generate modular, atomic commit messages for **all files with active changes**, ensuring every changed file is included in the plan. Each commit should be focused, follow best practices, and match issues where possible.

---


# System Prompt — Atomic Git Push (Modular Commits)


## Purpose
Push **uncommitted** changes to GitHub as **small, single-purpose, reviewable commits**.


**Rules for commits:**
- One commit = one **task**, **fix**, or **feature** only.
- No unrelated changes in the same commit.
- **Every file with active changes must be included in the commit plan.**
- Use **Conventional Commits** style:
```txt
type[optional scope] #ID: short description
```
- If related to a GitHub issue, include `#ID:` at the start of the description (e.g., `FEAT #12: add user profile page`). Use `Closes #ID:` if it fully resolves it, or just `#ID:` if partial.


## Workflow

### 1. Identify Current Changes and Status
```bash
git rev-parse --show-toplevel && git branch --show-current
git diff --name-only
git status --porcelain
```


### 2. Save Full Diff for Planning
- Run the following commands **in this exact order**:
```bash
git diff > temp_git_changes.diff
git diff --staged >> temp_git_changes.diff
for file in $(git ls-files --others --exclude-standard); do
  echo "\n\n" >> temp_git_changes.diff
  git diff --no-index /dev/null "$file" >> temp_git_changes.diff
done
```

### 3. Retrieve GitHub Issues
```bash
gh issue list --state open --limit 200 --json number,title,labels,body > temp_gh_issues.json
```

### 4. Commit Message Format
- Format:
```txt
type[optional scope] #ID: short imperative description
```
- Examples:
	- DOCS #4: update Architecture.md with enhanced tech stack
	- FEAT(api): add POST /reports endpoint
	- REFACTOR(ui): extract Button into shared lib
- Allowed common types:
    - FEAT — new feature
    - FIX — bug fix
    - DOCS — documentation only
    - REFACTOR — code restructuring
    - TEST — tests only
    - CHORE — maintenance
    - BUILD — build system changes
    - CI — CI/CD changes
    - PERF — performance improvements


### 5. Create Modular Commit Plan
- Read `temp_git_changes.diff` and **identify all files with changes**.
- **Group related changes into a single, logical commit** based on their semantic purpose, not just file type or directory.  
  - If multiple files contribute to the same feature, bug fix, or documentation update, they should be in one commit.  
  - Example: Adding two new prompt files for the same feature should result in one commit: `FEAT: add 2 new prompts`, not two separate commits.
- If a single task involves both code and documentation, include both in the same commit.
- **Every changed file must be included** in exactly one commit group — no file should be omitted or appear in multiple commits.
- Deduce a **clear, imperative commit description** based on the purpose of the changes (e.g., “Add”, “Fix”, “Update”), using clues from file names, paths, and diff content.
- For each commit in the plan, match to an issue from `temp_gh_issues.json` if applicable:
  - If related → `#ID: <COMMIT_MESSAGE>`
  - If no match → omit the issue reference.
- Follow **Conventional Commits** for `type` (e.g., `FEAT`, `FIX`, `DOCS`, `REFACTOR`, `TEST`, `CHORE`, `BUILD`, `CI`, `PERF`).
- Output format:
```json
{
  "commits": [
    {
      "type": "FEAT",
      "description": "#2: add user profile page",
      "files": ["profile.html", "profile.css", "profile.js"]
    },
    {
      "type": "DOCS",
      "description": "update Architecture.md with tech stack info",
      "files": ["Architecture.md"]
    },
    {
      "type": "FEAT",
      "description": "add 2 new prompts for onboarding flow",
      "files": ["prompts/welcome.prompt.md", "prompts/help.prompt.md"]
    }
    // ...repeat for all logical commit groups
  ]
}


### 6. Batch Staging and Committing

- For each commit in the plan, generate and execute the following commands:
```sh
git add FILE_1 FILE_2
git commit -m "TYPE #ID: COMMIT_MESSAGE_1"
git add FILE_3
git commit -m "TYPE #ID: COMMIT_MESSAGE_2"
# ...repeat for each modular commit
```
- If you staged too much:
```bash
git reset
```

### 7. Push Changes
```bash
# First push of a new branch
git push -u origin "$(git branch --show-current)"

# Otherwise
git push
```

### 8. Cleanup Temporary Files (Always Do This Last)
```bash
rm -f temp_git_changes.diff temp_gh_issues.json
```


## Notes
- Keep commits small — easier to review and revert.
- If unsure about a command:
```bash
git <command> --help
gh issue --help
# Or
gh issue list --help
```
