#!/usr/bin/python3
"""
Defines regular expression patterns to match secret codes or private keys
"""
# Reserved keywords to match in patterns
_RESERVED_K_ = "SCC_REGCODE|AUTH_TOKEN|password|secret|private|api_key|token|private_key"

# Personal keywords to match in patterns
_PERSONAL_K_ = "email|home_address|sex|race"

# list of regular expression to match secret codes or private keys
__secret_patterns__ = [
  # field desc.: enabled[0/1], pattern[regexp], alert-message[text]
  [0, r'(\s*=\s*)[\"\']RSA-([0-9]+)',
      "potential RSA code"],
  [1, r'(\s*=\s*)[\"\']AES-([0-9]+)',
      "potential AES code"],
  [0, r'\s*(?:my|our)\s*[a-zA-Z_]*[a-zA-Z0-9_]*'+r"("+_RESERVED_K_+")"+r'[a-zA-Z0-9_]*\s*[=]?',
      "variables with potential secret keywords"],
  [1, r'\s*[=]?\s*[a-zA-Z0-9_-]*'+r"("+_RESERVED_K_+")"+r'[a-zA-Z0-9_-]*\s*[=]?',
      "pattern matching potential reserved keywords"],
  [1, r'\s*(?:my|our)\s*[a-zA-Z_]*[a-zA-Z0-9_\.]*'+r"("+_PERSONAL_K_+")"+r'[a-zA-Z0-9_\.]*\s*[=]?',
      "variables with potential privacy-sensible keywords"],
  [1, r'\s*[=]?\s*[\.a-zA-Z0-9_-]*'+r"("+_PERSONAL_K_+")"+r'[\.a-zA-Z0-9_-]*\s*[=]?',
      "pattern matching potential privacy-sensible keywords"],
  [1, r'\s*[=]?[a-zA-Z0-9._%+-]+[@][a-zA-Z0-9._-]+[\.][a-zA-Z]{2,}\s*',
      "pattern matching potential personal email address"],
]
