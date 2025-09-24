"""
GeneBot Core Module Entry Point
==============================

This allows the genebot.core package to be executed as a module.
Currently redirects to the runner module.
"""

from .runner import main

if __name__ == '__main__':
    main()