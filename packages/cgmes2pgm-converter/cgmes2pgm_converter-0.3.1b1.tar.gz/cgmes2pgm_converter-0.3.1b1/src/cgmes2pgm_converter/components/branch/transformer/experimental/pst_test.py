import cmath
import math
from os import wait

import numpy as np


def _calc_rated_ratio(rated_u1, rated_u2, nominal_ratio):
    return (rated_u1 / rated_u2) / nominal_ratio


def _calc_ratio_from_step(
    end,
    step_,
    step_neutral_,
    step_size_,
    rated_u1,
    rated_u2,
    nominal_ratio,
):
    if end == 1:
        step_size_kv = rated_u1 * (step_size_ / 100)
    elif end == 2:
        step_size_kv = rated_u2 * (step_size_ / 100)
    else:
        step_size_kv = 0.0

    corr_u_tc = (step_ - step_neutral_) * step_size_kv
    corr_u_tc = 0.0 if np.isnan(corr_u_tc) else corr_u_tc

    corr_u1 = rated_u1
    corr_u2 = rated_u2
    if end == 1:
        corr_u1 += corr_u_tc
    elif end == 2:
        corr_u2 += corr_u_tc

    return _calc_rated_ratio(corr_u1, corr_u2, nominal_ratio)


deg_to_rad = np.pi / 180


def chapter8(
    rtc_tapside,
    rtc_step,
    rtc_voltage_increment,
    pst_tapside,
    pst_step,
    pst_voltage_increment,
    winding_connection_angle,
    u_rated1,
    u_rated2,
    u_netz1,
    u_netz2,
):

    nominal_ratio_ = u_netz1 / u_netz2
    k = _calc_ratio_from_step(
        rtc_tapside,
        rtc_step,
        0,
        rtc_voltage_increment,
        u_rated1,
        u_rated2,
        nominal_ratio_,
    )

    # -------
    winding_connection_angle_rad = winding_connection_angle * deg_to_rad
    theta_rad = (180 - winding_connection_angle) * deg_to_rad
    pst_zusatz_v_betrag = (pst_voltage_increment / 100) * pst_step

    pst_zusatz_v_complex = cmath.rect(
        pst_zusatz_v_betrag,
        # winding_connection_angle * deg_to_rad
        theta_rad,
    )

    v1_complex = cmath.rect(k, 0.0)

    v2_complex = v1_complex + pst_zusatz_v_complex

    a = abs(pst_zusatz_v_complex)
    b = abs(v2_complex)
    c = abs(v1_complex)

    b2 = np.sqrt(a**2 + c**2)

    alpha = np.angle(v2_complex)
    # alpha = np.acos((-(a**2) + b**2 + c**2) / (2 * b * c))

    zz = np.tan(alpha) / (
        np.sin(winding_connection_angle_rad)
        - np.tan(alpha) * np.cos(winding_connection_angle_rad)
    )
    c1 = complex(1, winding_connection_angle_rad)
    z = 1 + c1 * zz

    z2 = z * k
    ## ----

    print(f"RTC k = {k} alpha = {alpha}")

    # r = rtc_step * (rtc_voltage_increment / 100)

    return 1, 2, 3


def copilot_test():
    # Daten
    u1_nom = 380
    u1_rated = 410
    u2_nom = 110
    u2_rated = 115

    # RTC
    step_rtc = -13
    du_rtc = 1

    # PST
    step_pst = 13
    du_pst = 1
    theta_deg = 90
    theta_rad = np.deg2rad(theta_deg)

    # k_RTC
    w0 = (u2_rated / u2_nom) / (u1_rated / u1_nom)
    k_rtc = w0 / (1 + step_rtc * du_rtc / 100)

    # t_PST
    alpha = np.exp(1j * theta_rad)
    t_pst = 1 / (1 + step_pst * du_pst / 100 * alpha)

    # Gesamt
    t_total = k_rtc * t_pst

    k = abs(t_total)
    theta = np.angle(t_total)

    print("k =", k)
    print("theta =", theta)


def copilot_test2():
    u1_nom = 380
    u1_rated = 410
    u2_nom = 110
    u2_rated = 115

    # step_rtc = -13
    # du_rtc = 1
    step_rtc = 13
    du_rtc = 1

    step_pst = 13
    du_pst = 1
    theta_deg = 90
    theta_rad = np.deg2rad(theta_deg)

    w0 = (u2_rated / u2_nom) / (u1_rated / u1_nom)

    rtc_factor = 1 + step_rtc * du_rtc / 100
    pst_factor = 1 + step_pst * du_pst / 100 * np.exp(1j * theta_rad)

    t_total = w0 / (rtc_factor * pst_factor)

    k = abs(t_total)
    theta = np.angle(t_total)

    print("k =", k)
    print("theta =", theta)


def dr_graf(
    rtc_tapside,
    rtc_step,
    rtc_voltage_increment,
    pst_tapside,
    pst_step,
    pst_voltage_increment,
    winding_connection_angle,
    u_rated1,
    u_rated2,
    u_netz1,
    u_netz2,
):
    angle = winding_connection_angle * deg_to_rad
    w0 = (u_rated2 / u_netz2) / (u_rated1 / u_netz1)
    ## w0 = (u_rated1 / u_netz1) / (u_rated2 / u_netz2)

    #
    # RTC
    #

    if rtc_tapside == 0:
        t_rtc = 1
    else:

        if rtc_tapside == pst_tapside:
            rtc_step = -rtc_step

        nenner_rtc = 1 + ((rtc_step / 100) * rtc_voltage_increment) * complex(
            np.cos(0), np.sin(0)
        )
        t_rtc = w0 / nenner_rtc

        # if rtc_tapside == pst_tapside:
        #     w0 = 1

    w0 = w0 * abs(t_rtc)

    ## TODO: abhängig von rtc_tapside oder pst_tapside?
    w0 = 1 / w0

    #
    # PST
    #

    nenner_pst = 1 + ((pst_step / 100) * pst_voltage_increment) * complex(
        np.cos(angle), np.sin(angle)
    )
    t_pst = w0 / nenner_pst

    print(t_rtc)
    print(t_pst)

    ## ----------------------

    if rtc_tapside == 0:
        k = abs(t_pst)
        theta = np.angle(t_pst)
    else:
        k = 1 / abs(t_pst)
        theta = -np.angle(t_pst)

    ## 0.956227 0.296973
    wait = 1
    # return k, theta
    return k, theta


def dr_schaefer(
    rtc_tapside,
    rtc_step,
    rtc_voltage_increment,
    pst_tapside,
    pst_step,
    pst_voltage_increment,
    winding_connection_angle,
    u_rated1,
    u_rated2,
    u_netz1,
    u_netz2,
):
    phi = winding_connection_angle * deg_to_rad
    w0 = (u_rated2 / u_netz2) / (u_rated1 / u_netz1)

    sin_2 = np.sin(phi) ** 2
    cos_2 = np.cos(phi) ** 2
    t = w0
    t = 1

    t_re = sin_2 + np.sqrt(sin_2**2 - sin_2 + t**2 * cos_2)

    t_im = -np.sin(phi) * np.cos(phi) + np.tan(phi) * np.sqrt(
        sin_2**2 - sin_2 + t**2 * cos_2
    )

    t = complex(t_re, t_im)

    k = 1 / abs(t)
    theta = -np.angle(t)
    return k, theta


# --- Beispiel ---
if __name__ == "__main__":
    U1 = 1.0 + 0j  # Referenzspannung
    ## Transformer_4
    U2, k, alpha = chapter8(
        rtc_tapside=1,
        rtc_step=-13,
        rtc_voltage_increment=1.0,
        pst_tapside=1,
        pst_step=13,
        pst_voltage_increment=1.0,
        winding_connection_angle=90,
        u_rated1=410.0,
        u_rated2=115.0,
        u_netz1=380.0,
        u_netz2=110.0,
    )

    # copilot_test()
    # copilot_test2()

    ## Transformer_4
    # k = 0.8432341842306574
    # theta = -0.10962044394998548
    k4, theta4 = dr_graf(
        rtc_tapside=1,
        rtc_step=-13,
        rtc_voltage_increment=1.0,
        pst_tapside=1,
        pst_step=13,
        pst_voltage_increment=1.0,
        winding_connection_angle=90,
        u_rated1=410.0,
        u_rated2=115.0,
        u_netz1=380.0,
        u_netz2=110.0,
    )

    ## Transformer_2
    ## 0.963679 0.105321
    k2g, theta2g = dr_graf(
        rtc_tapside=0,
        rtc_step=0,
        rtc_voltage_increment=0,
        pst_tapside=1,
        pst_step=13,
        pst_voltage_increment=1.0,
        winding_connection_angle=60,
        u_rated1=410.0,
        u_rated2=115.0,
        u_netz1=380.0,
        u_netz2=110.0,
    )
    k2s, theta2s = dr_schaefer(
        rtc_tapside=0,
        rtc_step=0,
        rtc_voltage_increment=0,
        pst_tapside=1,
        pst_step=13,
        pst_voltage_increment=1.0,
        winding_connection_angle=60,
        u_rated1=410.0,
        u_rated2=115.0,
        u_netz1=380.0,
        u_netz2=110.0,
    )

    ## 0.956227 0.296973
    k_pst, theta_pst = dr_graf(
        rtc_tapside=2,
        rtc_step=9,
        rtc_voltage_increment=1.0,
        pst_tapside=1,
        pst_step=30,
        pst_voltage_increment=1.0,
        winding_connection_angle=90,
        u_rated1=237.0,
        u_rated2=237.0,
        u_netz1=220.0,
        u_netz2=220.0,
    )

    wait = 1

    # print(f"U2 = {U2:.6f}")
    # print(f"k  = {k:.6f}")
    # print(f"α  = {alpha:.6f}°")
