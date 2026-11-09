# Football Strike 1.63.2 — Local Analysis

This repository contains **analysis notes and tooling**, not the original game or a modified IPA.

## Verified input
- Bundle ID: `com.miniclip.footballstrike`
- App version: `1.63.2` (build `1465`)
- iOS minimum: `15.0`
- Unity IL2CPP, ARM64
- IPA ZIP integrity: PASS
- IL2CPP metadata version field: `39`

## Current status
Static inspection identified metadata strings related to ball level, shooting power, accuracy, curve, goalkeeper outcomes, and coins. These are **string references only**. They do not prove the corresponding values can be changed locally or that they control server-side gameplay.

**No game binary has been patched. No modified IPA has been produced or tested.**

## Scope
Research and test local, offline, noncompetitive game resources and training behavior where technically possible. Do not include copyrighted game binaries, credentials, signing keys, or methods for altering server-managed currency/purchases or competitive results.

## Workflow
1. Preserve the original IPA and record checksums.
2. Inventory Unity assets and metadata.
3. Identify actual asset objects and relevant native code, not just names.
4. Validate any proposed offline-only changes in an isolated test.
5. Record results and limitations before packaging.
