#ifdef __CLING__
#pragma cling optimize(0)
#endif
void Fit()
{
//=========Macro generated from canvas: Canvas_1/Canvas_1
//=========  (Sat Nov 30 18:47:43 2024) by ROOT version 6.30/04
   TCanvas *Canvas_1 = new TCanvas("Canvas_1", "Canvas_1",258,79,1483,829);
   Canvas_1->Range(-512.5001,-1.019297,4612.5,6.163369);
   Canvas_1->SetFillColor(0);
   Canvas_1->SetBorderMode(0);
   Canvas_1->SetBorderSize(2);
   Canvas_1->SetLogy();
   Canvas_1->SetFrameBorderMode(0);
   Canvas_1->SetFrameBorderMode(0);
   
   TH1F *htemp__1 = new TH1F("htemp__1","adc40",100,0,4100);
   htemp__1->SetBinContent(1,147080);
   htemp__1->SetBinContent(3,340);
   htemp__1->SetBinContent(4,10856);
   htemp__1->SetBinContent(5,88697);
   htemp__1->SetBinContent(6,28781);
   htemp__1->SetBinContent(7,562);
   htemp__1->SetBinContent(11,3);
   htemp__1->SetBinContent(12,2);
   htemp__1->SetBinContent(13,5);
   htemp__1->SetBinContent(14,2);
   htemp__1->SetBinContent(15,2);
   htemp__1->SetBinContent(16,133);
   htemp__1->SetBinContent(17,1208);
   htemp__1->SetBinContent(18,2549);
   htemp__1->SetBinContent(19,2912);
   htemp__1->SetBinContent(20,1473);
   htemp__1->SetBinContent(21,496);
   htemp__1->SetBinContent(22,28);
   htemp__1->SetBinContent(23,2);
   htemp__1->SetBinContent(24,5);
   htemp__1->SetBinContent(25,2);
   htemp__1->SetBinContent(26,2);
   htemp__1->SetBinContent(27,2);
   htemp__1->SetBinContent(28,1);
   htemp__1->SetBinContent(29,2);
   htemp__1->SetBinContent(30,1);
   htemp__1->SetBinContent(31,1);
   htemp__1->SetBinContent(32,4);
   htemp__1->SetBinContent(33,2);
   htemp__1->SetBinContent(34,2);
   htemp__1->SetBinContent(35,4);
   htemp__1->SetBinContent(36,2);
   htemp__1->SetBinContent(37,6);
   htemp__1->SetBinContent(38,10);
   htemp__1->SetBinContent(39,25);
   htemp__1->SetBinContent(40,51);
   htemp__1->SetBinContent(41,76);
   htemp__1->SetBinContent(42,60);
   htemp__1->SetBinContent(43,31);
   htemp__1->SetBinContent(44,20);
   htemp__1->SetBinContent(45,4);
   htemp__1->SetBinContent(46,1);
   htemp__1->SetBinContent(47,1);
   htemp__1->SetBinContent(54,1);
   htemp__1->SetBinContent(57,1);
   htemp__1->SetBinContent(63,1);
   htemp__1->SetBinContent(65,1);
   htemp__1->SetBinContent(66,1);
   htemp__1->SetBinContent(92,1);
   htemp__1->SetEntries(285452);
   htemp__1->SetDirectory(nullptr);
   
   TPaveStats *ptstats = new TPaveStats(0.78,0.775,0.98,0.935,"brNDC");
   ptstats->SetName("stats");
   ptstats->SetBorderSize(1);
   ptstats->SetFillColor(0);
   ptstats->SetTextAlign(12);
   ptstats->SetTextFont(42);
   TText *ptstats_LaTex = ptstats->AddText("htemp");
   ptstats_LaTex->SetTextSize(0.0368);
   ptstats_LaTex = ptstats->AddText("Entries = 285452 ");
   ptstats_LaTex = ptstats->AddText("Mean  =  110.4");
   ptstats_LaTex = ptstats->AddText("Std Dev   =  156.3");
   ptstats->SetOptStat(1111);
   ptstats->SetOptFit(0);
   ptstats->Draw();
   htemp__1->GetListOfFunctions()->Add(ptstats);
   ptstats->SetParent(htemp__1);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   htemp__1->SetLineColor(ci);
   htemp__1->GetXaxis()->SetTitle("adc40");
   htemp__1->GetXaxis()->SetRange(1,100);
   htemp__1->GetXaxis()->SetLabelFont(42);
   htemp__1->GetXaxis()->SetTitleOffset(1);
   htemp__1->GetXaxis()->SetTitleFont(42);
   htemp__1->GetYaxis()->SetLabelFont(42);
   htemp__1->GetYaxis()->SetTitleFont(42);
   htemp__1->GetZaxis()->SetLabelFont(42);
   htemp__1->GetZaxis()->SetTitleOffset(1);
   htemp__1->GetZaxis()->SetTitleFont(42);
   htemp__1->Draw("");
   
   TPaveText *pt = new TPaveText(0.4452239,0.94,0.5547761,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *pt_LaTex = pt->AddText("adc40");
   pt->Draw();
   Canvas_1->Modified();
   Canvas_1->SetSelected(Canvas_1);

   // Retrieve the bin edges for bins 21 and 32 Choosed
   double xLow = htemp__1->GetXaxis()->GetBinLowEdge(12);
   double xHigh = htemp__1->GetXaxis()->GetBinUpEdge(32);

   // Fit a Gaussian between these edges
   TF1 *gausFit = new TF1("gausFit", "gaus", xLow, xHigh);
   htemp__1->Fit(gausFit, "R");

   // Draw the fitted Gaussian
   gausFit->SetLineColor(kRed);
   gausFit->SetLineWidth(2);
   gausFit->Draw("SAME");

   Canvas_1->Modified();
   Canvas_1->SetSelected(Canvas_1);
}
