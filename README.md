# butler-skill-template

Start here to build a Butler skill. Click **Use this template** on GitHub (or
`gh repo create <you>/butler-skill-<name> --template Virtual-Protocol/butler-skill-template --public`),
then hand your Claude the hub README and the task:

> Read https://github.com/Virtual-Protocol/butler-skills/blob/main/README.md — now build this skill: …

The files here are the scaffold the hub's validator expects: `SKILL.md` (every
section and `[FIXED]`/`[ADAPT]` marker pre-filled with a `TODO` the validator
rejects), `duty.py`, `CHANGELOG.md`, and a CI workflow that runs the hub's
validator and the offline replay on every push.

When it validates: tag `v1.0.0`, then open a PR to
[Virtual-Protocol/butler-skills](https://github.com/Virtual-Protocol/butler-skills)
adding your repo as a submodule under `skills/<name>` at that tag. Maintainers
review the pinned commit; Butler containers clone exactly that commit.
