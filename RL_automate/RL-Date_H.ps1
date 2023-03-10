$watinPath = "C:\Program Files\WatiN-2.1.0.1196\bin\net40\WatiN.Core.dll"
$watin = [Reflection.Assembly]::LoadFrom( $watinPath )
[System.Reflection.Assembly]::LoadWithPartialName("'System.Windows.Forms")

Function wait($ie) {
	do {sleep 5} until (-not ($ie.busy))
}
$ie = new-object WatiN.Core.IE("about:blank");
$AlertDialog = New-Object WatiN.Core.DialogHandlers.AlertDialogHandler

		$ie.GoTo("http://qdcws3206.us.qdx.com/billingteam4/");
		$ie.ShowWindow("show");
#wait($ie);
        $ie.SelectList("ctl00_MainContent_DropDownList1").SelectByValue("1035141");

#foreach($selectList in $ie.SelectLists) {
#			if($selectList.Name -eq "ctl00$MainContent$Gridview1$ctl02$ddlTimings") 
  #          { 
   #         $selectList.SelectByValue("Outside Office"); break;}
	#	}
   wait($ie);
     
  foreach($link in $ie.Links) {
		#	if($link.Text -eq "31") { echo "hello"; $link.Click(); break; } 		}
            if($link.Title -eq "February 21") { echo "hello"; $link.Click(); break; } 		}
   $count=02;
  wait($ie);
   $sheet = Import-Csv "C:\RL_automate\Task.csv"
   foreach($detail in $sheet)
{
   $time = $detail.Timings;

   switch($time){
   "Office" { $ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count + '_ddlTimings').SelectByValue("Office"); Break;}
   "Outside Office"{ $ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count + '_ddlTimings').SelectByValue("Outside Office"); Break}
    }
   # $ie.SelectList("ctl00_MainContent_Gridview1_ctl02_eco ddlApplication").SelectByValue("2");
   $application = $detail.Application;
   switch($application){
   "Billing Web" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlApplication').SelectByValue("1"); Break;}
   "Web Billing System" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlApplication').SelectByValue("2"); Break;}
   "PRS" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlApplication').SelectByValue("3"); Break;}
   "EMPI" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlApplication').SelectByValue("4"); Break;}
   "Billing EDI" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlApplication').SelectByValue("5"); Break;}
   "IMDB" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlApplication').SelectByValue("6"); Break;}
   "QuestNet" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlApplication').SelectByValue("7"); Break;}
   "Physician Web Portal" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlApplication').SelectByValue("8"); Break;}
   "H2.0" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlApplication').SelectByValue("9"); Break;}
   "PHR" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlApplication').SelectByValue("10"); Break;}
   "ADT" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlApplication').SelectByValue("11"); Break;}
    }

   # $ie.SelectList("ctl00_MainContent_Gridview1_ctl02_ddlActivity_type").SelectByValue("4");
   # $ie.SelectList("ctl00_MainContent_Gridview1_ctl02_ddlActivity_Subtype").SelectByValue("1C");
   $activity = $detail.Activity;
   $subactivity = $detail.SubActivity;
 
    switch($activity){
    "Production Support - IM activities" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_type').SelectByValue("1");
    if($subactivity -eq "IM activity"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("1A"); }
    if($subactivity -eq "Customer meeting"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("1B"); }
    if($subactivity -eq "Documentation"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("1C"); }
    if($subactivity -eq "Knowledge Transition from Quest"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("1D"); }
    if($subactivity -eq "PI Activity"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("1E"); }
    if($subactivity -eq "Internal Meeting"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("1F"); }
    if($subactivity -eq "Sev-9"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("1G"); }
    Break;}
   
    "Production Support - Non IM activities" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_type').SelectByValue("2");
    if($subactivity -eq "Non IM activity"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("2A"); }
    if($subactivity -eq "Customer meeting"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("2B"); }
    if($subactivity -eq "Documentation"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("2C"); }
    if($subactivity -eq "Knowledge Transition from Quest"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("2D"); }
    if($subactivity -eq "PI Activity"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("2E"); }
    if($subactivity -eq "Internal Meeting"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("2F"); }
    Break;
    }

    "Enhancements less than 80 hour" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_type').SelectByValue("3");
    if($subactivity -eq "Enhancement"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("3A"); }
    if($subactivity -eq "Customer meeting"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("3B"); }
    if($subactivity -eq "Documentation"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("3C"); }
    if($subactivity -eq "Knowledge Transition from Quest"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("3D"); }
    if($subactivity -eq "PI Activity"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("3E"); }
    if($subactivity -eq "Internal Meeting"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("3F"); }
    if($subactivity -eq "Requirement Finalization"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("3G"); }
    if($subactivity -eq "Analysis & Design"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("3H"); }
    if($subactivity -eq "Coding"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("3I"); }
    if($subactivity -eq "Testing"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("3J"); }
    if($subactivity -eq "Implementation"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("3K"); }
    if($subactivity -eq "Post Implementation"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("3L"); }
    Break;
    }

    "Enhancements greater than 80 hour" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_type').SelectByValue("4");
    if($subactivity -eq "Enhancement"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("4A"); }
    if($subactivity -eq "Customer meeting"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("4B"); }
    if($subactivity -eq "Documentation"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("4C"); }
    if($subactivity -eq "Knowledge Transition from Quest"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("4D"); }
    if($subactivity -eq "PI Activity"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("4E"); }
    if($subactivity -eq "Internal Meeting"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("4F"); }
    if($subactivity -eq "Requirement Finalization"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("4G"); }
    if($subactivity -eq "Analysis & Design"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("4H"); }
    if($subactivity -eq "Coding"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("4I"); }
    if($subactivity -eq "Testing"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("4J"); }
    if($subactivity -eq "Implementation"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("4K"); }
    if($subactivity -eq "Post Implementation"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("4L"); }
    Break;
    }

    "Project / Capex" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_type').SelectByValue("5");
    if($subactivity -eq "Development/Coding"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("5A"); }
    if($subactivity -eq "Testing"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("5B");}
    if($subactivity -eq "Customer meeting"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("5C"); }
    if($subactivity -eq "Documentation"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("5D"); }
    if($subactivity -eq "Knowledge Transition from Quest"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("5E"); }
    if($subactivity -eq "PI Activity"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("5F"); }
    if($subactivity -eq "Internal Meeting"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("5G"); }
    Break;
    }
    
    "Others" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_type').SelectByValue("6");
    if($subactivity -eq "TCS internal Project Management"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("6A"); }
    if($subactivity -eq "TCS internal Training"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("6B");}
    if($subactivity -eq "Self learning"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("6C");}
    if($subactivity -eq "Leave"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("6D"); }
    if($subactivity -eq "Break"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("6E"); }
    if($subactivity -eq "TCS Internal IPMS/IQMS"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("6F"); }
    if($subactivity -eq "Late due to cab delay"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("6G"); }
    if($subactivity -eq "Internal Meeting"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("6H"); }
    Break;
    }

    "Problem Management" {$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_type').SelectByValue("7");
    if($subactivity -eq "Internal Meeting"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("7F"); }
    if($subactivity -eq "Requirement Finalization"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("7G"); }
    if($subactivity -eq "Analysis & Design"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("7H"); }
    if($subactivity -eq "Coding"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("7I"); }
    if($subactivity -eq "Testing"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("7J"); }
    if($subactivity -eq "Implementation"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("7K"); }
    if($subactivity -eq "Post Implementation"){$ie.SelectList('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ddlActivity_Subtype').SelectByValue("7L"); }
    Break;
    }
    }
    $decription = $detail.Description;
    $Hrs = $detail.Hours;

    $ie.TextField('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_TextBox2').TypeText("$decription");
    $ie.TextField('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_TextBox3').TypeText("$Hrs");
    $count=$count+1;

    if($detail.Complete -eq "continue"){
    $ie.Button('ctl00_MainContent_Gridview1_ctl' + "{0:D2}" -f $count  + '_ButtonAdd').click();
    }else {Break;}

    }
   
    $ie.Button('ctl00_MainContent_Button1').click();
    #$AlertDialog.WaitUntilExists();
    #$AlertDialog.OKButton.Click();
    
  
   
  # $ie.Button("ctl00_MainContent_Gridview1_ctl03_ButtonAdd").click();
  # $ie.Button("ctl00_MainContent_Button1").click();
  #  $AlertDialog.WaitUntilExists();
  #  $AlertDialog.OKButton.Click();
  # $ie.WaitForComplete();
  # $ie.RemoveDialogHandler($AlertDialog);
    

#$sheet = Import-Csv "C:\Users\1035141\Documents\WIP\Drive D\RL automate\Task.csv"
#foreach($detail in $sheet){$a = $detail.Description echo $a}	

#$count = 1..10 ; foreach ($number in $count)	{		"{0:D2}" -f $number	}