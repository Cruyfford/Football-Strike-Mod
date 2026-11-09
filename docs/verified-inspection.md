# Verified inspection — Football Strike 1.63.2

Input: `com.miniclip.footballstrike-1.63.2-Decrypted.ipa`

| Field | Value |
|---|---|
| IPA size | 118,642,337 bytes |
| ZIP integrity | PASS |
| ZIP entries | 370 |
| Bundle ID | com.miniclip.footballstrike |
| Version/build | 1.63.2 / 1465 |
| Minimum iOS | 15.0 |
| IL2CPP metadata size | 14,643,104 bytes |
| IL2CPP metadata version field | 39 |
| UnityFramework size | 126,782,112 bytes |
| UnityFramework SHA256 | `5a5343149135e43ed02d5d8e9473e8903a7c5317e3b8c09e1c8072dacabccd19` |

## Metadata strings observed
- Shooting: `get_strength`, `set_strength`, `get_last_shot_strength`, `skill_power`, `skill_accuracy`, `skill_curve`, `ball_level`
- Goalkeeper: `goalkeeper_outcome`, `get_goalkeeper_pos`, `get_result_goalkeeper`, `gloves_skill`, `ball_saved`
- Currency and purchases: `get_user_coins`, `set_user_coins`, `purchase_history`, `purchase_product`, `invalid_purchase`

## Interpretation
Metadata strings do not identify native function addresses or prove client-side authority. No local MAX ball stats, unlocks, coin changes, goalkeeper changes, or competitive gameplay changes have been demonstrated.

## Next technical investigation
Map Unity serialized assets and IL2CPP metadata records to actual objects and code paths; assess whether an offline-only training modification is possible.

## Status
**Inspection only. Original IPA unmodified. No patched or signed IPA.**
