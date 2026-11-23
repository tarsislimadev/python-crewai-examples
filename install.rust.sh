#!/usr/bin/env sh

set -eu

if ! command -v curl >/dev/null 2>&1; then
  echo "Error: curl is required to install Rust." >&2
  exit 1
fi

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs |
  sh -s -- -y
