"""
External API Caller - XAC

A utility package for making external API calls with comprehensive logging.
"""

from .api_caller import ExternalAPICaller, make_external_api_request

__version__ = "1.0.0"
__author__ = "Ayush Sonar"
__all__ = ["ExternalAPICaller", "make_external_api_request"]
