# Ops Workspace

Layer 2 stage contract for operations: deploy, monitoring, CI/CD, scripts.

## Inputs

- Layer 4 (working): `../build/` — the built application
- Layer 4 (working): `../planning/` — architecture decisions
- Layer 3 (reference): `../_config/user.md` — user identity and preferences
- Layer 3 (reference): `../_config/project-rules.md` — project-specific constraints
- Layer 3 (reference): `../_config/tool-rules.md` — tool conventions
- Layer 3 (reference): `../instructions/coding-rules.md` — coding conventions

## Process

### Workflow

1. **Read the spec** (tool: read) — Understand what's being deployed from `../planning/` and `../build/`.
2. **Review infra requirements** (tool: read, grep, bash) — Check dependencies, environment vars, and access before touching anything.
3. **Stage the change** (tool: bash, edit) — Prepare scripts, configs, and run logs in a local/staging environment first.
4. **Dry-run** (tool: bash) — Use dry-run flags, `--check`, or `--simulate` modes when available.
5. **Deploy** (tool: bash) — Small, reversible steps. Document every manual action.
6. **Verify** (tool: bash, read) — Confirm the deployment works. Log the result in `../outputs/by-system/`.

### Rules

- **Small, reversible steps.** Never make multiple changes at once. Deploy one change, verify, then proceed.
- **Dry-run before deploy.** Always use dry-run or preview modes before executing destructive operations.
- **Test scripts in isolation.** Run deployment scripts on a non-production environment first.
- **Document manual steps.** If a step can't be automated, write it down so it's repeatable.
- **Never expose secrets.** Don't log, echo, or display credentials, connection strings, or tokens.

## Outputs

- Deployment scripts and configs → this folder
- CI/CD pipeline definitions → this folder
- Run logs and monitoring notes → `../outputs/by-skill/` or `../outputs/by-system/`

## Exit Criteria

An ops task is complete when:
- [ ] Scripts/configs tested in isolation (staging or dry-run)
- [ ] Deployment executed in the correct environment
- [ ] Result verified and logged
- [ ] Manual steps documented if not automatable
- [ ] No secrets exposed in any output or log

## Safety Rules

- **Never run destructive commands without explicit confirmation.** This includes `rm`, `dd`, `mkfs`, `sudo` operations, and any bulk delete.
- **Never expose secrets or credentials in output or logs.** Connection strings, passwords, tokens, API keys — mask or omit them.
- **Prefer dry-run modes when available.** `--dry-run`, `--check`, `--simulate` — use them before the real operation.
- **Prefer `preview_dml` before `execute_dml`** on Oracle. Never run INSERT/UPDATE/DELETE without previewing the affected rows first.

## Conventions

- Name scripts descriptively: `deploy-app.sh`, `backup-db.sh`, `restore-staging.sh`.
- Document required environment variables at the top of each script.
- Keep secrets out of scripts. Use env vars, `.env` files (gitignored), or a secrets manager.
- Log deployment outcomes: `../outputs/by-system/deploy-2026-06-13.log`.

## Common Pitfalls

- **Skipping the dry-run.** The one time you skip it is when it would have caught the mistake.
- **Testing in production.** Use a staging or local environment first. If there is none, say so before deploying.
- **Multiple changes at once.** If something breaks, you won't know which change caused it. One change, verify, next.
- **Secrets in logs.** A single debug log can expose a password. Review output before sharing or storing.
