import math


def pst_transform(
    U1: complex,
    t: int,
    s: int,
    z_deg: float,
    delta_beta_percent: float,
    delta_r_percent: float,
    t0: int = 0,
    s0: int = 0,
    multiplicative_r: bool = False,
):
    """
    Berechnet U2 = k * exp(j*alpha) * U1 für einen asynchronen PST + In-Phase-Regler.

    Parameter
    ---------
    U1 : complex
        Eingangsspannung (als komplexer Phasor, meist 1+0j)
    t : int
        Tap-Stellung PST
    s : int
        Tap-Stellung Längsregler
    z_deg : float
        fester Winkel der Zusatzspannung (z.B. 15, 30, 60, 90 Grad)
    delta_beta_percent : float
        Prozent pro Stufe der Zusatzspannung (z.B. 0.125 für 0.125 %)
    delta_r_percent : float
        Prozent pro Stufe des Längsreglers (z.B. 1.0 für 1 %)
    t0 : int
        Tap-Offset für PST (Tap-Stellung, die 0 % Zusatzspannung entspricht)
    s0 : int
        Tap-Offset für Längsregler (Tap-Stellung, die r=1.0 entspricht)
    multiplicative_r : bool
        Wenn True: multiplikatives Mapping für r, sonst additiv.

    Rückgabe
    --------
    U2 : complex
        Ausgangsspannung
    k : float
        Betrag von U2 / U1
    alpha_deg : float
        Phasenwinkel von U2/U1 in Grad
    """

    # Schrittweiten in p.u.
    delta_beta = delta_beta_percent / 100.0
    delta_r = delta_r_percent / 100.0

    # Zusatzspannung (relativ, p.u.)
    beta = (t - t0) * delta_beta

    # In-phase-Regler
    if multiplicative_r:
        r = (1.0 + delta_r) ** (s - s0)
    else:
        r = 1.0 + (s - s0) * delta_r

    # Zusatzwinkel in rad
    z = math.radians(z_deg)

    # komplexer Verstärkungsfaktor
    a = 1.0 + beta * (math.cos(z) + 1j * math.sin(z))

    factor = r * a

    U2 = factor * U1
    k = abs(factor)
    alpha_deg = math.degrees(math.atan2(factor.imag, factor.real))

    return U2, k, alpha_deg


# --- Beispiel ---
if __name__ == "__main__":
    U1 = 1.0 + 0j  # Referenzspannung
    U2, k, alpha = pst_transform(
        U1=U1,
        t=10,  # PST Tap
        s=3,  # Längsregler Tap
        z_deg=90.0,  # Zusatzspannung im Quadratur
        delta_beta_percent=0.125,  # % pro Stufe Zusatzspannung
        delta_r_percent=1.0,  # % pro Stufe Längsregler
        t0=0,
        s0=0,
        multiplicative_r=False,
    )

    print(f"U2 = {U2:.6f}")
    print(f"k  = {k:.6f}")
    print(f"α  = {alpha:.6f}°")
