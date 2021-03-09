import FWCore.ParameterSet.Config as cms
from RecoEgamma.ElectronIdentification.Identification.mvaElectronID_tools import *

EleMVA_SUSYveryLoose17 = [
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

idNameSUSYveryLoose = "mvaEleID-Fall17-SUSYveryLoose"
MVA_SUSYveryLoose = EleMVA_WP(
    idName = idNameSUSYveryLoose, mvaTag = mvaTag,
    cutCategory0 = "tanh(-0.135)",
    cutCategory1 = "tanh(-0.417)",
    cutCategory2 = "tanh(-0.470)",
    cutCategory3 = "tanh(-0.93 + (0.043/15.)*(pt - 10.))",
    cutCategory4 = "tanh(-0.93 + (0.04/15.)*(pt - 10.))",
    cutCategory5 = "tanh(-0.942 + (0.032/15.)*(pt - 10.))",
    cutCategory6 = "tanh(-0.887)",
    cutCategory7 = "tanh(-0.89)",
    cutCategory8 = "tanh(-0.91)",
)

mvaEleID_Fall17_SUSYveryLoose_config = cms.PSet(
    mvaName             = cms.string(mvaClassName),
    mvaTag              = cms.string(mvaTag),
    # Category parameters
    nCategories         = cms.int32(9),
    categoryCuts        = cms.vstring(*EleMVA_SUSYveryLoose17),
    # Weight files and variable definitions
    #weightFileNames     = mvaFall17WeightFiles_V1,
    variableDefinition  = cms.string("RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt")
    )

mvaEleID_Fall17_SUSYveryLoose = configureVIDMVAEleID(MVA_SUSYveryLoose)

mvaEleID_Fall17_SUSYveryLoose.isPOGApproved = cms.untracked.bool(True)
