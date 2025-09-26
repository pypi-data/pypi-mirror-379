#################################################################################
# WaterTAP Copyright (c) 2020-2025, The Regents of the University of California,
# through Lawrence Berkeley National Laboratory, Oak Ridge National Laboratory,
# National Renewable Energy Laboratory, and National Energy Technology
# Laboratory (subject to receipt of any required approvals from the U.S. Dept.
# of Energy). All rights reserved.
#
# Please see the files COPYRIGHT.md and LICENSE.md for full copyright and license
# information, respectively. These files are also available online at the URL
# "https://github.com/watertap-org/watertap/"
#################################################################################

import pytest

from watertap_contrib.reflo.flowsheets.KBHDP import (
    KBHDP_SOA,
    KBHDP_RPT_1,
    KBHDP_RPT_2,
    KBHDP_RPT_3,
    KBHDP_ZLD,
)


class TestKBHDPComponents:

    @pytest.mark.component
    def test_SOA(self):
        m = KBHDP_SOA.main()

    @pytest.mark.component
    def test_RPT1(self):
        m = KBHDP_RPT_1.main()

    @pytest.mark.component
    def test_RPT2(self):
        m = KBHDP_RPT_2.main()

    @pytest.mark.component
    def test_RPT3(self):
        m = KBHDP_RPT_3.main()

    @pytest.mark.component
    def test_ZLD(self):
        m = KBHDP_ZLD.main()
