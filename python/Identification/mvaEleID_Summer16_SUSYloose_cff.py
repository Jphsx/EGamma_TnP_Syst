import FWCore.ParameterSet.Config as cms
from RecoEgamma.ElectronIdentification.Identification.mvaElectronID_tools import *

EleMVA_SUSYloose16 = [
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

idNameSUSYloose = "mvaEleID-Summer16-SUSYloose"
MVA_SUSYloose = EleMVA_WP(
    idName = idNameSUSYloose, mvaTag = mvaTag,
    cutCategory0 = "tanh(1.309)",
    cutCategory1 = "tanh(0.373)",
    cutCategory2 = "tanh(0.071)",
    cutCategory3 = "tanh(0.887 + 0.088*(pt - 25.))",
    cutCategory4 = "tanh(0.112 + 0.099*(pt - 25.))",
    cutCategory5 = "tanh(-0.017 + 0.137*(pt - 25.))",
    cutCategory6 = "tanh(0.887)",
    cutCategory7 = "tanh(0.112)",
    cutCategory8 = "tanh(-0.017)",
)

mvaEleID_Summer16_SUSYloose_config = cms.PSet(
    mvaName             = cms.string(mvaClassName),
    mvaTag              = cms.string(mvaTag),
    # Category parameters
    nCategories         = cms.int32(6),
    categoryCuts        = cms.vstring(*EleMVA_SUSYloose16),
    # Weight files and variable definitions
    #weightFileNames     = mvaFall17WeightFiles_V1,
    variableDefinition  = cms.string(mvaVariablesFile)
    )

mvaEleID_Summer16_SUSYloose = configureVIDMVAEleID(MVA_SUSYloose)

mvaEleID_Summer16_SUSYloose.isPOGApproved = cms.untracked.bool(True)
