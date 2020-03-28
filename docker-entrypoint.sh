#! /usr/bin/env sh

# SPDX-License-Identifier: MIT
#
# Copyright (c) 2019 Michael Herman
# Copyright (c) 2020 Louis Moureaux

python -m longturn.manage flush --no-input
python -m longturn.manage migrate

exec "$@"

