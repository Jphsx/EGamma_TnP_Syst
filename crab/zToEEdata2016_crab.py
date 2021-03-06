from CRABClient.UserUtilities import config #getUsernameFromSiteDB
config = config()

config.General.requestName = 'TnP_SingleElectron2016'
config.General.workArea = '../crabJobs'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.allowUndistributedCMSSW = True


config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/home/t3-ku/aabreuna/WorkDir/CMSSW_10_2_10/src/EgammaAnalysis/TnPTreeProducer/python/TnPTreeProducer_cfg.py'

config.Data.inputDataset = 'SingleElectron/Run2016B-17Jul2018_ver2-v1/MINIAOD'
#/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
#config.Data.useParent = True
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/aabreuna/'
config.Data.publication = True
config.Data.outputDatasetTag = 'TnP_SingleElectron2016'

config.Site.storageSite = 'T2_US_Nebraska'
