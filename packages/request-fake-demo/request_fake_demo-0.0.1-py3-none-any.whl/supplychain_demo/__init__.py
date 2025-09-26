# harmless supply-chain demo: runs on import and writes a local marker file
# Purpose: demonstrate that package code can execute on the host during import/install.
import os
import sys
import traceback

WARNING_TEXT = (
    "=== SUPPLY-CHAIN DEMO WARNING ===\n"
    "This is a harmless demo file created by the supplychain-demo package.\n"
    "It demonstrates that code inside a dependency can run on the host.\n"
    "Be careful when installing unverified pip packages. Only install from sources you trust.\n"
)

def _write_marker_file():
    try:
        if os.name == "nt":  # Windows
            path = os.path.join(os.getcwd(), "pwned_supplychain_demo.txt")
        else:  # assume Unix-like
            path = "/tmp/pwned_supplychain_demo.txt"

        # Write the marker file (append if exists)
        with open(path, "a", encoding="utf-8") as f:
            f.write(WARNING_TEXT)
            f.write(f"Created by process: pid={os.getpid()} python={sys.version.split()[0]}\n")
            f.write("-" * 40 + "\n")

        # Also print an explicit message so demo viewers see it during install/import
        print(f"[supplychain-demo] marker file written: {path}")
    except Exception:
        # Do not raise — demo must remain non-destructive and safe.
        print("[supplychain-demo] could not write marker file (permission issue or other).")
        traceback.print_exc(limit=0)

# Run on import
_write_marker_file()
