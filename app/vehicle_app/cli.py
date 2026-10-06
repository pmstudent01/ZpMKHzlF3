"""Command-line interface for the Vehicle Service app."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from .client import VehicleService
from .config import Config


def _print_result(result: Any) -> None:
    """Pretty-print an SDK result as JSON when possible."""
    # Pydantic models from the SDK expose model_dump(); dicts/lists print directly.
    if hasattr(result, "model_dump"):
        result = result.model_dump()
    try:
        print(json.dumps(result, indent=2, default=str))
    except (TypeError, ValueError):
        print(result)


def _add_vehicle_fields(parser: argparse.ArgumentParser) -> None:
    """Shared vehicle attribute options for create/update."""
    parser.add_argument("--nick-name", dest="nick_name")
    parser.add_argument("--vin")
    parser.add_argument("--make")
    parser.add_argument("--model")
    parser.add_argument("--year")
    parser.add_argument("--miles", type=int)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="vehicle_app",
        description="Interact with the Vehicle Service API via the generated SDK.",
    )
    parser.add_argument("--base-url", help="Override the API base URL.")
    parser.add_argument("--api-key", help="Override the API key (X-API-Key header).")

    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="List all vehicles.")

    get_p = sub.add_parser("get", help="Retrieve a vehicle by id.")
    get_p.add_argument("id", help="Vehicle id.")

    create_p = sub.add_parser("create", help="Create a vehicle.")
    _add_vehicle_fields(create_p)

    update_p = sub.add_parser("update", help="Update a vehicle by id.")
    update_p.add_argument("id", help="Vehicle id.")
    _add_vehicle_fields(update_p)

    delete_p = sub.add_parser("delete", help="Delete a vehicle by id.")
    delete_p.add_argument("id", help="Vehicle id.")

    return parser


def _build_service(args: argparse.Namespace) -> VehicleService:
    config = Config.from_env()
    if args.base_url:
        config = Config(base_url=args.base_url, api_key=config.api_key)
    if args.api_key:
        config = Config(base_url=config.base_url, api_key=args.api_key)
    return VehicleService(config)


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    service = _build_service(args)

    try:
        if args.command == "list":
            _print_result(service.list_vehicles())
        elif args.command == "get":
            _print_result(service.get_vehicle(args.id))
        elif args.command == "create":
            _print_result(
                service.create_vehicle(
                    nick_name=args.nick_name,
                    vin=args.vin,
                    make=args.make,
                    model=args.model,
                    year=args.year,
                    miles=args.miles,
                )
            )
        elif args.command == "update":
            _print_result(
                service.update_vehicle(
                    args.id,
                    nick_name=args.nick_name,
                    vin=args.vin,
                    make=args.make,
                    model=args.model,
                    year=args.year,
                    miles=args.miles,
                )
            )
        elif args.command == "delete":
            service.delete_vehicle(args.id)
            print(f"Deleted vehicle {args.id}.")
    except Exception as exc:  # noqa: BLE001 - surface SDK/request errors to the user
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
