# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Leland Stanford Junior University
# Copyright (c) 2018 The Regents of the University of California
#
# This file is part of the SimCenter Backend Applications
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# You should have received a copy of the BSD 3-Clause License along with
# this file. If not, see <http://www.opensource.org/licenses/>.
#
# Contributors:
# Adam Zsarnóczay
# Kuanshi Zhong
#
# Based on rulesets developed by:
# Karen Angeles
# Meredith Lockhead
# Tracy Kijewski-Correa

import datetime
from brails.inferers.hazus_inferer_wind.WindMetaVarRulesets import is_ready_to_infer

def MLRI_config(BIM):
    """
    Rules to identify a HAZUS MLRI configuration based on BIM data

    Parameters
    ----------
    BIM: dictionary
        Information about the building characteristics.

    Returns
    -------
    config: str
        A string that identifies a specific configration within this buidling
        class.
    """
    available_features = BIM.keys()

    # Shutters

    if "Shutters" in BIM:
        shutters = BIM["Shutters"]
    else:
        shutters = False

    # Metal RDA
    # 1507.2.8.1 High Wind Attachment.
    # Underlayment applied in areas subject to high winds (Vasd greater
    # than 110 mph as determined in accordance with Section 1609.3.1) shall
    #  be applied with corrosion-resistant fasteners in accordance with
    # the manufacturer’s instructions. Fasteners are to be applied along
    # the overlap not more than 36 inches on center.

    if "RoofDeckAttachment" in BIM:
        MRDA = BIM["RoofDeckAttachment"]

    elif is_ready_to_infer(available_features=available_features, needed_features = ["DesignWindSpeed"], inferred_feature= "RoofDeckAttachment"):
        if BIM['DesignWindSpeed'] > 142:
            MRDA = 'Standard'  # standard
        else:
            MRDA = 'Superior'  # superior



    if "RoofQuality" in BIM:
        roof_quality = BIM["RoofQuality"]

    elif is_ready_to_infer(available_features=available_features, needed_features = ["RoofShape"], inferred_feature= "RoofQuality"):
        if BIM['RoofShape'] in ['Gable', 'Hip']:
            #roof_cover = '' # null
            roof_quality = 'Good' # default supported by HAZUS
        else:

            is_ready_to_infer(available_features=available_features, needed_features = ["YearBuilt"], inferred_feature= "RoofQuality")
            if BIM['YearBuilt'] >= 1975:
                #roof_cover = 'Single-Ply Membrane'
                if BIM['YearBuilt'] >= (datetime.datetime.now().year - 35):
                    roof_quality = 'Good'
                else:
                    roof_quality = 'Poor'
            else:
                # year < 1975
                #roof_cover = 'Built-Up Roof'
                if BIM['YearBuilt'] >= (datetime.datetime.now().year - 30):
                    roof_quality = 'Good'
                else:
                    roof_quality = 'Poor'


    is_ready_to_infer(available_features=available_features, needed_features = ['BuildingType','StructureType','LandCover','MasonryReinforcing'], inferred_feature= "M.LRI class")
    essential_features = dict(
        BuildingType=BIM['BuildingType'],
        StructureType=BIM['StructureType'],
        LandCover=BIM['LandCover'],
        RoofQuality = roof_quality,
        RoofDeckAttachment = MRDA,
        Shutters = int(shutters),
        MasonryReinforcing = int(BIM['MasonryReinforcing']),
        NumberOfStories = int(BIM['NumberOfStories'])
        )

    # extend the BIM dictionary
    BIM.update(dict(essential_features))

    # bldg_config = f"M.LRI." \
    #               f"{int(shutters)}." \
    #               f"{int(BIM['MasonryReinforcing'])}." \
    #               f"{roof_quality}." \
    #               f"{MRDA}." \
    #               f"{BIM['LandCover']}"

    return essential_features

