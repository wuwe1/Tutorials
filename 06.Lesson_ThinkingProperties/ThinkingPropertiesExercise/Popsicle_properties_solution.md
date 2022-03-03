1. **Variable transition** - `totalSupply` increase only when `mint` is called and decrease only when `burn` is called.
2. **Variable transition** - `totalFeesEarnedPerShare` increase only and only when `OwnerDoItsJobAndEarnsFeesToItsClients` is called.
3. **Variable transition** - `feesCollectedPerShare` increase only, otherwise user can get more reward than deserved.
4. **High-level** - solvency: sum of balance of all users should not larger than `totalSupply`.
5. **High-level** - solvency: sum of `assetsOf` of all users should not larger than `address(this).balance`.
6. **High-level** - `totalSupply` should be bounded.

## Prioritizing


### High Priority:
- Property 1 is high priority because violation of this rule will lead to funds loss or wrong accounting. 
- Property 2 is high priority because otherwise reward calculation will be messed up.
- Property 3 is high priority because we want user able to claim the deserved amount of reward.
- Property 4, 5 are high priority because violation of this rule will prevent user from getting their ETH.
- Property 6 is high priority because unbounded totalSupply can lead to revert in mint.
