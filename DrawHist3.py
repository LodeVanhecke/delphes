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
  c.BuildLegend(1,1,1,1)
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
      c.cd(i+1)
      hist[i].DrawNormalized('e same box')
     else:
      c.cd(i+1)
      hist[i].Draw('e same box')
    else:
     if norm == True:
      c.cd(i+1)
      hist[i].DrawNormalized('same box')
     else:
      c.cd(i+1)
      hist[i].Draw('same box')
    if logx == True:
     c.SetLogx()
    if logy == True:
     c.SetLogy()
  c.BuildLegend()
  c.SaveAs(filename)



file = ROOT.TFile(sys.argv[1],"READ")


histMaxCKaon = [file.Get('histMaxCKaonL')]+[file.Get('histMaxCKaonS')]+[file.Get('histMaxCKaonC')]+[file.Get('histMaxCKaonB')]
Cosmetic2(histMaxCKaon,'DeltaPhi of max charged kaons in jet','DeltaTheta of max charged kaons in jet',False,False,False,False,'histMaxCKaon_'+sys.argv[1][:-5]+'.png')

histMaxNKaon = [file.Get('histMaxNKaonL')]+[file.Get('histMaxNKaonS')]+[file.Get('histMaxNKaonC')]+[file.Get('histMaxNKaonB')]
Cosmetic2(histMaxNKaon,'DeltaPhi of max neutral kaons in jet','DeltaTheta of max neutral kaons in jet',False,False,False,False,'histMaxNKaon_'+sys.argv[1][:-5]+'.png')


histMaxCPion = [file.Get('histMaxCPionL')]+[file.Get('histMaxCPionS')]+[file.Get('histMaxCPionC')]+[file.Get('histMaxCPionB')]
Cosmetic2(histMaxCPion,'DeltaPhi of max charged pions in jet','DeltaTheta of max charged pions in jet',False,False,False,False,'histMaxCPion_'+sys.argv[1][:-5]+'.png')

histMaxNPion = [file.Get('histMaxNPionL')]+[file.Get('histMaxNPionS')]+[file.Get('histMaxNPionC')]+[file.Get('histMaxNPionB')]
Cosmetic2(histMaxNPion,'DeltaPhi of max neutral pions in jet','DeltaTheta of max neutral pions in jet',False,False,False,False,'histMaxNPion_'+sys.argv[1][:-5]+'.png')


histMaxElec = [file.Get('histMaxElecL')]+[file.Get('histMaxElecS')]+[file.Get('histMaxElecC')]+[file.Get('histMaxElecB')]
Cosmetic2(histMaxElec,'DeltaPhi of max electrons/positrons in jet','DeltaTheta of max electrons/positrons in jet',False,False,False,False,'histMaxElec_'+sys.argv[1][:-5]+'.png')


histMaxMuon = [file.Get('histMaxMuonL')]+[file.Get('histMaxMuonS')]+[file.Get('histMaxMuonC')]+[file.Get('histMaxMuonB')]
Cosmetic2(histMaxMuon,'DeltaPhi of max muons (pos and neg) in jet','DeltaTheta of max muons (pos and neg) in jet',False,False,False,False,'histMaxMuon_'+sys.argv[1][:-5]+'.png')


histMaxProt = [file.Get('histMaxProtL')]+[file.Get('histMaxProtS')]+[file.Get('histMaxProtC')]+[file.Get('histMaxProtB')]
Cosmetic2(histMaxProt,'DeltaPhi of max protons in jet','DeltaTheta of max protons in jet',False,False,False,False,'histMaxProt_'+sys.argv[1][:-5]+'.png')


histMaxNeut = [file.Get('histMaxNeutL')]+[file.Get('histMaxNeutS')]+[file.Get('histMaxNeutC')]+[file.Get('histMaxNeutB')]
Cosmetic2(histMaxNeut,'DeltaPhi of max neutrons in jet','DeltaTheta of max neutrons in jet',False,False,False,False,'histMaxNeut_'+sys.argv[1][:-5]+'.png')


histMaxPhot = [file.Get('histMaxPhotL')]+[file.Get('histMaxPhotS')]+[file.Get('histMaxPhotC')]+[file.Get('histMaxPhotB')]
Cosmetic2(histMaxPhot,'DeltaPhi of max photons in jet','DeltaTheta of max photons in jet',False,False,False,False,'histMaxPhot_'+sys.argv[1][:-5]+'.png')



histCloseNeut = [file.Get('histCloseNeutL')]+[file.Get('histCloseNeutS')]+[file.Get('histCloseNeutC')]+[file.Get('histCloseNeutB')]
Cosmetic2(histCloseNeut,'DeltaPhi of closest neutrons in jet','DeltaTheta of closest neutrons in jet',False,False,False,False,'histCloseNeut_'+sys.argv[1][:-5]+'.png')




histJetL = [file.Get('histJetCKaonL')]+[file.Get('histJetNKaonL')]+[file.Get('histJetCPionL')]+[file.Get('histJetNPionL')]+[file.Get('histJetElecL')]+[file.Get('histJetMuonL')]+[file.Get('histJetProtL')]+[file.Get('histJetNeutL')]+[file.Get('histJetPhotL')]
Cosmetic3(histJetL,'DeltaPhi of particles in jet','DeltaTheta of particles in jet',False,False,False,False,'histJetL_'+sys.argv[1][:-5]+'.png')

histJetS = [file.Get('histJetCKaonS')]+[file.Get('histJetNKaonS')]+[file.Get('histJetCPionS')]+[file.Get('histJetNPionS')]+[file.Get('histJetElecS')]+[file.Get('histJetMuonS')]+[file.Get('histJetProtS')]+[file.Get('histJetNeutS')]+[file.Get('histJetPhotS')]
Cosmetic3(histJetS,'DeltaPhi of particles in jet','DeltaTheta of particles in jet',False,False,False,False,'histJetS_'+sys.argv[1][:-5]+'.png')

histJetC = [file.Get('histJetCKaonC')]+[file.Get('histJetNKaonC')]+[file.Get('histJetCPionC')]+[file.Get('histJetNPionC')]+[file.Get('histJetElecC')]+[file.Get('histJetMuonC')]+[file.Get('histJetProtC')]+[file.Get('histJetNeutC')]+[file.Get('histJetPhotC')]
Cosmetic3(histJetC,'DeltaPhi of particles in jet','DeltaTheta of particles in jet',False,False,False,False,'histJetC_'+sys.argv[1][:-5]+'.png')

histJetB = [file.Get('histJetCKaonB')]+[file.Get('histJetNKaonB')]+[file.Get('histJetCPionB')]+[file.Get('histJetNPionB')]+[file.Get('histJetElecB')]+[file.Get('histJetMuonB')]+[file.Get('histJetProtB')]+[file.Get('histJetNeutB')]+[file.Get('histJetPhotB')]
Cosmetic3(histJetB,'DeltaPhi of particles in jet','DeltaTheta of particles in jet',False,False,False,False,'histJetB_'+sys.argv[1][:-5]+'.png')
