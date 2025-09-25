"""
Gophr Bridge SDK Client
A Python implementation of the Gophr Bridge API client

⚠️  CUSTOMER-ONLY SOFTWARE ⚠️ 
This SDK is proprietary software licensed exclusively to Gophr customers.
Valid API credentials and an active customer account are required.
Contact sales@gophr.com to become a customer.
"""

import requests
from typing import Dict, Any, Optional, List, Union
import logging


class GophrBridgeError(Exception):
    """Base exception for Gophr Bridge SDK"""
    
    def __init__(self, message: str, status_code: Optional[int] = None, 
                 details: Optional[Dict[str, Any]] = None, is_network_error: bool = False):
        super().__init__(message)
        self.status_code = status_code
        self.details = details
        self.is_network_error = is_network_error


class GophrBridge:
    """
    Gophr Bridge SDK for Python
    A simple SDK for interacting with the Gophr Bridge API
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the Gophr Bridge SDK
        
        Args:
            config (dict): Configuration dictionary containing:
                - client_id (str): Gophr client ID
                - client_secret (str): Gophr client secret  
                - testing (bool, optional): Use development API when True, production when False (default: True)
        
        Raises:
            ValueError: If required configuration is missing
        """
        if not config.get('client_id') or not config.get('client_secret'):
            raise ValueError("client_id and client_secret are required")
        
        self.client_id = config['client_id']
        self.client_secret = config['client_secret']
        
        # Determine API host based on testing flag
        testing = config.get('testing', True)
        if testing:
            self.host = 'https://dev-api-bridge.gophr.app'
        else:
            self.host = 'https://api-bridge.gophr.app'
        
        # Create requests session with default headers
        self.session = requests.Session()
        self.session.headers.update({
            'client-id': self.client_id,
            'client-secret': self.client_secret,
            'Content-Type': 'application/json'
        })
    
    def get_quote(self, quote_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get a quote for delivery
        
        Args:
            quote_data (dict): Quote request data containing:
                - first_name (str): Customer first name
                - last_name (str): Customer last name
                - phone (str): Customer phone number
                - email (str, optional): Customer email
                - address_1 (str): Delivery address line 1
                - address_2 (str, optional): Delivery address line 2
                - city (str): Delivery city
                - state (str): Delivery state
                - zip (str): Delivery ZIP code
                - country (str, optional): Delivery country (default: 'US')
                - pick_up_instructions (str, optional): Pickup instructions
                - drop_off_instructions (str, optional): Drop-off instructions
                - scheduled_for (str|None, optional): Scheduled delivery date (YYYY-MM-DD format, None for ASAP)
                - items (list): Array of items to be delivered
        
        Returns:
            dict: Quote response with standard and expedited options
            
        Raises:
            GophrBridgeError: If the API request fails
        """
        try:
            response = self.session.post(f"{self.host}/quote", json=quote_data)
            return self._handle_response(response)
        except requests.RequestException as error:
            raise self._handle_error(error)
    
    def create_shipment(self, shipment_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a shipment using a quote ID
        
        Args:
            shipment_data (dict): Shipment creation data containing:
                - quote_id (str): Quote ID from previous quote request
                - drop_off_instructions (str, optional): Drop-off instructions
        
        Returns:
            dict: Shipment creation response
            
        Raises:
            GophrBridgeError: If the API request fails
        """
        try:
            response = self.session.post(f"{self.host}/create", json=shipment_data)
            return self._handle_response(response)
        except requests.RequestException as error:
            raise self._handle_error(error)
    
    def build_quote_data(self, customer_info: Dict[str, str], address_info: Dict[str, str], 
                        items: List[Dict[str, Any]], options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Helper method to build quote data with defaults
        
        Args:
            customer_info (dict): Customer information with keys:
                - first_name (str)
                - last_name (str)
                - phone (str)
                - email (str, optional)
            address_info (dict): Address information with keys:
                - address_1 (str)
                - address_2 (str, optional)
                - city (str)
                - state (str)
                - zip (str)
                - country (str, optional)
            items (list): Items array
            options (dict, optional): Additional options with keys:
                - pickup_instructions (str, optional)
                - dropoff_instructions (str, optional)
                - scheduled_for (str|None, optional)
        
        Returns:
            dict: Formatted quote data
        """
        if options is None:
            options = {}
        
        return {
            'first_name': customer_info['first_name'],
            'last_name': customer_info['last_name'],
            'phone': customer_info['phone'],
            'email': customer_info.get('email', ''),
            'address_1': address_info['address_1'],
            'address_2': address_info.get('address_2', ''),
            'city': address_info['city'],
            'state': address_info['state'],
            'zip': address_info['zip'],
            'country': address_info.get('country', 'US'),
            'pick_up_instructions': options.get('pickup_instructions', ''),
            'drop_off_instructions': options.get('dropoff_instructions', ''),
            'scheduled_for': options.get('scheduled_for'),
            'items': items
        }
    
    # Quote Response Getter Methods
    def get_standard_quote_id(self, quote_response: Dict[str, Any]) -> Optional[str]:
        """Extract standard quote ID from quote response"""
        return quote_response.get('payload', {}).get('standard_quote', {}).get('quote_id')
    
    def get_expedited_quote_id(self, quote_response: Dict[str, Any]) -> Optional[str]:
        """Extract expedited quote ID from quote response"""
        return quote_response.get('payload', {}).get('expedited_quote', {}).get('quote_id')
    
    def get_standard_quote_fee(self, quote_response: Dict[str, Any]) -> Optional[float]:
        """Extract standard quote fee from quote response"""
        return quote_response.get('payload', {}).get('standard_quote', {}).get('fee')
    
    def get_expedited_quote_fee(self, quote_response: Dict[str, Any]) -> Optional[float]:
        """Extract expedited quote fee from quote response"""
        return quote_response.get('payload', {}).get('expedited_quote', {}).get('fee')
    
    # Shipment Response Getter Methods
    def get_delivery_id(self, shipment_response: Dict[str, Any]) -> Optional[Union[str, int]]:
        """Extract delivery ID from shipment response"""
        return shipment_response.get('payload', {}).get('delivery_id')
    
    def get_delivery_status(self, shipment_response: Dict[str, Any]) -> Optional[str]:
        """Extract delivery status from shipment response"""
        return shipment_response.get('payload', {}).get('delivery_status')
    
    def get_shipping_fee(self, shipment_response: Dict[str, Any]) -> Optional[float]:
        """Extract shipping fee from shipment response"""
        return shipment_response.get('payload', {}).get('shipping_fee')
    
    def get_vehicle_type(self, shipment_response: Dict[str, Any]) -> Optional[str]:
        """Extract vehicle type from shipment response"""
        return shipment_response.get('payload', {}).get('vehicle_type')
    
    def get_distance(self, shipment_response: Dict[str, Any]) -> Optional[float]:
        """Extract distance from shipment response"""
        return shipment_response.get('payload', {}).get('distance')
    
    def get_pickup_address(self, shipment_response: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Extract pickup address from shipment response"""
        return shipment_response.get('payload', {}).get('pick_up')
    
    def get_dropoff_address(self, shipment_response: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Extract drop-off address from shipment response"""
        return shipment_response.get('payload', {}).get('drop_off')
    
    def get_shipment_items(self, shipment_response: Dict[str, Any]) -> Optional[List[Dict[str, Any]]]:
        """Extract items array from shipment response"""
        return shipment_response.get('payload', {}).get('items')
    
    def get_shipment_weight(self, shipment_response: Dict[str, Any]) -> Optional[float]:
        """Extract weight from shipment response"""
        return shipment_response.get('payload', {}).get('weight')
    
    def is_expedited(self, shipment_response: Dict[str, Any]) -> Optional[bool]:
        """Check if shipment is expedited"""
        payload = shipment_response.get('payload', {})
        return payload.get('is_expedited') if 'is_expedited' in payload else None
    
    def get_scheduled_for(self, shipment_response: Dict[str, Any]) -> Optional[str]:
        """Extract scheduled_for date from shipment response"""
        return shipment_response.get('payload', {}).get('scheduled_for')
    
    # Payload Getter Methods
    def get_quote_payload(self, quote_response: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Extract full payload from quote response"""
        return quote_response.get('payload')
    
    def get_shipment_payload(self, shipment_response: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Extract full payload from shipment response"""
        return shipment_response.get('payload')
    
    # Utility Methods
    def is_successful(self, response: Dict[str, Any]) -> bool:
        """Check if response is successful"""
        return response.get('status') == 'successful' and response.get('status_code') == 200
    
    def get_quote_summary(self, quote_response: Dict[str, Any]) -> Dict[str, Any]:
        """Get a formatted summary of quote response"""
        if not self.is_successful(quote_response):
            return {
                'success': False,
                'error': quote_response.get('message', 'Unknown error'),
                'status_code': quote_response.get('status_code')
            }
        
        return {
            'success': True,
            'standard': {
                'quote_id': self.get_standard_quote_id(quote_response),
                'fee': self.get_standard_quote_fee(quote_response)
            },
            'expedited': {
                'quote_id': self.get_expedited_quote_id(quote_response),
                'fee': self.get_expedited_quote_fee(quote_response)
            }
        }
    
    def get_shipment_summary(self, shipment_response: Dict[str, Any]) -> Dict[str, Any]:
        """Get a formatted summary of shipment response"""
        if not self.is_successful(shipment_response):
            return {
                'success': False,
                'error': shipment_response.get('message', 'Unknown error'),
                'status_code': shipment_response.get('status_code')
            }
        
        return {
            'success': True,
            'delivery_id': self.get_delivery_id(shipment_response),
            'status': self.get_delivery_status(shipment_response),
            'fee': self.get_shipping_fee(shipment_response),
            'vehicle_type': self.get_vehicle_type(shipment_response),
            'distance': self.get_distance(shipment_response),
            'weight': self.get_shipment_weight(shipment_response),
            'is_expedited': self.is_expedited(shipment_response),
            'scheduled_for': self.get_scheduled_for(shipment_response)
        }
    
    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """Handle API response and extract JSON data"""
        try:
            response.raise_for_status()
            return response.json()
        except requests.HTTPError:
            # Handle HTTP errors
            try:
                error_data = response.json()
                raise GophrBridgeError(
                    message=error_data.get('message', f'HTTP {response.status_code} error'),
                    status_code=response.status_code,
                    details=error_data
                )
            except ValueError:
                # Response is not JSON
                raise GophrBridgeError(
                    message=f'HTTP {response.status_code}: {response.text}',
                    status_code=response.status_code
                )
        except ValueError:
            # JSON decode error
            raise GophrBridgeError(
                message='Invalid JSON response from API',
                status_code=response.status_code
            )
    
    def _handle_error(self, error: requests.RequestException) -> GophrBridgeError:
        """Handle request errors and convert to GophrBridgeError"""
        if isinstance(error, requests.ConnectionError):
            return GophrBridgeError(
                message=f'Connection error: {str(error)}',
                is_network_error=True
            )
        elif isinstance(error, requests.Timeout):
            return GophrBridgeError(
                message=f'Request timeout: {str(error)}',
                is_network_error=True
            )
        else:
            return GophrBridgeError(
                message=f'Request error: {str(error)}',
                is_network_error=True
            )
    
    @staticmethod
    def log_error(error: Exception):
        """Utility method to log errors in a formatted way"""
        if isinstance(error, GophrBridgeError):
            logging.error(f"Gophr Bridge API Error: {error}")
            if error.status_code:
                logging.error(f"Status Code: {error.status_code}")
            if error.details:
                logging.error(f"Details: {error.details}")
            if error.is_network_error:
                logging.error("This appears to be a network-related error")
        else:
            logging.error(f"Error: {error}")
