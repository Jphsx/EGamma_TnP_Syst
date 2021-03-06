import FWCore.ParameterSet.Config as cms
from RecoEgamma.ElectronIdentification.Identification.mvaElectronID_tools import *

EleMVA_SUSYtight17 = [
    "pt >= 5. && pt < 10. && abs(superCluster.eta) < 0.800",
    "pt >= 5. && pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479",
    "pt >= 5. && pt < 10. && abs(superCluster.eta) >= 1.479 && abs(superCluster.eta) < 2.5",
    "pt >= 10. && pt < 25. && abs(superCluster.eta) < 0.800",
    "pt >= 10. && pt < 25. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479",
    "pt >= 10. && pt < 25. && abs(superCluster.eta) >= 1.479 && abs(superCluster.eta) < 2.5",
    "pt >= 25. && abs(superCluster.eta) < 0.800",
    "pt >= 25. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479",
    "pt >= 25. && abs(superCluster.eta) >= 1.479 && abs(superCluster.eta) < 2.5",
    ]

mvaTag = "Fall17NoIsoV1"

idNameSUSYtight = "mvaEleID-Fall17-SUSYtight"
MVA_SUSYtight = EleMVA_WP(
    idName = idNameSUSYtight, mvaTag = mvaTag,
    cutCategory0 = "tanh(0.488)",
    cutCategory1 = "tanh(-0.045)",
    cutCategory2 = "tanh(0.176)",
    cutCategory3 = "tanh(0.2 + 0.032*(pt - 10.))",
    cutCategory4 = "tanh(0.1 + 0.025*(pt - 10.))",
    cutCategory5 = "tanh(-0.1 + 0.028*(pt - 10.))",
    cutCategory6 = "tanh(0.68)",
    cutCategory7 = "tanh(0.475)",
    cutCategory8 = "tanh(0.32)",
)

mvaEleID_Fall17_SUSYtight_config = cms.PSet(
    mvaName             = cms.string(mvaClassName),
    mvaTag              = cms.string(mvaTag),
    # Category parameters
    nCategories         = cms.int32(9),
    categoryCuts        = cms.vstring(*EleMVA_SUSYtight17),
    # Weight files and variable definitions
    #weightFileNames     = mvaFall17WeightFiles_V1,
    variableDefinition  = cms.string("RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt")
    )

mvaEleID_Fall17_SUSYtight = configureVIDMVAEleID(MVA_SUSYtight)

mvaEleID_Fall17_SUSYtight.isPOGApproved = cms.untracked.bool(True)
