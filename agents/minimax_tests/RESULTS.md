# MiniMax API test results

Run on 2026-11-05 from a cloud session with the settings in `agents/minimax.yaml` (default model `MiniMax-M3.1-Flash`, `max_tokens` 2000). The scripts read the key from `MINIMAX_API_KEY`; in cloud sessions the network secret supplies it. To re-run them from the repo root:

```bash
python3 agents/minimax_tests/check_models.py
python3 agents/minimax_tests/check_params.py [model]
python3 agents/minimax_tests/check_effect.py [model] [runs]
```

## Summary

- **Models:** only `MiniMax-M3.1-Flash` and `MiniMax-M3` answer. The seven M2.x models that `/v1/models` still lists return 404 "no longer available".
- **Unknown parameters are silently accepted.** The made-up `foo_bar` went through, so "accepted" does not mean "applied".
- **Enforced:** `top_p` must be in (0, 1], and `n` above 1 is rejected. `top_p` 0 is accepted anyway, probably treated as unset.
- **`stop`:** accepted but ignored; the output ran past the stop text.
- **`temperature`, `top_p`, `seed`:** no measurable effect on either model. Near-zero values still gave a different answer on almost every run, and a fixed seed did not repeat answers.
- **Earlier exploratory run (same day, not scripted):** `MiniMax-M3.1-Flash` gave 4 distinct answers of 5 at temperature 0.01, matching the results below. `MiniMax-M3` repeated one answer 3 times of 4 at temperature 0.01, but the scripted run below did not reproduce that.
- **Small samples:** 4 or 5 runs per setting, so a weak effect could go unseen.

## check_models.py

```
MiniMax-M3.1-Flash       HTTP 200  available
MiniMax-M3               HTTP 200  available
MiniMax-M2.7             HTTP 404  The model "MiniMax-M2.7" is no longer available. (2069)
MiniMax-M2.7-highspeed   HTTP 404  The model "MiniMax-M2.7-highspeed" is no longer available. (2069)
MiniMax-M2.5             HTTP 404  The model "MiniMax-M2.5" is no longer available. (2069)
MiniMax-M2.5-highspeed   HTTP 404  The model "MiniMax-M2.5-highspeed" is no longer available. (2069)
MiniMax-M2.1             HTTP 404  The model "MiniMax-M2.1" is no longer available. (2069)
MiniMax-M2.1-highspeed   HTTP 404  The model "MiniMax-M2.1-highspeed" is no longer available. (2069)
MiniMax-M2               HTTP 404  The model "MiniMax-M2" is no longer available. (2069)
```

## check_params.py (MiniMax-M3.1-Flash)

```
control: made-up foo_bar=1   HTTP 200  accepted -> 'Hi there, friend!'
temperature 0                HTTP 200  accepted -> 'Hi there, friend!'
temperature 2.5              HTTP 200  accepted -> 'Hi there, friend!'
top_p 0                      HTTP 200  accepted -> 'Hi there, friend!'
top_p 0.5                    HTTP 200  accepted -> 'Hi there, friend!'
top_p 1.5                    HTTP 400  invalid params, param 'top_p' should be in (0,1] (2013)
top_k 40                     HTTP 200  accepted -> 'Hi there, friend!'
presence_penalty 0.5         HTTP 200  accepted -> 'Hi there, friend!'
frequency_penalty 0.5        HTTP 200  accepted -> 'Hi there, friend!'
seed 42                      HTTP 200  accepted -> 'Hi there, friend!'
n 2                          HTTP 400  invalid params, model[MiniMax-M3.1-Flash] does not support n > 1 (2013)
stop ['3']                   HTTP 200  accepted -> '1 2 3 4 5'
```

## check_effect.py (MiniMax-M3.1-Flash, 5 runs)

```
temperature 0.01             distinct=5/5  {'Velvet Brew': 1, 'Ember & Oat': 1, 'The Velvet Grind': 1, 'Velvet Pour': 1, 'Brew & Bloom': 1}
temperature 1.0              distinct=5/5  {'The Velvet Grind': 1, 'Velvet Roast': 1, 'Velvet Grind': 1, 'Velvet Pour': 1, 'Velvet Ember Coffee': 1}
temperature 2.0              distinct=5/5  {'Brew Meridian': 1, 'Velour Brew': 1, 'Velvet Ember Coffee': 1, 'The Velvet Pour': 1, 'Copper Kettle Coffee Co.': 1}
top_p 0.01, temperature 1.0  distinct=4/5  {'Velvet Pour': 2, 'Velour & Steam': 1, 'The Copper Kettle': 1, 'Cedar & Steam': 1}
seed 42, temperature 1.0     distinct=5/5  {'Velvet Pour': 1, 'The Steeping Hour': 1, 'The Ember & Oak Café': 1, 'The Steeped Haven': 1, 'The Velvet Grind': 1}
```

## check_effect.py MiniMax-M3 4

```
temperature 0.01             distinct=4/4  {'Brew & Bloom': 1, 'Emberleaf Coffee': 1, 'Sable & Steam Coffee': 1, 'Velvet Grind': 1}
temperature 1.0              distinct=4/4  {'Velvet Ember': 1, 'Ember & Oat': 1, 'Velvet Ember Coffee': 1, 'Velvet Grind': 1}
temperature 2.0              distinct=4/4  {'Velvet Ember Coffee': 1, 'Bean There Coffee Co.': 1, 'Sip & Solstice': 1, 'The Gilded Bean': 1}
top_p 0.01, temperature 1.0  distinct=4/4  {'Velvet Ember': 1, 'Velvet Pour': 1, 'Ember & Oak': 1, 'Velvet Ember Coffee': 1}
seed 42, temperature 1.0     distinct=4/4  {'Ember & Oak': 1, 'Copper & Crema': 1, 'Velvet Ember': 1, 'The Velvet Ember': 1}
```
