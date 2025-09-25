"""Tool schema definitions separated from server runtime.

This module returns the list of MCP Tool objects supported by the
current server implementation. It mirrors the previous inline
definitions from ``server.py`` (pre-refactor) to preserve backwards
compatibility for clients and tests.
"""

from mcp.types import Tool


def get_tool_definitions() -> list[Tool]:
    """Return tool definitions (schemas + descriptions)."""
    return [
        Tool(
            name="search_collections",
            description="Search and list available STAC collections",
            inputSchema={
                "type": "object",
                "properties": {
                    "output_format": {
                        "type": "string",
                        "description": "Result output format: 'text' (default) or 'json'",
                        "enum": ["text", "json"],
                        "default": "text",
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of collections to return",
                        "default": 10,
                        "minimum": 1,
                        "maximum": 100,
                    },
                    "catalog_url": {
                        "type": "string",
                        "description": "STAC catalog URL (optional, defaults to Microsoft Planetary Computer)",
                    },
                },
            },
        ),
        Tool(
            name="get_collection",
            description="Get detailed information about a specific STAC collection",
            inputSchema={
                "type": "object",
                "properties": {
                    "output_format": {
                        "type": "string",
                        "description": "Result output format: 'text' (default) or 'json'",
                        "enum": ["text", "json"],
                        "default": "text",
                    },
                    "collection_id": {
                        "type": "string",
                        "description": "ID of the collection to retrieve",
                    },
                    "catalog_url": {
                        "type": "string",
                        "description": "STAC catalog URL (optional, defaults to Microsoft Planetary Computer)",
                    },
                },
                "required": ["collection_id"],
            },
        ),
        Tool(
            name="search_items",
            description="Search for STAC items across collections",
            inputSchema={
                "type": "object",
                "properties": {
                    "output_format": {
                        "type": "string",
                        "description": "Result output format: 'text' (default) or 'json'",
                        "enum": ["text", "json"],
                        "default": "text",
                    },
                    "collections": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of collection IDs to search within",
                    },
                    "bbox": {
                        "type": "array",
                        "items": {"type": "number"},
                        "minItems": 4,
                        "maxItems": 4,
                        "description": "Bounding box [west, south, east, north] in WGS84",
                    },
                    "datetime": {
                        "type": "string",
                        "description": "Date/time filter (ISO 8601 format, e.g., '2023-01-01/2023-12-31')",
                    },
                    "query": {
                        "type": "object",
                        "description": "Additional query parameters for filtering items",
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of items to return",
                        "default": 10,
                        "minimum": 1,
                        "maximum": 100,
                    },
                    "catalog_url": {
                        "type": "string",
                        "description": "STAC catalog URL (optional, defaults to Microsoft Planetary Computer)",
                    },
                },
            },
        ),
        Tool(
            name="get_item",
            description="Get detailed information about a specific STAC item",
            inputSchema={
                "type": "object",
                "properties": {
                    "output_format": {
                        "type": "string",
                        "description": "Result output format: 'text' (default) or 'json'",
                        "enum": ["text", "json"],
                        "default": "text",
                    },
                    "collection_id": {
                        "type": "string",
                        "description": "ID of the collection containing the item",
                    },
                    "item_id": {
                        "type": "string",
                        "description": "ID of the item to retrieve",
                    },
                    "catalog_url": {
                        "type": "string",
                        "description": "STAC catalog URL (optional, defaults to Microsoft Planetary Computer)",
                    },
                },
                "required": ["collection_id", "item_id"],
            },
        ),
        Tool(
            name="estimate_data_size",
            description="Estimate data size for STAC items using lazy loading with odc.stac",
            inputSchema={
                "type": "object",
                "properties": {
                    "output_format": {
                        "type": "string",
                        "description": "Result output format: 'text' (default) or 'json'",
                        "enum": ["text", "json"],
                        "default": "text",
                    },
                    "collections": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of collection IDs to search within",
                    },
                    "bbox": {
                        "type": "array",
                        "items": {"type": "number"},
                        "minItems": 4,
                        "maxItems": 4,
                        "description": "Bounding box [west, south, east, north] in WGS84",
                    },
                    "datetime": {
                        "type": "string",
                        "description": "Date/time filter (ISO 8601 format, e.g., '2023-01-01/2023-12-31')",
                    },
                    "query": {
                        "type": "object",
                        "description": "Additional query parameters for filtering items",
                    },
                    "aoi_geojson": {
                        "type": "object",
                        "description": "Area of Interest as GeoJSON geometry for clipping (will use smallest bbox between this and bbox parameter)",
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of items to analyze for size estimation",
                        "default": 100,
                        "minimum": 1,
                        "maximum": 500,
                    },
                    "catalog_url": {
                        "type": "string",
                        "description": "STAC catalog URL (optional, defaults to Microsoft Planetary Computer)",
                    },
                },
            },
        ),
    ]
