# Asset string inventory — Football Strike 1.63.2

This is a **read-only byte-string search**, not a Unity object decoder or a gameplay patch.

Original IPA SHA256: `3c32da95e2332b14f9e5aac4f783a33adec879f4ac1b72ca7704f4c2e1c120ac`

| Unity asset | String | Byte offset (decimal) |
|---|---|---:|
| sharedassets1.assets | mt_GoldenBall | 652484 |
| sharedassets1.assets | mt_ElectricShiftBall | 692356 |
| sharedassets1.assets | mt_GoldenShiftBall | 704932 |
| sharedassets1.assets | mt_ball_blue | 653556 |
| sharedassets1.assets | mt_ball_red | 654308 |
| sharedassets0.assets | ball_level | 2109488 |

Additional `ball_level` occurrences were detected in `sharedassets0.assets`; run the script for the full list.

Run locally:

```sh
python3 tools/inspect_unity_assets.py footballstrike.ipa --output inventory.json
```

## Important limitations

String locations are not validated serialized Unity object IDs or numeric stat values. No unlock, MAX power, coin modification, or goalkeeper behavior change has been implemented or tested. The original IPA is unchanged.
