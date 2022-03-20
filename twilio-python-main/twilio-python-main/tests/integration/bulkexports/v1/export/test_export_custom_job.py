# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class ExportCustomJobTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.bulkexports.v1.exports("resource_type") \
                                      .export_custom_jobs.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://bulkexports.twilio.com/v1/Exports/resource_type/Jobs',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "previous_page_url": null,
                    "url": "https://bulkexports.twilio.com/v1/Exports/Messages/Jobs?PageSize=50&Page=0",
                    "page_size": 50,
                    "key": "jobs",
                    "first_page_url": "https://bulkexports.twilio.com/v1/Exports/Messages/Jobs?PageSize=50&Page=0",
                    "next_page_url": null,
                    "page": 0
                },
                "jobs": []
            }
            '''
        ))

        actual = self.client.bulkexports.v1.exports("resource_type") \
                                           .export_custom_jobs.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "previous_page_url": null,
                    "url": "https://bulkexports.twilio.com/v1/Exports/Messages/Jobs?PageSize=50&Page=0",
                    "page_size": 50,
                    "key": "jobs",
                    "first_page_url": "https://bulkexports.twilio.com/v1/Exports/Messages/Jobs?PageSize=50&Page=0",
                    "next_page_url": null,
                    "page": 0
                },
                "jobs": [
                    {
                        "start_day": "start_day",
                        "job_sid": "JSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "friendly_name",
                        "webhook_method": "webhook_method",
                        "details": {},
                        "end_day": "end_day",
                        "webhook_url": "webhook_url",
                        "email": "email",
                        "resource_type": "resource_type",
                        "job_queue_position": "1",
                        "estimated_completion_time": "2021-03-15T20:20:14.547"
                    }
                ]
            }
            '''
        ))

        actual = self.client.bulkexports.v1.exports("resource_type") \
                                           .export_custom_jobs.list()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.bulkexports.v1.exports("resource_type") \
                                      .export_custom_jobs.create(start_day="start_day", end_day="end_day", friendly_name="friendly_name")

        values = {'StartDay': "start_day", 'EndDay': "end_day", 'FriendlyName': "friendly_name", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://bulkexports.twilio.com/v1/Exports/resource_type/Jobs',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "start_day": "start_day",
                "job_sid": "JSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "webhook_method": "webhook_method",
                "details": {},
                "end_day": "end_day",
                "webhook_url": "webhook_url",
                "email": "email",
                "resource_type": "resource_type",
                "job_queue_position": "1",
                "estimated_completion_time": "2021-03-15T20:20:14.547"
            }
            '''
        ))

        actual = self.client.bulkexports.v1.exports("resource_type") \
                                           .export_custom_jobs.create(start_day="start_day", end_day="end_day", friendly_name="friendly_name")

        self.assertIsNotNone(actual)
