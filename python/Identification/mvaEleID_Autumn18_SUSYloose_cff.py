import FWCore.ParameterSet.Config as cms
from RecoEgamma.ElectronIdentification.Identification.mvaElectronID_tools import *

EleMVA_SUSYloose18 = [
    "pt >= 5. && pt < 10. && abs(superCluster.eta) < 0.800",
    "pt >= 5. && pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479",
    "pt >= 5. && pt < 10. && abs(superCluster.eta) >= 1.479 && abs(superCluster.eta) < 2.5",
    "pt >= 10. && pt < 25 && abs(superCluster.eta) < 0.800",
    "pt >= 10. && pt < 25 && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479",
    "pt >= 10. && pt < 25 && abs(superCluster.eta) >= 1.479 && abs(superCluster.eta) < 2.5",
    "pt >= 25. && abs(superCluster.eta) < 0.800",
    "pt >= 25. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479",
    "pt >= 25. && abs(superCluster.eta) >= 1.479 && abs(superCluster.eta) < 2.5",
    ]

mvaTag = "Fall17NoIsoV2"

idNameSUSYloose = "mvaEleID-Autumn18-SUSYloose"
MVA_SUSYloose = EleMVA_WP(
    idName = idNameSUSYloose, mvaTag = mvaTag,
    cutCategory0 = "tanh(1.320)",
    cutCategory1 = "tanh(0.192)",
    cutCategory2 = "tanh(0.362)",
    cutCategory3 = "tanh(1.204 + 0.066*(pt - 25.))",
    cutCategory4 = "tanh(0.084 + 0.033*(pt - 25.))",
    cutCategory5 = "tanh(-0.123 + 0.053*(pt - 25.))",
    cutCategory6 = "tanh(1.204)",
    cutCategory7 = "tanh(0.084)",
    cutCategory8 = "tanh(-0.123)",
)

mvaEleID_Autumn18_SUSYloose_config = cms.PSet(
    mvaName             = cms.string(mvaClassName),
    mvaTag              = cms.string(mvaTag),
    # Category parameters
    nCategories         = cms.int32(6),
    categoryCuts        = cms.vstring(*EleMVA_SUSYloose18),
    # Weight files and variable definitions
    #weightFileNames     = mvaFall17WeightFiles_V1,
    variableDefinition  = cms.string(mvaVariablesFile)
    )

mvaEleID_Autumn18_SUSYloose = configureVIDMVAEleID(MVA_SUSYloose)

mvaEleID_Autumn18_SUSYloose.isPOGApproved = cms.untracked.bool(True)
