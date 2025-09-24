# Copyright [2025] [SOPTIM AG]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import math

import numpy as np
import pandas as pd

from .pst_calculation import pst_transform
from .pst_test import dr_graf

# calculations from ENTSO-E Phase Shift Transformers Modelling
# α: tapAngle
# r: ratio
# ∂u: voltageStepIncrement
# θ: windingConnectionAngle

deg_to_rad = np.pi / 180


def calc_theta_k_2w(
    trafo: pd.Series, tapside: int, tapside_rtc: int
) -> tuple[float, float]:
    """Calculates theta and k for a 2-winding transformer
    based on the tapchanger type.

    Args:
        trafo (pd.Series): Transformer data
        tapside (int): Tap side (1 or 2)
    Returns:
        tuple: theta and k
    """
    theta, k = 0.0, 1.0
    taptype = trafo[f"taptype{tapside}"]

    if taptype == "PhaseTapChangerAsymmetrical" and tapside_rtc != 0:
        taptype = "InPhaseAndAsymPST"

    if taptype == "PhaseTapChangerTabular" and tapside_rtc != 0:
        taptype = "InPhaseAndTabularPST"

    match taptype:
        case "PhaseTapChangerTabular":
            theta = _calc_theta_tabular(trafo, tapside)
            k = _calc_k(trafo)
        case "InPhaseAndTabularPST":
            theta = _calc_theta_tabular(trafo, tapside)
            # k = _calc_k(trafo)
            k = calc_k_from_rtc_and_tabular(trafo, tapside, tapside_rtc)
            ## TODO: RTC auswerten
        case "PhaseTapChangerLinear":
            theta = _calc_theta_linear(trafo, tapside)
            k = _calc_k(trafo)
        case "PhaseTapChangerSymmetrical":
            theta = _calc_theta_symmetrical(trafo, tapside)
            k = _calc_k(trafo)
            # k, theta = _calc_theta_symmetrical_tng(trafo, tapside)
        case "PhaseTapChangerAsymmetrical":
            logging.warning("Found Transformer with a PhaseTapChangerAsymmetrical.")
            logging.warning("\tElectrical Parameters may be inaccurate.")
            a = complex(1, 0)
            theta, k = _calc_theta_k_asymmetrical(trafo, tapside)
            # k = calc_k_from_step_size_only_asym_no_rtc(
            #     trafo,
            #     tapside,
            #     theta,
            #     trafo["nomU1"],
            #     trafo["nomU2"],
            #     trafo["ratedU1"],
            #     trafo["ratedU2"],
            # )
            #  k = 0.99
        case "PhaseTapChanger" | "PhaseTapChangerNonLinear":
            logging.warning(
                "Tapchanger type %s for transformer %s is an abstract class",
                taptype,
                trafo["name1"],
            )
        case "InPhaseAndAsymPST":
            # theta, k = _calc_theta_k_asymmetrical(trafo, tapside)
            theta, k = calc_k_from_step_size_asym_with_rtc(trafo, tapside, tapside_rtc)
            # k = calc_k_from_step_size(
            #     trafo,
            #     tapside_rtc,
            #     trafo["nomU1"],
            #     trafo["nomU2"],
            #     trafo["ratedU1"],
            #     trafo["ratedU2"],
            # )
            # k -= 0.05
        case _:
            logging.warning(
                "Unknown tapchanger type %s for transformer %s",
                taptype,
                trafo["name1"],
            )

    return theta, k


def calc_k_from_step_size(
    trafo,
    winding,
    node_u1,
    node_u2,
    trafo_u1,
    trafo_u2,
):
    step = trafo[f"step{winding}_rtc"]
    if np.isnan(step):
        step = 0
        neutral_step = 0
        step_size_kv = 0

    else:
        neutral_step = trafo[f"neutralStep{winding}_rtc"]
        step_size = trafo[f"stepSize{winding}"]
        if winding == 1:
            step_size_kv = trafo_u1 * (step_size / 100)
        elif winding == 2:
            step_size_kv = trafo_u2 * (step_size / 100)
        else:
            step_size_kv = 0.0

    u1_corr = trafo_u1
    u2_corr = trafo_u2
    if winding == 1:
        u1_corr += (step - neutral_step) * step_size_kv
    elif winding == 2:
        u2_corr += (step - neutral_step) * step_size_kv

    nominal_ratio = node_u1 / node_u2

    _k = (u1_corr / u2_corr) / nominal_ratio

    return _k


def calc_k_from_step_size_only_asym_no_rtc(
    trafo,
    winding,
    theta,
    node_u1,
    node_u2,
    trafo_u1,
    trafo_u2,
):
    step = trafo[f"step{winding}"]
    if np.isnan(step):
        step = 0
        neutral_step = 0
        step_size_kv = 0

    else:
        neutral_step = trafo[f"neutralStep{winding}"]
        step_size = trafo[f"stepVoltageIncrement{winding}"]
        if winding == 1:
            step_size_kv = trafo_u1 * (step_size / 100)
            # step_size_kv = step_size
        elif winding == 2:
            step_size_kv = trafo_u2 * (step_size / 100)
            # step_size_kv = step_size
        else:
            step_size_kv = 0.0

    u1_corr = trafo_u1
    u2_corr = trafo_u2
    if winding == 1:
        u1_corr += (step - neutral_step) * step_size_kv
    elif winding == 2:
        u2_corr += (step - neutral_step) * step_size_kv

    nominal_ratio = node_u1 / node_u2

    _k = (u1_corr / u2_corr) / nominal_ratio

    return _k


t = """

 0.99 = (u1_corr / u2_corr) / nominal_ratio
=> 0.99 * nominal_ratio = u1_corr / u2_corr
=> 0.99 * nominal_ratio * u2_corr = u1_corr
=> 0.99 * nominal_ratio * u2_corr = trafo_u1 + 13 *step_size_kv
=> 0.99 * nominal_ratio * u2_corr - trafo_u1 = 13 *step_size_kv
"""


def calc_k_from_step_size_asym_with_rtc(
    trafo,
    tapside,
    tapside_rtc,
):
    ## PST
    ### steps = trafo[f"neutralStep{tapside}"] - trafo[f"step{tapside}"]
    steps = trafo[f"step{tapside}"] - trafo[f"neutralStep{tapside}"]

    voltage_increment = trafo[f"stepVoltageIncrement{tapside}"]
    winding_connection_angle = trafo[f"windingConnectionAngle{tapside}"] * deg_to_rad

    ## RTC

    ### steps_rtc = trafo[f"neutralStep{tapside_rtc}_rtc"] - trafo[f"step{tapside_rtc}_rtc"]
    steps_rtc = trafo[f"step{tapside_rtc}_rtc"] - trafo[f"neutralStep{tapside_rtc}_rtc"]
    voltage_increment_rtc = trafo[f"stepSize{tapside_rtc}"]

    # # if 1 == 1:
    u_netz1 = trafo["nomU1"]
    u_netz2 = trafo["nomU2"]
    u_rated1 = trafo["ratedU1"]
    u_rated2 = trafo["ratedU2"]

    # steps = 2 ## -13
    # steps_rtc = 10 ## 13

    theta, k = funct2(
        tapside,
        tapside_rtc,
        u_netz1,
        u_netz2,
        u_rated1,
        u_rated2,
        winding_connection_angle,
        voltage_increment,
        steps,
        voltage_increment_rtc,
        steps_rtc,
    )

    # k = 1 / k
    # theta *= -1

    if "TNG_Transformator_4" in trafo["name1"]:
        for step_pst in range(-13, 14):
            for step_rtc in range(-13, 14):
                theta_tmp, k_tmp = funct2(
                    tapside,
                    tapside_rtc,
                    u_netz1,
                    u_netz2,
                    u_rated1,
                    u_rated2,
                    winding_connection_angle,
                    voltage_increment,
                    step_pst,
                    voltage_increment_rtc,
                    step_rtc,
                )
                k_tmp = 1 / k_tmp
                if k_tmp > 0.84 and k_tmp < 0.85:
                    print(
                        ""
                        f"steps: {step_pst:2d}, {step_rtc:2d}  ->  k: {k_tmp:.5f}, theta: {theta_tmp:.5f}"
                    )

        wait = 1

    fun = lambda uu: rads(
        pst_transform(
            complex(1, 0),
            steps,
            steps_rtc,
            winding_connection_angle / deg_to_rad,
            uu,  # voltage_increment,
            voltage_increment_rtc,
            0,
            0,
            True,
        )
    )
    ### --------------

    if tapside_rtc == 1:
        step_size_kv = u_rated1 * (voltage_increment_rtc / 100)
    elif tapside_rtc == 2:
        step_size_kv = u_rated2 * (voltage_increment_rtc / 100)
    else:
        step_size_kv = 0.0

    corr_u_tc = steps_rtc * step_size_kv
    corr_u_tc = 0.0 if np.isnan(corr_u_tc) else corr_u_tc

    corr_u1 = u_rated1
    corr_u2 = u_rated2
    if tapside_rtc == 1:
        corr_u1 += corr_u_tc
    elif tapside_rtc == 2:
        corr_u2 += corr_u_tc

    ####----------

    nominal_ratio_ = u_netz1 / u_netz2
    rr = (corr_u1 / corr_u2) / nominal_ratio_

    w0 = (u_rated2 / u_netz2) / (u_rated1 / u_netz1)
    r = rr
    k1, theta1 = r_beta(r, winding_connection_angle, steps, voltage_increment)

    # theta = res1_theta
    # k = res1_k

    # Theta = 0.13935403130192373
    # k  = 0.8454636719045613
    # return theta, k

    ## from copilot
    # k = 0.8503296603006003
    # theta = -0.12927500404814304

    ## from Dr Graf
    # k = 0.8432341842306574
    # theta = -0.10962044394998548

    ### oben alt, unten neu und gut

    k, theta = dr_graf(
        rtc_tapside=tapside_rtc,
        rtc_step=steps_rtc,
        rtc_voltage_increment=voltage_increment_rtc,
        pst_tapside=tapside,
        pst_step=steps,
        pst_voltage_increment=voltage_increment,
        winding_connection_angle=winding_connection_angle / deg_to_rad,
        u_rated1=u_rated1,
        u_rated2=u_rated2,
        u_netz1=u_netz1,
        u_netz2=u_netz2,
    )

    return theta, k


def r_beta(r, winding_connection_angle_rad, steps, voltage_increment_percent):
    z = winding_connection_angle_rad
    beta = steps * (voltage_increment_percent / 100)
    ## beta = steps * (voltage_increment_percent )

    k = r * np.sqrt((1 + beta * np.cos(z)) ** 2 + (beta * np.sin(z)) ** 2)

    alpha = np.arctan2(beta * np.sin(z), (1 + beta * np.cos(z)))

    return k, alpha


def rads(x: tuple[complex, float, float]):
    u, k, theta = x
    return u, k, theta * deg_to_rad


def calc_k_from_rtc_and_tabular(
    trafo,
    tapside,
    tapside_rtc,
):
    ## PST
    # steps = trafo[f"neutralStep{tapside}"] - trafo[f"step{tapside}"]
    # voltage_increment = trafo[f"stepVoltageIncrement{tapside}"]
    # winding_connection_angle = trafo[f"windingConnectionAngle{tapside}"] * deg_to_rad

    ## RTC

    steps_rtc = trafo[f"neutralStep{tapside_rtc}_rtc"] - trafo[f"step{tapside_rtc}_rtc"]
    voltage_increment_rtc = trafo[f"stepSize{tapside_rtc}"]

    ## Testing
    steps_rtc = 2

    # # if 1 == 1:
    u_netz1 = trafo["nomU1"]
    u_netz2 = trafo["nomU2"]
    u_rated1 = trafo["ratedU1"]
    u_rated2 = trafo["ratedU2"]

    # steps = 2 ## -13
    # steps_rtc = 10 ## 13

    k = funct3_tabular_mit_ratio(
        trafo,
        tapside,
        u_netz1,
        u_netz2,
        u_rated1,
        u_rated2,
        voltage_increment_rtc,
        steps_rtc,
    )

    k = 1 / k

    # theta *= -1

    # if "TNG_Transformator_4" in trafo["name1"]:
    #     for step_pst in range(-13, 14):
    #         for step_rtc in range(-13, 14):
    #             theta_tmp, k_tmp = funct2(
    #                 tapside,
    #                 u_netz1,
    #                 u_netz2,
    #                 u_rated1,
    #                 u_rated2,
    #                 winding_connection_angle,
    #                 voltage_increment,
    #                 step_pst,
    #                 voltage_increment_rtc,
    #                 step_rtc,
    #             )
    #             k_tmp = 1 / k_tmp
    #             if k_tmp > 0.84 and k_tmp < 0.85:
    #                 print(
    #                     ""
    #                     f"steps: {step_pst:2d}, {step_rtc:2d}  ->  k: {k_tmp:.5f}, theta: {theta_tmp:.5f}"
    #                 )

    #     wait = 1

    # return 0.0, 1.0
    return k


def calc_theta_k_3w(trafo, tapside, current_side):
    """Calculates theta and k for a 3-winding transformer

    Args:
        trafo (pd.Series): Transformer data
        tapside (int): Tap side of the transformer
        current_side (int): Current side of the transformer

    Returns:
        tuple: theta and k
    """
    if tapside == current_side:
        return calc_theta_k_2w(trafo, tapside)

    # The current 2w is a trafo without a tapchanger
    return 0.0, _calc_k(trafo)


def _calc_theta_tabular(trafo, tapside):

    # --- Shift theta ---
    tc_angle1 = trafo["tcAngle1"]
    tc_angle2 = trafo["tcAngle2"]

    tc_angle = tc_angle1 if not np.isnan(tc_angle1) else tc_angle2

    theta = tc_angle * deg_to_rad

    if tapside == 2:
        theta *= -1

    return theta


def _calc_theta_linear(trafo, tapside):
    # s = n-n_0
    # α = s * ∂α
    # r = 1

    steps = trafo[f"neutralStep{tapside}"] - trafo[f"step{tapside}"]
    shift_per_step = trafo[f"stepPhaseShift{tapside}"] * deg_to_rad
    theta = steps * shift_per_step

    # TODO: check with an example where tapside == 2
    if tapside == 1:
        theta *= -1

    return theta


def _calc_theta_symmetrical(trafo, tapside):
    # s = n-n_0
    # α = 2 * atan(0.5 * s * ∂u)
    # r = 1
    steps = trafo[f"neutralStep{tapside}"] - trafo[f"step{tapside}"]
    voltage_increment = trafo[f"stepVoltageIncrement{tapside}"]

    ## from ENTSO-E "Phase Shift Transformers Modelling", chapter 4.2
    theta = 2.0 * np.arctan(0.5 * steps * voltage_increment)

    # TODO: check with an example where tapside == 2
    if tapside == 1:
        theta *= -1

    return theta


## schlechtere Ergebnisse als mit _calc_theta_symmetrical()
def _calc_theta_symmetrical_tng(trafo, tapside):
    # s = n-n_0
    # α = 2 * atan(0.5 * s * ∂u)
    # r = 1
    steps = trafo[f"neutralStep{tapside}"] - trafo[f"step{tapside}"]
    voltage_increment = trafo[f"stepVoltageIncrement{tapside}"]
    theta = 2.0 * np.arctan(0.5 * steps * voltage_increment)

    a, abs_a, phi_deg = pst_sym_factor(
        trafo[f"step{tapside}"], trafo[f"neutralStep{tapside}"], voltage_increment
    )
    theta *= deg_to_rad
    theta *= 0.5

    # TODO: check with an example where tapside == 2
    if tapside == 1:
        theta *= -1

    return abs_a, theta

    # s = n-n_0


## schlechtere Ergebnisse als mit _calc_theta_symmetrical()
def pst_sym_factor(step, neutral_step, voltage_step_increment_deg):
    """
    Berechnet den komplexen Übertragungsfaktor a = k * exp(j*phi)
    für einen symmetrischen PST (PhaseTapChangerSymmetrical).

    Parameter
    ---------
    step : int
        Aktuelle Stufenstellung (z. B. -13 ... +13).
    neutral_step : int
        Neutralstellung (meist 0).
    voltage_step_increment_deg : float
        Schrittweite in Grad (z. B. 1.0 = 1° pro Stufe).

    Rückgabe
    --------
    a : complex
        Komplexer Übertragungsfaktor (Betrag ≈ 1, Winkel in rad).
    k : float
        Betrag des Faktors.
    phi_deg : float
        Phasenwinkel in Grad.
    """

    # Differenz zur Neutralstellung
    delta_step = step - neutral_step

    # Phasenwinkel in Grad
    phi_deg = delta_step * voltage_step_increment_deg

    # Umrechnung in Radiant
    phi_rad = math.radians(phi_deg)

    # Komplexer Faktor (Betrag ~ 1, nur Winkeländerung)
    a = math.cos(phi_rad) + 1j * math.sin(phi_rad)

    return a, abs(a), phi_deg


def _calc_theta_k_asymmetrical(trafo, tapside):
    # z = s * ∂u * sin(θ)
    # tan(α) = (z)/(1 + s * ∂u * cos(θ))
    # 1/r = √[z^2 + (1 + z)^2]

    # steps = trafo[f"neutralStep{tapside}"] - trafo[f"step{tapside}"]
    steps = trafo[f"step{tapside}"] - trafo[f"neutralStep{tapside}"]
    ## steps = 8 TODO: Prüfer wo der Wert herkommt
    # voltage_increment = trafo[f"stepVoltageIncrement{tapside}"]
    voltage_increment = trafo[f"stepVoltageIncrement{tapside}"]
    winding_connection_angle = trafo[f"windingConnectionAngle{tapside}"] * deg_to_rad

    # z = steps * voltage_increment * np.sin(winding_connection_angle)

    # theta = np.arctan(
    #     z / (1 + steps * voltage_increment * np.cos(winding_connection_angle))
    # )

    # # FIXME: Both calculations produce inaccurate results
    # r = 1 / np.sqrt(z**2 + (1 + z) ** 2)
    # k = _calc_k(trafo)
    # # r = 1 / np.sqrt(
    # #     (z) ** 2 + (1 + z) ** 2
    # # )
    # k = 1 - r

    # if tapside == 1:
    #     theta *= -1

    # # if 1 == 1:
    u_netz1 = trafo["nomU1"]
    u_netz2 = trafo["nomU2"]
    u_rated1 = trafo["ratedU1"]
    u_rated2 = trafo["ratedU2"]
    # w0 = (u_rated2 / u_netz2) / (u_rated1 / u_netz1)

    # alpha_strich = complex(np.cos(winding_connection_angle), np.sin(winding_connection_angle))

    # tmp  = 1 + voltage_increment / 100 * steps * alpha_strich

    # t_strich = w0 / (tmp)
    # # t_strich = 1/t_strich

    # k = np.abs(t_strich)
    # theta = np.angle(t_strich)

    theta, k = funct(
        tapside,
        u_netz1,
        u_netz2,
        u_rated1,
        u_rated2,
        winding_connection_angle,
        voltage_increment,
        steps,
    )

    w0 = (u_rated2 / u_netz2) / (u_rated1 / u_netz1)
    k1, theta1 = r_beta(w0, winding_connection_angle, steps, voltage_increment)

    ###### oben alt, unten neu und gut

    k, theta = dr_graf(
        rtc_tapside=0,
        rtc_step=0,
        rtc_voltage_increment=0,
        pst_tapside=tapside,
        pst_step=steps,
        pst_voltage_increment=voltage_increment,
        winding_connection_angle=winding_connection_angle / deg_to_rad,
        u_rated1=u_rated1,
        u_rated2=u_rated2,
        u_netz1=u_netz1,
        u_netz2=u_netz2,
    )

    return theta, k
    # return theta1, 1/k1


def funct(
    tapside,
    u_netz1,
    u_netz2,
    u_rated1,
    u_rated2,
    winding_connection_angle,
    voltage_increment,
    steps,
):
    w0 = (u_rated2 / u_netz2) / (u_rated1 / u_netz1)
    if tapside == 1:
        w0 = 1 / w0

    alpha_strich = complex(
        np.cos(winding_connection_angle), np.sin(winding_connection_angle)
    )

    tmp = 1 + voltage_increment / 100 * steps * alpha_strich

    t_strich = w0 / (tmp)
    # t_strich = 1/t_strich

    k = np.abs(t_strich)
    theta = np.angle(t_strich)

    if tapside == 1:
        theta *= -1  ## TODO: validieren !!!!

    # return 0.0, 1.0
    return theta, k


def funct2(
    tapside,
    tapside_rtc,
    u_netz1,
    u_netz2,
    u_rated1,
    u_rated2,
    winding_connection_angle,
    voltage_increment,
    steps,
    voltage_increment_rtc,
    steps_rtc,
):
    ## für TNG_Transformator_4 => k=0.845464 theta=0.139354
    # if tapside_rtc == 1:
    if u_netz1 != u_netz2:
        w0 = (u_rated2 / u_netz2) / (u_rated1 / u_netz1)

        ### PST
        alpha_strich = complex(
            np.cos(winding_connection_angle), np.sin(winding_connection_angle)
        )

        tmp = 1 + voltage_increment / 100 * steps * alpha_strich

        t_strich = w0 / (tmp)
        # t_strich = 1/t_strich

        k_pst = np.abs(t_strich)
        theta_pst = np.angle(t_strich)

        if tapside == 1:
            theta_pst *= -1  ## TODO: validieren !!!!

        ## TODO:  potentiell u_rated2 und u_netz2 wenn PST an Seite 2 hängt???
        u_tot = steps * (voltage_increment / 100) * u_rated1
        epsilon = u_tot / u_netz1
    else:
        w0 = (u_rated2 / u_netz2) / (u_rated1 / u_netz1)

        u_tot = steps * (voltage_increment / 100) * u_rated2
        epsilon = u_tot / u_netz2

    ### RTC

    ## k_tap = w0 * (1 + (voltage_increment_rtc / 100 * steps_rtc)) ## w0 von steps beinflusst, aber nicht von steps_rtc !!!!
    ## k_tap = (1.0/w0) * (1 + (voltage_increment_rtc / 100 * steps_rtc))
    k_tap = w0 * (
        1
        + ((u_rated2 / u_netz2) * (voltage_increment_rtc / 100) * steps_rtc)
        # 1 + ((u_rated1 / u_netz1) * (voltage_increment_rtc / 100) * steps_rtc)
    )

    ## COMBINED

    k = k_tap * np.sqrt(
        (1 + epsilon * np.cos(winding_connection_angle)) ** 2
        + (epsilon * np.sin(winding_connection_angle)) ** 2
    )
    theta = np.arctan2(
        epsilon * np.sin(winding_connection_angle),
        1 + epsilon * np.cos(winding_connection_angle),
    )

    ## PST 1
    # k = 0.94
    # theta = 0.29

    ## für "TNG_PST 1" => k=0.956227 theta=0.296973
    # if winding_connection_angle / deg_to_rad == 90:# and tapside_rtc == 2:
    if u_netz1 == u_netz2:

        u_rated_xx = u_rated1
        steps_rtc_xx = steps_rtc
        if tapside_rtc == 2:
            u_rated_xx = u_rated2
            steps_rtc_xx = -steps_rtc

        r = (
            u_rated_xx + (u_rated_xx * (voltage_increment_rtc / 100) * steps_rtc_xx)
        ) / u_netz1

        v_1 = u_rated_xx * r
        v_r = u_rated_xx * (voltage_increment / 100) * steps
        alpha = np.arctan2(
            v_r * np.sin(winding_connection_angle),
            v_1 + v_r * np.cos(winding_connection_angle),
        )

        betrag = np.sqrt(
            v_1**2 + v_r**2 + 2 * v_1 * v_r * np.cos(winding_connection_angle)
        )
        k = v_1 / betrag

        theta = alpha

    return theta, k


def funct3_tabular_mit_ratio(
    trafo,
    tapside,
    u_netz1,
    u_netz2,
    u_rated1,
    u_rated2,
    voltage_increment_rtc,
    steps_rtc,
):
    w0 = (u_rated2 / u_netz2) / (u_rated1 / u_netz1)
    if tapside == 1:
        w0 = 1 / w0

    ### PST
    tc_ratio1 = trafo["tcRatio1"]
    tc_ratio2 = trafo["tcRatio2"]
    tc_ratio = 1  ## dummy

    if not np.isnan(tc_ratio1):
        tc_ratio = tc_ratio1
        # tc_ratio = 1 / tc_ratio
    elif not np.isnan(tc_ratio2):
        tc_ratio = tc_ratio2
        # tc_ratio = 1 / tc_ratio

    ### RTC

    k_tap = w0 * (1 + (voltage_increment_rtc / 100 * steps_rtc))

    ## COMBINED
    k = k_tap * tc_ratio

    return k


uu = """

    [410kv] U1   ----oo----  U2 [230 kv]

                w0
    t = -------------------
        1 + du / 100 * step

                  w0                             w0
    t = -----------------------  <OP>  -----------------------
        1 + du / 100 * (step/2)        1 + du / 100 * (step/2)

              w0                        w0
    t = -----------------  <OP>  -----------------
        1 + v_increment/2        1 + v_increment/2


"""


def _calc_k(trafo):
    nominal_ratio_ = trafo["nomU1"] / trafo["nomU2"]
    rated_u1_ = trafo["ratedU1"]
    rated_u2_ = trafo["ratedU2"]

    tc_ratio1 = trafo["tcRatio1"]
    tc_ratio2 = trafo["tcRatio2"]

    corr_u1_ = rated_u1_
    corr_u2_ = rated_u2_
    if not np.isnan(tc_ratio1):
        # tc_ratio1 = 1 / tc_ratio1
        corr_u1_ *= tc_ratio1
    elif not np.isnan(tc_ratio2):
        corr_u2_ *= tc_ratio2
    k = (corr_u1_ / corr_u2_) / nominal_ratio_

    k = 1 / k  ## bei MSHIP ist der Kehrwert besser, bei 50Hz nicht
    return k
