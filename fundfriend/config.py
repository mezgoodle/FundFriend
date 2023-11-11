#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """Bot Configuration"""

    PORT = os.environ.get("PORT", 8000)
    APP_ID = os.environ.get("MicrosoftAppId", "547df17e-07a6-4f8a-a745-a8bd3bf65a56")
    APP_PASSWORD = os.environ.get(
        "MicrosoftAppPassword", "U6g8Q~SV-3F1RtCwoiKrq4B14kkM_fQSeyUrLaUS"
    )
