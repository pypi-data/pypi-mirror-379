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

def CECB_config(BIM):
    """
    Rules to identify a HAZUS CECB configuration based on BIM data

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


    if "RoofCover" in BIM:
        roof_cover = BIM["RoofCover"]

    elif is_ready_to_infer(available_features=available_features, needed_features = ["YearBuilt","RoofShape"], inferred_feature= "RoofCover"):
        # Roof cover
        if BIM['RoofShape'] in ['Gable', 'Hip']:
            roof_cover = 'Built-Up Roof'
            # Warning: HAZUS does not have N/A option for CECB, so here we use bur
        else:
            if BIM['YearBuilt'] >= 1975:
                roof_cover = 'Single-Ply Membrane'
            else:
                # year < 1975
                roof_cover = 'Built-Up Roof'

    if "Shutters" in BIM:
        shutters = BIM["Shutters"]

    elif is_ready_to_infer(available_features=available_features, needed_features = ["YearBuilt","WindBorneDebris"], inferred_feature= "Shutters"):
    
        # shutters
        if BIM['YearBuilt'] >= 2000:
            shutters = BIM['WindBorneDebris']
        # BOCA 1996 and earlier:
        # Shutters were not required by code until the 2000 IBC. Before 2000, the
        # percentage of commercial buildings that have shutters is assumed to be
        # 46%. This value is based on a study on preparedness of small businesses
        # for hurricane disasters, which says that in Sarasota County, 46% of
        # business owners had taken action to wind-proof or flood-proof their
        # facilities. In addition to that, 46% of business owners reported boarding
        # up their businesses before Hurricane Katrina. In addition, compliance
        # rates based on the Homeowners Survey data hover between 43 and 50 percent.
        else:
            if BIM['WindBorneDebris']:
                shutters = random.random() < 0.46
            else:
                shutters = False


    if "WindDebrisClass" in BIM:
        WIDD = BIM["WindDebrisClass"]

    elif is_ready_to_infer(available_features=available_features, needed_features = ["OccupancyClass"], inferred_feature= "WindDebrisClass"):
     
        # Wind Debris (widd in HAZSU)
        # HAZUS A: Res/Comm, B: Varies by direction, C: Residential, D: None
        WIDD = 'C' # residential (default)
        if BIM['OccupancyClass'] in ['RES1', 'RES2', 'RES3A', 'RES3B', 'RES3C','RES3D']:
            WIDD = 'C' # residential
        elif BIM['OccupancyClass'] == 'AGR1':
            WIDD = 'D' # None
        else:
            WIDD = 'A' # Res/Comm


    # if "WindowAreaRatio" in BIM:
    #     WWR = BIM["WindowAreaRatio"]

    # elif is_ready_to_infer(available_features=available_features, needed_features = ["WindowArea"], inferred_feature= "WindowAreaRatio"):
         
    #     # Window area ratio
    #     if BIM['WindowArea'] < 0.33:
    #         WWR = 'low'
    #     elif BIM['WindowArea'] < 0.5:
    #         WWR = 'med'
    #     else:
    #         WWR = 'hig'


    # is_ready_to_infer(available_features=available_features, needed_features = ['LandCover',"NumberOfStories"], inferred_feature= "C.ECB class")

    # if BIM['NumberOfStories'] <= 2:
    #     bldg_tag = 'C.ECB.L'
    # elif BIM['NumberOfStories'] <= 5:
    #     bldg_tag = 'C.ECB.M'
    # else:
    #     bldg_tag = 'C.ECB.H'

    # extend the BIM dictionary
    is_ready_to_infer(available_features=available_features, needed_features = ['StructureType',"BuildingType",'LandCover',"WindowArea","NumberOfStories"], inferred_feature= "C.ECB class")

    essential_features = dict(
        BuildingType=BIM['BuildingType'],
        StructureType=BIM['StructureType'],
        LandCover=BIM['LandCover'],
        RoofCover = roof_cover,
        Shutters = int(shutters),
        WindowArea = BIM['WindowArea'],
        NumberOfStories = int(BIM['NumberOfStories']),
        WindDebrisClass = WIDD
        )

        
    BIM.update(dict(essential_features))

    # bldg_config = f"{bldg_tag}." \
    #               f"{roof_cover}." \
    #               f"{int(shutters)}." \
    #               f"{WIDD}." \
    #               f"{WWR}." \
    #               f"{BIM['LandCover']}"

    return essential_features

