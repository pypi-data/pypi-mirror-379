# -*- coding: utf-8 -*-
"""
connection: Provides a HTTP client to make requests to calm

Example:

pc_ip = "<pc_ip>"
pc_port = 9440
client = get_connection(pc_ip, pc_port,
                        auth=("<pc_username>", "<pc_passwd>"))

"""

import traceback
import json
import urllib3
import sys

from requests import Session as Session
from requests_toolbelt import MultipartEncoder
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectTimeout
from requests.packages.urllib3.util.retry import Retry

from calm.dsl.log import get_logging_handle
from calm.dsl.config import get_context
from calm.dsl.constants import MULTICONNECT

urllib3.disable_warnings()
LOG = get_logging_handle(__name__)


class REQUEST:
    """Request related constants"""

    class SCHEME:
        """
        Connection schemes
        """

        HTTP = "http"
        HTTPS = "https"

    class AUTH_TYPE:
        """
        Types of auth
        """

        NONE = "none"
        BASIC = "basic"
        JWT = "jwt"

    class METHOD:
        """
        Request methods
        """

        DELETE = "delete"
        GET = "get"
        POST = "post"
        PUT = "put"


def build_url(host, port, endpoint="", scheme=REQUEST.SCHEME.HTTPS):
    """Build url.

    Args:
        host (str): hostname/ip
        port (int): port of the service
        endpoint (str): url endpoint
        scheme (str): http/https/tcp/udp
    Returns:
    Raises:
    """
    url = "{scheme}://{host}".format(scheme=scheme, host=host)
    if port is not None:
        url += ":{port}".format(port=port)
    url += "/{endpoint}".format(endpoint=endpoint)
    return url


class MultiConnection:
    """
    Encapsulates all type of connection objects here.
    """

    def __init__(self):
        setattr(self, MULTICONNECT.PC_OBJ, None)
        setattr(self, MULTICONNECT.NCM_OBJ, None)

    def get_pc_object(self):
        return getattr(self, MULTICONNECT.PC_OBJ, None)

    def get_ncm_object(self):
        return getattr(self, MULTICONNECT.NCM_OBJ, None)

    @property
    def base_url(self):
        """
        Dynamically fetch the base_url based on the connection type.

        @property decorator:
            - Provides a consistent interface for accessing base_url, regardless of
              whether client.connection is a Connection or MultiConnection object.
            - Improves flexibility and reduces the risk of errors when switching connection types.
        """
        context = get_context()
        ncm_server_config = context.get_ncm_server_config()
        try:
            if ncm_server_config.get("ncm_enabled", False):
                return self.get_ncm_object().base_url
            else:
                return self.get_pc_object().base_url
        except:
            LOG.debug("client.connection object does not exist or has no base_url.")
        return None

    def connect(self):

        # Case for one host (single connection object)
        if isinstance(self, Connection):
            self.connect()
            return

        if isinstance(self.get_pc_object(), PcConnection):
            self.get_pc_object().connect()
        else:
            LOG.debug("PC connection is not present")

        if isinstance(self.get_ncm_object(), NcmConnection):
            self.get_ncm_object().connect()
        else:
            LOG.debug("NCM connection is not present")

    def close(self):
        if isinstance(self.get_pc_object(), PcConnection):
            self.get_pc_object().close()
        else:
            LOG.debug("PC connection is not present")

        if isinstance(self.get_ncm_object(), NcmConnection):
            self.get_ncm_object().close()
        else:
            LOG.debug("NCM connection is not present")


class Connection:
    def __init__(
        self,
        host,
        port,
        auth_type=REQUEST.AUTH_TYPE.BASIC,
        scheme=REQUEST.SCHEME.HTTPS,
        auth=None,
        pool_maxsize=20,
        pool_connections=20,
        pool_block=True,
        base_url="",
        response_processor=None,
        session_headers=None,
        **kwargs,
    ):
        """Generic client to connect to server.

        Args:
            host (str): Hostname/IP address
            port (int): Port to connect to
            pool_maxsize (int): The maximum number of connections in the pool
            pool_connections (int): The number of urllib3 connection pools
                                    to cache
            pool_block (bool): Whether the connection pool should block
                               for connections
            base_url (str): Base URL
            scheme (str): http scheme (http or https)
            response_processor (dict): response processor dict
            session_headers (dict): session headers dict
            auth_type (str): auth type that needs to be used by the client
            auth (tuple): authentication
        Returns:
        Raises:
        """
        self.base_url = base_url
        self.host = host
        self.port = port
        self.session_headers = session_headers or {}
        self._pool_maxsize = pool_maxsize
        self._pool_connections = pool_connections
        self._pool_block = pool_block
        self.session = None
        self.auth = auth
        self.scheme = scheme
        self.auth_type = auth_type
        self.response_processor = response_processor

    def connect(self):
        """Connect to api server, create http session pool.

        Args:
        Returns:
            api server session
        Raises:
        """

        context = get_context()
        connection_config = context.get_connection_config()
        if connection_config["retries_enabled"]:
            retry_strategy = Retry(
                total=3,
                status_forcelist=[429, 500, 502, 503, 504],
                method_whitelist=[
                    "GET",
                    "PUT",
                    "DELETE",
                    "POST",
                ],
            )
            http_adapter = HTTPAdapter(
                pool_block=bool(self._pool_block),
                pool_connections=int(self._pool_connections),
                pool_maxsize=int(self._pool_maxsize),
                max_retries=retry_strategy,
            )

        else:
            http_adapter = HTTPAdapter(
                pool_block=bool(self._pool_block),
                pool_connections=int(self._pool_connections),
                pool_maxsize=int(self._pool_maxsize),
            )

        self.session = Session()
        if self.auth and self.auth_type == REQUEST.AUTH_TYPE.BASIC:
            self.session.auth = self.auth
        self.session.headers.update({"Content-Type": "application/json"})

        self.session.mount("http://", http_adapter)
        self.session.mount("https://", http_adapter)
        self.base_url = build_url(self.host, self.port, scheme=self.scheme)
        LOG.debug("{} session created".format(self.__class__.__name__))
        return self.session

    def close(self):
        """
        Close the session.

        Args:
            None
        Returns:
            None
        """
        self.session.close()

    def _call(
        self,
        endpoint,
        method=REQUEST.METHOD.POST,
        cookies=None,
        request_json=None,
        request_params=None,
        verify=True,
        headers=None,
        files=None,
        ignore_error=False,
        warning_msg="",
        **kwargs,
    ):
        """Private method for making http request to calm

        Args:
            endpoint (str): calm server endpoint
            method (str): calm server http method
            cookies (dict): cookies that need to be forwarded.
            request_json (dict): request data
            request_params (dict): request params
            timeout (touple): (connection timeout, read timeout)
        Returns:
            (tuple (requests.Response, dict)): Response
        """
        timeout = kwargs.get("timeout", None)
        if not timeout:
            context = get_context()
            connection_config = context.get_connection_config()
            timeout = (
                connection_config["connection_timeout"],
                connection_config["read_timeout"],
            )

        if request_params is None:
            request_params = {}

        request_json = request_json or {}
        LOG.debug(
            """Server Request- '{method}' at '{endpoint}' with body:
            '{body}'""".format(
                method=method, endpoint=endpoint, body=request_json
            )
        )
        res = None
        err = None
        try:
            res = None
            url = build_url(self.host, self.port, endpoint=endpoint, scheme=self.scheme)
            LOG.debug("URL is: {}".format(url))
            base_headers = self.session.headers
            if headers:
                base_headers.update(headers)

            if method == REQUEST.METHOD.POST:
                if files is not None:
                    request_json.update(files)
                    m = MultipartEncoder(fields=request_json)
                    res = self.session.post(
                        url,
                        data=m,
                        verify=verify,
                        headers={"Content-Type": m.content_type},
                        timeout=timeout,
                    )
                else:
                    res = self.session.post(
                        url,
                        params=request_params,
                        data=json.dumps(request_json),
                        verify=verify,
                        headers=base_headers,
                        cookies=cookies,
                        timeout=timeout,
                    )
            elif method == REQUEST.METHOD.PUT:
                res = self.session.put(
                    url,
                    params=request_params,
                    data=json.dumps(request_json),
                    verify=verify,
                    headers=base_headers,
                    cookies=cookies,
                    timeout=timeout,
                )
            elif method == REQUEST.METHOD.GET:
                res = self.session.get(
                    url,
                    params=request_params or request_json,
                    verify=verify,
                    headers=base_headers,
                    cookies=cookies,
                    timeout=timeout,
                )
            elif method == REQUEST.METHOD.DELETE:
                res = self.session.delete(
                    url,
                    params=request_params,
                    data=json.dumps(request_json),
                    verify=verify,
                    headers=base_headers,
                    cookies=cookies,
                    timeout=timeout,
                )
            res.raise_for_status()
            if not url.endswith("/download"):
                if not res.ok:
                    LOG.debug("Server Response: {}".format(res.json()))
        except ConnectTimeout as cte:
            LOG.error(
                "Could not establish connection to server at https://{}:{}.".format(
                    self.host, self.port
                )
            )
            LOG.debug("Error Response: {}".format(cte))
            sys.exit(-1)
        except Exception as ex:
            LOG.debug("Got traceback\n{}".format(traceback.format_exc()))
            if hasattr(res, "json") and callable(getattr(res, "json")):
                try:
                    err_msg = res.json()
                except Exception:
                    err_msg = "{}".format(ex)
                    pass
            elif hasattr(res, "text"):
                err_msg = res.text
            else:
                err_msg = "{}".format(ex)
            status_code = res.status_code if hasattr(res, "status_code") else 500
            err = {"error": err_msg, "code": status_code}

            if ignore_error:
                if warning_msg:
                    LOG.warning(warning_msg)
                return None, err

            LOG.error(
                "Oops! Something went wrong.\n{}".format(
                    json.dumps(err, indent=4, separators=(",", ": "))
                )
            )

        return res, err


class PcConnection(Connection):
    pass


class NcmConnection(Connection):
    pass


_CONNECTION = None


def get_connection_obj(
    host,
    port,
    auth_type=REQUEST.AUTH_TYPE.BASIC,
    scheme=REQUEST.SCHEME.HTTPS,
    auth=None,
):
    """Returns object of Connection class"""

    return Connection(host, port, auth_type, scheme, auth)


def get_pc_connection_obj(
    host,
    port,
    auth_type=REQUEST.AUTH_TYPE.BASIC,
    scheme=REQUEST.SCHEME.HTTPS,
    auth=None,
):
    """Returns object of PcConnection class"""

    return PcConnection(host, port, auth_type, scheme, auth)


def get_ncm_connection_obj(
    host,
    port,
    auth_type=REQUEST.AUTH_TYPE.BASIC,
    scheme=REQUEST.SCHEME.HTTPS,
    auth=None,
):
    """Returns object of NcmConnection class"""

    return NcmConnection(host, port, auth_type, scheme, auth)


def get_pc_connection_handle(
    host,
    port,
    auth_type=REQUEST.AUTH_TYPE.BASIC,
    scheme=REQUEST.SCHEME.HTTPS,
    auth=None,
):
    """Get api server (aplos/styx) handle.

    Args:
        host (str): Hostname/IP address
        port (int): Port to connect to
        auth_type (str): auth type that needs to be used by the client
        scheme (str): http scheme (http or https)
        session_headers (dict): session headers dict
        auth (tuple): authentication
    Returns:
        Client handle
    Raises:
        Exception: If cannot connect
    """
    global _PC_CONNECTION
    if not _PC_CONNECTION:
        update_pc_connection_handle(host, port, auth_type, scheme, auth)
    return _PC_CONNECTION


def get_ncm_connection_handle(
    host,
    port,
    auth_type=REQUEST.AUTH_TYPE.BASIC,
    scheme=REQUEST.SCHEME.HTTPS,
    auth=None,
):
    """Get api server (aplos/styx) handle.

    Args:
        host (str): Hostname/IP address
        port (int): Port to connect to
        auth_type (str): auth type that needs to be used by the client
        scheme (str): http scheme (http or https)
        session_headers (dict): session headers dict
        auth (tuple): authentication
    Returns:
        Client handle
    Raises:
        Exception: If cannot connect
    """
    global _NCM_CONNECTION
    if not _NCM_CONNECTION:
        update_ncm_connection_handle(host, port, auth_type, scheme, auth)
    return _NCM_CONNECTION


def update_pc_connection_handle(
    host,
    port,
    auth_type=REQUEST.AUTH_TYPE.BASIC,
    scheme=REQUEST.SCHEME.HTTPS,
    auth=None,
):
    global _PC_CONNECTION
    _PC_CONNECTION = PcConnection(host, port, auth_type, scheme=scheme, auth=auth)


def update_ncm_connection_handle(
    host,
    port,
    auth_type=REQUEST.AUTH_TYPE.BASIC,
    scheme=REQUEST.SCHEME.HTTPS,
    auth=None,
):
    global _NCM_CONNECTION
    _NCM_CONNECTION = NcmConnection(host, port, auth_type, scheme=scheme, auth=auth)
