import asyncio
import os
import ssl
import threading
from typing import Callable

import socketio
from mcp import ClientSession, StdioServerParameters
from mcp.client.sse import sse_client
from mcp.client.stdio import stdio_client
from mcp.client.streamable_http import streamablehttp_client

from .session_manager import get_session_manager


def start_socket_connection(config, all_tools, notify_on_connect: Callable[[str], None] = None, notify_on_disconnect: Callable[[str], None] = None):
    common_timeout = 90
    
    # Check if SSL verification should be disabled (useful for corporate environments)
    # Priority: environment variable > config file > default (disabled for corporate environments)
    env_ssl_setting = os.environ.get('ALITA_DISABLE_SSL_VERIFY', '').lower()
    if env_ssl_setting in ('true', 'false'):
        disable_ssl_verify = env_ssl_setting == 'true'
    else:
        disable_ssl_verify = not config.get("ssl_verify", False)
    
    if disable_ssl_verify:
        # Create SocketIO client with SSL verification disabled
        # The ssl_verify parameter should be passed during client creation
        sio = socketio.Client(ssl_verify=False, logger=False, engineio_logger=False)
        print("SSL verification disabled for SocketIO connection")
    else:
        sio = socketio.Client()
        print("SSL verification enabled for SocketIO connection")

    @sio.event
    def connect():
        sio.emit("mcp_connect", {
            "project_id": config["project_id"],
            "toolkit_configs": all_tools,
            "timeout_tools_list": common_timeout,
            "timeout_tools_call": common_timeout
        })
        print("Connected to platform")
        notify_on_connect and notify_on_connect("Connected to platform")

    @sio.event
    def disconnect():
        print("Disconnected from platform")
        notify_on_disconnect and notify_on_disconnect("Disconnected from platform")
        # Clean up persistent sessions when disconnecting
        session_manager = get_session_manager()
        try:
            session_manager.cleanup_all()
            print("Cleaned up persistent sessions")
        except Exception as e:
            print(f"Error during session cleanup: {e}")

    @sio.event
    def on_mcp_tools_list(data):
        all_tools = asyncio.run(get_all_tools(config["servers"]))

        return {
            "project_id": config["project_id"],
            "toolkit_configs": all_tools,
            "timeout_tools_list": common_timeout,
            "timeout_tools_call": common_timeout
        }

    @sio.event
    def on_mcp_tools_call(data):
        if "server" in data:
            # Use synchronous wrapper to avoid asyncio.run() conflicts
            tool_result = _mcp_tools_call_sync(
                config["servers"][data["server"]], 
                data["params"], 
                server_name=data["server"]
            )
            #
            return tool_result

    @sio.event
    def on_mcp_notification(notification):
        print(f"Platform Notification: {notification}")

    @sio.event
    def on_mcp_ping(data):
        return True

    try:
        sio.connect(config["deployment_url"], headers={
            'Authorization': f"Bearer {config['auth_token']}"}, 
            wait_timeout=30,
            retry=True)
    except Exception as e:
        print(f"Failed to connect to platform: {e}")
        print("This might be due to SSL certificate issues or network connectivity problems.")
        print("Please check your network connection and try again.")
        raise

    sio.on('mcp_tools_list', on_mcp_tools_list)
    sio.on('mcp_tools_call', on_mcp_tools_call)
    sio.on('mcp_notification', on_mcp_notification)
    sio.on('mcp_ping', on_mcp_ping)

    def socketio_background_task():
        sio.wait()

    socketio_thread = threading.Thread(target=socketio_background_task, daemon=True)
    socketio_thread.start()

    return sio


def _mcp_tools_call_sync(server_conf, params, server_name=None):
    """Synchronous wrapper for MCP tool calls that handles both stateful and stateless sessions."""
    session_manager = get_session_manager()
    
    # Check if this server should use stateful sessions
    if session_manager.is_stateful(server_conf) and server_name:
        # Use persistent session with recovery
        try:
            result = session_manager.call_tool_with_recovery_sync(server_name, server_conf, params)
            return result
        except Exception as e:
            print(f"Failed to call tool with stateful session: {e}")
            print("Falling back to stateless session...")
            # Fall through to stateless mode as fallback
    
    # Use stateless session (original behavior) via async wrapper
    async def _stateless_call():
        return await _mcp_tools_call(server_conf, params, server_name)
    
    # Run in session manager's event loop to avoid conflicts
    return session_manager._run_in_loop(_stateless_call())


async def get_all_tools(servers=[]):
    tasks = [
        _process_server(server_name, server_conf)
        for server_name, server_conf in servers.items()
    ]
    results = await asyncio.gather(*tasks)

    # WORKAROUND
    #
    for server in results:
        for tool in server.get("tools", []):
            input_schema = tool.get("inputSchema")
            if input_schema is not None and "required" not in input_schema:
                input_schema["required"] = []
    
    return results


async def _process_server(server_name, server_conf):
    if server_conf.get('type', 'stdio').lower() == "stdio":
        server_parameters = StdioServerParameters(**server_conf)
        async with stdio_client(server_parameters) as (read, write):
            async with ClientSession(
                    read, write
            ) as session:
                await session.initialize()
                tools_response = await session.list_tools()
                return {"name": server_name, "tools": [tool.model_dump() for tool in tools_response.tools]}

    elif server_conf["type"].lower() == "http":
        async with streamablehttp_client(server_conf["url"], server_conf["headers"]) as (read_stream, write_stream, _):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                tools_response = await session.list_tools()
                return {"name": server_name, "tools": [tool.model_dump() for tool in tools_response.tools]}

    elif server_conf["type"].lower() == "sse":
        async with sse_client(server_conf["url"], server_conf["headers"]) as streams:
            async with ClientSession(*streams) as session:
                await session.initialize()
                tools_response = await session.list_tools()
                return {"name": server_name, "tools": [tool.model_dump() for tool in tools_response.tools]}



async def _mcp_tools_call(server_conf, params, server_name=None):
    """Async function for stateless MCP tool calls."""
    # Use stateless session (original behavior)
    if server_conf.get('type', 'stdio').lower() == "stdio":
        server_parameters = StdioServerParameters(**server_conf)
        async with stdio_client(server_parameters) as (read, write):
            async with ClientSession(
                    read, write
            ) as session:
                await session.initialize()
                tool_result = await session.call_tool(params["name"], params["arguments"])
                return tool_result.content[0].text

    elif server_conf["type"].lower() == "http":
        async with streamablehttp_client(server_conf["url"], server_conf["headers"]) as (read_stream, write_stream, _):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                tool_result = await session.call_tool(params["name"], params["arguments"])
                return tool_result.content[0].text

    elif server_conf["type"].lower() == "sse":
        async with sse_client(server_conf["url"], server_conf.get("headers", {})) as streams:
            async with ClientSession(*streams) as session:
                await session.initialize()
                tool_result = await session.call_tool(params["name"], params["arguments"])
                return tool_result.content[0].text