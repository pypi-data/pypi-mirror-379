"""
Unit tests for the Gophr Bridge SDK
"""

import pytest
import responses
import json
from unittest.mock import patch
from gophr_bridge import GophrBridge, GophrBridgeError


class TestGophrBridge:
    """Test cases for the GophrBridge class"""
    
    def test_init_with_valid_config(self):
        """Test initialization with valid configuration"""
        config = {
            'client_id': 'test_client_id',
            'client_secret': 'test_client_secret',
            'testing': True
        }
        gophr = GophrBridge(config)
        
        assert gophr.client_id == 'test_client_id'
        assert gophr.client_secret == 'test_client_secret'
        assert gophr.host == 'https://dev-api-bridge.gophr.app'
        assert gophr.session.headers['client-id'] == 'test_client_id'
        assert gophr.session.headers['client-secret'] == 'test_client_secret'
    
    def test_init_production_host(self):
        """Test initialization with production configuration"""
        config = {
            'client_id': 'test_client_id',
            'client_secret': 'test_client_secret',
            'testing': False
        }
        gophr = GophrBridge(config)
        assert gophr.host == 'https://api-bridge.gophr.app'
    
    def test_init_missing_client_id(self):
        """Test initialization fails without client_id"""
        config = {
            'client_secret': 'test_client_secret'
        }
        with pytest.raises(ValueError, match="client_id and client_secret are required"):
            GophrBridge(config)
    
    def test_init_missing_client_secret(self):
        """Test initialization fails without client_secret"""
        config = {
            'client_id': 'test_client_id'
        }
        with pytest.raises(ValueError, match="client_id and client_secret are required"):
            GophrBridge(config)
    
    @responses.activate
    def test_get_quote_success(self):
        """Test successful quote request"""
        config = {
            'client_id': 'test_client_id',
            'client_secret': 'test_client_secret'
        }
        gophr = GophrBridge(config)
        
        # Mock successful response
        mock_response = {
            'status': 'successful',
            'status_code': 200,
            'payload': {
                'standard_quote': {
                    'quote_id': 'std_123',
                    'fee': 15.50
                },
                'expedited_quote': {
                    'quote_id': 'exp_123',
                    'fee': 25.00
                }
            }
        }
        
        responses.add(
            responses.POST,
            'https://dev-api-bridge.gophr.app/quote',
            json=mock_response,
            status=200
        )
        
        quote_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '5555551234',
            'address_1': '123 Main St',
            'city': 'New York',
            'state': 'NY',
            'zip': '10001',
            'items': [{'quantity': 1, 'name': 'Test Item', 'weight': 1}]
        }
        
        result = gophr.get_quote(quote_data)
        
        assert result == mock_response
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == 'https://dev-api-bridge.gophr.app/quote'
    
    @responses.activate
    def test_get_quote_http_error(self):
        """Test quote request with HTTP error"""
        config = {
            'client_id': 'test_client_id',
            'client_secret': 'test_client_secret'
        }
        gophr = GophrBridge(config)
        
        # Mock error response
        error_response = {
            'status': 'error',
            'message': 'Bad request',
            'status_code': 400
        }
        
        responses.add(
            responses.POST,
            'https://dev-api-bridge.gophr.app/quote',
            json=error_response,
            status=400
        )
        
        quote_data = {
            'first_name': 'John',
            'last_name': 'Doe'
        }
        
        with pytest.raises(GophrBridgeError) as exc_info:
            gophr.get_quote(quote_data)
        
        assert exc_info.value.status_code == 400
        assert 'Bad request' in str(exc_info.value)
    
    @responses.activate
    def test_create_shipment_success(self):
        """Test successful shipment creation"""
        config = {
            'client_id': 'test_client_id',
            'client_secret': 'test_client_secret'
        }
        gophr = GophrBridge(config)
        
        # Mock successful response
        mock_response = {
            'status': 'successful',
            'status_code': 200,
            'payload': {
                'delivery_id': 'DEL_123456',
                'delivery_status': 'confirmed',
                'shipping_fee': 15.50,
                'vehicle_type': 'car',
                'distance': 5.2,
                'weight': 2.5,
                'is_expedited': False,
                'scheduled_for': None,
                'pick_up': {
                    'address': '123 Pickup St',
                    'city': 'Pickup City'
                },
                'drop_off': {
                    'address': '456 Dropoff Ave',
                    'city': 'Dropoff City'
                },
                'items': [
                    {'quantity': 1, 'name': 'Test Item', 'weight': 2.5}
                ]
            }
        }
        
        responses.add(
            responses.POST,
            'https://dev-api-bridge.gophr.app/create',
            json=mock_response,
            status=200
        )
        
        shipment_data = {
            'quote_id': 'std_123',
            'drop_off_instructions': 'Ring doorbell'
        }
        
        result = gophr.create_shipment(shipment_data)
        
        assert result == mock_response
        assert len(responses.calls) == 1
    
    def test_build_quote_data(self):
        """Test build_quote_data helper method"""
        config = {
            'client_id': 'test_client_id',
            'client_secret': 'test_client_secret'
        }
        gophr = GophrBridge(config)
        
        customer_info = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'phone': '5555559876',
            'email': 'jane@example.com'
        }
        
        address_info = {
            'address_1': '456 Oak St',
            'address_2': 'Apt 2B',
            'city': 'Los Angeles',
            'state': 'CA',
            'zip': '90210',
            'country': 'US'
        }
        
        items = [
            {'quantity': 1, 'name': 'Laptop', 'weight': 3}
        ]
        
        options = {
            'pickup_instructions': 'Call first',
            'dropoff_instructions': 'Leave with doorman',
            'scheduled_for': '2025-09-25'
        }
        
        result = gophr.build_quote_data(customer_info, address_info, items, options)
        
        expected = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'phone': '5555559876',
            'email': 'jane@example.com',
            'address_1': '456 Oak St',
            'address_2': 'Apt 2B',
            'city': 'Los Angeles',
            'state': 'CA',
            'zip': '90210',
            'country': 'US',
            'pick_up_instructions': 'Call first',
            'drop_off_instructions': 'Leave with doorman',
            'scheduled_for': '2025-09-25',
            'items': [{'quantity': 1, 'name': 'Laptop', 'weight': 3}]
        }
        
        assert result == expected
    
    def test_build_quote_data_with_defaults(self):
        """Test build_quote_data with default values"""
        config = {
            'client_id': 'test_client_id',
            'client_secret': 'test_client_secret'
        }
        gophr = GophrBridge(config)
        
        customer_info = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '5555551234'
        }
        
        address_info = {
            'address_1': '123 Main St',
            'city': 'New York',
            'state': 'NY',
            'zip': '10001'
        }
        
        items = [{'quantity': 1, 'name': 'Package', 'weight': 1}]
        
        result = gophr.build_quote_data(customer_info, address_info, items)
        
        assert result['email'] == ''
        assert result['address_2'] == ''
        assert result['country'] == 'US'
        assert result['pick_up_instructions'] == ''
        assert result['drop_off_instructions'] == ''
        assert result['scheduled_for'] is None


class TestGetterMethods:
    """Test cases for getter methods"""
    
    def setup_method(self):
        """Set up test instance"""
        config = {
            'client_id': 'test_client_id',
            'client_secret': 'test_client_secret'
        }
        self.gophr = GophrBridge(config)
    
    def test_quote_getters(self):
        """Test quote response getter methods"""
        quote_response = {
            'payload': {
                'standard_quote': {
                    'quote_id': 'std_123',
                    'fee': 15.50
                },
                'expedited_quote': {
                    'quote_id': 'exp_123',
                    'fee': 25.00
                }
            }
        }
        
        assert self.gophr.get_standard_quote_id(quote_response) == 'std_123'
        assert self.gophr.get_standard_quote_fee(quote_response) == 15.50
        assert self.gophr.get_expedited_quote_id(quote_response) == 'exp_123'
        assert self.gophr.get_expedited_quote_fee(quote_response) == 25.00
        assert self.gophr.get_quote_payload(quote_response) == quote_response['payload']
    
    def test_shipment_getters(self):
        """Test shipment response getter methods"""
        shipment_response = {
            'payload': {
                'delivery_id': 'DEL_123456',
                'delivery_status': 'confirmed',
                'shipping_fee': 15.50,
                'vehicle_type': 'car',
                'distance': 5.2,
                'weight': 2.5,
                'is_expedited': False,
                'scheduled_for': '2025-09-25',
                'pick_up': {'address': '123 Pickup St'},
                'drop_off': {'address': '456 Dropoff Ave'},
                'items': [{'name': 'Test Item'}]
            }
        }
        
        assert self.gophr.get_delivery_id(shipment_response) == 'DEL_123456'
        assert self.gophr.get_delivery_status(shipment_response) == 'confirmed'
        assert self.gophr.get_shipping_fee(shipment_response) == 15.50
        assert self.gophr.get_vehicle_type(shipment_response) == 'car'
        assert self.gophr.get_distance(shipment_response) == 5.2
        assert self.gophr.get_shipment_weight(shipment_response) == 2.5
        assert self.gophr.is_expedited(shipment_response) is False
        assert self.gophr.get_scheduled_for(shipment_response) == '2025-09-25'
        assert self.gophr.get_pickup_address(shipment_response) == {'address': '123 Pickup St'}
        assert self.gophr.get_dropoff_address(shipment_response) == {'address': '456 Dropoff Ave'}
        assert self.gophr.get_shipment_items(shipment_response) == [{'name': 'Test Item'}]
        assert self.gophr.get_shipment_payload(shipment_response) == shipment_response['payload']
    
    def test_getters_with_missing_data(self):
        """Test getter methods with missing data"""
        empty_response = {}
        
        assert self.gophr.get_standard_quote_id(empty_response) is None
        assert self.gophr.get_delivery_id(empty_response) is None
        assert self.gophr.get_quote_payload(empty_response) is None
    
    def test_is_successful(self):
        """Test is_successful method"""
        successful_response = {
            'status': 'successful',
            'status_code': 200
        }
        
        failed_response = {
            'status': 'error',
            'status_code': 400
        }
        
        assert self.gophr.is_successful(successful_response) is True
        assert self.gophr.is_successful(failed_response) is False
        assert self.gophr.is_successful({}) is False
    
    def test_get_quote_summary(self):
        """Test get_quote_summary method"""
        successful_quote = {
            'status': 'successful',
            'status_code': 200,
            'payload': {
                'standard_quote': {
                    'quote_id': 'std_123',
                    'fee': 15.50
                },
                'expedited_quote': {
                    'quote_id': 'exp_123',
                    'fee': 25.00
                }
            }
        }
        
        failed_quote = {
            'status': 'error',
            'status_code': 400,
            'message': 'Invalid request'
        }
        
        successful_summary = self.gophr.get_quote_summary(successful_quote)
        failed_summary = self.gophr.get_quote_summary(failed_quote)
        
        assert successful_summary['success'] is True
        assert successful_summary['standard']['quote_id'] == 'std_123'
        assert successful_summary['standard']['fee'] == 15.50
        
        assert failed_summary['success'] is False
        assert failed_summary['error'] == 'Invalid request'
        assert failed_summary['status_code'] == 400
    
    def test_get_shipment_summary(self):
        """Test get_shipment_summary method"""
        successful_shipment = {
            'status': 'successful',
            'status_code': 200,
            'payload': {
                'delivery_id': 'DEL_123456',
                'delivery_status': 'confirmed',
                'shipping_fee': 15.50,
                'vehicle_type': 'car',
                'distance': 5.2,
                'weight': 2.5,
                'is_expedited': False,
                'scheduled_for': None
            }
        }
        
        summary = self.gophr.get_shipment_summary(successful_shipment)
        
        assert summary['success'] is True
        assert summary['delivery_id'] == 'DEL_123456'
        assert summary['status'] == 'confirmed'
        assert summary['fee'] == 15.50
        assert summary['vehicle_type'] == 'car'
        assert summary['distance'] == 5.2
        assert summary['weight'] == 2.5
        assert summary['is_expedited'] is False
        assert summary['scheduled_for'] is None


class TestErrorHandling:
    """Test cases for error handling"""
    
    def setup_method(self):
        """Set up test instance"""
        config = {
            'client_id': 'test_client_id',
            'client_secret': 'test_client_secret'
        }
        self.gophr = GophrBridge(config)
    
    def test_gophr_bridge_error(self):
        """Test GophrBridgeError exception"""
        error = GophrBridgeError(
            message="Test error",
            status_code=400,
            details={'field': 'invalid'},
            is_network_error=False
        )
        
        assert str(error) == "Test error"
        assert error.status_code == 400
        assert error.details == {'field': 'invalid'}
        assert error.is_network_error is False
    
    @patch('gophr_bridge.client.logging')
    def test_log_error_gophr_bridge_error(self, mock_logging):
        """Test log_error with GophrBridgeError"""
        error = GophrBridgeError(
            message="API Error",
            status_code=400,
            details={'error': 'bad request'},
            is_network_error=True
        )
        
        GophrBridge.log_error(error)
        
        # Check that logging methods were called
        mock_logging.error.assert_called()
        calls = mock_logging.error.call_args_list
        assert len(calls) >= 3  # At least 3 logging calls
    
    @patch('gophr_bridge.client.logging')
    def test_log_error_generic_exception(self, mock_logging):
        """Test log_error with generic exception"""
        error = ValueError("Generic error")
        
        GophrBridge.log_error(error)
        
        mock_logging.error.assert_called_once_with("Error: Generic error")


if __name__ == '__main__':
    pytest.main([__file__])
