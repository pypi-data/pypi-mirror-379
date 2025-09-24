import sys
import warnings


def main():
    warnings.warn(
        "The CLI 'ctd-tools' is deprecated. Please use the CLI from 'seasenselib'.",
        DeprecationWarning,
        stacklevel=2,
    )
    try:
        from seasenselib.__main__ import main as _seasense_main
    except Exception:
        sys.stderr.write(
            "The package 'ctd-tools' has been renamed to 'seasenselib'.\n"
            "Please install and use 'seasenselib' instead.\n"
        )
        sys.exit(1)
    _seasense_main()


if __name__ == "__main__":
    main()
