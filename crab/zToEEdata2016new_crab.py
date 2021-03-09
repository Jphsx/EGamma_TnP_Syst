from CRABClient.UserUtilities import config#, getUsernameFromSiteDB
config = config()

config.General.requestName = 'TnP_SingleElectron2016'
config.General.workArea = '../crabJobs'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.allowUndistributedCMSSW = True


config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/home/t3-ku/aabreuna/WorkDir/CMSSW_10_2_10/src/EgammaAnalysis/TnPTreeProducer/python/TnPTreeProducer_cfg.py'

config.Data.inputDataset = '/SingleElectron/Run2016B-17Jul2018_ver2-v1/MINIAOD'
#config.Data.useParent = True
config.Data.inputDBS = 'global'
#config.Data.lumiMask = 'Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
config.Data.splitting = 'EventAwareLumiBased'
#config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 50000
config.Data.outLFNDirBase = '/store/user/aabreuna'
config.Data.publication = False
config.Data.outputDatasetTag = 'TnP_SingleElectron2016'

config.Site.storageSite = 'T2_US_Nebraska'
