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


class RecordingTestCase(IntegrationTestCase):

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .recordings("REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(status="in-progress")

        values = {'Status': "in-progress", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conferences/CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Recordings/REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "channels": 1,
                "date_created": "Fri, 14 Oct 2016 21:56:34 +0000",
                "date_updated": "Fri, 14 Oct 2016 21:56:39 +0000",
                "start_time": "Fri, 14 Oct 2016 21:56:34 +0000",
                "price": null,
                "price_unit": null,
                "duration": null,
                "sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "source": "StartConferenceRecordingAPI",
                "status": "paused",
                "error_code": null,
                "encryption_details": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .recordings("REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(status="in-progress")

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .recordings("REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conferences/CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Recordings/REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "channels": 1,
                "date_created": "Fri, 14 Oct 2016 21:56:34 +0000",
                "date_updated": "Fri, 14 Oct 2016 21:56:38 +0000",
                "start_time": "Fri, 14 Oct 2016 21:56:34 +0000",
                "price": "-0.0025",
                "price_unit": "USD",
                "duration": "4",
                "sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "source": "StartConferenceRecordingAPI",
                "status": "completed",
                "error_code": null,
                "encryption_details": {
                    "encryption_public_key_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "encryption_cek": "OV4h6zrsxMIW7h0Zfqwfn6TI2GCNl54KALlg8wn8YB8KYZhXt6HlgvBWAmQTlfYVeLWydMiCewY0YkDDT1xmNe5huEo9vjuKBS5OmYK4CZkSx1NVv3XOGrZHpd2Pl/5WJHVhUK//AUO87uh5qnUP2E0KoLh1nyCLeGcEkXU0RfpPn/6nxjof/n6m6OzZOyeIRK4Oed5+rEtjqFDfqT0EVKjs6JAxv+f0DCc1xYRHl2yV8bahUPVKs+bHYdy4PVszFKa76M/Uae4jFA9Lv233JqWcxj+K2UoghuGhAFbV/JQIIswY2CBYI8JlVSifSqNEl9vvsTJ8bkVMm3MKbG2P7Q==",
                    "encryption_iv": "8I2hhNIYNTrwxfHk"
                },
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .recordings("REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .recordings("REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conferences/CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Recordings/REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .recordings("REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .recordings.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conferences/CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Recordings.json',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json?PageSize=50&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "recordings": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "api_version": "2010-04-01",
                        "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "channels": 1,
                        "date_created": "Fri, 14 Oct 2016 21:56:34 +0000",
                        "date_updated": "Fri, 14 Oct 2016 21:56:38 +0000",
                        "start_time": "Fri, 14 Oct 2016 21:56:34 +0000",
                        "price": "-0.0025",
                        "price_unit": "USD",
                        "duration": "4",
                        "sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "source": "StartConferenceRecordingAPI",
                        "status": "completed",
                        "error_code": null,
                        "encryption_details": {
                            "encryption_public_key_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                            "encryption_cek": "OV4h6zrsxMIW7h0Zfqwfn6TI2GCNl54KALlg8wn8YB8KYZhXt6HlgvBWAmQTlfYVeLWydMiCewY0YkDDT1xmNe5huEo9vjuKBS5OmYK4CZkSx1NVv3XOGrZHpd2Pl/5WJHVhUK//AUO87uh5qnUP2E0KoLh1nyCLeGcEkXU0RfpPn/6nxjof/n6m6OzZOyeIRK4Oed5+rEtjqFDfqT0EVKjs6JAxv+f0DCc1xYRHl2yV8bahUPVKs+bHYdy4PVszFKa76M/Uae4jFA9Lv233JqWcxj+K2UoghuGhAFbV/JQIIswY2CBYI8JlVSifSqNEl9vvsTJ8bkVMm3MKbG2P7Q==",
                            "encryption_iv": "8I2hhNIYNTrwxfHk"
                        },
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
                    }
                ],
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json?PageSize=50&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .recordings.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json?PageSize=50&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "recordings": [],
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json?PageSize=50&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .recordings.list()

        self.assertIsNotNone(actual)
