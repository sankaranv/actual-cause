from actual_cause.definitions import ModifiedHP
from actual_cause.examples import RockThrowing
from actual_cause.inference import HPExhaustiveSearch
from actual_cause.utils import *

env = RockThrowing()
ac_defn = ModifiedHP()
state = {
    "suzy_throws": 1,
    "billy_throws": 1,
    "suzy_hits": 1,
    "billy_hits": 0,
    "bottle_shatters": 1,
}
noise = {"suzy_throws": 1, "billy_throws": 1}
event = {"suzy_throws": 1, "billy_hits": 0}
outcome = {"bottle_shatters": 1}
#
# factual, info = ac_defn.is_factual(env, event, outcome, state, noise)
# print(f"Factual: {factual} Info: {info}")
# sufficient, info = ac_defn.is_sufficient(env, event, outcome, state, noise)
# print(f"Sufficient: {sufficient} Info: {info}")
# necessary, info = ac_defn.is_necessary(env, event, outcome, state, noise)
# print(f"Necessary: {necessary} Info: {info}")
# minimal, info = ac_defn.is_minimal(env, event, outcome, state, noise)
# print(f"Minimal: {minimal} Info: {info}")
# result, info = ac_defn.is_actual_cause(env, event, outcome, state, noise)
# print(f"Actual Cause: {result}! Info: {info}")

print("\n Running solver...\n")

solver = HPExhaustiveSearch(env, ac_defn)
actual_causes = solver.solve(state, outcome, noise)
print(actual_causes.keys())
