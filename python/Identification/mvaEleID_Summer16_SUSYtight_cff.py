import FWCore.ParameterSet.Config as cms
from RecoEgamma.ElectronIdentification.Identification.mvaElectronID_tools import *

EleMVA_SUSYtight16 = [
    "pt >= 5. && pt < 10. && abs(superCluster.eta) < 0.800",
    "pt >= 5. && pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479",
    "pt >= 5. && pt < 10. && abs(superCluster.eta) >= 1.479 && abs(superCluster.eta) < 2.5",
    "pt >= 10. && pt < 40 && abs(superCluster.eta) < 0.800",
    "pt >= 10. && pt < 40 && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479",
    "pt >= 10. && pt < 40 && abs(superCluster.eta) >= 1.479 && abs(superCluster.eta) < 2.5",
    "pt >= 40. && abs(superCluster.eta) < 0.800",
    "pt >= 40. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479",
    "pt >= 40. && abs(superCluster.eta) >= 1.479 && abs(superCluster.eta) < 2.5",
    ]

mvaTag = "Fall17NoIsoV2"

idNameSUSYtight = "mvaEleID-Summer16-SUSYtight"
MVA_SUSYtight = EleMVA_WP(
    idName = idNameSUSYtight, mvaTag = mvaTag,
    cutCategory0 = "tanh(1.309)",
    cutCategory1 = "tanh(0.373)",
    cutCategory2 = "tanh(0.071)",
    cutCategory3 = "tanh(3.447 + 0.063*(pt - 25.))",
    cutCategory4 = "tanh(2.522 + 0.058*(pt - 25.))",
    cutCategory5 = "tanh(1.555 + 0.075*(pt - 25.))",
    cutCategory6 = "tanh(4.392)",
    cutCategory7 = "tanh(3.392)",
    cutCategory8 = "tanh(2.680)",
)

mvaEleID_Fall17_SUSYtight_config = cms.PSet(
    mvaName             = cms.string(mvaClassName),
    mvaTag              = cms.string(mvaTag),
    # Category parameters
    nCategories         = cms.int32(6),
    categoryCuts        = cms.vstring(*EleMVA_SUSYtight16),
    # Weight files and variable definitions
    #weightFileNames     = mvaFall17WeightFiles_V1,
    variableDefinition  = cms.string(mvaVariablesFile)
    )

mvaEleID_Summer16_SUSYtight = configureVIDMVAEleID(MVA_SUSYtight)

mvaEleID_Summer16_SUSYtight.isPOGApproved = cms.untracked.bool(True)
