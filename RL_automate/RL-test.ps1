$watinPath = "C:\Program Files\WatiN-2.1.0.1196\bin\net40\WatiN.Core.dll"
$watin = [Reflection.Assembly]::LoadFrom( $watinPath )
[System.Reflection.Assembly]::LoadWithPartialName("'System.Windows.Forms")

Function wait($ie) {
	do {sleep 5} until (-not ($ie.busy))
}
$ie = new-object WatiN.Core.IE("about:blank");
$AlertDialog = New-Object WatiN.Core.DialogHandlers.AlertDialogHandler

		$ie.GoTo("http://qdcws0417.us.qdx.com/billingteam4/resourcemanager.aspx");
		$ie.ShowWindow("show");
        $ie.SelectList("ctl00_MainContent_DropDownList1").SelectByValue("1035141");

#foreach($selectList in $ie.SelectLists) {
#			if($selectList.Name -eq "ctl00$MainContent$Gridview1$ctl02$ddlTimings") 
  #          { 
   #         $selectList.SelectByValue("Outside Office"); break;}
	#	}
    wait($ie);
  foreach($link in $ie.Links) {
		#	if($link.Text -eq "31") { echo "hello"; $link.Click(); break; } 		}
            if($link.Title -eq "July 31") { echo "hello"; $link.Click(); break; } 		}
    

#$link = $ie.Links
#if ($link.Title -eq "July 31") {echo $link; break;}

   #wait($ie);
   # $ie.SelectList("ctl00_MainContent_Gridview1_ctl02_ddlTimings").SelectByValue("Outside Office");
  # $ie.SelectList("ctl00_MainContent_Gridview1_ctl02_ddlApplication").SelectByValue("2");
  #     $ie.SelectList("ctl00_MainContent_Gridview1_ctl02_ddlActivity_type").SelectByValue("4");
    
    #$ie.SelectList("ctl00_MainContent_Gridview1_ctl02_ddlActivity_Subtype").SelectByValue("1C");
 
 #   $ie.TextField("ctl00_MainContent_Gridview1_ctl02_TextBox2").TypeText("Test");
   
  # $ie.TextField("ctl00_MainContent_Gridview1_ctl02_TextBox3").TypeText("0");
  # $ie.Button("ctl00_MainContent_Gridview1_ctl03_ButtonAdd").click();
  # $ie.Button("ctl00_MainContent_Button1").ClickNoWait();
    $AlertDialog.WaitUntilExists(40);
    $AlertDialog.OKButton.ClickNoWait();
  $ie.WaitForComplete();
   $ie.RemoveDialogHandler($AlertDialog);
    

#$sheet = Import-Csv "C:\Users\1035141\Documents\WIP\Drive D\RL automate\Task.csv"
#foreach($detail in $sheet)
 #{
#$a = $detail.Timings echo $a }	

$count = 1..2 ; foreach ($number in $count)
	{
		"{0:D2}" -f $number
	}