from dataclasses import dataclass

import numpy as np

from sparks.core import NDArrayType
from sparks.data import MonomerType

from .model import RateCoefficients, ModelState, SequenceModelState


def get_kt_from_Cheong_2003(s: ModelState, k: RateCoefficients):

    T_C = k.T_C
    if T_C == 115:
        ka = 0.23e14  # L/mol/min
    elif T_C == 140:
        ka = 0.8e14  # L/mol/min
    else:
        raise ValueError(f"Unsupported temperature: {T_C} C")

    ktBB = k.mpropsB.kt
    ktAA = (np.sqrt(ka) - s.beta * np.sqrt(ktBB)) ** 2
    ktAB = np.sqrt(ktAA * ktBB)

    return ktAA, ktAB, ktBB


@dataclass
class Context:

    init_state: ModelState | None = None


def kinetic_odes(
    dydt: ModelState,
    k: RateCoefficients,
    t: NDArrayType,
    s: ModelState,
    context: Context = Context(),
) -> ModelState:
    """Defines the ODEs for the full FRP2 model."""

    dydt.t = t

    T_C = k.T_C
    T_K = T_C + 273.15  # Convert Celsius to Kelvin

    # Extract properties
    iprops = k.iprops
    mpropsA = k.mpropsA
    mpropsB = k.mpropsB

    # Save initial state
    if not context.init_state and t >= 0:
        context.init_state = s

    # A0, B0 are initial moles for volume balance calculations
    A0 = context.init_state.A
    B0 = context.init_state.B
    M0 = A0 + B0

    ######################
    ### Rate Constants ###
    ######################

    kpAA, kpAB, kpBA, kpBB = k.kp()
    kpRAA, kpRAB, kpRBA, kpRBB = k.kp(f=1e1)
    kdAA, kdAB, kdBA, kdBB = k.kd()

    # Initiation
    kd = iprops.kd[MonomerType.General]
    f = iprops.f[MonomerType.General]

    # Thermal Initiation
    kthA = mpropsA.kth
    kthB = mpropsB.kth

    # Chain Transfer to Monomer
    kf_mAA, kf_mAB, kf_mBA, kf_mBB = k.kfm()
    kfm = kfm_pseudo = (
        kf_mAA * s.pA * s.fA
        + kf_mAB * s.pA * s.fB
        + kf_mBA * s.pB * s.fA
        + kf_mBB * s.pB * s.fB
    )

    RpA = (
        s.A_conc
        * (
            kpRAA * (s.R_conc + s.RA_conc)
            + kpRBA * s.RB_conc
            + kpAA * s.PA_conc
            + kpBA * s.PB_conc
        )
        - s.PA_conc * (kdAA * s.pAA + kdBA * s.pBA)
        + s.A_conc * (kf_mAA * s.PA_conc + kf_mBA * s.PB_conc)
        + 2 * kthA * s.A_conc**3
    )
    RpB = (
        s.B_conc
        * (
            kpRBB * (s.R_conc + s.RB_conc)
            + kpRAB * s.RA_conc
            + kpBB * s.PB_conc
            + kpAB * s.PA_conc
        )
        - s.PB_conc * (kdBB * s.pBB + kdAB * s.pAB)
        + s.B_conc * (kf_mAB * s.PA_conc + kf_mBB * s.PB_conc)
        + 2 * kthB * s.B_conc**3
    )

    ###########################################
    ### Calculate the pseudo rate constants ###
    ###########################################

    # Pseudo rate constant for propagation
    kp = (
        # i=A, j=A
        (kpAA * s.pA * s.fA - kdAA * s.pAA * s.pA / s.M_conc)
        # i=A, j=B
        + (kpAB * s.pA * s.fB - kdAB * s.pAB * s.pB / s.M_conc)
        # i=B, j=A
        + (kpBA * s.pB * s.fA - kdBA * s.pBA * s.pA / s.M_conc)
        # i=B, j=B
        + (kpBB * s.pB * s.fB - kdBB * s.pBB * s.pB / s.M_conc)
    )

    ktAA, ktAB, ktBB = get_kt_from_Cheong_2003(s, k)
    kt = ktAA * s.pA * s.pA + ktBB * s.pB * s.pB + 2 * ktAB * s.pA * s.pB
    ktd_ratio = mpropsA.ktd_ratio * s.pA + mpropsB.ktd_ratio * s.pB

    ########################################
    ### Calculate the overall properties ###
    ########################################

    # Calculate the mass/volume of monomer
    m_A = s.A * mpropsA.MW
    m_B = s.B * mpropsB.MW
    vol_A = m_A / mpropsA.dens_m
    vol_B = m_B / mpropsB.dens_m
    vol_m = vol_A + vol_B

    # Calculate the mass/volume of polymer
    m_PA = s.nPA * mpropsA.MW
    m_PB = s.nPB * mpropsB.MW
    m_P = m_PA + m_PB
    vol_PA = m_PA / mpropsA.dens_p
    vol_PB = m_PB / mpropsB.dens_p
    vol_P = vol_PA + vol_PB  # Volume of polymer in L

    ktc = kt / (1 + ktd_ratio)
    ktd = kt * ktd_ratio / (1 + ktd_ratio)

    # Calculate volume change from monomer
    vdelta_mA = RpA * vol_A / s.A if s.A > 0 else 0.0
    vdelta_mB = RpB * vol_B / s.B if s.B > 0 else 0.0
    vdelta_PA = RpA * vol_PA / s.nPA if s.nPA > 0 else 0.0
    vdelta_PB = RpB * vol_PB / s.nPB if s.nPB > 0 else 0.0
    vdelta = vdelta_mA + vdelta_mB - vdelta_PA - vdelta_PB
    dydt.V = -s.V * vdelta

    """ Moles of Initiator """
    dydt.I = s.V * (-kd * s.I_conc)

    """ Moles of Free Radical, R """
    dydt.R = s.V * (
        # Formation by initiation
        +2 * f * kd * s.I_conc
        # Consumption by propagation
        - kpRAA * s.R_conc * s.A_conc
        - kpRBB * s.R_conc * s.B_conc
    )

    """ Moles of A Monomer """
    dydt.A = s.V * (
        # Consumption by propagation
        -kpRAA * (s.R_conc + s.RA_conc) * s.A_conc
        - kpRBA * s.RB_conc * s.A_conc
        - kpAA * s.PA_conc * s.A_conc
        - kpBA * s.PB_conc * s.A_conc
        # Formation by depropagation
        + kdAA * s.PAA_conc
        + kdBA * s.PBA_conc
        # Consumption by chain transfer to monomer
        - kf_mAA * s.PA_conc * s.A_conc
        - kf_mBA * s.PB_conc * s.A_conc
        # Consumption by thermal initiation
        - 3 * kthA * s.A_conc**3
    )

    """ Moles of B Monomer """
    dydt.B = s.V * (
        # Consumption by propagation
        -kpRBB * (s.R_conc + s.RB_conc) * s.B_conc
        - kpRAB * s.RA_conc * s.B_conc
        - kpAB * s.PA_conc * s.B_conc
        - kpBB * s.PB_conc * s.B_conc
        # Formation by depropagation
        + kdAB * s.PAB_conc
        + kdBB * s.PBB_conc
        # Consumption by chain transfer to monomer
        - kf_mAB * s.PA_conc * s.B_conc
        - kf_mBB * s.PB_conc * s.B_conc
        # Consumption by thermal initiation
        - 3 * kthB * s.B_conc**3
    )

    """ Moles of R-A dyad"""
    dydt.RA = s.V * (
        # Formation by thermal initiation (3A -> 2RA)
        +2 * kthA * s.A_conc**3
        # Formation by propagation (R + A -> RA)
        + kpRAA * s.R_conc * s.A_conc
        # Consumption by propagation (RA + A -> PAA, RA + B -> PAB)
        - kpRAA * s.RA_conc * s.A_conc
        - kpRAB * s.RA_conc * s.B_conc
        # Formation by chain transfer (PA + A -> PD + RA)
        + kf_mAA * s.PA_conc * s.A_conc
        # Formation by chain transfer (PB + A -> PD + RA)
        + kf_mBA * s.PB_conc * s.A_conc
    )

    """ Total moles of R-B dyad """
    dydt.RB = s.V * (
        # Formation by thermal initiation (3B -> 2RB)
        +2 * kthB * s.B_conc**3
        # Formation by propagation (R + B -> RB)
        + kpRBB * s.R_conc * s.B_conc
        # Consumption by propagation (RB + A -> PBA, RB + B -> PBB)
        - kpRBA * s.RB_conc * s.A_conc
        - kpRBB * s.RB_conc * s.B_conc
        # Formation by chain transfer (PA + B -> PD + RB)
        + kf_mAB * s.PA_conc * s.B_conc
        # Formation by chain transfer (PB + B -> PD + RB)
        + kf_mBB * s.PB_conc * s.B_conc
    )

    c_tAA = c_tBB = 1
    c_tAB = 1

    """ Total moles of ~~AA* polymer """
    dydt.PAA = s.V * (
        # Formation by propagation (RA + A -> PAA)
        +kpRAA * s.RA_conc * s.A_conc
        # Formation by propagation (PBA + A -> PAA)
        + kpAA * s.PBA_conc * s.A_conc
        # Consumption by propagation (PAA + B -> PAB)
        - kpAB * s.PAA_conc * s.B_conc
        # Formation by depropagation (PAAB -> PAA + B)
        + kdAB * s.pAA * s.PAB_conc
        # Consumption by depropagation (PBAA -> PBA + A)
        - kdAA * s.pBA * s.PAA_conc
        # Consumption by chain transfer to monomer (PAA + B -tr-> PD + RB)
        - kf_mAB * s.PAA_conc * s.B_conc
        # Consumption by chain transfer to monomer (PAA + A -tr-> PD + RA)
        - kf_mAA * s.PAA_conc * s.A_conc
        # Consumption by termination (PAA + PA -> (2)PD, PAA + PB -> (2)PD)
        - c_tAA * ktAA * s.PAA_conc * s.PA_conc
        - c_tAB * ktAB * s.PAA_conc * s.PB_conc
    )

    """ Total moles of ~~AB* polymer """
    dydt.PAB = s.V * (
        # Formation by propagation (RA + B -> PAB)
        +kpRAB * s.RA_conc * s.B_conc
        # Formation by propagation (PA + B -> PAB)
        + kpAB * s.PA_conc * s.B_conc
        # Consumption by propagation (PAB + A -> PBA)
        - kpBA * s.PAB_conc * s.A_conc
        # Consumption by propagation (PAB + B -> PBB)
        - kpBB * s.PAB_conc * s.B_conc
        # Formation by depropagation (PABA -> PAB + A)
        + kdBA * s.pAB * s.PBA_conc
        # Formation by depropagation (PABB -> PAB + B)
        + kdBB * s.pAB * s.PBB_conc
        # Consumption by depropagation (PAB -> PA + B)
        - kdAB * s.PAB_conc
        # Consumption by chain transfer to monomer (PAB + A -tr-> PD + RA)
        - kf_mBA * s.PAB_conc * s.A_conc
        # Consumption by chain transfer to monomer (PAB + B -tr-> PD + RB)
        - kf_mBB * s.PAB_conc * s.B_conc
        # Consumption by termination (PAB + PA -> (2)PD, PAB + PB -> (2)PD)
        - c_tAB * ktAB * s.PAB_conc * s.PA_conc
        - c_tBB * ktBB * s.PAB_conc * s.PB_conc
    )

    """ Total moles of ~~BA* polymer """
    dydt.PBA = s.V * (
        # Formation by propagation (RB + A -> PBA)
        +kpRBA * s.RB_conc * s.A_conc
        # Formation by propagation (PB + A -> PBA)
        + kpBA * s.PB_conc * s.A_conc
        # Consumption by propagation (PBA + A -> PAA)
        - kpAA * s.PBA_conc * s.A_conc
        # Consumption by propagation (PBA + B -> PBB)
        - kpAB * s.PBA_conc * s.B_conc
        # Formation by depropagation (PBAA -> PBA + A)
        + kdAA * s.pBA * s.PAA_conc
        # Formation by depropagation (PBAB -> PBA + B)
        + kdAB * s.pBA * s.PAB_conc
        # Consumption by depropagation (PBA -> PB + A)
        - kdBA * s.PBA_conc
        # Consumption by chain transfer to monomer (PBA + A -tr-> PD + RA)
        - kf_mAA * s.PBA_conc * s.A_conc
        # Consumption by chain transfer to monomer (PBA + B -tr-> PD + RB)
        - kf_mAB * s.PBA_conc * s.B_conc
        # Consumption by termination (PBA + PA -> (2)PD, PBA + PB -> (2)PD)
        - c_tAA * ktAA * s.PBA_conc * s.PA_conc
        - c_tAB * ktAB * s.PBA_conc * s.PB_conc
    )

    """ Total moles of ~~BB* polymer """
    dydt.PBB = s.V * (
        # Formation by propagation (RB + B -> PBB)
        +kpRBB * s.RB_conc * s.B_conc
        # Formation by propagation (PAB + B -> PBB)
        + kpBB * s.PAB_conc * s.B_conc
        # Consumption by propagation (PBB + A -> PBA)
        - kpBA * s.PBB_conc * s.A_conc
        # Formation by depropagation (PBBA -> PBB + A)
        + kdBA * s.pBB * s.PBA_conc
        # Consumption by depropagation (PABB -> PAB + B)
        - kdBB * s.pAB * s.PBB_conc
        # Consumption by chain transfer to monomer (PBB + A -tr-> PD + RA)
        - kf_mBA * s.PBB_conc * s.A_conc
        # Consumption by chain transfer to monomer (PBB + B -tr-> PD + RB)
        - kf_mBB * s.PBB_conc * s.B_conc
        # Consumption by termination (PBB + PA -> (2)PD, PBB + PB -> (2)PD)
        - c_tBB * ktBB * s.PBB_conc * s.PB_conc
        - c_tAB * ktAB * s.PBB_conc * s.PA_conc
    )

    """ Total moles of A and B monomer in polymer"""
    dydt.nPA = s.V * RpA
    dydt.nPB = s.V * RpB

    # Formation of polymer from active radicals
    poly_form = (
        kpRAA * s.R_conc * s.A_conc
        + kpRBB * s.R_conc * s.B_conc
        + 2 * kthA * s.A_conc**3
        + 2 * kthB * s.B_conc**3
    )

    """ Active radicals (0th order moment) """
    dydt.lam_0 = s.V * (
        # Formation by propagation
        poly_form
        # Consumption by termination
        - kt * s.lam_0_conc**2
    )

    """ Active radicals (1st order moment) """
    dydt.lam_1 = s.V * (
        # Formation by propagation
        poly_form
        # Formation by propagation
        + kp * s.M_conc * s.lam_0_conc
        # Consumption by termination
        - kt * s.lam_0_conc * s.lam_1_conc
        # Consumption from chain transfer
        - kfm * s.M_conc * (s.lam_1_conc - s.lam_0_conc)
    )

    """Active radicals (2nd order moment)"""
    dydt.lam_2 = s.V * (
        # Formation by propagation
        poly_form
        # Formation by propagation
        + kp * s.M_conc * (s.lam_0_conc + 2 * s.lam_1_conc)
        # Consumption by termination
        - kt * s.lam_0_conc * s.lam_2_conc
        # Consumption from chain transfer
        - kfm * s.M_conc * (s.lam_2_conc - s.lam_0_conc)
    )

    """Dead radicals (0th order moment)"""
    dydt.mu_0 = s.V * (
        # Formation by termination
        +(0.5 * ktc + ktd) * s.lam_0_conc**2
        # Formation by chain transfer
        + kfm * s.M_conc * s.lam_0_conc
    )

    """Dead radicals (1st order moment)"""
    dydt.mu_1 = s.V * (
        # Formation by termination
        +(ktc + ktd) * s.lam_0_conc * s.lam_1_conc
        # Formation by chain transfer
        + kfm * s.M_conc * s.lam_1_conc
    )

    """Dead radicals (2nd order moment)"""
    dydt.mu_2 = s.V * (
        # Formation by termination (comb.)
        +ktc * (s.lam_0_conc * s.lam_2_conc + s.lam_1_conc**2)
        # Formation by termination (disp.)
        + ktd * s.lam_0_conc * s.lam_2_conc
        # Formation by chain transfer
        + kfm * s.M_conc * s.lam_2_conc
    )

    return dydt


def sequence_odes(
    dydt: SequenceModelState,
    k: RateCoefficients,
    t: NDArrayType,
    sms: SequenceModelState,
    s: ModelState,
) -> SequenceModelState:

    dydt.t = t

    kpAA, kpAB, kpBA, kpBB = k.kp()
    kdAA, kdAB, kdBA, kdBB = k.kd()
    ktAA, ktAB, ktBB = get_kt_from_Cheong_2003(s, k)

    kf_mAA, kf_mAB, kf_mBA, kf_mBB = k.kfm()

    aSA0_conc = sms.aSA0 / s.V
    aSB0_conc = sms.aSB0 / s.V
    aSA1_conc = sms.aSA1 / s.V
    aSB1_conc = sms.aSB1 / s.V
    aSA2_conc = sms.aSA2 / s.V
    aSB2_conc = sms.aSB2 / s.V

    # Rates of termination and chain transfer to monomer
    # Ctrij_x = c_tij * ktij * sms.aSijx * sms.aSij0 + c_tij * kf_mij * sms.aSijx * s.j
    RtAA_0 = ktAA * aSA0_conc * aSA0_conc + kf_mAA * aSA0_conc * s.A_conc
    RtAB_0 = ktAB * aSA0_conc * aSB0_conc + kf_mAB * aSA0_conc * s.B_conc
    RtBA_0 = ktAB * aSB0_conc * aSA0_conc + kf_mBA * aSB0_conc * s.A_conc
    RtBB_0 = ktBB * aSB0_conc * aSB0_conc + kf_mBB * aSB0_conc * s.B_conc
    RtAA_1 = ktAA * aSA1_conc * aSA0_conc + kf_mAA * aSA1_conc * s.A_conc
    RtAB_1 = ktAB * aSA1_conc * aSB0_conc + kf_mAB * aSA1_conc * s.B_conc
    RtBA_1 = ktAB * aSB1_conc * aSA0_conc + kf_mBA * aSB1_conc * s.A_conc
    RtBB_1 = ktBB * aSB1_conc * aSB0_conc + kf_mBB * aSB1_conc * s.B_conc
    RtAA_2 = ktAA * aSA2_conc * aSA0_conc + kf_mAA * aSA2_conc * s.A_conc
    RtAB_2 = ktAB * aSA2_conc * aSB0_conc + kf_mAB * aSA2_conc * s.B_conc
    RtBA_2 = ktAB * aSB2_conc * aSA0_conc + kf_mBA * aSB2_conc * s.A_conc
    RtBB_2 = ktBB * aSB2_conc * aSB0_conc + kf_mBB * aSB2_conc * s.B_conc

    a10_frac = aSA1_conc / aSA0_conc if aSA0_conc > 0 else 0
    b10_frac = aSB1_conc / aSB0_conc if aSB0_conc > 0 else 0
    a20_frac = aSA2_conc / aSA0_conc if aSA0_conc > 0 else 0
    b20_frac = aSB2_conc / aSB0_conc if aSB0_conc > 0 else 0
    kthA = k.mpropsA.kth
    kthB = k.mpropsB.kth

    # Active A sequences (0th order moment)
    dydt.aSA0 = s.V * (
        # Formation by propagation (PA + A -> PA, PB + A -> PA)
        +kpAA * s.A_conc * (s.R_conc + aSA0_conc)
        + kpBA * s.A_conc * (s.RB_conc + aSB0_conc)
        + kthA * s.A_conc**3
        # Consumption by propagation (PA + A -> PA, PA + B -> PB)
        - kpAA * s.A_conc * aSA0_conc
        - kpAB * s.B_conc * (s.RA_conc + aSA0_conc)
        # Formation by depropagation (PAA -> PA + A, PAB -> PA + B)
        + kdAA * s.pAA * aSA0_conc
        + kdAB * s.pAB * aSB0_conc
        # Consumption by depropagation (PAA -> PA + A, PBA -> PB + A)
        - kdAA * s.pAA * aSA0_conc
        - kdBA * s.pBA * aSA0_conc
        # Consumption by termination (PA + PA -> D, PA + PB -> D)
        - RtAA_0
        - RtAB_0
    )

    # Active B sequences (0th order moment)
    dydt.aSB0 = s.V * (
        # Formation by propagation (PB + B -> PB, PA + B -> PB)
        +kpBB * s.B_conc * (s.R_conc + aSB0_conc)
        + kpAB * s.B_conc * (s.RA_conc + aSA0_conc)
        + kthB * s.B_conc**3
        # Consumption by propagation (PB + B -> PB, PB + A -> PA)
        - kpBB * s.B_conc * aSB0_conc
        - kpBA * s.A_conc * (s.RB_conc + aSB0_conc)
        # Formation by depropagation (PBB -> PB + B, PBA -> PB + A)
        + kdBB * s.pBB * aSB0_conc
        + kdBA * s.pBA * aSA0_conc
        # Consumption by depropagation (PBB -> PB + B, PAB -> PA + B)
        - kdBB * s.pBB * aSB0_conc
        - kdAB * s.pAB * aSB0_conc
        # Consumption by termination (PB + PB -> D, PB + PA -> D)
        - RtBB_0
        - RtBA_0
    )

    # Active A sequences (1st order moment)
    dydt.aSA1 = s.V * (
        # Formation by propagation (PA + A -> PA, PB + A -> PA)
        +kpAA * s.A_conc * (s.R_conc + aSA0_conc + aSA1_conc)
        + kpBA * s.A_conc * (s.RB_conc + aSB0_conc)
        # Consumption by propagation (PA + A -> PA, PA + B -> PB)
        - kpAA * s.A_conc * aSA1_conc
        - kpAB * s.B_conc * (s.RA_conc + aSA1_conc)
        # Formation by depropagation (PAA -> PA + A, PAB -> PA + B)
        + kdAA * s.pAA * (aSA1_conc - aSA0_conc)
        + kdAB * s.pAB * a10_frac * aSB0_conc
        # Consumption by depropagation (PAA -> PA + A, PBA -> PB + A)
        - kdAA * s.pAA * aSA1_conc
        - kdBA * s.pBA * aSA0_conc
        # Consumption by termination (PA + PA -> D, PA + PB -> D)
        - RtAA_1
        - RtAB_1
    )

    # Active B sequences (1st order moment)
    dydt.aSB1 = s.V * (
        # Formation by propagation (PB + B -> PB, PA + B -> PB)
        +kpBB * s.B_conc * (s.R_conc + aSB0_conc + aSB1_conc)
        + kpAB * s.B_conc * (s.RA_conc + aSA0_conc)
        # Consumption by propagation (PB + B -> PB, PB + A -> PA)
        - kpBB * s.B_conc * aSB1_conc
        - kpBA * s.A_conc * (s.RB_conc + aSB1_conc)
        # Formation by depropagation (PBB -> PB + B, PBA -> PB + A)
        + kdBB * s.pBB * (aSB1_conc - aSB0_conc)
        + kdBA * s.pBA * b10_frac * aSA0_conc
        # Consumption by depropagation (PBB -> PB + B, PAB -> PA + B)
        - kdBB * s.pBB * aSB1_conc
        - kdAB * s.pAB * aSB0_conc
        # Consumption by termination (PB + PB -> D, PB + PA -> D)
        - RtBB_1
        - RtBA_1
    )

    # return dydt

    # Active A sequences (2nd order moment)
    dydt.aSA2 = s.V * (
        # Formation by propagation (PA + A -> PA, PB + A -> PA)
        +kpAA * s.A_conc * (s.R_conc + aSA0_conc + 2 * aSA1_conc + aSA2_conc)
        + kpBA * s.A_conc * (s.RB_conc + aSB0_conc)
        # Consumption by propagation (PA + A -> PA, PA + B -> PB)
        - kpAA * s.A_conc * aSA2_conc
        - kpAB * s.B_conc * (s.RA_conc + aSA2_conc)
        # Formation by depropagation (PAA -> PA + A, PAB -> PA + B)
        + kdAA * s.pAA * (aSA2_conc - 2 * aSA1_conc + aSA0_conc)
        + kdAB * s.pAB * a20_frac * aSB0_conc
        # Consumption by depropagation (PAA -> PA + A, PBA -> PB + A)
        - kdAA * s.pAA * aSA2_conc
        - kdBA * s.pBA * aSA0_conc
        # Consumption by termination (PA + PA -> D, PA + PB -> D)
        - RtAA_2
        - RtAB_2
    )

    # Active B sequences (2nd order moment)
    dydt.aSB2 = s.V * (
        # Formation by propagation (PB + B -> PB, PA + B -> PB)
        +kpBB * s.B_conc * (s.R_conc + aSB0_conc + 2 * aSB1_conc + aSB2_conc)
        + kpAB * s.B_conc * (s.RA_conc + aSA0_conc)
        # Consumption by propagation (PB + B -> PB, PB + A -> PA)
        - kpBB * s.B_conc * aSB2_conc
        - kpBA * s.A_conc * (s.RB_conc + aSB2_conc)
        # Formation by depropagation (PBB -> PB + B, PBA -> PB + A)
        + kdBB * s.pBB * (aSB2_conc - 2 * aSB1_conc + aSB0_conc)
        + kdBA * s.pBA * b20_frac * aSA0_conc
        # Consumption by depropagation (PBB -> PB + B, PAB -> PA + B)
        - kdBB * s.pBB * aSB2_conc
        - kdAB * s.pAB * aSB0_conc
        # Consumption by termination (PB + PB -> D, PB + PA -> D)
        - RtBB_2
        - RtBA_2
    )

    # Inactive A sequences (0th order moment)
    dydt.iSA0 = s.V * (
        # Formation by cross-propagation (PA + B -> PB)
        +kpAB * s.B_conc * (s.RA_conc + aSA0_conc)
        # Consumption by depropagation (PAB -> PA + B)
        - kdAB * s.pAB * aSB0_conc
        # Formation by termination (PA + PA -> D, PA + PB -> D)
        + RtAA_0
        + RtAB_0
    )

    # Inactive B sequences (0th order moment)
    dydt.iSB0 = s.V * (
        # Formation by cross-propagation (PB + A -> PA)
        +kpBA * s.A_conc * (s.RB_conc + aSB0_conc)
        # Consumption by depropagation (PBA -> PB + A)
        - kdBA * s.pBA * aSA0_conc
        # Formation by termination (PB + PB -> D, PB + PA -> D)
        + RtBB_0
        + RtBA_0
    )

    # Inactive A sequences (1st order moment)
    dydt.iSA1 = s.V * (
        # Formation by cross-propagation (PA + B -> PB)
        +kpAB * s.B_conc * (s.RA_conc + aSA1_conc)
        # Consumption by depropagation (PAB -> PA + B)
        - kdAB * s.pAB * a10_frac * aSB0_conc
        # Formation by termination (PA + PA -> D, PA + PB -> D)
        + RtAA_1
        + RtAB_1
    )

    # Inactive B sequences (1st order moment)
    dydt.iSB1 = s.V * (
        # Formation by cross-propagation (PB + A -> PA)
        +kpBA * s.A_conc * (s.RB_conc + aSB1_conc)
        # Consumption by depropagation (PBA -> PB + A)
        - kdBA * s.pBA * b10_frac * aSA0_conc
        # Formation by termination (PB + PB -> D, PB + PA -> D)
        + RtBB_1
        + RtBA_1
    )

    # Inactive A sequences (2nd order moment)
    dydt.iSA2 = s.V * (
        # Formation by cross-propagation (PA + B -> PB)
        +kpAB * s.B_conc * (s.RA_conc + aSA2_conc)
        # Consumption by depropagation (PAB -> PA + B)
        - kdAB * s.pAB * a20_frac * aSB0_conc
        # Formation by termination (PA + PA -> D, PA + PB -> D)
        + RtAA_2
        + RtAB_2
    )

    # Inactive B sequences (2nd order moment)
    dydt.iSB2 = s.V * (
        # Formation by cross-propagation (PB + A -> PA)
        +kpBA * s.A_conc * (s.RB_conc + aSB2_conc)
        # Consumption by depropagation (PBA -> PB + A)
        - kdBA * s.pBA * b20_frac * aSA0_conc
        # Formation by termination (PB + PB -> D, PB + PA -> D)
        + RtBB_2
        + RtBA_2
    )

    return dydt
