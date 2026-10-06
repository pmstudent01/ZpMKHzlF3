# Vehicle Service App

A small Python application that implements the **Vehicle Service API** using the
generated `vehicle_service_collection_sdk` Python SDK (located under
`postman/sdks/Collections SDKs/Vehicle Service Collection/python`).

It exposes a simple command-line interface for all five vehicle operations:

| Command  | SDK method                 | HTTP            |
|----------|----------------------------|-----------------|
| `list`   | `get_all_vehicles()`       | `GET /vehicles`      |
| `get`    | `retrieve_a_vehicle(id)`   | `GET /vehicles/:id`  |
| `create` | `create_a_vehicle(body)`   | `POST /vehicles`     |
| `update` | `update_a_collection(body, id)` | `PATCH /vehicles/:id` |
| `delete` | `delete_a_vehicle(id)`     | `DELETE /vehicles/:id` |

## Setup

1. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```

2. Install the local SDK and this app's dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   `requirements.txt` installs the SDK from its local path, so no publishing to
   PyPI is required.

## Configuration

The app reads configuration from environment variables (a `.env` file is
supported via `python-dotenv`):

| Variable          | Description                               | Default                 |
|-------------------|-------------------------------------------|-------------------------|
| `VEHICLE_BASE_URL`| Base URL of the Vehicle Service API       | `http://localhost:4500` |
| `VEHICLE_API_KEY` | API key sent as the `X-API-Key` header    | _(none)_                |

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

> Tip: Point `VEHICLE_BASE_URL` at the running Postman mock server
> (e.g. `http://localhost:65252`) to try it without a real backend.

## Usage

```bash
# List all vehicles
python -m vehicle_app list

# Retrieve a single vehicle
python -m vehicle_app get 1

# Create a vehicle
python -m vehicle_app create \
  --nick-name "The Lisa Marie" \
  --vin 4M2DV11W4RDJ53329 \
  --make Mercury --model Villager --year 1994 --miles 159864

# Update a vehicle
python -m vehicle_app update 1 --miles 159999

# Delete a vehicle
python -m vehicle_app delete 1
```

All responses are printed as formatted JSON.
