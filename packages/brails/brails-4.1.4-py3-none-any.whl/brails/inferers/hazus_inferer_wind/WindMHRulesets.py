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

import random
from brails.inferers.hazus_inferer_wind.WindMetaVarRulesets import is_ready_to_infer

def MH_config(BIM):
    """
    Rules to identify a HAZUS WSF configuration based on BIM data

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


    if "Shutters" in BIM:
        shutters = BIM["Shutters"]

    elif is_ready_to_infer(available_features=available_features, needed_features = ["YearBuilt"], inferred_feature= "Shutters"):

        year = BIM['YearBuilt'] # just for the sake of brevity
        if year <= 1976:
            is_ready_to_infer(available_features=available_features, needed_features = ["WindBorneDebris"], inferred_feature= "Shutters")
            if BIM['WindBorneDebris']:
                shutters = random.random() < 0.45
            else:
                shutters = False
        elif year <= 1994:
            is_ready_to_infer(available_features=available_features, needed_features = ["WindBorneDebris"], inferred_feature= "Shutters")
            if BIM['WindBorneDebris']:
                shutters = random.random() < 0.45
            else:
                shutters = False
        else:
            # MH94HUD I, II, III
            is_ready_to_infer(available_features=available_features, needed_features = ["DesignWindSpeed"], inferred_feature= "Shutters")
            if BIM['DesignWindSpeed'] >= 100.0:
                shutters = True
            else:
                shutters = False

    if "TieDowns" in BIM:
        TD = BIM["TieDowns"]

    elif is_ready_to_infer(available_features=available_features, needed_features = ["YearBuilt"], inferred_feature= "TieDowns"):
        year = BIM['YearBuilt'] # just for the sake of brevity
        if year <= 1976:
            TD = random.random() < 0.45

        elif year <= 1994:
            TD = random.random() < 0.45

        else:
            is_ready_to_infer(available_features=available_features, needed_features = ["DesignWindSpeed"], inferred_feature= "TieDowns")
            if BIM['DesignWindSpeed'] >= 70.0:
                TD = True
            else:
                TD = False


    # is_ready_to_infer(available_features=available_features, needed_features = ["YearBuilt"], inferred_feature= "bldg_tag")
    # year = BIM['YearBuilt'] # just for the sake of brevity
    # if year <= 1976:
    #     bldg_tag = 'MH.PHUD'
    # elif year <= 1994:
    #     bldg_tag = 'MH.76HUD'
    # else:
    #     is_ready_to_infer(available_features=available_features, needed_features = ["WindZone"], inferred_feature= "BuildingTag")
    #     bldg_tag = 'MH.94HUD' + BIM['WindZone']


    is_ready_to_infer(available_features=available_features, needed_features = ['BuildingType','StructureType','LandCover','NumberOfStories'], inferred_feature= f"MH.XHUD class")
    essential_features = dict(
        BuildingType=BIM['BuildingType'],
        StructureType=BIM['StructureType'],
        LandCover=BIM['LandCover'],
        Shutters = int(shutters),
        TieDowns = int(TD),
        NumberOfStories = int(BIM['NumberOfStories'])
        )

    # extend the BIM dictionary
    BIM.update(dict(essential_features))

    # bldg_config = f"{bldg_tag}." \
    #               f"{int(shutters)}." \
    #               f"{int(TD)}." \
    #               f"{BIM['LandCover']}"

    return essential_features

