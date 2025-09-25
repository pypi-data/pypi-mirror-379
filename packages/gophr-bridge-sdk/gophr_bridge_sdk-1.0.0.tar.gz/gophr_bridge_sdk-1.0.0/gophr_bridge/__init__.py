"""
Gophr Bridge SDK for Python
A simple SDK for interacting with the Gophr Bridge API

⚠️  CUSTOMER-ONLY SOFTWARE ⚠️ 
This SDK is proprietary software licensed exclusively to Gophr customers.
Contact sales@gophr.com to become a customer.
"""

from .client import GophrBridge, GophrBridgeError

__version__ = "1.0.3"
__author__ = "Gophr App <engineering@gophr.com>"
__license__ = "Proprietary"

__all__ = ["GophrBridge", "GophrBridgeError"]
