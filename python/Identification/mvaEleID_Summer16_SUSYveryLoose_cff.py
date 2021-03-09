import FWCore.ParameterSet.Config as cms
from RecoEgamma.ElectronIdentification.Identification.mvaElectronID_tools import *

EleMVA_SUSYveryLoose16 = [
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

idNameSUSYveryLoose = "mvaEleID-Summer16-SUSYveryLoose"
MVA_SUSYveryLoose = EleMVA_WP(
    idName = idNameSUSYveryLoose, mvaTag = mvaTag,
    cutCategory0 = "tanh(-0.259)",
    cutCategory1 = "tanh(-0.256)",
    cutCategory2 = "tanh(-1.630)",
    cutCategory3 = "tanh(-0.388 + 0.109*(pt - 25.))",
    cutCategory4 = "tanh(-0.696 + 0.106*(pt - 25.))",
    cutCategory5 = "tanh(-1.219 + 0.148*(pt - 25.))",
    cutCategory6 = "tanh(-0.388)",
    cutCategory7 = "tanh(-0.696)",
    cutCategory8 = "tanh(-1.219)",
)

mvaEleID_Summer16_SUSYveryLoose_config = cms.PSet(
    mvaName             = cms.string(mvaClassName),
    mvaTag              = cms.string(mvaTag),
    # Category parameters
    nCategories         = cms.int32(6),
    categoryCuts        = cms.vstring(*EleMVA_SUSYveryLoose16),
    # Weight files and variable definitions
    #weightFileNames     = mvaFall17WeightFiles_V1,
    variableDefinition  = cms.string(mvaVariablesFile)
    )

mvaEleID_Summer16_SUSYveryLoose = configureVIDMVAEleID(MVA_SUSYveryLoose)

mvaEleID_Summer16_SUSYveryLoose.isPOGApproved = cms.untracked.bool(True)
