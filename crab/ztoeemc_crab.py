from CRABClient.UserUtilities import config #getUsernameFromSiteDB
config = config()

config.General.requestName = 'TnP_DYJets2017_ZtoEE'
config.General.workArea = '../crabJobs'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.allowUndistributedCMSSW = True


config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/home/t3-ku/aabreuna/WorkDir/CMSSW_10_2_10/src/EgammaAnalysis/TnPTreeProducer/python/TnPTreeProducer_cfg.py'

config.Data.inputDataset = '/DYJetsToLL_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
#/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
#config.Data.useParent = True
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/aabreuna/'
config.Data.publication = True
config.Data.outputDatasetTag = 'TnP_DYJets2017_ZtoEE'

config.Site.storageSite = 'T2_US_Nebraska'
