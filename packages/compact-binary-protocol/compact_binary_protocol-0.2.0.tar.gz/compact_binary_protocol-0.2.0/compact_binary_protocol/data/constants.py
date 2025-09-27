# Central definitions of SensorData type codes
# Version numbers remain defined in each implementation class

TYPE_NULL = 0
TYPE_KV = 1
TYPE_LOCATION = 10
TYPE_CUSTOMER_ID = 11

TYPE_VERSIONS = 20
TYPE_NETWORK_INFO = 21

TYPE_BASIC = 30
TYPE_MULTI = 31
TYPE_STEPS = 32

__all__ = [
    'TYPE_NULL',
    'TYPE_MULTI',
    'TYPE_STEPS',
    'TYPE_VERSIONS',
    'TYPE_NETWORK_INFO',
    'TYPE_LOCATION',
    'TYPE_CUSTOMER_ID',
    'TYPE_KV',
]
