"""duty.py scaffold — TODO: replace this docstring with what the duty does.

Conventions (enforced by scripts/validate.py):
  - `import bevo` + stdlib only. Never `from bevo import ...` or an alias.
  - Read configuration only from declared `params` via os.environ, with the
    declared defaults.
  - Every bevo.trade(...)/bevo.execute(...) call passes idempotency_key=
    derived from the source event id and bevo.SERVICE_ID.
  - No bare `except: pass`, no subprocess/os.system/eval/exec.

Prefer the TYPED generators — bevo.trades(), bevo.messages(), bevo.transfers(),
bevo.ticks(), bevo.polls(), bevo.webhooks(), bevo.frames() — over the raw
bevo.events(), which is there for a kind they do not cover. `bevo.state` is a
dict that saves itself across restarts, so a duty needs no state file of its
own; the idempotency key is what stops a replayed event acting twice.
"""
import os

import bevo

# TODO: read your declared params with their defaults, e.g.:
# TODO_PARAM = os.environ.get("TODO_PARAM", "default-value")


def main() -> None:
    # TODO: swap bevo.trades() for the generator matching your trigger kind.
    for trade in bevo.trades():
        # One key per SOURCE EVENT, never a timestamp: the pump can replay a
        # row it already handed over after a restart, and the same key answers
        # "already filed" instead of acting a second time.
        key = f"TODO-skill:{bevo.SERVICE_ID}:{trade.id}"

        # TODO: skip what the owner's knobs exclude, returning early — then
        # act: bevo.buy / sell / long / short / close / stock_buy / stock_sell,
        # or bevo.execute for a contract call. Each takes idempotency_key=key.
        bevo.log(f"TODO handling {trade.id} with key {key}")


if __name__ == "__main__":
    main()
