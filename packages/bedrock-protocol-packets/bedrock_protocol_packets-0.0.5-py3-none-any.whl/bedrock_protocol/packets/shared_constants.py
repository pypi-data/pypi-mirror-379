# Copyright © 2025 GlacieTeam. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
# distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0


class SharedConstants:
    @staticmethod
    def get_network_protocol_version() -> int:
        return 827

    @staticmethod
    def get_minecraft_version() -> str:
        return "1.21.100"
