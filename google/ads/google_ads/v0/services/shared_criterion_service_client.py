# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Accesses the google.ads.googleads.v0.services SharedCriterionService API."""

import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.grpc_helpers
import google.api_core.path_template
import grpc

from google.ads.google_ads.v0.services import shared_criterion_service_client_config
from google.ads.google_ads.v0.services.transports import shared_criterion_service_grpc_transport
from google.ads.google_ads.v0.proto.services import shared_criterion_service_pb2

_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    'google-ads', ).version


class SharedCriterionServiceClient(object):
    """Service to manage shared criteria."""

    SERVICE_ADDRESS = 'googleads.googleapis.com:443'
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = 'google.ads.googleads.v0.services.SharedCriterionService'

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            SharedCriterionServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(
            filename)
        kwargs['credentials'] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def shared_criteria_path(cls, customer, shared_criteria):
        """Return a fully-qualified shared_criteria string."""
        return google.api_core.path_template.expand(
            'customers/{customer}/sharedCriteria/{shared_criteria}',
            customer=customer,
            shared_criteria=shared_criteria,
        )

    def __init__(self,
                 transport=None,
                 channel=None,
                 credentials=None,
                 client_config=shared_criterion_service_client_config.config,
                 client_info=None):
        """Constructor.

        Args:
            transport (Union[~.SharedCriterionServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.SharedCriterionServiceGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config:
            warnings.warn('The `client_config` argument is deprecated.',
                          PendingDeprecationWarning)
        if channel:
            warnings.warn(
                'The `channel` argument is deprecated; use '
                '`transport` instead.', PendingDeprecationWarning)

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=shared_criterion_service_grpc_transport.
                    SharedCriterionServiceGrpcTransport,
                )
            else:
                if credentials:
                    raise ValueError(
                        'Received both a transport instance and '
                        'credentials; these are mutually exclusive.')
                self.transport = transport
        else:
            self.transport = shared_criterion_service_grpc_transport.SharedCriterionServiceGrpcTransport(
                address=self.SERVICE_ADDRESS,
                channel=channel,
                credentials=credentials,
            )

        if client_info is None:
            client_info = (
                google.api_core.gapic_v1.client_info.DEFAULT_CLIENT_INFO)
        client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config['interfaces'][self._INTERFACE_NAME], )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def get_shared_criterion(self,
                             resource_name,
                             retry=google.api_core.gapic_v1.method.DEFAULT,
                             timeout=google.api_core.gapic_v1.method.DEFAULT,
                             metadata=None):
        """
        Returns the requested shared criterion in full detail.

        Args:
            resource_name (str): The resource name of the shared criterion to fetch.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.ads.google_ads.v0.types.SharedCriterion` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_shared_criterion' not in self._inner_api_calls:
            self._inner_api_calls[
                'get_shared_criterion'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.get_shared_criterion,
                    default_retry=self._method_configs[
                        'GetSharedCriterion'].retry,
                    default_timeout=self._method_configs['GetSharedCriterion']
                    .timeout,
                    client_info=self._client_info,
                )

        request = shared_criterion_service_pb2.GetSharedCriterionRequest(
            resource_name=resource_name, )
        return self._inner_api_calls['get_shared_criterion'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def mutate_shared_criteria(self,
                               customer_id,
                               operations,
                               retry=google.api_core.gapic_v1.method.DEFAULT,
                               timeout=google.api_core.gapic_v1.method.DEFAULT,
                               metadata=None):
        """
        Creates or removes shared criteria. Operation statuses are returned.

        Args:
            customer_id (str): The ID of the customer whose shared criteria are being modified.
            operations (list[Union[dict, ~google.ads.google_ads.v0.types.SharedCriterionOperation]]): The list of operations to perform on individual shared criteria.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.ads.google_ads.v0.types.SharedCriterionOperation`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.ads.google_ads.v0.types.MutateSharedCriteriaResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'mutate_shared_criteria' not in self._inner_api_calls:
            self._inner_api_calls[
                'mutate_shared_criteria'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.mutate_shared_criteria,
                    default_retry=self._method_configs['MutateSharedCriteria']
                    .retry,
                    default_timeout=self._method_configs[
                        'MutateSharedCriteria'].timeout,
                    client_info=self._client_info,
                )

        request = shared_criterion_service_pb2.MutateSharedCriteriaRequest(
            customer_id=customer_id,
            operations=operations,
        )
        return self._inner_api_calls['mutate_shared_criteria'](
            request, retry=retry, timeout=timeout, metadata=metadata)
