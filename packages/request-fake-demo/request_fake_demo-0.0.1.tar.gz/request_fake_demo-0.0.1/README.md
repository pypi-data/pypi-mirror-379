# supplychain-demo

Harmless demo package to show that code inside a dependency can execute at import/install time.
On Linux it writes `/tmp/pwned_supplychain_demo.txt`. On Windows it writes `pwned_supplychain_demo.txt`
in the current directory.

**DO NOT** use on production machines. Run only on isolated VMs/containers or Test PyPI.
