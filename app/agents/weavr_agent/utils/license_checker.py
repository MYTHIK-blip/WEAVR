SAFE_LICENSES = [
    "MIT",
    "Apache-2.0",
    "Apache 2.0",
    "Apache License 2.0",
    "Unlicense",
    "BSD-3-Clause"
]

RESTRICTED_LICENSES = [
    "GPL-3.0",
    "GPL-2.0",
    "LGPL",
    "AGPL",
    "Proprietary",
    "Commercial"
]

def classify_license(license_name):
    """
    Classify a license as safe, restricted, or unknown.
    """
    if not license_name:
        return "unknown"

    normalized = license_name.strip().lower()

    for safe in SAFE_LICENSES:
        if safe.lower() in normalized:
            return "safe"

    for restricted in RESTRICTED_LICENSES:
        if restricted.lower() in normalized:
            return "restricted"

    return "unknown"
