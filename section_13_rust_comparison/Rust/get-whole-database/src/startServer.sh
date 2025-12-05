#!/bin/bash

# RUST_LOG=error: Displays only error messages.
# RUST_LOG=warn: Displays warning and error messages.
# RUST_LOG=info: Displays info, warning, and error messages.
# RUST_LOG=debug: Displays debug, info, warning, and error messages.
# RUST_LOG=trace: Displays all log messages, including trace-level details.
# RUST_LOG=off: Disables all logging for the entire application.

export RUST_LOG="actix_web=info,get_whole_database=info"

cargo run

exit 0


