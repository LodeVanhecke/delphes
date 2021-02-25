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
      hist[i].DrawNormalized('same e')
     else:
      hist[i].Draw('same e')
    else:
     if norm == True:
      hist[i].DrawNormalized('same')
     else:
      hist[i].Draw('same')
    if logx == True:
     c.SetLogx()
    if logy == True:
     c.SetLogy()
  c.BuildLegend()
  c.SaveAs(filename)

def Cosmetic2(hist,xtitle,ytitle,error,norm,logx,logy,filename):
  c = ROOT.TCanvas()
  c.Divide(2,2,0.01,0.01)
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
      hist[i].DrawNormalized('e box')
     else:
      c.cd(i+1)
      hist[i].Draw('e box')
    else:
     if norm == True:
      c.cd(i+1)
      hist[i].DrawNormalized('box')
     else:
      c.cd(i+1)
      hist[i].Draw('box')
    if logx == True:
     c.SetLogx()
    if logy == True:
     c.SetLogy()
 # c.BuildLegend()
  c.SaveAs(filename)



file = ROOT.TFile(sys.argv[1],"READ")


histNJet = [file.Get('histNJetL')]+[file.Get('histNJetS')]+[file.Get('histNJetC')]+[file.Get('histNJetB')]
Cosmetic(histNJet,'Number of jets in event','',False,True,False,False,'histNJet_'+sys.argv[1][:-5]+'.png')


histCKaon = [file.Get('histCKaonL')]+[file.Get('histCKaonS')]+[file.Get('histCKaonC')]+[file.Get('histCKaonB')]
Cosmetic2(histCKaon,'DeltaPhi of charged kaons in jet','DeltaEta of charged kaons in jet',False,False,False,False,'histCKaon_'+sys.argv[1][:-5]+'.png')

histNKaon = [file.Get('histNKaonL')]+[file.Get('histNKaonS')]+[file.Get('histNKaonC')]+[file.Get('histNKaonB')]
Cosmetic2(histNKaon,'DeltaPhi of neutral kaons in jet','DeltaEta of neutral kaons in jet',False,False,False,False,'histNKaon_'+sys.argv[1][:-5]+'.png')


histCPion = [file.Get('histCPionL')]+[file.Get('histCPionS')]+[file.Get('histCPionC')]+[file.Get('histCPionB')]
Cosmetic2(histCPion,'DeltaPhi of charged pions in jet','DeltaEta of charged pions in jet',False,False,False,False,'histCPion_'+sys.argv[1][:-5]+'.png')

histNPion = [file.Get('histNPionL')]+[file.Get('histNPionS')]+[file.Get('histNPionC')]+[file.Get('histNPionB')]
Cosmetic2(histNPion,'DeltaPhi of neutral pions in jet','DeltaEta of neutral pions in jet',False,False,False,False,'histNPion_'+sys.argv[1][:-5]+'.png')


histElec = [file.Get('histElecL')]+[file.Get('histElecS')]+[file.Get('histElecC')]+[file.Get('histElecB')]
Cosmetic2(histElec,'DeltaPhi of electrons/positrons in jet','DeltaEta of electrons/positrons in jet',False,False,False,False,'histElec_'+sys.argv[1][:-5]+'.png')


histMuon = [file.Get('histMuonL')]+[file.Get('histMuonS')]+[file.Get('histMuonC')]+[file.Get('histMuonB')]
Cosmetic2(histMuon,'DeltaPhi of muons (pos and neg) in jet','DeltaEta of muons (pos and neg) in jet',False,False,False,False,'histMuon_'+sys.argv[1][:-5]+'.png')


histProt = [file.Get('histProtL')]+[file.Get('histProtS')]+[file.Get('histProtC')]+[file.Get('histProtB')]
Cosmetic2(histProt,'DeltaPhi of protons in jet','DeltaEta of protons in jet',False,False,False,False,'histProt_'+sys.argv[1][:-5]+'.png')


histNeut = [file.Get('histNeutL')]+[file.Get('histNeutS')]+[file.Get('histNeutC')]+[file.Get('histNeutB')]
Cosmetic2(histNeut,'DeltaPhi of neutrons in jet','DeltaEta of neutrons in jet',False,False,False,False,'histNeut_'+sys.argv[1][:-5]+'.png')




histMaxCKaon = [file.Get('histMaxCKaonL')]+[file.Get('histMaxCKaonS')]+[file.Get('histMaxCKaonC')]+[file.Get('histMaxCKaonB')]
Cosmetic2(histMaxCKaon,'DeltaPhi of max charged kaons in jet','DeltaEta of max charged kaons in jet',False,False,False,False,'histMaxCKaon_'+sys.argv[1][:-5]+'.png')

histMaxNKaon = [file.Get('histMaxNKaonL')]+[file.Get('histMaxNKaonS')]+[file.Get('histMaxNKaonC')]+[file.Get('histMaxNKaonB')]
Cosmetic2(histMaxNKaon,'DeltaPhi of max neutral kaons in jet','DeltaEta of max neutral kaons in jet',False,False,False,False,'histMaxNKaon_'+sys.argv[1][:-5]+'.png')


histMaxCPion = [file.Get('histMaxCPionL')]+[file.Get('histMaxCPionS')]+[file.Get('histMaxCPionC')]+[file.Get('histMaxCPionB')]
Cosmetic2(histMaxCPion,'DeltaPhi of max charged pions in jet','DeltaEta of max charged pions in jet',False,False,False,False,'histMaxCPion_'+sys.argv[1][:-5]+'.png')

histMaxNPion = [file.Get('histMaxNPionL')]+[file.Get('histMaxNPionS')]+[file.Get('histMaxNPionC')]+[file.Get('histMaxNPionB')]
Cosmetic2(histMaxNPion,'DeltaPhi of max neutral pions in jet','DeltaEta of max neutral pions in jet',False,False,False,False,'histMaxNPion_'+sys.argv[1][:-5]+'.png')


histMaxElec = [file.Get('histMaxElecL')]+[file.Get('histMaxElecS')]+[file.Get('histMaxElecC')]+[file.Get('histMaxElecB')]
Cosmetic2(histMaxElec,'DeltaPhi of max electrons/positrons in jet','DeltaEta of max electrons/positrons in jet',False,False,False,False,'histMaxElec_'+sys.argv[1][:-5]+'.png')


histMaxMuon = [file.Get('histMaxMuonL')]+[file.Get('histMaxMuonS')]+[file.Get('histMaxMuonC')]+[file.Get('histMaxMuonB')]
Cosmetic2(histMaxMuon,'DeltaPhi of max muons (pos and neg) in jet','DeltaEta of max muons (pos and neg) in jet',False,False,False,False,'histMaxMuon_'+sys.argv[1][:-5]+'.png')


histMaxProt = [file.Get('histMaxProtL')]+[file.Get('histMaxProtS')]+[file.Get('histMaxProtC')]+[file.Get('histMaxProtB')]
Cosmetic2(histMaxProt,'DeltaPhi of max protons in jet','DeltaEta of max protons in jet',False,False,False,False,'histMaxProt_'+sys.argv[1][:-5]+'.png')


histMaxNeut = [file.Get('histMaxNeutL')]+[file.Get('histMaxNeutS')]+[file.Get('histMaxNeutC')]+[file.Get('histMaxNeutB')]
Cosmetic2(histMaxNeut,'DeltaPhi of max neutrons in jet','DeltaEta of max neutrons in jet',False,False,False,False,'histMaxNeut_'+sys.argv[1][:-5]+'.png')




histDCKaon = [file.Get('histDCKaonL')]+[file.Get('histDCKaonS')]+[file.Get('histDCKaonC')]+[file.Get('histDCKaonB')]
Cosmetic2(histDCKaon,'dx of charged kaons in jet','dy of charged kaons in jet',False,False,False,False,'histDCKaon_'+sys.argv[1][:-5]+'.png')

histDNKaon = [file.Get('histDNKaonL')]+[file.Get('histDNKaonS')]+[file.Get('histDNKaonC')]+[file.Get('histDNKaonB')]
Cosmetic2(histDNKaon,'dx of neutral kaons in jet','dy of neutral kaons in jet',False,False,False,False,'histDNKaon_'+sys.argv[1][:-5]+'.png')


histDCPion = [file.Get('histDCPionL')]+[file.Get('histDCPionS')]+[file.Get('histDCPionC')]+[file.Get('histDCPionB')]
Cosmetic2(histDCPion,'dx of charged pions in jet','dy of charged pions in jet',False,False,False,False,'histDCPion_'+sys.argv[1][:-5]+'.png')

histDNPion = [file.Get('histDNPionL')]+[file.Get('histDNPionS')]+[file.Get('histDNPionC')]+[file.Get('histDNPionB')]
Cosmetic2(histDNPion,'dx of neutral pions in jet','dy of neutral pions in jet',False,False,False,False,'histDNPion_'+sys.argv[1][:-5]+'.png')


histDElec = [file.Get('histDElecL')]+[file.Get('histDElecS')]+[file.Get('histDElecC')]+[file.Get('histDElecB')]
Cosmetic2(histDElec,'dx of electrons/positrons in jet','dy of electrons/positrons in jet',False,False,False,False,'histDElec_'+sys.argv[1][:-5]+'.png')


histDMuon = [file.Get('histDMuonL')]+[file.Get('histDMuonS')]+[file.Get('histDMuonC')]+[file.Get('histDMuonB')]
Cosmetic2(histDMuon,'dx of muons (pos and neg) in jet','dy of muons (pos and neg) in jet',False,False,False,False,'histDMuon_'+sys.argv[1][:-5]+'.png')


histDProt = [file.Get('histDProtL')]+[file.Get('histDProtS')]+[file.Get('histDProtC')]+[file.Get('histDProtB')]
Cosmetic2(histDProt,'dx of protons in jet','dy of protons in jet',False,False,False,False,'histDProt_'+sys.argv[1][:-5]+'.png')


histDNeut = [file.Get('histDNeutL')]+[file.Get('histDNeutS')]+[file.Get('histDNeutC')]+[file.Get('histDNeutB')]
Cosmetic2(histDNeut,'dx of neutrons in jet','dy of neutrons in jet',False,False,False,False,'histDNeut_'+sys.argv[1][:-5]+'.png')
