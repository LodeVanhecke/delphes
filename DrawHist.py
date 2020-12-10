import sys
import ROOT

def Cosmetic(hist,xtitle,ytitle,norm,logx,logy,filename):
  c = ROOT.TCanvas()
  ROOT.gStyle.SetOptStat(0)
  hist[0].GetXaxis().SetTitle(xtitle)
  hist[0].GetYaxis().SetTitle(ytitle)
  for i in range(len(hist)):
    hist[i].SetLineColor(i+1)
    hist[i].SetLineWidth(3)
    hist[i].SetTitle("")
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

file = ROOT.TFile(sys.argv[1],"READ")
histJetPT = [file.Get('histGenJetPTD').Rebin(2)]+[file.Get('histGenJetPTU').Rebin(2)]+[file.Get('histGenJetPTS').Rebin(2)]+[file.Get('histGenJetPTC').Rebin(2)]+[file.Get('histGenJetPTB').Rebin(2)]
Cosmetic(histJetPT,'Transverse momentum','',True,False,False,'histJetPT_'+sys.argv[1][:-5]+'.png')

histNCKaon = [file.Get('histNCKaonD')]+[file.Get('histNCKaonU')]+[file.Get('histNCKaonS')]+[file.Get('histNCKaonC')]+[file.Get('histNCKaonB')]
Cosmetic(histNCKaon,'Number charged kaons in jet','',False,False,True,'histNCKaon_'+sys.argv[1][:-5]+'.png')

histNCPion = [file.Get('histNCPionD')]+[file.Get('histNCPionU')]+[file.Get('histNCPionS')]+[file.Get('histNCPionC')]+[file.Get('histNCPionB')]
Cosmetic(histNCPion,'Number charged pions in jet','',False,False,True,'histNCPion_'+sys.argv[1][:-5]+'.png')

histJetC = [file.Get('histJetCD')]+[file.Get('histJetCU')]+[file.Get('histJetCS')]+[file.Get('histJetCC')]+[file.Get('histJetCB')]
Cosmetic(histJetC,'Charge of jet','',False,False,True,'histJetC_'+sys.argv[1][:-5]+'.png')
