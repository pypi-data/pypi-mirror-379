"""
Gophr Bridge SDK for Python
A simple SDK for interacting with the Gophr Bridge API

⚠️  CUSTOMER-ONLY SOFTWARE ⚠️ 
This SDK is proprietary software licensed exclusively to Gophr customers.
Contact sales@gophr.app to become a customer.
"""

from .client import GophrBridge, GophrBridgeError

__version__ = "1.0.10"
__author__ = "Gophr App <engineering@gophr.app>"
__license__ = "Proprietary"

__all__ = ["GophrBridge", "GophrBridgeError"]
