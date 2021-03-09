import FWCore.ParameterSet.Config as cms
from RecoEgamma.ElectronIdentification.Identification.mvaElectronID_tools import *

EleMVA_SUSYloose17 = [
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

idNameSUSYloose = "mvaEleID-Fall17-SUSYloose"
MVA_SUSYloose = EleMVA_WP(
    idName = idNameSUSYloose, mvaTag = mvaTag,
    cutCategory0 = "tanh(0.488)",
    cutCategory1 = "tanh(-0.045)",
    cutCategory2 = "tanh(0.176)",
    cutCategory3 = "tanh(-0.788 + (0.148/15.)*(pt - 10.))",
    cutCategory4 = "tanh(-0.85 + (0.075/15.)*(pt - 10.))",
    cutCategory5 = "tanh(-0.81 + (0.077/15.)*(pt - 10.))",
    cutCategory6 = "tanh(-0.64)",
    cutCategory7 = "tanh(-0.775)",
    cutCategory8 = "tanh(-0.733)",
)

mvaEleID_Fall17_SUSYloose_config = cms.PSet(
    mvaName             = cms.string(mvaClassName),
    mvaTag              = cms.string(mvaTag),
    # Category parameters
    nCategories         = cms.int32(9),
    categoryCuts        = cms.vstring(*EleMVA_SUSYloose17),
    # Weight files and variable definitions
    #weightFileNames     = mvaFall17WeightFiles_V1,
    variableDefinition  = cms.string("RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt")
    )

mvaEleID_Fall17_SUSYloose = configureVIDMVAEleID(MVA_SUSYloose)

mvaEleID_Fall17_SUSYloose.isPOGApproved = cms.untracked.bool(True)
