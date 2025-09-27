from __future__ import annotations

import argparse
import sys
import warnings

from pepystats import api

# Deduplicated help strings (Sonar: avoid repeating literals)
PROJ_HELP = "Project name (on PyPI/pepy)"
GRAN_HELP = "Aggregation granularity"


def _print_err(msg: str) -> None:
    print(msg, file=sys.stderr)


def _add_common_time_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--months", type=int, default=3, help="Limit to the last N months (0 means all)")
    # Back-compat: accept but ignore --include-ci (deprecated).
    p.add_argument(
        "--include-ci",
        action="store_true",
        default=None,
        help="(deprecated; ignored) Historically toggled CI downloads in older APIs.",
    )


def _add_fmt_arg(p: argparse.ArgumentParser) -> None:
    p.add_argument("--fmt", choices=["md", "csv"], default="md", help="Output format")


def cmd_overall(args: argparse.Namespace) -> int:
    try:
        total = api.get_overall(args.project, months=args.months)
        print(int(total))
        return 0
    except Exception as e:
        _print_err(f"Error: {e}")
        return 1


def cmd_detailed(args: argparse.Namespace) -> int:
    try:
        df = api.get_detailed(args.project, months=args.months, granularity=args.granularity)
        print(api.to_markdown(df) if args.fmt == "md" else api.to_csv(df), end="" if args.fmt == "csv" else "\n")
        return 0
    except Exception as e:
        _print_err(f"Error: {e}")
        return 1


def cmd_versions(args: argparse.Namespace) -> int:
    try:
        df = api.get_versions(
            args.project,
            versions=args.versions,
            months=args.months,
            granularity=args.granularity,
        )
        print(api.to_markdown(df) if args.fmt == "md" else api.to_csv(df), end="" if args.fmt == "csv" else "\n")
        return 0
    except Exception as e:
        _print_err(f"Error: {e}")
        return 1


def cmd_recent(args: argparse.Namespace) -> int:
    try:
        df = api.get_recent(args.project, granularity=args.granularity)
        print(api.to_markdown(df) if args.fmt == "md" else api.to_csv(df), end="" if args.fmt == "csv" else "\n")
        return 0
    except Exception as e:
        _print_err(f"Error: {e}")
        return 1


def main(argv: list[str] | None = None) -> int | None:
    parser = argparse.ArgumentParser(prog="pepystats", description="CLI for pepy.tech stats")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # overall
    p_overall = sub.add_parser("overall", help="Print overall downloads total")
    p_overall.add_argument("project", help=PROJ_HELP)
    _add_common_time_args(p_overall)
    p_overall.set_defaults(func=cmd_overall)

    # detailed
    p_detailed = sub.add_parser("detailed", help="Print per-period totals (tidy)")
    p_detailed.add_argument("project", help=PROJ_HELP)
    _add_common_time_args(p_detailed)
    _add_fmt_arg(p_detailed)
    p_detailed.add_argument(
        "--granularity",
        choices=["daily", "weekly", "monthly", "yearly"],
        default="daily",
        help=GRAN_HELP,
    )
    p_detailed.set_defaults(func=cmd_detailed)

    # versions
    p_versions = sub.add_parser("versions", help="Print per-version totals per period")
    p_versions.add_argument("project", help=PROJ_HELP)
    p_versions.add_argument("--versions", nargs="+", required=True, help="Versions to include")
    _add_common_time_args(p_versions)
    _add_fmt_arg(p_versions)
    p_versions.add_argument(
        "--granularity",
        choices=["daily", "weekly", "monthly", "yearly"],
        default="daily",
        help=GRAN_HELP,
    )
    p_versions.set_defaults(func=cmd_versions)

    # recent (last 7 days)
    p_recent = sub.add_parser("recent", help="Print last 7 days of totals")
    p_recent.add_argument("project", help=PROJ_HELP)
    _add_fmt_arg(p_recent)
    p_recent.add_argument(
        "--granularity",
        choices=["daily", "weekly", "monthly", "yearly"],
        default="daily",
        help=GRAN_HELP,
    )
    p_recent.set_defaults(func=cmd_recent)

    args = parser.parse_args(argv)

    # Only warn if user actually supplied the flag.
    if getattr(args, "include_ci", None) is True:
        warnings.filterwarnings("default", category=DeprecationWarning)
        warnings.warn(
            "--include-ci is deprecated and ignored; pepy v2 does not expose CI filtering.",
            DeprecationWarning,
        )

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
