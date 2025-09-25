from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_metadata_response import AgentMetadataResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  agent_type: str,
  *,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": f"/v1/graphs/{graph_id}/agent/{agent_type}/metadata",
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AgentMetadataResponse, Any, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = AgentMetadataResponse.from_dict(response.json())

    return response_200
  if response.status_code == 404:
    response_404 = cast(Any, None)
    return response_404
  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422
  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AgentMetadataResponse, Any, HTTPValidationError]]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  agent_type: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[AgentMetadataResponse, Any, HTTPValidationError]]:
  """Get agent metadata

   Get comprehensive metadata for a specific agent type.

  **Returns:**
  - Agent name and description
  - Version information
  - Supported capabilities and modes
  - Credit requirements
  - Author and tags
  - Configuration options

  Use this to understand agent capabilities before execution.

  Args:
      graph_id (str): Graph database identifier
      agent_type (str): Agent type identifier (e.g., 'financial', 'research', 'rag')
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[AgentMetadataResponse, Any, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    agent_type=agent_type,
    token=token,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  agent_type: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[AgentMetadataResponse, Any, HTTPValidationError]]:
  """Get agent metadata

   Get comprehensive metadata for a specific agent type.

  **Returns:**
  - Agent name and description
  - Version information
  - Supported capabilities and modes
  - Credit requirements
  - Author and tags
  - Configuration options

  Use this to understand agent capabilities before execution.

  Args:
      graph_id (str): Graph database identifier
      agent_type (str): Agent type identifier (e.g., 'financial', 'research', 'rag')
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[AgentMetadataResponse, Any, HTTPValidationError]
  """

  return sync_detailed(
    graph_id=graph_id,
    agent_type=agent_type,
    client=client,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  agent_type: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[AgentMetadataResponse, Any, HTTPValidationError]]:
  """Get agent metadata

   Get comprehensive metadata for a specific agent type.

  **Returns:**
  - Agent name and description
  - Version information
  - Supported capabilities and modes
  - Credit requirements
  - Author and tags
  - Configuration options

  Use this to understand agent capabilities before execution.

  Args:
      graph_id (str): Graph database identifier
      agent_type (str): Agent type identifier (e.g., 'financial', 'research', 'rag')
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[AgentMetadataResponse, Any, HTTPValidationError]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    agent_type=agent_type,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  agent_type: str,
  *,
  client: AuthenticatedClient,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[AgentMetadataResponse, Any, HTTPValidationError]]:
  """Get agent metadata

   Get comprehensive metadata for a specific agent type.

  **Returns:**
  - Agent name and description
  - Version information
  - Supported capabilities and modes
  - Credit requirements
  - Author and tags
  - Configuration options

  Use this to understand agent capabilities before execution.

  Args:
      graph_id (str): Graph database identifier
      agent_type (str): Agent type identifier (e.g., 'financial', 'research', 'rag')
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[AgentMetadataResponse, Any, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      agent_type=agent_type,
      client=client,
      token=token,
      authorization=authorization,
    )
  ).parsed
