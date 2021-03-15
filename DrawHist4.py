import sys
import ROOT

def Cosmetic(hist,xtitle,ytitle,error,norm,logx,logy,filename):
  c = ROOT.TCanvas()
  ROOT.gStyle.SetOptStat(0)
  hist[0].GetXaxis().SetTitle(xtitle)
  hist[0].GetYaxis().SetTitle(ytitle)
  for i in range(len(hist)):
    hist[i].SetLineColor(i+1)
    hist[i].SetLineWidth(1)
    hist[i].SetTitle("")
    if error == True:
     if norm == True:
      hist[i].DrawNormalized('same e hist')
     else:
      hist[i].Draw('same e hist')
    else:
     if norm == True:
      hist[i].DrawNormalized('same hist')
     else:
      hist[i].Draw('same hist')
    if logx == True:
     c.SetLogx()
    if logy == True:
     c.SetLogy()
  c.BuildLegend(1,1,1,1)
  c.SaveAs(filename)

def Cosmetic2(hist,xtitle,ytitle,error,norm,logx,logy,filename):
  c = ROOT.TCanvas()
  c.Divide(2,1,0.01,0.01)
  ROOT.gStyle.SetOptStat(0)
  for i in range(len(hist)):
    hist[i].GetXaxis().SetTitle(xtitle)
    hist[i].GetYaxis().SetTitle(ytitle)
    hist[i].SetFillColor(i+1)
    hist[i].SetLineWidth(1)
   # hist[i].SetTitle("")
    if error == True:
     if norm == True:
      c.cd(i+1)
      hist[i].DrawNormalized('e colz')
     else:
      c.cd(i+1)
      hist[i].Draw('e colz')
    else:
     if norm == True:
      c.cd(i+1)
      hist[i].DrawNormalized('colz')
     else:
      c.cd(i+1)
      hist[i].Draw('colz')
    if logx == True:
     c.SetLogx()
    if logy == True:
     c.SetLogy()
 # c.BuildLegend()
  c.SaveAs(filename)


def Cosmetic3(hist,xtitle,ytitle,error,norm,logx,logy,filename):
  c = ROOT.TCanvas()
  ROOT.gStyle.SetOptStat(0)
  for i in range(len(hist)):
    hist[i].GetXaxis().SetTitle(xtitle)
    hist[i].GetYaxis().SetTitle(ytitle)
    hist[i].SetFillColorAlpha(i+1,0.70)
    hist[i].SetLineWidth(1)
    hist[i].SetTitle("")
    if error == True:
     if norm == True:
      hist[i].DrawNormalized('e same box')
     else:
      hist[i].Draw('e same box')
    else:
     if norm == True:
      hist[i].DrawNormalized('same box')
     else:
      hist[i].Draw('same box')
    if logx == True:
     c.SetLogx()
    if logy == True:
     c.SetLogy()
  c.BuildLegend()
  c.SaveAs(filename)



file = ROOT.TFile(sys.argv[1],"READ")


#histMaxCKaon = [file.Get('histMaxCKaonL')]+[file.Get('histMaxCKaonS')]
#Cosmetic2(histMaxCKaon,'DeltaPhi of max charged kaons in jet','DeltaTheta of max charged kaons in jet',False,False,False,False,'histMaxCKaon_'+sys.argv[1][:-5]+'.png')

#histMaxNKaon = [file.Get('histMaxNKaonL')]+[file.Get('histMaxNKaonS')]
#Cosmetic2(histMaxNKaon,'DeltaPhi of max neutral kaons in jet','DeltaTheta of max neutral kaons in jet',False,False,False,False,'histMaxNKaon_'+sys.argv[1][:-5]+'.png')


#histMaxCPion = [file.Get('histMaxCPionL')]+[file.Get('histMaxCPionS')]
#Cosmetic2(histMaxCPion,'DeltaPhi of max charged pions in jet','DeltaTheta of max charged pions in jet',False,False,False,False,'histMaxCPion_'+sys.argv[1][:-5]+'.png')

#histMaxNPion = [file.Get('histMaxNPionL')]+[file.Get('histMaxNPionS')]
#Cosmetic2(histMaxNPion,'DeltaPhi of max neutral pions in jet','DeltaTheta of max neutral pions in jet',False,False,False,False,'histMaxNPion_'+sys.argv[1][:-5]+'.png')


#histMaxElec = [file.Get('histMaxElecL')]+[file.Get('histMaxElecS')]
#Cosmetic2(histMaxElec,'DeltaPhi of max electrons/positrons in jet','DeltaTheta of max electrons/positrons in jet',False,False,False,False,'histMaxElec_'+sys.argv[1][:-5]+'.png')


#histMaxMuon = [file.Get('histMaxMuonL')]+[file.Get('histMaxMuonS')]
#Cosmetic2(histMaxMuon,'DeltaPhi of max muons (pos and neg) in jet','DeltaTheta of max muons (pos and neg) in jet',False,False,False,False,'histMaxMuon_'+sys.argv[1][:-5]+'.png')


#histMaxProt = [file.Get('histMaxProtL')]+[file.Get('histMaxProtS')]
#Cosmetic2(histMaxProt,'DeltaPhi of max protons in jet','DeltaTheta of max protons in jet',False,False,False,False,'histMaxProt_'+sys.argv[1][:-5]+'.png')


#histMaxNeut = [file.Get('histMaxNeutL')]+[file.Get('histMaxNeutS')]
#Cosmetic2(histMaxNeut,'DeltaPhi of max neutrons in jet','DeltaTheta of max neutrons in jet',False,False,False,False,'histMaxNeut_'+sys.argv[1][:-5]+'.png')


#histMaxPhot = [file.Get('histMaxPhotL')]+[file.Get('histMaxPhotS')]
#Cosmetic2(histMaxPhot,'DeltaPhi of max photons in jet','DeltaTheta of max photons in jet',False,False,False,False,'histMaxPhot_'+sys.argv[1][:-5]+'.png')



#histCloseNeut = [file.Get('histCloseNeutL')]+[file.Get('histCloseNeutS')]
#Cosmetic2(histCloseNeut,'DeltaPhi of closest neutrons in jet','DeltaTheta of closest neutrons in jet',False,False,False,False,'histCloseNeut_'+sys.argv[1][:-5]+'.png')


histJetL = [file.Get('histJetCKaonL')]+[file.Get('histJetNKaonL')]+[file.Get('histJetCPionL')]+[file.Get('histJetNPionL')]+[file.Get('histJetElecL')]+[file.Get('histJetMuonL')]+[file.Get('histJetProtL')]+[file.Get('histJetNeutL')]+[file.Get('histJetPhotL')]
Cosmetic3(histJetL,'DeltaPhi of particles in jet','DeltaTheta of particles in jet',False,False,False,False,'histJetL_'+sys.argv[1][:-5]+'.pdf')

histJetS = [file.Get('histJetCKaonS')]+[file.Get('histJetNKaonS')]+[file.Get('histJetCPionS')]+[file.Get('histJetNPionS')]+[file.Get('histJetElecS')]+[file.Get('histJetMuonS')]+[file.Get('histJetProtS')]+[file.Get('histJetNeutS')]+[file.Get('histJetPhotS')]
Cosmetic3(histJetS,'DeltaPhi of particles in jet','DeltaTheta of particles in jet',False,False,False,False,'histJetS_'+sys.argv[1][:-5]+'.pdf')


#histRatCPionPhot = [file.Get('histRatCPionPhotL')]+[file.Get('histRatCPionPhotS')]
#Cosmetic(histRatCPionPhot,'Ratio of charged pions and photons','',False,True,False,False,'histRatCPionPhot_'+sys.argv[1][:-5]+'.png')


#histRatNPionPhot = [file.Get('histRatNPionPhotL')]+[file.Get('histRatNPionPhotS')]
#Cosmetic(histRatNPionPhot,'Ratio of neutral pions and photons','',False,True,False,False,'histRatNPionPhot_'+sys.argv[1][:-5]+'.png')


#histRatNPionElec = [file.Get('histRatNPionElecL')]+[file.Get('histRatNPionElecS')]
#Cosmetic(histRatNPionElec,'Ratio of neutral pions and electrons/positrons','',False,True,False,False,'histRatNPionElec_'+sys.argv[1][:-5]+'.png')


#histRatCPionMuon = [file.Get('histRatCPionMuonL')]+[file.Get('histRatCPionMuonS')]
#Cosmetic(histRatCPionMuon,'Ratio of charged pions and muons','',False,True,False,False,'histRatCPionMuon_'+sys.argv[1][:-5]+'.png')


#histRatCKaonMuon = [file.Get('histRatCKaonMuonL')]+[file.Get('histRatCKaonMuonS')]
#Cosmetic(histRatCKaonMuon,'Ratio of charged kaons and muons','',False,True,False,False,'histRatCKaonMuon_'+sys.argv[1][:-5]+'.png')


#histRatNKaonCPion = [file.Get('histRatNKaonCPionL')]+[file.Get('histRatNKaonCPionS')]
#Cosmetic(histRatNKaonCPion,'Ratio of neutral kaons and charged pions','',False,True,False,False,'histRatNKaonCPion_'+sys.argv[1][:-5]+'.png')

