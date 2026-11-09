#!/usr/bin/env python3
"""Read-only Unity asset string locator for an iOS IPA. No patching."""
import argparse
import hashlib
import json
import zipfile

NEEDLES = ["mt_GoldenBall", "mt_ElectricShiftBall", "mt_GoldenShiftBall",
           "mt_ball_blue", "mt_ball_red", "mt_ball", "ball_level", "skill_power"]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ipa", help="Path to an IPA you are authorized to inspect")
    parser.add_argument("--output", help="Optional path to save JSON findings")
    args = parser.parse_args()
    results = {"ipa_sha256": None, "asset_hits": []}
    h = hashlib.sha256()
    with open(args.ipa, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    results["ipa_sha256"] = h.hexdigest()
    with zipfile.ZipFile(args.ipa) as z:
        for info in z.infolist():
            if not ("/Data/" in info.filename and info.filename.endswith(".assets")):
                continue
            raw = z.read(info)
            matches = []
            for needle in NEEDLES:
                pattern = needle.encode("ascii")
                start = 0
                while (offset := raw.find(pattern, start)) >= 0:
                    matches.append({"name": needle, "offset": offset})
                    start = offset + len(pattern)
            if matches:
                results["asset_hits"].append({"asset": info.filename, "size": len(raw), "matches": matches})
    output = json.dumps(results, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output + "\n")
    print(output)

if __name__ == "__main__":
    main()
