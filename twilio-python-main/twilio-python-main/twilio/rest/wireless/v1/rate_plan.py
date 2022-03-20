# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class RatePlanList(ListResource):

    def __init__(self, version):
        """
        Initialize the RatePlanList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.wireless.v1.rate_plan.RatePlanList
        :rtype: twilio.rest.wireless.v1.rate_plan.RatePlanList
        """
        super(RatePlanList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/RatePlans'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams RatePlanInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.rate_plan.RatePlanInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists RatePlanInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.rate_plan.RatePlanInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of RatePlanInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RatePlanInstance
        :rtype: twilio.rest.wireless.v1.rate_plan.RatePlanPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return RatePlanPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of RatePlanInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RatePlanInstance
        :rtype: twilio.rest.wireless.v1.rate_plan.RatePlanPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return RatePlanPage(self._version, response, self._solution)

    def create(self, unique_name=values.unset, friendly_name=values.unset,
               data_enabled=values.unset, data_limit=values.unset,
               data_metering=values.unset, messaging_enabled=values.unset,
               voice_enabled=values.unset, national_roaming_enabled=values.unset,
               international_roaming=values.unset,
               national_roaming_data_limit=values.unset,
               international_roaming_data_limit=values.unset):
        """
        Create the RatePlanInstance

        :param unicode unique_name: An application-defined string that uniquely identifies the resource
        :param unicode friendly_name: A string to describe the resource
        :param bool data_enabled: Whether SIMs can use GPRS/3G/4G/LTE data connectivity
        :param unicode data_limit: The total data usage in Megabytes that the Network allows during one month on the home network
        :param unicode data_metering: The model used to meter data usage
        :param bool messaging_enabled: Whether SIMs can make, send, and receive SMS using Commands
        :param bool voice_enabled: Deprecated
        :param bool national_roaming_enabled: Whether SIMs can roam on networks other than the home network in the United States
        :param list[unicode] international_roaming: The services that SIMs capable of using GPRS/3G/4G/LTE data connectivity can use outside of the United States
        :param unicode national_roaming_data_limit: The total data usage in Megabytes that the Network allows during one month on non-home networks in the United States
        :param unicode international_roaming_data_limit: The total data usage (download and upload combined) in Megabytes that the Network allows during one month when roaming outside the United States

        :returns: The created RatePlanInstance
        :rtype: twilio.rest.wireless.v1.rate_plan.RatePlanInstance
        """
        data = values.of({
            'UniqueName': unique_name,
            'FriendlyName': friendly_name,
            'DataEnabled': data_enabled,
            'DataLimit': data_limit,
            'DataMetering': data_metering,
            'MessagingEnabled': messaging_enabled,
            'VoiceEnabled': voice_enabled,
            'NationalRoamingEnabled': national_roaming_enabled,
            'InternationalRoaming': serialize.map(international_roaming, lambda e: e),
            'NationalRoamingDataLimit': national_roaming_data_limit,
            'InternationalRoamingDataLimit': international_roaming_data_limit,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return RatePlanInstance(self._version, payload, )

    def get(self, sid):
        """
        Constructs a RatePlanContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.wireless.v1.rate_plan.RatePlanContext
        :rtype: twilio.rest.wireless.v1.rate_plan.RatePlanContext
        """
        return RatePlanContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a RatePlanContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.wireless.v1.rate_plan.RatePlanContext
        :rtype: twilio.rest.wireless.v1.rate_plan.RatePlanContext
        """
        return RatePlanContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Wireless.V1.RatePlanList>'


class RatePlanPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the RatePlanPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.wireless.v1.rate_plan.RatePlanPage
        :rtype: twilio.rest.wireless.v1.rate_plan.RatePlanPage
        """
        super(RatePlanPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RatePlanInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.wireless.v1.rate_plan.RatePlanInstance
        :rtype: twilio.rest.wireless.v1.rate_plan.RatePlanInstance
        """
        return RatePlanInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Wireless.V1.RatePlanPage>'


class RatePlanContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the RatePlanContext

        :param Version version: Version that contains the resource
        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.wireless.v1.rate_plan.RatePlanContext
        :rtype: twilio.rest.wireless.v1.rate_plan.RatePlanContext
        """
        super(RatePlanContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/RatePlans/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the RatePlanInstance

        :returns: The fetched RatePlanInstance
        :rtype: twilio.rest.wireless.v1.rate_plan.RatePlanInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return RatePlanInstance(self._version, payload, sid=self._solution['sid'], )

    def update(self, unique_name=values.unset, friendly_name=values.unset):
        """
        Update the RatePlanInstance

        :param unicode unique_name: An application-defined string that uniquely identifies the resource
        :param unicode friendly_name: A string to describe the resource

        :returns: The updated RatePlanInstance
        :rtype: twilio.rest.wireless.v1.rate_plan.RatePlanInstance
        """
        data = values.of({'UniqueName': unique_name, 'FriendlyName': friendly_name, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return RatePlanInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the RatePlanInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Wireless.V1.RatePlanContext {}>'.format(context)


class RatePlanInstance(InstanceResource):

    class DataLimitStrategy(object):
        BLOCK = "block"
        THROTTLE = "throttle"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the RatePlanInstance

        :returns: twilio.rest.wireless.v1.rate_plan.RatePlanInstance
        :rtype: twilio.rest.wireless.v1.rate_plan.RatePlanInstance
        """
        super(RatePlanInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'unique_name': payload.get('unique_name'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'data_enabled': payload.get('data_enabled'),
            'data_metering': payload.get('data_metering'),
            'data_limit': deserialize.integer(payload.get('data_limit')),
            'messaging_enabled': payload.get('messaging_enabled'),
            'voice_enabled': payload.get('voice_enabled'),
            'national_roaming_enabled': payload.get('national_roaming_enabled'),
            'national_roaming_data_limit': deserialize.integer(payload.get('national_roaming_data_limit')),
            'international_roaming': payload.get('international_roaming'),
            'international_roaming_data_limit': deserialize.integer(payload.get('international_roaming_data_limit')),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: RatePlanContext for this RatePlanInstance
        :rtype: twilio.rest.wireless.v1.rate_plan.RatePlanContext
        """
        if self._context is None:
            self._context = RatePlanContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def data_enabled(self):
        """
        :returns: Whether SIMs can use GPRS/3G/4G/LTE data connectivity
        :rtype: bool
        """
        return self._properties['data_enabled']

    @property
    def data_metering(self):
        """
        :returns: The model used to meter data usage
        :rtype: unicode
        """
        return self._properties['data_metering']

    @property
    def data_limit(self):
        """
        :returns: The total data usage in Megabytes that the Network allows during one month on the home network
        :rtype: unicode
        """
        return self._properties['data_limit']

    @property
    def messaging_enabled(self):
        """
        :returns: Whether SIMs can make, send, and receive SMS using Commands
        :rtype: bool
        """
        return self._properties['messaging_enabled']

    @property
    def voice_enabled(self):
        """
        :returns: Deprecated. Whether SIMs can make and receive voice calls
        :rtype: bool
        """
        return self._properties['voice_enabled']

    @property
    def national_roaming_enabled(self):
        """
        :returns: Whether SIMs can roam on networks other than the home network in the United States
        :rtype: bool
        """
        return self._properties['national_roaming_enabled']

    @property
    def national_roaming_data_limit(self):
        """
        :returns: The total data usage in Megabytes that the Network allows during one month on non-home networks in the United States
        :rtype: unicode
        """
        return self._properties['national_roaming_data_limit']

    @property
    def international_roaming(self):
        """
        :returns: The services that SIMs capable of using GPRS/3G/4G/LTE data connectivity can use outside of the United States
        :rtype: list[unicode]
        """
        return self._properties['international_roaming']

    @property
    def international_roaming_data_limit(self):
        """
        :returns: The total data usage (download and upload combined) in Megabytes that the Network allows during one month when roaming outside the United States
        :rtype: unicode
        """
        return self._properties['international_roaming_data_limit']

    @property
    def date_created(self):
        """
        :returns: The date when the resource was created, given as GMT in ISO 8601 format
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date when the resource was last updated, given as GMT in ISO 8601 format
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the RatePlanInstance

        :returns: The fetched RatePlanInstance
        :rtype: twilio.rest.wireless.v1.rate_plan.RatePlanInstance
        """
        return self._proxy.fetch()

    def update(self, unique_name=values.unset, friendly_name=values.unset):
        """
        Update the RatePlanInstance

        :param unicode unique_name: An application-defined string that uniquely identifies the resource
        :param unicode friendly_name: A string to describe the resource

        :returns: The updated RatePlanInstance
        :rtype: twilio.rest.wireless.v1.rate_plan.RatePlanInstance
        """
        return self._proxy.update(unique_name=unique_name, friendly_name=friendly_name, )

    def delete(self):
        """
        Deletes the RatePlanInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Wireless.V1.RatePlanInstance {}>'.format(context)
