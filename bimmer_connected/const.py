"""URLs for different services and error code mapping."""

AUTH_URL = 'https://{gcdm_oauth_endpoint}/oauth/authenticate'
TOKEN_URL = 'https://{gcdm_oauth_endpoint}/oauth/token'
BASE_URL = 'https://{server}/webapi/v1'
BASE_URL_LEGACY = 'https://{server}/api/vehicle'

VEHICLES_URL = BASE_URL + '/user/vehicles'
VEHICLE_VIN_URL = VEHICLES_URL + '/{vin}'
VEHICLE_STATUS_URL = VEHICLE_VIN_URL + '/status'

REMOTE_SERVICE_STATUS_URL = VEHICLE_VIN_URL + '/serviceExecutionStatus?serviceType={service_type}'
REMOTE_SERVICE_URL = VEHICLE_VIN_URL + "/executeService"

REMOTE_SERVICE_EADRAX_BASE_URL = 'https://{server}/eadrax-vrccs/v2/presentation/remote-commands'
REMOTE_SERVICE_EADRAX_URL = REMOTE_SERVICE_EADRAX_BASE_URL + '/{vin}/{service_type}'
REMOTE_SERVICE_EADRAX_STATUS_URL = REMOTE_SERVICE_EADRAX_BASE_URL + '/eventStatus?eventId={event_id}'

VEHICLE_IMAGE_URL = VEHICLE_VIN_URL + "/image?width={width}&height={height}&view={view}"
VEHICLE_POI_URL = VEHICLE_VIN_URL + '/sendpoi'
VEHICLE_EADRAX_POI_URL = 'https://{server}/eadrax-dcs/v1/send-to-car/send-to-car'
VEHICLE_STATISTICS_URL = VEHICLE_VIN_URL + '/statistics'
VEHICLE_STATISTICS_LAST_TRIP_URL = VEHICLE_STATISTICS_URL + '/lastTrip'
VEHICLE_STATISTICS_ALL_TRIPS_URL = VEHICLE_STATISTICS_URL + '/allTrips'
VEHICLE_CHARGING_PROFILE_URL = VEHICLE_VIN_URL + '/chargingprofile'
VEHICLE_DESTINATIONS_URL = VEHICLE_VIN_URL + '/destinations'
VEHICLE_RANGEMAP_URL = VEHICLE_VIN_URL + '/rangemap'
VEHICLE_EFFICIENCY = BASE_URL_LEGACY + '/efficiency' + '/v1/{vin}'
VEHICLE_NAVIGATION = BASE_URL_LEGACY + '/navigation' + '/v1/{vin}'

SERVICE_STATUS = 'STATUS'
SERVICE_LAST_TRIP = 'LAST_TRIP'
SERVICE_ALL_TRIPS = 'ALL_TRIPS'
SERVICE_CHARGING_PROFILE = 'CHARGING_PROFILE'
SERVICE_DESTINATIONS = 'DESTINATIONS'
SERVICE_RANGEMAP = 'RANGEMAP'
SERVICE_EFFICIENCY = 'EFFICIENCY'
SERVICE_NAVIGATION = 'NAVIGATION'

# Possible error codes, other codes are mapped to UNKNOWN_ERROR
ERROR_CODE_MAPPING = {
    401: 'UNAUTHORIZED',
    404: 'NOT_FOUND',
    405: 'MOBILE_ACCESS_DISABLED',
    408: 'VEHICLE_UNAVAILABLE',
    423: 'ACCOUNT_LOCKED',
    429: 'TOO_MANY_REQUESTS',
    500: 'SERVER_ERROR',
    503: 'SERVICE_MAINTENANCE',
}
