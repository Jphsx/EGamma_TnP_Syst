import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.TnP_Electron_ID = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
    ## Input, output 
    InputFileNames = cms.vstring(                                 
        "/home/t3-ku/aabreuna/WorkDir/CMSSW_10_2_10/src/EgammaAnalysis/TnPTreeProducer/src/root/tp_Iso_data2018_1.root",
        "/home/t3-ku/aabreuna/WorkDir/CMSSW_10_2_10/src/EgammaAnalysis/TnPTreeProducer/src/root/tp_Iso_data2018_2.root",
        "/home/t3-ku/aabreuna/WorkDir/CMSSW_10_2_10/src/EgammaAnalysis/TnPTreeProducer/src/root/tp_Iso_data2018_3.root",
        "/home/t3-ku/aabreuna/WorkDir/CMSSW_10_2_10/src/EgammaAnalysis/TnPTreeProducer/src/root/tp_Iso_data2018_4.root",
        "/home/t3-ku/aabreuna/WorkDir/CMSSW_10_2_10/src/EgammaAnalysis/TnPTreeProducer/src/root/tp_Iso_data2018_5.root",
        "/home/t3-ku/aabreuna/WorkDir/CMSSW_10_2_10/src/EgammaAnalysis/TnPTreeProducer/src/root/tp_Iso_data2018_6.root",
        "/home/t3-ku/aabreuna/WorkDir/CMSSW_10_2_10/src/EgammaAnalysis/TnPTreeProducer/src/root/tp_Iso_data2018_7.root",
        "/home/t3-ku/aabreuna/WorkDir/CMSSW_10_2_10/src/EgammaAnalysis/TnPTreeProducer/src/root/tp_Iso_data2018_8.root",
        "/home/t3-ku/aabreuna/WorkDir/CMSSW_10_2_10/src/EgammaAnalysis/TnPTreeProducer/src/root/tp_Iso_data2018_9.root",
                                 ), ## can put more than one
    ## copy locally to be faster: xrdcp root://eoscms//eos/cms/store/cmst3/user/botta/TnPtrees/tnpZ_Data.190456-193557.root $PWD/tnpZ_Data.190456-193557.root
    ## and then set InputFileNames = cms.vstring("tnpZ_Data.190456-193557.root"), 
    OutputFileName = cms.string("TnPZ_susyID_Data.root"),
    InputTreeName = cms.string("fitter_tree"), 
    InputDirectoryName = cms.string("tpTree"),  
    ## Variables for binning
    Variables = cms.PSet(
        mass   = cms.vstring("Tag-electron Mass", "76", "125", "GeV/c^{2}"),
        el_pt     = cms.vstring("electron p_{T}", "0", "1000", "GeV/c"),
        el_abseta = cms.vstring("electron |#eta|", "0", "2.4", ""),
        el_dxy = cms.vstring("electron dxy", "0", "100", ""),
        el_dz = cms.vstring("electron dz", "0", "100", ""),
        #pair_dz = cms.vstring("#Deltaz between two electrons", "-100", "100", "cm"),
	el_sip = cms.vstring("3d impact sig.", "0", "500", ""),
	miniIsoAll = cms.vstring("abs miniIso EA", "0", "500", "GeV/c^{2}"),
        absPFIso_All = cms.vstring("abs PF Iso", "0", "500", "GeV/c^{2}"),
        passPFIso = cms.vstring("pass iso < (300+20/pt)", "0", "1", ""),
    ),
    ## Flags you want to use to define numerator and possibly denominator
    Categories = cms.PSet(
        #PF = cms.vstring("PF Muon", "dummy[pass=1,fail=0]"),
	#Medium = cms.vstring("Medium Muon", "dummy[pass=1,fail=0]"),	
        passingMVA94XAutumn18SUSYtight = cms.vstring("MVA SUSY tight wp", "dummy[pass=1,fail=0]"),
        passingMVA94XAutumn18SUSYveryLoose = cms.vstring("MVA SUSY very loose wp", "dummy[pass=1,fail=0]"),
        passEleVeryLoose = cms.vstring("Electron very loose definition", "dummy[pass=1,fail=0]"),
#       tag_IsoMu24_eta2p1 = cms.vstring("Medium Muon", "dummy[pass=1,fail=0]"),i
    ),
    Cuts = cms.PSet(
	SIP4 = cms.vstring("SIP4", "el_sip", "2"),
	Mini = cms.vstring("Mini", "miniIsoAll", "4"),
        PFIso = cms.vstring("PFIso", "absPFIso_All", "4"),
    ),

    ## What to fit
    Efficiencies = cms.PSet(
        TightSUSY_pt_eta = cms.PSet(
            UnbinnedVariables = cms.vstring("mass"),
            #EfficiencyCategoryAndState = cms.vstring("PF", "pass"), ## Numerator definition
            #EfficiencyCategoryAndState = cms.vstring("Medium", "pass", "SIP4", "below", "Mini", "below"),
            #EfficiencyCategoryAndState = cms.vstring("passingMVA94XAutumn18SUSYtight", "pass", "SIP4", "below", "Mini", "below", "PFIso", "below"),
            #EfficiencyCategoryAndState = cms.vstring("SIP4", "below"),
            #EfficiencyCategoryAndState = cms.vstring("Mini", "below", "PFIso", "below"),
            #EfficiencyCategoryAndState = cms.vstring("passingMVA94XAutumn18SUSYveryLoose", "pass", "passEleVeryLoose", "pass"),
            EfficiencyCategoryAndState = cms.vstring("passingMVA94XAutumn18SUSYtight", "pass"),
	    BinnedVariables = cms.PSet(
                ## Binning in continuous variables
                #pt     = cms.vdouble( 10, 20, 30, 40, 60, 100 ),
                #abseta = cms.vdouble( 0.0, 1.2, 2.4),
                el_pt  = cms.vdouble(0, 5, 10, 20, 30, 40, 60, 100 ),
                el_abseta = cms.vdouble(0.0, 0.8, 1.479, 2.5),
                ## flags and conditions required at the denominator,
                #passingMVA94XAutumn18SUSYtight = cms.vstring("pass"),
                passingMVA94XAutumn18SUSYveryLoose = cms.vstring("pass"),
                passEleVeryLoose = cms.vstring("pass"),
                #miniIsoAll = cms.vdouble(0.,4.,),
                #absPFIso_All = cms.vdouble(0.,4.,),
                #tag_IsoMu24_eta2p1 = cms.vstring("pass"), ## i.e. use only events for which this flag is true
                #pair_dz = cms.vdouble(-1.,1.)             ## and for which -1.0 < dz < 1.0

            ),
            BinToPDFmap = cms.vstring("vpvPlusExpo"), ## PDF to use, as defined below
        )
    ),
    ## PDF for signal and background (double voigtian + exponential background)
    PDFs = cms.PSet(
        vpvPlusExpo = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
            "SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.0])",
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.0])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
#        vpvPlusExpo = cms.vstring(
#            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
#            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
#            "SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
#            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
#            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
#            "efficiency[0.9,0,1]",
#            "signalFractionInPassing[0.9]"
#        ),
    ),
    ## How to do the fit
    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(40),
    saveDistributionsPlot = cms.bool(True),
    NumCPU = cms.uint32(1), ## leave to 1 for now, RooFit gives funny results otherwise
    SaveWorkspace = cms.bool(False),
)

#### Slighly different configuration for isolation, where the "passing" is defined by a cut
"""process.TnP_Muon_Iso = process.TnP_Muon_ID.clone(
    OutputFileName = cms.string("TnP_Muon_Iso_Simple.root"),
    ## More variables
    Variables = process.TnP_Muon_ID.Variables.clone(
       # combRelIsoPF04dBeta = cms.vstring("PF Combined Relative Iso", "-100", "99999", ""),
        tag_nVertices       = cms.vstring("N(vertices)", "0", "99", "")
    ),
    ## Cuts: name, variable, cut threshold
    Cuts = cms.PSet()
       # PFIsoLoose = cms.vstring("PFIsoLoose" ,"combRelIsoPF04dBeta", "0.20"),
       # PFIsoTight = cms.vstring("PFIsoTight" ,"combRelIsoPF04dBeta", "0.12"),
   # ),
    ## What to fit
    Efficiencies = cms.PSet(
        Iso_vtx_tight = cms.PSet(
            UnbinnedVariables = cms.vstring("mass"),
            EfficiencyCategoryAndState = cms.vstring("PFIsoTight", "below"), ## variable is below cut value 
            BinnedVariables = cms.PSet(
                tag_nVertices = cms.vdouble(0.5,4.5,8.5,12.5,16.5,20.5,24.5,30.5), 
                PF = cms.vstring("pass"),                 ## 
                tag_IsoMu24_eta2p1 = cms.vstring("pass"), ## tag trigger matched
                pair_dz = cms.vdouble( -1.,1. ),          ## and for which -1.0 < dz < 1.0
                pt     = cms.vdouble( 25,  100 ),
                abseta = cms.vdouble( 0.0, 2.4 ),
            ),
            BinToPDFmap = cms.vstring("vpvPlusExpo"), ## PDF to use, as defined below
        ),
        Iso_vtx_loose = cms.PSet(
            UnbinnedVariables = cms.vstring("mass"),
            EfficiencyCategoryAndState = cms.vstring("PFIsoLoose", "below"), ## variable is below cut value 
            BinnedVariables = cms.PSet(
                tag_nVertices = cms.vdouble(0.5,4.5,8.5,12.5,16.5,20.5,24.5,30.5), 
                PF = cms.vstring("pass"),                 ## 
                tag_IsoMu24_eta2p1 = cms.vstring("pass"), ## tag trigger matched
                pair_dz = cms.vdouble( -1.,1. ),          ## and for which -1.0 < dz < 1.0
                pt     = cms.vdouble( 25,  100 ),
                abseta = cms.vdouble( 0.0, 2.4 ),
            ),
            BinToPDFmap = cms.vstring("vpvPlusExpo"), ## PDF to use, as defined below
        ),
    ),
)
"""
process.p1 = cms.Path(process.TnP_Electron_ID)
#process.p2 = cms.Path(process.TnP_Muon_Iso)
