import warnings as _warnings

_warnings.warn(
    "'ctd-tools' is deprecated and has been renamed to 'seasenselib'.\n"
    "Please switch to:\n"
    "    pip install seasenselib\n"
    "    from seasenselib import ...",
    DeprecationWarning,
    stacklevel=2,
)

try:
    from seasenselib import *  # noqa: F401,F403
except Exception as exc:
    raise ImportError(
        "'ctd-tools' is deprecated. Please install and import 'seasenselib' instead:\n"
        "    pip install seasenselib\n"
        "    from seasenselib import ..."
    ) from exc
