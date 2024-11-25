#!/usr/bin/python3

# Defines a regular expression pattern to match secret codes or private keys
__secret_patterns__ = [
    # enabled, pattern, print-message
    [0, r'(\s*=\s*)[\"\']RSA-([0-9]+)',
        "potential RSA code"],
    [1, r'(\s*=\s*)[\'\"]AES-([0-9]+)',
        "potential AES code"],
    [1, r'\s*(?:my|our)\s*[a-zA-Z_]*[a-zA-Z0-9_]*(SCC_REGCODE|AUTH_TOKEN|passwd|password|secret|private|api_key|token|ssh_private_key)[a-zA-Z0-9_]*\s*[=]?',
        "variables with potential secret keywords"],
    [1, r'\s*[=]?\s*[a-zA-Z0-9_-]*(SCC_REGCODE|AUTH_TOKEN|passwd|password|secret|private|api_key|token|ssh_private_key)[a-zA-Z0-9_-]*\s*[=]?',
        "pattern matching potential reserved keywords"],
    [1, r'\s*(?:my|our)\s*[a-zA-Z_]*[a-zA-Z0-9_\.]*(email|home_address)[a-zA-Z0-9_\.]*\s*[=]?', 
        "variables with potential privacy-sensible keywords"],
    [1, r'\s*[=]?\s*[\.a-zA-Z0-9_-]*(email|home_address)[\.a-zA-Z0-9_-]*\s*[=]?', 
        "pattern matching potential privacy-sensible keywords"],
    [1, r'\s*[=]?[a-zA-Z0-9._%+-]+[@][a-zA-Z0-9._-]+[\.][a-zA-Z]{2,}\s*', 
        "pattern matching potential personal email address"],
]
