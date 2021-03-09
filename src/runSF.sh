




#root -b -q -l 'extractPlotsAndComputeTheSFs.C("Medium_PtEtaBins","./fit_output/TnP_MuonID_data2017_mu17_Gmedsip2_A.root","./fit_output/TnP_MuonID_mc2017_weight_mu17_Gmedsip2_A.root")'
#python createJsonFile.py EfficienciesAndSF_Medium_pt_eta.root ./sf_output/TnPZ_mu17_Gmedsip2_A.json
#mv EfficienciesAndSF_Medium_pt_eta.root ./sf_output/EffandSF_Z_mu17_Gmedsip2_A.root


#root -b -q -l 'extractPlotsAndComputeTheSFs.C("Medium_PtEtaBins","./fit_output/TnP_MuonID_data2017_mu17_Smedsip2_A.root","./fit_output/TnP_MuonID_mc2017_weight_mu17_Smedsip2_A.root")'
#python createJsonFile.py EfficienciesAndSF_Medium_pt_eta.root ./sf_output/TnPZ_mu17_Smedsip2_A.json
#mv EfficienciesAndSF_Medium_pt_eta.root ./sf_output/EffandSF_Z_mu17_Smedsip2_A.root


#root -b -q -l 'extractPlotsAndComputeTheSFs.C("Medium_PtEtaBins","./fit_output/TnP_MuonID_data2017_mu17_GminiIso5_A.root","./fit_output/TnP_MuonID_mc2017_weight_mu17_GminiIso5_A.root")'
#python createJsonFile.py EfficienciesAndSF_Medium_pt_eta.root ./sf_output/TnPZ_mu17_GminiIso5_A.json
#mv EfficienciesAndSF_Medium_pt_eta.root ./sf_output/EffandSF_Z_mu17_GminiIso5_A.root

root -b -q -l 'extractPlotsAndComputeTheSFs.C("Tight_PtEtaBins","analized/TnPZ_susyID_data2018_tight.root","analized/TnPZ_susyID_MC2018_tight.root")'
python createJsonFile.py EfficienciesAndSF_Medium_pt_eta.root ./sf_output/TnPZ_mu17_GSIP3D_A.json
mv EfficienciesAndSF_Medium_pt_eta.root ./sf_output/EffandSF_Z_mu17_GSIP3D_A.root
