"""NCP SDK Tools module.

This module provides the @tool decorator and related functionality for creating
tools that can be used by NCP agents. Tools are functions that agents can call
to perform specific tasks.
"""

from .decorator import tool

__all__ = ["tool"]