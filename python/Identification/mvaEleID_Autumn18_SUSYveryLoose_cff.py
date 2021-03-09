import FWCore.ParameterSet.Config as cms
from RecoEgamma.ElectronIdentification.Identification.mvaElectronID_tools import *

EleMVA_SUSYveryLoose18 = [
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

idNameSUSYveryLoose = "mvaEleID-Autumn18-SUSYveryLoose"
MVA_SUSYveryLoose = EleMVA_WP(
    idName = idNameSUSYveryLoose, mvaTag = mvaTag,
    cutCategory0 = "tanh(0.053)",
    cutCategory1 = "tanh(-0.434)",
    cutCategory2 = "tanh(-0.956)",
    cutCategory3 = "tanh(-0.106 + 0.062*(pt - 25.))",
    cutCategory4 = "tanh(-0.769 + 0.038*(pt - 25.))",
    cutCategory5 = "tanh(-1.461 + 0.042*(pt - 25.))",
    cutCategory6 = "tanh(-0.106)",
    cutCategory7 = "tanh(-0.769)",
    cutCategory8 = "tanh(-1.461)",
)

mvaEleID_Autumn18_SUSYveryLoose_config = cms.PSet(
    mvaName             = cms.string(mvaClassName),
    mvaTag              = cms.string(mvaTag),
    # Category parameters
    nCategories         = cms.int32(6),
    categoryCuts        = cms.vstring(*EleMVA_SUSYveryLoose18),
    # Weight files and variable definitions
    #weightFileNames     = mvaFall17WeightFiles_V1,
    variableDefinition  = cms.string(mvaVariablesFile)
    )

mvaEleID_Autumn18_SUSYveryLoose = configureVIDMVAEleID(MVA_SUSYveryLoose)

mvaEleID_Autumn18_SUSYveryLoose.isPOGApproved = cms.untracked.bool(True)
