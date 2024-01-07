#!/bin/sh
echo "Starting Application..."
uvicorn main:app --reload --port "$UVICORN_PORT" --host "$UVICORN_HOST"